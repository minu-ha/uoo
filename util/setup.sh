#!/usr/bin/env bash
# One-time setup for macOS + Sikarugir (Wine): make the game read its Scripts and
# Profiles folders straight out of this repo, so whatever you change in-game lands here.
#
#   util/setup.sh                    # you = first part of your git email (jane.doe@x.com -> config/jane/)
#   util/setup.sh <name>             # pick the folder name yourself
#   util/setup.sh [<name>] /path/to/ClassicUO/Data/Plugins/Assistant   # if it is not under ~/Applications
#   util/setup.sh --undo [/path/to/Assistant]     # put real folders back (copies, the repo keeps its files)
#
# To rename: git mv config/<old> config/<new>, then util/setup.sh <new>. It relinks the now-dangling links.
#
# Everyone shares script/. config/<name>/ is yours alone. The repo can live anywhere; paths are
# taken from where this script sits.
#
# Asks one thing only: whether to use a config/<name> that already has files (second machine).
# Never destroys: empty folders and scripts the repo already has are dropped, anything else this
# run replaces stays next to its old place as Scripts-bak / Profiles-bak / <Char>-bak.
# Re-running is safe: folders that are already links are skipped.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
UNDO=0
if [ "${1:-}" = "--undo" ]; then UNDO=1; shift; set -- "" "${1:-}"; fi
if [ -e "${1:-}" ]; then set -- "" "$1"; fi              # only a path was given
NAME="${1:-$(git config user.email 2>/dev/null | cut -d@ -f1 | cut -d. -f1)}"
NAME="${NAME:-$USER}"
CFG="$REPO/config/$NAME"

# Razor's folder is .../ClassicUO/Data/Plugins/Assistant. Outlands builds Razor into
# ClassicUO.exe, so there is no Razor.exe to look for; the folder itself is the anchor.
# The path argument may be that folder, or any file inside it.
ASSIST="${2:-$(find "$HOME/Applications" -type d -name Assistant -path '*/Plugins/*' 2>/dev/null | head -1)}"
if [ -f "$ASSIST" ]; then ASSIST="$(dirname "$ASSIST")"; fi
[ -d "$ASSIST" ] || { echo "Razor's Assistant folder not found. Pass it: util/setup.sh [<name>] <drive_c>/.../ClassicUO/Data/Plugins/Assistant" >&2; exit 1; }
ASSIST="$(cd "$ASSIST" && pwd)"                   # .../ClassicUO/Data/Plugins/Assistant
CUO="$(cd "$ASSIST/../../.." && pwd)"             # .../ClassicUO
echo "game  $CUO"
echo "repo  $REPO"
echo "you   $CFG"

# undo <game path>: replace a link into this repo with a real folder holding a copy. Repo untouched.
undo() {
	local game="$1" target
	[ -L "$game" ] || { echo "skip  $game is not a link"; return; }
	target="$(readlink "$game")"
	case "$target" in "$REPO"/*) ;; *) echo "skip  $game -> $target (not this repo)"; return;; esac
	rm "$game"
	if [ -d "$target" ]; then cp -R "$target" "$game"; rm -f "$game/.gitkeep"; echo "real  $game  (copied from $target)"
	else mkdir -p "$game"; echo "real  $game  (link was dangling, made an empty folder)"; fi
}

if [ "$UNDO" = 1 ]; then
	undo "$ASSIST/Scripts"
	undo "$ASSIST/Profiles"
	for char in "$CUO"/Data/Profiles/*/*/*; do [ -L "$char" ] && undo "$char"; done
	ls -d "$ASSIST"/*-bak* >/dev/null 2>&1 && echo "note  *-bak folders are still there, delete them when you are sure"
	echo; echo "done. The game now uses plain folders again; config/<name> in the repo is unchanged."
	exit 0
fi

# About to point this game at a config/<name> that already holds files: second machine, a renamed
# folder (link is dangling), or someone else's name. Ask first.
if { [ ! -L "$ASSIST/Profiles" ] || [ ! -e "$ASSIST/Profiles" ]; } && [ -n "$(find "$CFG" -type f ! -name .gitkeep 2>/dev/null | head -1)" ]; then
	echo "config/$NAME already has files (pushed from another machine?)."
	echo "y = point this game at them; anything this machine has in their place is kept as *-bak. Nothing in the repo is changed."
	echo "n = stop. If this is not your name, run again with yours."
	printf 'Use config/%s for this game? [y/N] ' "$NAME"
	read -r answer
	[ "$answer" = y ] || { echo "aborted, nothing changed"; exit 1; }
fi

# stash <path>: drop a folder this run replaces if it holds no files, else keep it next to itself as *-bak.
stash() {
	if [ -z "$(find "$1" -type f | head -1)" ]; then rm -rf "$1"; echo "gone  $1 (empty)"; return; fi
	local bak="$1-bak"; [ -e "$bak" ] && bak="$bak-$(date +%Y%m%d%H%M%S)"
	mv "$1" "$bak"; echo "kept  $bak"
}

# adopt <game dir> <repo dir>
# Move the game's files into the repo and leave a link behind. If the repo side already has
# files (second machine) the game's own copy is stashed instead of merged.
adopt() {
	local game="$1" repo="$2"
	if [ -L "$game" ]; then
		if [ "$(readlink "$game")" = "$repo" ]; then echo "ok    $game already linked"; return; fi
		if [ -e "$game" ]; then echo "note  $game -> $(readlink "$game")  (different name; run util/setup.sh --undo first to change it)"; return; fi
		rm "$game"; echo "fix   $game pointed at a folder that no longer exists, relinking"   # renamed config/<name> or moved repo
	fi
	mkdir -p "$repo"
	if [ -d "$game" ]; then
		if [ -z "$(ls -A "$repo" | grep -v '^\.gitkeep$')" ]; then
			find "$game" -mindepth 1 -maxdepth 1 -exec mv {} "$repo"/ \;
			rmdir "$game"
			echo "moved $game/* -> $repo"
		else
			stash "$game"      # repo already has your files (other machine); this game's own copy goes aside
		fi
	fi
	ln -s "$repo" "$game"
	echo "link  $game -> $repo"
}

# Razor scripts: the repo is the source of truth. Old folder stays as Scripts-bak.
if [ -L "$ASSIST/Scripts" ] && [ ! -e "$ASSIST/Scripts" ]; then rm "$ASSIST/Scripts"; echo "fix   Scripts link was dangling, relinking"; fi
if [ -L "$ASSIST/Scripts" ]; then
	echo "ok    $ASSIST/Scripts already linked"
else
	if [ -d "$ASSIST/Scripts" ]; then
		# Anything in the game's Scripts folder that the repo does not already have (same name, same content)?
		extra=""
		while IFS= read -r f; do
			match="$(find "$REPO/script" -name "$(basename "$f")" -type f | head -1)"
			if [ -z "$match" ] || ! cmp -s "$f" "$match"; then extra="$extra
    ${f#$ASSIST/Scripts/}"; fi
		done < <(find "$ASSIST/Scripts" -type f -name '*.razor')
		if [ -z "$extra" ]; then
			rm -rf "$ASSIST/Scripts"; echo "gone  $ASSIST/Scripts (nothing the repo lacks)"
		else
			echo "these files in Scripts are not in the repo:$extra"
			stash "$ASSIST/Scripts"
		fi
	fi
	ln -s "$REPO/script" "$ASSIST/Scripts"
	echo "link  $ASSIST/Scripts -> $REPO/script"
fi

# Razor profiles: hotkeys, agents, variables
adopt "$ASSIST/Profiles" "$CFG/razor/profiles"

# ClassicUO per-character settings. Only the character folder is linked,
# so account and server names never enter the repo.
for char in "$CUO"/Data/Profiles/*/*/*/; do
	[ -d "$char" ] || continue
	adopt "${char%/}" "$CFG/classicuo/$(basename "$char")"
done

echo
echo "done. Start the game, change something, then: git status"
