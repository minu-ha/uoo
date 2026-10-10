#!/usr/bin/env bash
# Check .razor files for two things Razor will not tell you about until it is too late:
#   1. unbalanced blocks: if/elseif/else/endif, while/endwhile, for|foreach/endfor
#   2. prefixed variables used before anything assigns them
#
# A missing endif is the most common way a script breaks. An undeclared variable is the
# quietest: Razor reads it as empty, the condition silently never matches, and the block
# just stops working. loadout.razor lost an afternoon to a single undeclared wait__long.
#
# Only prefixed names are checked, since those are the ones this repo controls:
#   config__ wait__ cooldown__ var__   must be assigned by setvar / @setvar! somewhere
#   alias__  label__                   must be bound by an "as" binding or by getlabel
# timer__ names are skipped: they live inside quoted strings, where timerexists guards them.
#
#   util/check.sh                    # every file under script/, except script/archive/,
#                                    # then util/build-scripts.py --check on the generated loops
#   util/check.sh path/a.razor ...   # just these
#
# Exit 1 if anything is wrong. Needs only bash and awk.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
checked_all=0
if [ $# -eq 0 ]; then checked_all=1; set -- $(find "$REPO/script" -name '*.razor' -not -path "$REPO/script/archive/*" | sort); fi

status=0
for f in "$@"; do
	awk -v file="${f#$REPO/}" '
	function fail(msg) { printf "%s:%d: %s\n", file, NR, msg; bad = 1 }
	function push(kind) { depth++; kinds[depth] = kind; lines[depth] = NR }
	function pop(kind, word) {
		if (depth == 0) { fail(word " without " kind); return }
		if (kinds[depth] != kind) { fail(word " closes " kinds[depth] " opened at line " lines[depth]); }
		depth--
	}
	{
		line = $0
		sub(/\r$/, "", line)              # CRLF: .gitattributes checks these files out with CRLF
		sub(/^[ \t]+/, "", line)          # indentation
		sub(/^@/, "", line)               # silent prefix
		if (line ~ /^(#|\/\/)/ || line == "") next
		split(line, w, /[ \t]+/)
		word = tolower(w[1])
		if (word == "if")                    push("if")
		else if (word == "while")            push("while")
		else if (word == "for" || word == "foreach") push("for")
		else if (word == "elseif" || word == "else") {
			if (depth == 0 || kinds[depth] != "if") fail(word " outside if")
		}
		else if (word == "endif")    pop("if", word)
		else if (word == "endwhile") pop("while", word)
		else if (word == "endfor")   pop("for", word)
	}
	END {
		for (i = depth; i >= 1; i--) printf "%s:%d: %s never closed\n", file, lines[i], kinds[i]
		exit (bad || depth > 0) ? 1 : 0
	}' "$f" || status=1

	awk -v file="${f#$REPO/}" '
	function fail(msg) { printf "%s:%d: %s\n", file, NR, msg; bad = 1 }
	{
		line = $0
		sub(/\r$/, "", line)
		sub(/^[ \t]+/, "", line)
		if (line ~ /^(#|\/\/)/) next

		# assignments: setvar name, @setvar! name
		probe = line
		sub(/^@/, "", probe)
		if (probe ~ /^setvar!?[ \t]/) {
			split(probe, a, /[ \t]+/)
			declared[a[2]] = 1
		}

		# bindings: "... as name" and "getlabel <source> name"
		rest = line
		while (match(rest, /[ \t]as[ \t]+[A-Za-z_][A-Za-z0-9_]*/)) {
			tok = substr(rest, RSTART, RLENGTH)
			split(tok, b, /[ \t]+/)
			bound[b[length(b)]] = 1
			rest = substr(rest, RSTART + RLENGTH)
		}
		if (line ~ /getlabel[ \t]/) {
			n = split(line, g, /[ \t]+/)
			for (i = 1; i < n - 1; i++) if (g[i] == "getlabel") bound[g[i + 2]] = 1
		}

		# foreach <name> in <list> binds the loop variable too
		if (line ~ /^foreach[ \t]/) {
			split(line, h, /[ \t]+/)
			bound[h[2]] = 1
		}

		# every prefixed name this line mentions, remembered with its first line number
		rest = line
		while (match(rest, /(config|wait|cooldown|var|alias|label)__[A-Za-z0-9_]+/)) {
			name = substr(rest, RSTART, RLENGTH)
			if (!(name in seen)) { seen[name] = NR }
			rest = substr(rest, RSTART + RLENGTH)
		}
	}
	END {
		for (name in seen) {
			if (name ~ /^(alias|label)__/) {
				if (!(name in bound)) fail_at(name, seen[name], "never bound by an as binding or getlabel")
			}
			else if (!(name in declared)) fail_at(name, seen[name], "never assigned")
		}
		exit bad ? 1 : 0
	}
	function fail_at(name, ln, msg) { printf "%s:%d: %s -- %s\n", file, ln, name, msg; bad = 1 }' "$f" || status=1
done
[ $status -eq 0 ] && echo "ok: $# files"
if [ "${checked_all:-0}" = 1 ]; then
	python3 "$REPO/util/build-scripts.py" --check || status=1
fi
exit $status
