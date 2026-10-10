<div align="center">

<img src="document/favicon.svg" width="96" height="96" alt="The Ultima Online glyph">

# uoo

**Razor scripts for Ultima Online Outlands.**

Hunt, gather, train and keep house. Every loop built from shared blocks, every reason written down.

[Outlands](https://uooutlands.com/) · [Razor Scripting](https://wiki.uooutlands.com/Razor_Scripting) · [Docs](document/README.md)

[![MIT](https://img.shields.io/badge/license-MIT-1111aa?style=flat-square)](LICENSE)
![UO Outlands](https://img.shields.io/badge/UO-Outlands-8b1a1a?style=flat-square)
![Razor](https://img.shields.io/badge/Razor-Outlands%20fork-2b6cb0?style=flat-square)
![Node 22+](https://img.shields.io/badge/node-22%2B-444444?style=flat-square)
![Docs](https://img.shields.io/badge/docs-for%20humanity-444444?style=flat-square)

[Quick start](#quick-start) · [Scripts](script/README.md) · [Docs](document/README.md) · [Config](config/README.md) · [한국어](language/README.ko.md)

</div>

## A few loops. Every reason kept.

- **Ready to run.** Hunting loops, hotkey macros, skill trainers and house chores for the Razor bundled with the Outlands client.
  They use its extended syntax, so stock Razor CE or UOSteam will not run them unmodified.
- **Written once.** Each combat and gathering loop is assembled from shared blocks in `module/` by a recipe in `recipe/`.
  Fix a block once and every loop that uses it gets the fix.
- **Reasons kept.** Mechanics, numbers and in-game checks live in the docs, each marked confirmed or not yet.
- **Settings in git.** Razor and ClassicUO profiles live in `config/`, linked into the game by one script.

## Quick start

- **Just want a script?** Copy the `.razor` file into your Razor `Scripts` folder. Done.
- **Run them from the repo, keep your own settings in git, contribute?** Clone it and run `util/setup.sh` once.
  [config/README.md](config/README.md) explains what that does.

### Build and check

To change a loop or the docs you need Node.js 22 or later and pnpm:

```sh
pnpm install
pnpm build       # assemble script/combat and script/gather from module/ and recipe/
pnpm check       # block balance, unassigned variables, out-of-date loops and docs links
pnpm test        # the PvP simulator and docs check tests
pnpm docs:dev    # read the docs at localhost:4321
```

Generated loops are never edited by hand: edit `module/` and `recipe/`, then run `pnpm build`.

## Where things are

| Folder                        | What                                                                                                                                      |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [`script/`](script/README.md) | the scripts, grouped by what they do                                                                                                      |
| `module/`, `recipe/`          | loop blocks written once, and the recipes `util/build-scripts.mjs` assembles into every loop in `script/combat/` and `script/gather/`      |
| [`document/`](document/README.md) | design docs in Markdown, read with [for humanity](https://for-humanity.fyi), one folder per group: how we work, scripting, game reference, templates, open questions. The [docs home](document/README.md) maps them |
| [`config/`](config/README.md) | Razor and ClassicUO settings, one folder per player, and how the game gets linked to this repo                                           |
| `util/`                       | `setup.sh` links the game to the repo, `build-scripts.mjs` assembles loops, `check.sh` checks scripts, `check-docs.mjs` checks docs links, `pvp-sim.mjs` models field duels, `razor-syntax/` highlights `.razor` in WebStorm and VS Code |
| `language/`                   | translations of these READMEs                                                                                                             |

## Credits

- [Jaseowns](https://outlands.uorazorscripts.com/) — mining, lumberjacking, recycle and the skill trainers are his or based on his
- Demlar — dress script concept
- raveX — steal trainer
- [outlandsbutler.com](https://www.outlandsbutler.com/) — generated the `shelf/` loadout scripts

## License

Everything else is [MIT](LICENSE). Third-party scripts stay under their authors' terms.
Not affiliated with UO Outlands.
