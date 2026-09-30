#!/usr/bin/env bash
# Check blueprint/*.html for five things the browser will not tell you about:
#   1. a link to a file that does not exist, or to an id the target page does not have
#   2. a page that is missing from blueprint_docs in blueprint/_index.js (it would not show in the nav)
#   3. a tag outside the short list the pages use, which is almost always a < in the text that
#      was not written as &lt; -- the browser swallows it as a tag and the words silently vanish
#   4. a numbered heading whose text does not start with its id, or a data-part off an h2
#   5. two docs in blueprint_docs whose names start with the same letter, or an <h1> that is not its name
#
# Section ids are section numbers (<h3 id="04.C">04.C ...), so renumbering a section breaks every
# link that points at it. Run this after moving or renumbering sections.
#
#   util/check-blueprint.sh
#
# Exit 1 if anything is wrong. Needs only bash, grep and sed.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$REPO/blueprint"
TAGS='html|meta|title|link|script|body|main|div|h[1-5]|p|ul|ol|li|table|thead|tbody|tr|th|td|pre|code|blockquote|a|strong|em|hr'

status=0
pages=0
for page in "$DIR"/*.html; do
	name="$(basename "$page")"
	pages=$((pages + 1))

	head -n 1 "$page" | grep -qix '<!doctype html>' || { echo "$name: first line is not <!doctype html>"; status=1; }

	if [ "$name" != _index.html ] && ! grep -qF "file: '$name'" "$DIR/_index.js"; then
		echo "$name: not listed in blueprint_docs in _index.js"
		status=1
	fi

	# The h1 is the doc's English name, the same one the sidebar and the index cards show.
	docname="$(grep -o "{ file: '$name', name: '[^']*'" "$DIR/_index.js" | sed "s/.*name: '//; s/'$//")"
	h1="$(grep -o '<h1>[^<]*</h1>' "$page" | head -n 1 | sed 's/<[^>]*>//g')"
	[ "$h1" = "$docname" ] || { echo "$name: <h1> is \"$h1\" but its name in blueprint_docs is \"$docname\""; status=1; }

	while IFS= read -r tag; do
		echo "$name: unexpected <$tag> -- write a literal < as &lt;"
		status=1
	done < <(grep -o '<[a-zA-Z][a-zA-Z0-9]*' "$page" | sed 's/^<//' | tr 'A-Z' 'a-z' | sort -u | grep -vxE "$TAGS")

	while IFS= read -r heading; do
		id="${heading#*id=\"}"
		id="${id%%\"*}"
		text="${heading#*>}"
		[ "${text%% *}" = "$id" ] || { echo "$name: heading id=\"$id\" but its text starts \"${text%% *}\""; status=1; }
	done < <(grep -oE '<h[23] id="[^"]*"[^>]*>[^<]*' "$page")

	grep -oE '<[a-z0-9]+ [^>]*data-part=' "$page" | grep -v '^<h2 ' | sed "s/^/$name: data-part only goes on an h2: /" | grep . && status=1

	while IFS= read -r href; do
		case "$href" in http://* | https://* | mailto:*) continue ;; esac
		file="${href%%#*}"
		frag=""
		[ "$file" != "$href" ] && frag="${href#*#}"
		target="$page"
		[ -n "$file" ] && target="$DIR/$file"
		if [ ! -e "$target" ]; then
			echo "$name: $href -- no such file"
			status=1
		elif [ -n "$frag" ] && ! grep -qF "id=\"$frag\"" "$target"; then
			echo "$name: $href -- no such id"
			status=1
		fi
	done < <(grep -o 'href="[^"]*"' "$page" | sed 's/^href="//; s/"$//')
done

# The sidebar marks each doc with the first letter of its name, so two names must not share one.
# The first entry is the index page, marked with a dot instead.
dupes="$(grep -o "{ file: '[^_][^']*', name: '[^']*'" "$DIR/_index.js" | sed "s/.*name: '//" | cut -c1 | sort | uniq -d | tr '\n' ' ')"
[ -n "$dupes" ] && { echo "_index.js: blueprint_docs names share a first letter: $dupes"; status=1; }

[ $status -eq 0 ] && echo "ok: $pages pages"
exit $status
