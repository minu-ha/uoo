#!/usr/bin/env bash
# Check .razor files for unbalanced blocks: if/elseif/else/endif, while/endwhile, for|foreach/endfor.
# Razor has no linter and a missing endif is the most common way a script breaks.
#
#   util/check.sh                    # every file under script/
#   util/check.sh path/a.razor ...   # just these
#
# Exit 1 if anything is wrong. Needs only bash and awk.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
if [ $# -eq 0 ]; then set -- $(find "$REPO/script" -name '*.razor' | sort); fi

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
done
[ $status -eq 0 ] && echo "ok: $# files"
exit $status
