#!/usr/bin/env python3
"""Assemble Razor loops from module/ and recipe/ (design: blueprint/modules.html).

A recipe says what a loop is: its header, the blocks it runs in order, and every setting it has.
A module is one block, written once: its code, its timers and state, and a description of the
settings it reads. Settings (config__) live only in recipes. Modules never set them.

    util/build-scripts.py                       build every recipe/*-recipe.razor
    util/build-scripts.py recipe/x-recipe.razor build one
    util/build-scripts.py --check               fail if a committed loop differs from its recipe
    util/build-scripts.py --settings recipe/x-recipe.razor
                                                print the settings the recipe still lacks, ready to paste

Recipe (recipe/<loop>-recipe.razor):
    # notes for whoever edits the recipe, before the first directive. Never emitted
    #@ output script/<folder>/<loop>.razor
    #@ header      the comment block at the top of the loop
    #@ blocks      one "#@ use <module>  note" per line, in the order they run. Comments are notes
    #@ config      every config__ the blocks read, with values and comments. Becomes CONFIG
    #@ state       loop-only state (optional)
    #@ setup       loop-only setup before the loop: startup message, loot pouch, resume list (optional)

Module (module/<area>/<name>.razor, named "<area>/<name>"):
    # notes before the first directive. The first line also heads its settings in --settings
    #@ needs <module> ...     modules this one reads from. Listed ones must be in the recipe, and a
                              needed module with no loop, prelude or setup text is added by itself
    #@ after <module> ...    must run later in the pass when both are in the recipe
    #@ hotkeys A, B          Razor hotkeys it calls, gathered into the loop header
    #@ settings              the config__ lines it reads, with suggested values. Never emitted
    #@ prelude | wait | timer | ready | state | setup | loop
                             its text for that part of the loop

Output: header (plus Hotkeys and a Generated line), prelude, CONFIG (the recipe's config),
WAIT AND COOLDOWN, TIMER (timer then ready), STATE (recipe first), setup (recipe first),
MAIN LOOP (while not dead, loop parts in block order, endwhile). CRLF line ends.
Needs only the Python standard library.
"""
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MODULE_SECTIONS = ['settings', 'prelude', 'wait', 'timer', 'ready', 'state', 'setup', 'loop']
RECIPE_SECTIONS = ['header', 'blocks', 'config', 'state', 'setup']
ACTIVE = ['prelude', 'setup', 'loop']
DECLARING = ['wait', 'state']
SETVAR = re.compile(r'^\s*@?setvar!?\s+(\S+)')
CREATETIMER = re.compile(r'^\s*createtimer\s+"([^"]+)"')
CONFIG = re.compile(r'config__[A-Za-z0-9_]+')


class BuildError(Exception):
    pass


def read_lines(path):
    return path.read_bytes().decode('utf-8').replace('\r\n', '\n').split('\n')


def banner(name):
    rule = '# ' + '#' * 84
    return [rule, '# # ' + name, rule]


def trim(lines):
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def code(lines):
    """Lines that are not comments or blank."""
    return [l for l in lines if l.strip() and not l.strip().startswith('#')]


def parse(path, kind):
    sections = MODULE_SECTIONS if kind == 'module' else RECIPE_SECTIONS
    unit = {'path': path, 'notes': [], 'needs': [], 'after': [], 'hotkeys': [], 'output': None,
            'uses': [], 'sections': {}}
    current = None
    where = lambda n: '%s:%d' % (path.relative_to(REPO), n)
    for number, line in enumerate(read_lines(path), 1):
        if not line.startswith('#@'):
            if current is None:
                unit['notes'].append(line)
            elif not (kind == 'recipe' and current == 'blocks'):
                unit['sections'][current].append(line)
            elif line.strip() and not line.strip().startswith('#'):
                raise BuildError('%s: only "#@ use" lines and comments go under #@ blocks' % where(number))
            continue
        words = line[2:].split()
        if not words:
            raise BuildError('%s: empty directive' % where(number))
        word, rest = words[0], ' '.join(words[1:])
        if word in sections:
            if word in unit['sections']:
                raise BuildError('%s: second #@ %s' % (where(number), word))
            current = word
            unit['sections'][word] = []
        elif kind == 'module' and word in ('needs', 'after') and current is None:
            unit[word] += words[1:]
        elif kind == 'module' and word == 'hotkeys' and current is None:
            unit['hotkeys'] += [h.strip() for h in rest.split(',') if h.strip()]
        elif kind == 'recipe' and word == 'output' and current is None:
            unit['output'] = rest
        elif kind == 'recipe' and word == 'use' and current == 'blocks':
            if not words[1:]:
                raise BuildError('%s: #@ use needs a module' % where(number))
            unit['uses'].append((words[1], number))
        elif kind == 'module' and word == 'config':
            raise BuildError('%s: modules do not set config. Describe it under #@ settings, set it in the recipe' % where(number))
        else:
            raise BuildError('%s: unknown or misplaced directive #@ %s' % (where(number), word))
    return unit


def load_module(ident, cache):
    if ident not in cache:
        path = REPO / 'module' / (ident + '.razor')
        if not path.is_file():
            raise BuildError('no module %s (module/%s.razor)' % (ident, ident))
        module = parse(path, 'module')
        for section, lines in module['sections'].items():
            if section != 'settings':
                for line in code(lines):
                    match = SETVAR.match(line)
                    if match and match.group(1).startswith('config__'):
                        raise BuildError('module %s sets %s outside #@ settings' % (ident, match.group(1)))
        cache[ident] = module
    return cache[ident]


def settings_of(module):
    return [SETVAR.match(l).group(1) for l in code(module['sections'].get('settings', [])) if SETVAR.match(l)]


def settings_order(order, cache):
    """Settings groups in a recipe: the shared switch modules first, then the blocks in order."""
    passive = [i for i in order if not any(trim(list(cache[i]['sections'].get(s, [])))
                                           for s in MODULE_SECTIONS if s != 'settings')]
    return passive + [i for i in order if i not in passive]


def settings_head(ident):
    head = '# ---- %s ' % ident
    return head + '-' * max(4, 86 - len(head))


def resolve(recipe, name, cache):
    """Modules in build order: the listed ones, with needed passive modules added in front of
    the first module that needs them."""
    listed = []
    for ident, number in recipe['uses']:
        if ident in listed:
            raise BuildError('%s:%d: %s listed twice' % (name, number, ident))
        listed.append(ident)
    order = []

    def add(ident, chain):
        if ident in order:
            return
        if ident in chain:
            raise BuildError('%s: modules need each other: %s' % (name, ' -> '.join(chain + [ident])))
        module = load_module(ident, cache)
        for need in module['needs']:
            if need in listed:
                continue
            needed = load_module(need, cache)
            if any(trim(list(needed['sections'].get(s, []))) for s in ACTIVE):
                raise BuildError('%s: %s needs %s, which runs in the loop. List it with #@ use' % (name, ident, need))
            add(need, chain + [ident])
        order.append(ident)

    for ident in listed:
        add(ident, [])
    for i, ident in enumerate(order):
        for before in load_module(ident, cache)['after']:
            if before in order and order.index(before) > i:
                raise BuildError('%s: %s must come after %s' % (name, ident, before))
    return order


def needed_settings(order, cache):
    """config__ name -> module that describes it."""
    owner = {}
    for ident in order:
        for setting in settings_of(cache[ident]):
            owner.setdefault(setting, ident)
    return owner


def check_settings(recipe, name, order, cache):
    owner = needed_settings(order, cache)
    # Every config__ a module's code reads is described by it or by a module it needs.
    for ident in order:
        module = cache[ident]
        known = set(settings_of(module))
        for need in module['needs']:
            known |= set(settings_of(load_module(need, cache)))
        for section, lines in module['sections'].items():
            if section == 'settings':
                continue
            for line in code(lines):
                for setting in CONFIG.findall(line):
                    if setting not in known:
                        raise BuildError('module %s reads %s but neither it nor its needs describe it under #@ settings'
                                         % (ident, setting))
    config = code(recipe['sections'].get('config', []))
    declared = []
    for line in config:
        match = SETVAR.match(line)
        if not match or not match.group(1).startswith('config__'):
            raise BuildError('%s: only @setvar! config__ lines go under #@ config: %s' % (name, line.strip()))
        if match.group(1) in declared:
            raise BuildError('%s: %s is set twice' % (name, match.group(1)))
        declared.append(match.group(1))
    missing = [s for s in owner if s not in declared]
    if missing:
        raise BuildError('%s: settings missing from #@ config: %s. Run util/build-scripts.py --settings %s'
                         % (name, ', '.join('%s (%s)' % (s, owner[s]) for s in missing), name))
    own = ' '.join(l for s in ('state', 'setup') for l in code(recipe['sections'].get(s, [])))
    unused = [s for s in declared if s not in owner and s not in CONFIG.findall(own)]
    if unused:
        raise BuildError('%s: no block reads %s' % (name, ', '.join(unused)))


def build(recipe_path, cache):
    recipe = parse(recipe_path, 'recipe')
    name = str(recipe_path.relative_to(REPO))
    if not recipe['output']:
        raise BuildError('%s: no #@ output' % name)
    if not recipe['uses']:
        raise BuildError('%s: no blocks' % name)
    order = resolve(recipe, name, cache)
    check_settings(recipe, name, order, cache)

    units = [('recipe', recipe)] + [(ident, cache[ident]) for ident in order]
    owner = {}
    for ident, unit in units:
        for section in DECLARING + ['timer']:
            for line in code(unit['sections'].get(section, [])):
                match = (CREATETIMER if section == 'timer' else SETVAR).match(line)
                if match and owner.setdefault(match.group(1), ident) != ident:
                    raise BuildError('%s: %s is declared by %s and %s' % (name, match.group(1), owner[match.group(1)], ident))

    def gather(section):
        parts = []
        for ident, unit in units:
            if ident == 'recipe' and section not in ('state', 'setup'):
                continue
            lines = trim(list(unit['sections'].get(section, [])))
            if lines:
                parts.append(lines)
        return parts

    def join(parts, gap=True):
        result = []
        for part in parts:
            if result and gap:
                result.append('')
            result += part
        return result

    hotkeys = []
    for ident in order:
        for hotkey in cache[ident]['hotkeys']:
            if hotkey not in hotkeys:
                hotkeys.append(hotkey)

    out = trim(list(recipe['sections'].get('header', [])))
    if hotkeys:
        line = '# Hotkeys: '
        for i, hotkey in enumerate(hotkeys):
            piece = hotkey + (',' if i < len(hotkeys) - 1 else '.')
            if len(line) + len(piece) > 100 and line.strip() != '# Hotkeys:':
                out.append(line.rstrip())
                line = '#          '
            line += piece + ' '
        out.append(line.rstrip())
    out.append('# Generated from %s by util/build-scripts.py. Edit module/ and recipe/, not this file.' % name)

    if gather('prelude'):
        out += [''] + join(gather('prelude'))
    config = trim(list(recipe['sections'].get('config', [])))
    if config:
        out += [''] + banner('CONFIG') + config
    if gather('wait'):
        out += [''] + banner('WAIT AND COOLDOWN') + join(gather('wait'))
    if gather('timer') or gather('ready'):
        out += [''] + banner('TIMER') + join(gather('timer'))
        if gather('ready'):
            out += ([''] if gather('timer') else []) + join(gather('ready'), gap=False)
    if gather('state'):
        out += [''] + banner('STATE') + join(gather('state'))
    if gather('setup'):
        out += [''] + join(gather('setup'))
    out += [''] + banner('MAIN LOOP') + ['while not dead'] + join(gather('loop')) + ['endwhile']
    return recipe['output'], '\r\n'.join(out) + '\r\n'


def settings_text(recipe_path, cache):
    """The #@ settings of every block whose settings the recipe lacks, as recipe config text."""
    recipe = parse(recipe_path, 'recipe')
    name = str(recipe_path.relative_to(REPO))
    order = resolve(recipe, name, cache)
    declared = {SETVAR.match(l).group(1) for l in code(recipe['sections'].get('config', [])) if SETVAR.match(l)}
    blocks = []
    for ident in settings_order(order, cache):
        module = cache[ident]
        if set(settings_of(module)) - declared:
            blocks.append([settings_head(ident)] + trim(list(module['sections'].get('settings', []))))
    return '\n\n'.join('\n'.join(b) for b in blocks)


def main(argv):
    check = '--check' in argv
    paths = [pathlib.Path(a).resolve() for a in argv if not a.startswith('--')]
    cache = {}
    if '--settings' in argv:
        for path in paths:
            try:
                text = settings_text(path, cache)
            except BuildError as error:
                print('build-scripts: %s' % error, file=sys.stderr)
                return 1
            print(text or '# %s already sets everything its blocks read.' % path.relative_to(REPO))
        return 0
    if not paths:
        paths = sorted((REPO / 'recipe').glob('*-recipe.razor'))
    stale, failed = [], False
    for path in paths:
        try:
            output, text = build(path, cache)
        except BuildError as error:
            print('build-scripts: %s' % error, file=sys.stderr)
            failed = True
            continue
        target = REPO / output
        current = target.read_bytes().decode('utf-8') if target.is_file() else None
        if check:
            if current != text:
                stale.append(output)
        elif current != text:
            target.write_bytes(text.encode('utf-8'))
            print('built %s' % output)
    for output in stale:
        print('build-scripts: %s differs from its recipe. Edit module/ and recipe/, then run util/build-scripts.py' % output,
              file=sys.stderr)
    if failed or stale:
        return 1
    if check:
        print('ok: %d recipes' % len(paths))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
