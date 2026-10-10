#!/usr/bin/env python3
"""Assemble Razor loops from module/ and recipe/ (design: blueprint/modules.html).

    util/build-scripts.py                         build every recipe and refresh its "#|" lines
    util/build-scripts.py recipe/x-recipe.razor   just that one
    util/build-scripts.py --check                 fail if a loop or a recipe is out of date
    util/build-scripts.py --settings recipe/x-recipe.razor
                                                  every setting of that loop: its value, what it
                                                  does, the blocks that read it, file and line
    util/build-scripts.py --new-module <folder>/<name>
                                                  write an empty module to fill in

Module: module/<folder>/<name>.razor, called <folder>/<name>. One block of a loop, the folder
says what it looks after. module/base.razor is the frame every loop gets without a #@ use line.
    # What the block does. The first line shows in --settings.
    #@ hotkeys A, B      the Razor hotkeys it calls, gathered into the loop header
    #@ config            config__ settings, each under a comment saying what it does
    #@ wait              wait__ and cooldown__ values, the same in every loop
    #@ timer             one "timer__x <start>" per line, the start a cooldown__ name or 0
    #@ state             var__ state
    #@ setup             code that runs once before the loop
    #@ loop              its block in every pass
    #@ end               base only: the end of every pass
Each section declares only names with its own prefix, and each name belongs to one module.
A block may use the names of any module the loop has. The builder works out which those are.

Recipe: recipe/<loop>-recipe.razor, one loop.
    #@ output            the loop file it builds
    #@ header            the comment block at the top of the loop
    #@ blocks            one "#@ use <module>  note" per line, in the order they run
    #@ config            only the settings this loop changes, each with its reason in "#" lines
                         right above it. The builder writes the "#|" lines: what the setting does,
                         its default, the blocks that read it, the module file
    #@ state, #@ setup   loop-only state (or another start value) and setup, both optional

Output: header with Hotkeys and Generated lines, CONFIG, WAIT AND COOLDOWN, TIMER, STATE,
setup, MAIN LOOP. Each part takes base first, then the blocks in order, then the recipe.
CRLF line ends. Needs only the Python standard library.
"""
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MODULE_DIR = REPO / 'module'
BASE = 'base'
MODULE_SECTIONS = ['config', 'wait', 'timer', 'state', 'setup', 'loop', 'end']
RECIPE_SECTIONS = ['header', 'blocks', 'config', 'state', 'setup']
DECLARES = {'config': ('config__',), 'wait': ('wait__', 'cooldown__'), 'timer': ('timer__',), 'state': ('var__',)}
NAME = re.compile(r'\b(?:config|wait|cooldown|timer|var)__[A-Za-z0-9_]+')
SETVAR = re.compile(r'^\s*@?setvar!?\s+(\S+)\s*(.*)$')
TIMER = re.compile(r'^(timer__[A-Za-z0-9_]+)\s+(0|(?:cooldown|wait)__[A-Za-z0-9_]+)$')
GUARD = re.compile(r'^\s*(if not varexist var__[A-Za-z0-9_]+|endif)\s*$')
WIDTH = 90


class BuildError(Exception):
    pass


def read_lines(path):
    return path.read_bytes().decode('utf-8').replace('\r\n', '\n').rstrip('\n').split('\n')


def text_of(lines):
    return '\r\n'.join(lines) + '\r\n'


def rel(path):
    return path.relative_to(REPO).as_posix()


def module_path(ident):
    return 'module/%s.razor' % ident


def trim(lines):
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def join(parts):
    """Parts one after another, a blank line between them."""
    result = []
    for part in parts:
        result += ([''] if result else []) + part
    return result


def is_code(line):
    return bool(line.strip()) and not line.strip().startswith('#')


def comment_text(line):
    text = line.strip()[1:]
    return text[1:] if text.startswith(' ') else text


def rule(text):
    return text + ' ' + '-' * max(4, WIDTH - len(text) - 1)


def banner(name):
    line = '# ' + '#' * 84
    return [line, '# # ' + name, line]


def parse(path, kind):
    allowed = MODULE_SECTIONS if kind == 'module' else RECIPE_SECTIONS
    unit = {'path': path, 'notes': [], 'hotkeys': [], 'output': None, 'uses': [], 'sections': {}}
    current = None
    for number, line in enumerate(read_lines(path), 1):
        where = '%s:%d' % (rel(path), number)
        if not line.startswith('#@'):
            if current is None:
                unit['notes'].append(line)
            elif kind == 'recipe' and current == 'blocks':
                if is_code(line):
                    raise BuildError('%s: only "#@ use" lines and comments go under #@ blocks' % where)
            else:
                unit['sections'][current].append((number, line))
            continue
        words = line[2:].split()
        word = words[0] if words else ''
        if word in allowed:
            if word in unit['sections']:
                raise BuildError('%s: a second #@ %s' % (where, word))
            current = word
            unit['sections'][word] = []
        elif word == 'hotkeys' and kind == 'module' and current is None:
            unit['hotkeys'] += [h.strip() for h in ' '.join(words[1:]).split(',') if h.strip()]
        elif word == 'output' and kind == 'recipe' and current is None:
            unit['output'] = ' '.join(words[1:])
        elif word == 'use' and kind == 'recipe' and current == 'blocks' and len(words) > 1:
            unit['uses'].append((words[1], number))
        else:
            raise BuildError('%s: unknown or misplaced directive: %s' % (where, line.strip()))
    return unit


def lines_of(unit, section):
    return [line for _, line in unit['sections'].get(section, [])]


def references(unit, sections):
    """Names the code of these sections mentions, without the name each declaring line declares."""
    found = set()
    for section in sections:
        for _, line in unit['sections'].get(section, []):
            if not is_code(line):
                continue
            text = line
            if section in DECLARES:
                match = TIMER.match(line.strip()) if section == 'timer' else SETVAR.match(line)
                if match:
                    text = line.replace(match.group(1), '', 1)
            found |= set(NAME.findall(text))
    return found


def settings_of(module):
    """The config__ settings of a module, each with its default, line and description. A setting
    right under another one, with no comment of its own, shares that one's description."""
    result, comments, last = [], [], None
    for number, line in module['sections'].get('config', []):
        if not line.strip():
            comments, last = [], None
        elif not is_code(line):
            comments.append(comment_text(line))
        else:
            match = SETVAR.match(line)
            description = comments or (last['description'] if last else None)
            if not description:
                raise BuildError('%s:%d: say what %s does in a comment right above it'
                                 % (rel(module['path']), number, match.group(1)))
            last = {'name': match.group(1), 'value': match.group(2).strip(), 'number': number,
                    'description': description}
            result.append(last)
            comments = []
    return result


def load_module(path):
    ident = path.relative_to(MODULE_DIR).with_suffix('').as_posix()
    module = parse(path, 'module')
    module['ident'] = ident
    name = rel(path)
    description = [comment_text(l) for l in module['notes'] if l.strip()]
    if not description or any(is_code(l) for l in module['notes']):
        raise BuildError('%s: say what the block does in "#" lines before the first #@' % name)
    module['description'] = description
    if 'end' in module['sections'] and ident != BASE:
        raise BuildError('%s: only module/base.razor has #@ end' % name)

    declared = {}
    for section, prefixes in DECLARES.items():
        for number, line in module['sections'].get(section, []):
            if not is_code(line):
                continue
            where = '%s:%d' % (name, number)
            if section == 'timer':
                match = TIMER.match(line.strip())
                if not match:
                    raise BuildError('%s: write a timer as "timer__<name> <cooldown__ name or 0>"' % where)
            else:
                match = SETVAR.match(line)
                if not match:
                    if section == 'state' and GUARD.match(line):
                        continue
                    raise BuildError('%s: only @setvar! lines go under #@ %s' % (where, section))
                if section != 'state' and not match.group(2).strip():
                    raise BuildError('%s: %s needs a value' % (where, match.group(1)))
            declared_name = match.group(1)
            if not declared_name.startswith(prefixes):
                raise BuildError('%s: #@ %s holds %s names, not %s'
                                 % (where, section, ' and '.join(p + '*' for p in prefixes), declared_name))
            if declared_name in declared:
                raise BuildError('%s: %s is declared twice' % (where, declared_name))
            declared[declared_name] = number
    for section in ('setup', 'loop', 'end'):
        for number, line in module['sections'].get(section, []):
            match = SETVAR.match(line) if is_code(line) else None
            if match and match.group(1).startswith('config__'):
                raise BuildError('%s:%d: a block never changes a setting. A recipe does, under #@ config'
                                 % (name, number))
    module['declared'] = declared
    module['settings'] = settings_of(module)
    module['refs'] = references(module, MODULE_SECTIONS)
    module['used'] = module['refs'] - set(declared)
    return module


def load_modules():
    modules = {}
    for path in sorted(MODULE_DIR.rglob('*.razor')):
        module = load_module(path)
        modules[module['ident']] = module
    if BASE not in modules:
        raise BuildError('module/base.razor is missing')
    owner = {}
    for ident, module in modules.items():
        for name in module['declared']:
            if name in owner:
                raise BuildError('%s is declared by both %s and %s. A name belongs to one module'
                                 % (name, module_path(owner[name]), module_path(ident)))
            owner[name] = ident
    return modules, owner


def overrides(recipe, name):
    """config__ name -> its value, the reason lines right above it, and its line number."""
    result, notes, first = {}, [], None
    for number, line in recipe['sections']['config']:
        text = line.strip()
        if text.startswith('#|'):
            continue
        if not text:
            if notes:
                raise BuildError('%s:%d: a reason goes right above its setting, with no blank line between'
                                 % (name, first))
            continue
        if text.startswith('#'):
            if ';' in text:
                raise BuildError('%s:%d: no ";" in a comment (blueprint/razor.html part 3)' % (name, number))
            notes.append(comment_text(line))
            first = first if len(notes) > 1 else number
            continue
        match = SETVAR.match(line)
        if not match or not match.group(1).startswith('config__') or not match.group(2).strip():
            raise BuildError('%s:%d: only "@setvar! config__<name> <value>" lines and their reasons go under #@ config'
                             % (name, number))
        if match.group(1) in result:
            raise BuildError('%s:%d: %s is set twice' % (name, number, match.group(1)))
        result[match.group(1)] = {'value': match.group(2).strip(), 'notes': notes, 'number': number}
        notes = []
    if notes:
        raise BuildError('%s:%d: this reason has no setting under it' % (name, first))
    return result


def prepare(path, modules, owner):
    """Read a recipe and check it against the modules it lists."""
    recipe = parse(path, 'recipe')
    name = rel(path)
    if not recipe['output']:
        raise BuildError('%s: no #@ output' % name)
    if 'config' not in recipe['sections']:
        raise BuildError('%s: no #@ config. Keep it even when the loop changes no setting' % name)

    order = [BASE]
    for ident, number in recipe['uses']:
        where = '%s:%d' % (name, number)
        if ident == BASE:
            raise BuildError('%s: every loop has base already. Leave it out of #@ blocks' % where)
        if ident not in modules:
            raise BuildError('%s: there is no %s' % (where, module_path(ident)))
        if ident in order:
            raise BuildError('%s: %s is listed twice' % (where, ident))
        order.append(ident)

    own = set()
    for number, line in recipe['sections'].get('state', []):
        match = SETVAR.match(line) if is_code(line) else None
        if match and not match.group(1).startswith('var__'):
            raise BuildError('%s:%d: a recipe sets var__ state only. Settings go under #@ config' % (name, number))
        if match:
            own.add(match.group(1))
    recipe_refs = references(recipe, ['state', 'setup'])

    def check(user, names):
        for used in sorted(names):
            if owner.get(used) in order or (owner.get(used) is None and used in own):
                continue
            if owner.get(used) is None:
                raise BuildError('%s uses %s, which no module declares' % (user, used))
            raise BuildError('%s uses %s from %s. Add "#@ use %s" to %s'
                             % (user, used, module_path(owner[used]), owner[used], name))

    for ident in order:
        check(module_path(ident), modules[ident]['used'])
    check(name, recipe_refs - own)

    over = overrides(recipe, name)
    for setting, value in over.items():
        where = '%s:%d' % (name, value['number'])
        if setting not in owner:
            raise BuildError('%s: no module has %s. Run util/build-scripts.py --settings %s for the list'
                             % (where, setting, name))
        if owner[setting] not in order:
            raise BuildError('%s: %s belongs to %s, which this loop does not use' % (where, setting, owner[setting]))

    readers = {}
    for ident in order:
        for used in modules[ident]['refs']:
            readers.setdefault(used, []).append(ident)
    for used, found in readers.items():
        found.sort(key=lambda ident: ident != owner.get(used))
    for used in recipe_refs:
        readers.setdefault(used, []).append('this recipe')
    return recipe, name, order, over, readers


def read_by(readers, setting):
    found = readers.get(setting)
    return 'Read by %s.' % ', '.join(found) if found else 'No block of this loop reads it.'


def config_lines(order, modules, over):
    """CONFIG: every setting of the loop by module, with the recipe's values and reasons."""
    groups = []
    for ident in order:
        lines = trim(lines_of(modules[ident], 'config'))
        if not lines:
            continue
        group = [rule('# ---- %s' % module_path(ident))]
        for line in lines:
            match = SETVAR.match(line) if is_code(line) else None
            if match and match.group(1) in over:
                value = over[match.group(1)]
                group += ['# This loop: ' + n if i == 0 else '# ' + n for i, n in enumerate(value['notes'])]
                group.append('@setvar! %s %s' % (match.group(1), value['value']))
            else:
                group.append(line)
        groups.append(group)
    return join(groups)


def recipe_config(name, order, modules, over, readers):
    """The canonical #@ config of a recipe: each change under its module, with the #| lines."""
    lines = ['#| Only the settings this loop changes. Every other setting keeps the default in its module.',
             '#| Put the reason in "#" lines right above the value. util/build-scripts.py writes the "#|" lines.',
             '#| Every setting of this loop: python3 util/build-scripts.py --settings ' + name]
    for ident in order:
        changed = [s for s in modules[ident]['settings'] if s['name'] in over]
        if not changed:
            continue
        lines += ['', rule('#| ---- %s' % module_path(ident))]
        for i, setting in enumerate(changed):
            value = over[setting['name']]
            lines += ([''] if i else []) + [('#| ' + d).rstrip() for d in setting['description']]
            lines.append('#| Default %s. %s' % (setting['value'], read_by(readers, setting['name'])))
            lines += ['# ' + n for n in value['notes']]
            lines.append('@setvar! %s %s' % (setting['name'], value['value']))
    return lines


def recipe_lines(path, config):
    lines = read_lines(path)
    start = next(i for i, l in enumerate(lines) if l.strip() == '#@ config')
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith('#@')), len(lines))
    return lines[:start + 1] + config + ([''] + lines[end:] if end < len(lines) else [])


def build(path, modules, owner):
    """The loop text and the recipe text, both as they should be on disk."""
    recipe, name, order, over, readers = prepare(path, modules, owner)
    units = [modules[ident] for ident in order]

    def parts(section, with_recipe=False):
        found = [trim(lines_of(unit, section)) for unit in units + ([recipe] if with_recipe else [])]
        return [part for part in found if part]

    out = trim(lines_of(recipe, 'header'))
    hotkeys = []
    for unit in units:
        hotkeys += [h for h in unit['hotkeys'] if h not in hotkeys]
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

    out += [''] + banner('CONFIG') + config_lines(order, modules, over)
    if parts('wait'):
        out += [''] + banner('WAIT AND COOLDOWN') + join(parts('wait'))
    create, ready = [], []
    for unit in units:
        comments = []
        for line in lines_of(unit, 'timer'):
            if not is_code(line):
                comments += [line] if line.strip() else []
                continue
            timer, start = TIMER.match(line.strip()).groups()
            create += ([''] if create else []) + comments
            create += ['if not timerexists "%s"' % timer, '    createtimer "%s"' % timer, 'endif']
            ready.append('settimer "%s" %s' % (timer, start))
            comments = []
    if create:
        out += [''] + banner('TIMER') + create + [''] + ready
    if parts('state', True):
        out += [''] + banner('STATE') + join(parts('state', True))
    if parts('setup', True):
        out += [''] + join(parts('setup', True))
    out += [''] + banner('MAIN LOOP') + ['while not dead'] + join(parts('loop') + parts('end')) + ['endwhile']

    for line in out:
        if line.strip().startswith('#') and ';' in line:
            raise BuildError('%s: a comment has ";" (blueprint/razor.html part 3): %s' % (name, line.strip()))
    recipe_text = text_of(recipe_lines(path, recipe_config(name, order, modules, over, readers)))
    return [(path, recipe_text), (REPO / recipe['output'], text_of(out))]


def settings_text(path, modules, owner):
    """Every setting of a loop, by module, with its value, meaning, readers, file and line."""
    recipe, name, order, over, readers = prepare(path, modules, owner)
    out = ['Settings of %s. "*" marks the ones its #@ config changes.' % name]
    for ident in order:
        module = modules[ident]
        if not module['settings']:
            continue
        out += ['', '%s  %s' % (module_path(ident), module['description'][0])]
        for setting in module['settings']:
            value = over.get(setting['name'])
            line = '  %s %s %s' % ('*' if value else ' ', setting['name'], value['value'] if value else setting['value'])
            if value:
                line += ' (default %s)' % setting['value']
            out.append('%-64s %s:%d' % (line, module_path(ident), setting['number']))
            out += ['        ' + d for d in setting['description']]
            out.append('        ' + read_by(readers, setting['name']))
            out += ['        This loop: ' + n for n in (value['notes'] if value else [])]
    return '\n'.join(out)


TEMPLATE = """# One line on what this block does. It shows in --settings and heads the module.
# More lines when the block needs them: what it waits for, why it works this way.
#@ hotkeys

#@ config
# What this setting changes. Every setting needs a comment like this right above it.
# @setvar! config__{snake}_example 1

#@ wait

#@ timer

#@ state

#@ setup

#@ loop
    # ################################################################################
    # # {title}
    # ################################################################################
"""


def new_module(ident):
    folders = sorted(p.name for p in MODULE_DIR.iterdir() if p.is_dir())
    if not re.match(r'^[a-z]+/[a-z0-9-]+$', ident) or ident.split('/')[0] not in folders:
        raise BuildError('name a module <folder>/<name> in kebab-case. The folders are %s. A new concern '
                         'gets its own folder: make it first' % ', '.join(folders))
    path = MODULE_DIR / (ident + '.razor')
    if path.exists():
        raise BuildError('%s already exists' % rel(path))
    name = ident.split('/')[1]
    path.write_bytes(text_of(TEMPLATE.format(snake=name.replace('-', '_'),
                                             title=name.replace('-', ' ').upper()).rstrip('\n').split('\n')).encode())
    print('wrote %s. Add "#@ use %s" to the recipe that runs it.' % (rel(path), ident))


def main(argv):
    flags = [a for a in argv if a.startswith('--')]
    args = [a for a in argv if not a.startswith('--')]
    if set(flags) - {'--check', '--settings', '--new-module'} or ('--settings' in flags and not args):
        print(__doc__.split('\n\n')[1], file=sys.stderr)
        return 2
    try:
        if '--new-module' in flags:
            for ident in args:
                new_module(ident)
            return 0
        modules, owner = load_modules()
        paths = [pathlib.Path(a).resolve() for a in args] or sorted((REPO / 'recipe').glob('*-recipe.razor'))
        if '--settings' in flags:
            print('\n\n'.join(settings_text(path, modules, owner) for path in paths))
            return 0
    except BuildError as error:
        print('build-scripts: %s' % error, file=sys.stderr)
        return 1

    check, failed = '--check' in flags, False
    for path in paths:
        try:
            results = build(path, modules, owner)
        except BuildError as error:
            print('build-scripts: %s' % error, file=sys.stderr)
            failed = True
            continue
        for target, text in results:
            current = target.read_bytes().decode('utf-8') if target.is_file() else None
            if current == text:
                continue
            if check:
                print('build-scripts: %s is out of date. Run python3 util/build-scripts.py' % rel(target), file=sys.stderr)
                failed = True
            else:
                target.write_bytes(text.encode('utf-8'))
                print('wrote %s' % rel(target))
    if check and not failed:
        print('ok: %d recipes, %d modules' % (len(paths), len(modules)))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
