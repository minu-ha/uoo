# uoo

**English** · [한국어](library/README.ko.md)

Razor scripts and client configuration for **[Ultima Online Outlands](https://uooutlands.com/)**.

![Outlands](https://img.shields.io/badge/UO-Outlands-8b1a1a) ![Razor](https://img.shields.io/badge/Razor-Outlands%20fork-2b6cb0) ![License](https://img.shields.io/badge/license-MIT-green)

Hunting loops, hotkey macros, skill trainers and house chores, written for the Razor build bundled
with the Outlands client and its extended syntax. Stock Razor CE or UOSteam will not run them
unmodified. Syntax reference: [Razor Scripting on the Outlands wiki](https://wiki.uooutlands.com/Razor_Scripting).

## Use it

- **Just want a script?** Copy the `.razor` file into your Razor `Scripts` folder. Done.
- **Run them from the repo, keep your own settings in git, contribute?** Clone it and run
  `util/setup.sh` once. [config/README.md](config/README.md) explains what that does.

## Where things are

| | |
|---|---|
| [`script/`](script/README.md) | the scripts, grouped by what they do |
| [`config/`](config/README.md) | Razor and ClassicUO settings, one folder per player, and how the game gets linked to this repo |
| `library/` | reference: item graphic IDs, hotkey layout, guides, template ↔ script map |
| `util/` | `setup.sh` links the game to the repo, `check.sh` finds unbalanced blocks in scripts |

## Credits

- [Jaseowns](https://outlands.uorazorscripts.com/) — mining, lumberjacking, recycle and the skill trainers are his or based on his
- Demlar — dress script concept
- raveX — steal trainer
- [outlandsbutler.com](https://www.outlandsbutler.com/) — generated the `shelf/` loadout scripts

Everything else is [MIT](LICENSE). Third-party scripts stay under their authors' terms.
Not affiliated with UO Outlands.
