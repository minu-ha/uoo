#!/usr/bin/env python3
"""Assemble Razor loops from module/ and recipe/ (design: blueprint/modules.html).

A module is one block of a loop, written once and shared by every loop that uses it.
A recipe names the output file, the modules in order, and the settings that differ.

    util/build-scripts.py               build every recipe/*.recipe
    util/build-scripts.py recipe/x.recipe ...
    util/build-scripts.py --check       rebuild in memory, fail if a committed file differs

Module file (module/<area>/<name>.razor, id "<area>/<name>"):
    lines before the first section are notes for whoever edits the module, never emitted
    #@ needs core/message ...      modules that must be in the recipe too (they declare what this reads)
    #@ after gather/x ...          modules that must come earlier in the pass when both are present
    #@ hotkeys Drink Cure, ...     Razor hotkeys the module calls, listed in the header
    #@ prelude | config | wait | timer | ready | state | setup | loop
                                   starts a section. Everything up to the next one is its text

Recipe file (recipe/<name>.recipe):
    #@ output script/<folder>/<name>.razor
    #@ modules <id> <id> ...       may repeat. "." places the recipe's own sections
    #@ set <variable> <value>      replaces the value of one @setvar! line
    other lines are the header comment, emitted first. The recipe may carry its own sections too.

Output order: header, prelude, CONFIG, WAIT AND COOLDOWN, TIMER (timer then ready), STATE,
setup, MAIN LOOP (while not dead, loop sections, endwhile). Each section takes its chunks in
recipe order. Needs only the Python standard library.
"""
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = ['prelude', 'config', 'wait', 'timer', 'ready', 'state', 'setup', 'loop']
DECLARING = ['config', 'wait', 'state']
BANNERS = {'config': 'CONFIG', 'wait': 'WAIT AND COOLDOWN', 'timer': 'TIMER', 'state': 'STATE'}
SETVAR = re.compile(r'^\s*@?setvar!?\s+(\S+)')
CREATETIMER = re.compile(r'^\s*createtimer\s+"([^"]+)"')


class BuildError(Exception):
    pass


def read_lines(path):
    return path.read_bytes().decode('utf-8').replace('\r\n', '\n').split('\n')


def banner(name):
    rule = '# ' + '#' * 84
    return [rule, '# # ' + name, rule]


def parse(path, kind):
    """Return the directives and sections of a module or recipe file."""
    unit = {'path': path, 'needs': [], 'after': [], 'hotkeys': [], 'modules': [], 'sets': [], 'output': None,
            'header': [], 'sections': {}}
    current = None
    for number, line in enumerate(read_lines(path), 1):
        if line.startswith('#@'):
            words = line[2:].split()
            if not words:
                raise BuildError('%s:%d: empty directive' % (path, number))
            word, rest = words[0], line[2:].strip()[len(words[0]):].strip()
            if word in SECTIONS:
                current = word
                unit['sections'].setdefault(word, [])
            elif word == 'needs' and kind == 'module':
                unit['needs'] += rest.split()
            elif word == 'after' and kind == 'module':
                unit['after'] += rest.split()
            elif word == 'hotkeys' and kind == 'module':
                unit['hotkeys'] += [h.strip() for h in rest.split(',') if h.strip()]
            elif word == 'output' and kind == 'recipe':
                unit['output'] = rest
            elif word == 'modules' and kind == 'recipe':
                unit['modules'] += rest.split()
            elif word == 'set' and kind == 'recipe':
                name, _, value = rest.partition(' ')
                if not value.strip():
                    raise BuildError('%s:%d: set needs a variable and a value' % (path, number))
                unit['sets'].append((name, value.strip(), number))
            else:
                raise BuildError('%s:%d: unknown directive %s' % (path, number, word))
        elif current:
            unit['sections'][current].append(line)
        elif kind == 'recipe':
            unit['header'].append(line)
    return unit


def trim(lines):
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def load_module(ident, cache):
    if ident not in cache:
        path = REPO / 'module' / (ident + '.razor')
        if not path.is_file():
            raise BuildError('no module %s (%s)' % (ident, path.relative_to(REPO)))
        cache[ident] = parse(path, 'module')
    return cache[ident]


def build(recipe_path, cache):
    recipe = parse(recipe_path, 'recipe')
    name = recipe_path.relative_to(REPO)
    if not recipe['output']:
        raise BuildError('%s: no #@ output' % name)
    order = recipe['modules'] if '.' in recipe['modules'] else ['.'] + recipe['modules']
    units, seen = [], []
    for ident in order:
        if ident in seen:
            raise BuildError('%s: %s listed twice' % (name, ident))
        unit = recipe if ident == '.' else load_module(ident, cache)
        for before in unit['after']:
            if before in order and before not in seen:
                raise BuildError('%s: %s must come after %s' % (name, ident, before))
        seen.append(ident)
        units.append((ident, unit))
    for ident, unit in units:
        for need in unit['needs']:
            if need not in order:
                raise BuildError('%s: %s needs %s in the recipe' % (name, ident, need))

    # A variable or timer is declared by one unit only.
    owner = {}
    for ident, unit in units:
        for section in DECLARING + ['timer']:
            for line in unit['sections'].get(section, []):
                match = (CREATETIMER if section == 'timer' else SETVAR).match(line)
                if match:
                    key = match.group(1)
                    if owner.setdefault(key, ident) != ident:
                        raise BuildError('%s: %s is declared by %s and %s' % (name, key, owner[key], ident))

    chunks = {section: [] for section in SECTIONS}
    for ident, unit in units:
        for section in SECTIONS:
            lines = trim(list(unit['sections'].get(section, [])))
            if lines:
                chunks[section].append(lines)

    for variable, value, number in recipe['sets']:
        pattern = re.compile(r'^(\s*@setvar!\s+%s\s+)\S+(.*)$' % re.escape(variable))
        hits = [(section, c, i) for section in DECLARING for c in chunks[section]
                for i, line in enumerate(c) if pattern.match(line)]
        if len(hits) != 1:
            raise BuildError('%s:%d: set %s matches %d @setvar! lines' % (name, number, variable, len(hits)))
        section, chunk, i = hits[0]
        chunk[i] = pattern.sub(lambda m: m.group(1) + value + m.group(2), chunk[i])

    hotkeys = []
    for ident, unit in units:
        for hotkey in unit['hotkeys']:
            if hotkey not in hotkeys:
                hotkeys.append(hotkey)

    out = list(trim(recipe['header']))
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

    def join(parts, gap=True):
        result = []
        for part in parts:
            if result and gap:
                result.append('')
            result += part
        return result

    if chunks['prelude']:
        out += [''] + join(chunks['prelude'])
    for section in ['config', 'wait']:
        if chunks[section]:
            out += [''] + banner(BANNERS[section]) + join(chunks[section])
    if chunks['timer'] or chunks['ready']:
        out += [''] + banner('TIMER') + join(chunks['timer'])
        if chunks['ready']:
            out += ([''] if chunks['timer'] else []) + join(chunks['ready'], gap=False)
    if chunks['state']:
        out += [''] + banner('STATE') + join(chunks['state'])
    if chunks['setup']:
        out += [''] + join(chunks['setup'])
    out += [''] + banner('MAIN LOOP') + ['while not dead'] + join(chunks['loop']) + ['endwhile']
    return recipe['output'], '\r\n'.join(out) + '\r\n'


def main(argv):
    check = '--check' in argv
    paths = [pathlib.Path(a).resolve() for a in argv if not a.startswith('--')]
    if not paths:
        paths = sorted((REPO / 'recipe').glob('*.recipe'))
    cache, stale, failed = {}, [], False
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
    if check and stale:
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
