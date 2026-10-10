#!/usr/bin/env python3
"""Assemble Razor loops from module/ and recipe/ (design: blueprint/modules.html).

    util/build-scripts.py                         build every recipe and rewrite its block boxes
    util/build-scripts.py recipe/x-recipe.razor   just that one
    util/build-scripts.py --check                 fail if a loop or a recipe is out of date
    util/build-scripts.py --settings recipe/x-recipe.razor
                                                  every setting of that loop: its value, what it
                                                  does, the blocks that read it, file and line
    util/build-scripts.py --new-module <folder>/<name>
                                                  write an empty module to fill in

Module: module/<folder>/<name>.razor, called <folder>/<name>. One block of a loop, the folder
says what it looks after. module/base.razor is the frame of every loop.
    # What the block does. The first line is a summary that ends on that line.
    #@ hotkeys A, B      the Razor hotkeys it calls, gathered into the loop header
    #@ config ---        config__ settings. Each: a comment saying what it does, then the default
    #@ wait ---          wait__ and cooldown__ values, the same in every loop
    #@ timer ---         one "timer__x <start>" per line, the start a cooldown__ name or 0
    #@ state ---         var__ state
    #@ setup ---         code that runs once before the loop
    #@ loop ---          its block in every pass
    #@ end ---           base only: the end of every pass
A section line may trail dashes. A blank line separates the entries of a section. Each section
declares only names with its own prefix, and each name belongs to one module. A block may use
the names of any module the loop has. The builder works out which those are.

Recipe: recipe/<loop>-recipe.razor, one loop.
    #@ output            the loop file it builds
    #@ header ---        the comment block at the top of the loop
    #@ blocks ---        one box per block, in the order they run, base first: a "=" rule, the
                         "#@ use <module>  note" line, the settings it changes (what each does, its
                         default, the other blocks that read it, "> " reason lines), a "=" rule.
                         Under the box, the @setvar! lines of those settings. The builder writes
                         the box. Only the "#@ use" line, the "> " lines and the @setvar! lines are
                         the reader's, and a "#" line right above an @setvar! line is its reason
    #@ state ---         loop-only state, or another start value for a module's state (optional)
    #@ setup ---         loop-only setup: loot pouch, resume list, loaded message (optional)

Output: header with Hotkeys and Generated lines, CONFIG, WAIT AND COOLDOWN, TIMER, STATE,
setup, MAIN LOOP. Each part takes base first, then the blocks in order, then the recipe, and
every piece starts with a line naming the file it came from. CRLF line ends.
Needs only the Python standard library.
"""
import pathlib
import re
import sys
import textwrap

REPO = pathlib.Path(__file__).resolve().parent.parent
MODULE_DIR = REPO / 'module'
BASE = 'base'
MODULE_SECTIONS = ['config', 'wait', 'timer', 'state', 'setup', 'loop', 'end']
RECIPE_SECTIONS = ['header', 'blocks', 'state', 'setup']
DECLARES = {'config': ('config__',), 'wait': ('wait__', 'cooldown__'), 'timer': ('timer__',), 'state': ('var__',)}
SECTION = re.compile(r'^#@\s*([a-z]+)\s*-*\s*$')
NAME = re.compile(r'\b(?:config|wait|cooldown|timer|var)__[A-Za-z0-9_]+')
SETVAR = re.compile(r'^\s*@?setvar!?\s+(\S+)\s*(.*)$')
TIMER = re.compile(r'^(timer__[A-Za-z0-9_]+)\s+(0|(?:cooldown|wait)__[A-Za-z0-9_]+)$')
BOX_RULE = re.compile(r'^#\s*={8,}\s*$')
BOX_SETTING = re.compile(r'^#\s+([a-z0-9_]+) \(default ')
GUARD = re.compile(r'^\s*(if not varexist var__[A-Za-z0-9_]+|endif)\s*$')
WIDTH = 100
INDENT = '    '


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


def join(parts, gap=1):
    """Parts one after another, gap blank lines between them."""
    result = []
    for part in parts:
        result += ([''] * gap if result else []) + part
    return result


def is_code(line):
    return bool(line.strip()) and not line.strip().startswith('#')


def comment_text(line):
    text = line.strip()[1:]
    return text[1:] if text.startswith(' ') else text


def rule(text, width=WIDTH):
    return text + ' ' + '-' * max(4, width - len(text) - 1)


def banner(name):
    line = '# ' + '#' * 84
    return [line, '# # ' + name, line]


def parse(path, kind):
    allowed = MODULE_SECTIONS if kind == 'module' else RECIPE_SECTIONS
    unit = {'path': path, 'notes': [], 'hotkeys': [], 'output': None, 'blocks': [], 'sections': {}, 'starts': {}}
    current = None
    for number, line in enumerate(read_lines(path), 1):
        where = '%s:%d' % (rel(path), number)
        section = SECTION.match(line)
        if section and section.group(1) in allowed:
            if section.group(1) in unit['sections']:
                raise BuildError('%s: a second #@ %s' % (where, section.group(1)))
            current = section.group(1)
            unit['sections'][current] = []
            unit['starts'][current] = number
            continue
        if line.startswith('#@'):
            words = line[2:].split()
            word = words[0] if words else ''
            if word == 'hotkeys' and kind == 'module' and current is None:
                unit['hotkeys'] += [h.strip() for h in ' '.join(words[1:]).split(',') if h.strip()]
            elif word == 'output' and kind == 'recipe' and current is None:
                unit['output'] = ' '.join(words[1:])
            elif word == 'use' and kind == 'recipe' and current == 'blocks' and len(words) > 1:
                unit['blocks'].append(('use', number, words[1], ' '.join(words[2:])))
            elif word == 'config' and kind == 'recipe':
                raise BuildError('%s: a recipe has no #@ config. A setting goes indented under its #@ use line' % where)
            else:
                raise BuildError('%s: unknown or misplaced directive: %s' % (where, line.strip()))
        elif current is None:
            unit['notes'].append(line)
        elif kind == 'recipe' and current == 'blocks':
            unit['blocks'].append(('line', number, line))
        else:
            unit['sections'][current].append((number, line))
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
                raise BuildError('%s:%d: a block never changes a setting. A recipe does, under its #@ use line'
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


def read_blocks(recipe, name):
    """#@ blocks as entries (the #@ use line and its note) and the settings written under them:
    config__ name -> value, reason lines, line number. Each block is a box: a rule line of "=",
    the #@ use line, what the builder writes about the settings, a rule line, then the
    @setvar! lines. In the box only the "> " lines are the reader's: the reasons. A comment
    right above an @setvar! line is a reason too, and moves into the box."""
    entries, over, reasons, pending = [], {}, {}, []
    box, setting = False, None

    def settle(number):
        if pending:
            raise BuildError('%s:%d: a reason goes right above its @setvar! line, or as a "> " line in the box'
                             % (name, pending[0][1]))

    for item in recipe['blocks']:
        if item[0] == 'use':
            settle(item[1])
            entries.append({'ident': item[2], 'note': item[3], 'number': item[1]})
            box, setting = True, None
            continue
        _, number, line = item
        text = line.strip()
        if not text:
            settle(number)
            continue
        if BOX_RULE.match(text):
            settle(number)
            box = False
            continue
        if text.startswith('#'):
            if ';' in text:
                raise BuildError('%s:%d: no ";" in a comment (blueprint/razor.html part 3)' % (name, number))
            body = comment_text(line).strip()
            reason = body[1:].strip() if body.startswith('>') else None
            if not box:
                pending.append((reason if reason is not None else body, number))
            elif BOX_SETTING.match(text):
                setting = 'config__' + BOX_SETTING.match(text).group(1)
            elif reason is not None:
                if not setting:
                    raise BuildError('%s:%d: a "> " reason goes under the setting it explains' % (name, number))
                reasons.setdefault(setting, []).append(reason)
            continue
        match = SETVAR.match(line)
        if not match or not match.group(1).startswith('config__') or not match.group(2).strip():
            raise BuildError('%s:%d: under #@ blocks go the block boxes and, under each box, '
                             '"@setvar! config__<name> <value>" lines' % (name, number))
        if not entries:
            raise BuildError('%s:%d: a setting goes under the box of its block' % (name, number))
        if match.group(1) in over:
            raise BuildError('%s:%d: %s is set twice' % (name, number, match.group(1)))
        box = False
        over[match.group(1)] = {'value': match.group(2).strip(), 'number': number,
                                'notes': [t for t, _ in pending]}
        del pending[:]
    settle(None)
    for setting, value in over.items():
        value['notes'] = reasons.get(setting, []) + value['notes']
    return entries, over


def prepare(path, modules, owner):
    """Read a recipe and check it against the modules it lists."""
    recipe = parse(path, 'recipe')
    name = rel(path)
    if not recipe['output']:
        raise BuildError('%s: no #@ output' % name)
    if 'blocks' not in recipe['sections']:
        raise BuildError('%s: no #@ blocks' % name)
    entries, over = read_blocks(recipe, name)
    if not entries or entries[0]['ident'] != BASE:
        raise BuildError('%s: the first block is always "#@ use base"' % name)

    order = []
    for entry in entries:
        where = '%s:%d' % (name, entry['number'])
        if entry['ident'] not in modules:
            raise BuildError('%s: there is no %s' % (where, module_path(entry['ident'])))
        if entry['ident'] in order:
            raise BuildError('%s: %s is listed twice' % (where, entry['ident']))
        order.append(entry['ident'])

    own = set()
    for number, line in recipe['sections'].get('state', []):
        match = SETVAR.match(line) if is_code(line) else None
        if match and not match.group(1).startswith('var__'):
            raise BuildError('%s:%d: a recipe sets var__ state only. A setting goes under its #@ use line'
                             % (name, number))
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
    for used in recipe_refs:
        readers.setdefault(used, []).append('this recipe')
    return {'recipe': recipe, 'name': name, 'order': order, 'entries': entries,
            'over': over, 'readers': readers, 'owner': owner}


def read_by(loop, setting):
    """Which other blocks of the loop read a setting, besides the module that has it."""
    found = loop['readers'].get(setting, [])
    others = [r for r in found if r != loop['owner'][setting]]
    if not found:
        return 'No block of this loop reads it.'
    if not others:
        return ''
    return ('Also read by ' if len(others) < len(found) else 'Read by ') + ', '.join(others) + '.'


def box_lines(loop, modules, entry, width):
    """One block of #@ blocks: its box, then the @setvar! lines of the settings it changes."""
    module, over = modules[entry['ident']], loop['over']
    changed = [s for s in module['settings'] if s['name'] in over]
    edge = '# ' + '=' * (WIDTH - 2)
    out = [edge, ('#@ use %-*s  %s' % (width, entry['ident'], entry['note'])).rstrip()]
    if 'setup' in module['sections'] and 'loop' not in module['sections']:
        out.append('#   Runs once, before the loop.')
    for setting in changed:
        value = over[setting['name']]
        same = ', the same value' if value['value'] == setting['value'] else ''
        out += ['#', '#   %s (default %s%s)' % (setting['name'][len('config__'):], setting['value'], same)]
        out += [('#      ' + d).rstrip() for d in setting['description']]
        if read_by(loop, setting['name']):
            out += textwrap.wrap(read_by(loop, setting['name']), WIDTH, initial_indent='#      ',
                                 subsequent_indent='#         ')
        out += ['#      > ' + n for n in value['notes']]
    out.append(edge)
    out += ['@setvar! %s %s' % (s['name'], over[s['name']]['value']) for s in changed]
    return out


def tidy_blocks(loop, modules):
    """The #@ blocks section as the builder writes it back: one box per block, a blank line
    between them, each change under the box of the module that has it."""
    width = max(len(e['ident']) for e in loop['entries'])
    return join([box_lines(loop, modules, entry, width) for entry in loop['entries']])


def recipe_lines(path, blocks):
    lines = read_lines(path)
    start = next(i for i, l in enumerate(lines) if SECTION.match(l) and SECTION.match(l).group(1) == 'blocks')
    end = next((i for i in range(start + 1, len(lines)) if SECTION.match(lines[i])), len(lines))
    return lines[:start + 1] + [''] + blocks + (['', ''] + lines[end:] if end < len(lines) else [])


def head(source, indent=''):
    return indent + rule('# ---- %s' % source, WIDTH - len(indent))


def config_lines(loop, modules):
    """CONFIG: every setting of the loop by module, with the recipe's values and reasons."""
    over, groups = loop['over'], []
    for ident in loop['order']:
        lines = trim(lines_of(modules[ident], 'config'))
        if not lines:
            continue
        group = [head(module_path(ident)), '']
        for line in lines:
            match = SETVAR.match(line) if is_code(line) else None
            if match and match.group(1) in over:
                value = over[match.group(1)]
                group += ['# This loop: ' + n if i == 0 else '# ' + n for i, n in enumerate(value['notes'])]
                group.append('@setvar! %s %s' % (match.group(1), value['value']))
            else:
                group.append(line)
        groups.append(group)
    return join(groups, 2)


def timer_lines(unit):
    """A module's timers, each made if missing and set to its start value."""
    out, comments = [], []
    for line in lines_of(unit, 'timer'):
        if not is_code(line):
            comments += [line] if line.strip() else []
            continue
        timer, start = TIMER.match(line.strip()).groups()
        out += ([''] if out else []) + comments
        out += ['if not timerexists "%s"' % timer, '    createtimer "%s"' % timer, 'endif',
                'settimer "%s" %s' % (timer, start)]
        comments = []
    return out


def build(path, modules, owner):
    """The recipe text and the loop text, both as they should be on disk."""
    loop = prepare(path, modules, owner)
    recipe, name = loop['recipe'], loop['name']
    units = [(module_path(ident), modules[ident]) for ident in loop['order']]
    with_recipe = units + [(name, recipe)]

    def parts(section, sources, indent=''):
        found = []
        for source, unit in sources:
            lines = timer_lines(unit) if section == 'timer' else trim(lines_of(unit, section))
            if lines:
                found.append([head(source, indent)] + ([] if indent else ['']) + lines)
        return found

    out = trim(lines_of(recipe, 'header'))
    hotkeys = []
    for _, unit in units:
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

    sections = [('CONFIG', config_lines(loop, modules)),
                ('WAIT AND COOLDOWN', join(parts('wait', units), 2)),
                ('TIMER', join(parts('timer', units), 2)),
                ('STATE', join(parts('state', with_recipe), 2))]
    for title, lines in sections:
        if lines:
            out += ['', ''] + banner(title) + [''] + lines
    if parts('setup', with_recipe):
        out += ['', ''] + join(parts('setup', with_recipe), 2)
    loop_parts = parts('loop', units, INDENT) + parts('end', units, INDENT)
    out += ['', ''] + banner('MAIN LOOP') + ['while not dead'] + join(loop_parts) + ['endwhile']

    for line in out:
        if line.strip().startswith('#') and ';' in line:
            raise BuildError('%s: a comment has ";" (blueprint/razor.html part 3): %s' % (name, line.strip()))
    recipe_text = text_of(recipe_lines(path, tidy_blocks(loop, modules)))
    return [(path, recipe_text), (REPO / recipe['output'], text_of(out))]


def settings_text(path, modules, owner):
    """Every setting of a loop, by module, with its value, meaning, readers, file and line."""
    loop = prepare(path, modules, owner)
    out = ['Settings of %s. "*" marks the ones it changes.' % loop['name']]
    for ident in loop['order']:
        module = modules[ident]
        if not module['settings']:
            continue
        out += ['', '', '%s  %s' % (module_path(ident), module['description'][0])]
        for setting in module['settings']:
            value = loop['over'].get(setting['name'])
            shown = value['value'] if value else setting['value']
            line = '  %s %s %s' % ('*' if value else ' ', setting['name'], shown)
            if value:
                line += ' (default %s)' % setting['value'] if shown != setting['value'] else ' (same as the default)'
            out += ['', '%-64s %s:%d' % (line, module_path(ident), setting['number'])]
            out += ['        ' + d for d in setting['description']]
            out += ['        ' + read_by(loop, setting['name'])] if read_by(loop, setting['name']) else []
            out += ['        This loop: ' + n for n in (value['notes'] if value else [])]
    return '\n'.join(out)


TEMPLATE = """# One line on what this block does. It shows in --settings and heads the module.
# More lines when the block needs them: what it waits for, why it works this way.
#@ hotkeys


{config}

# What this setting changes. Every setting needs a comment like this right above it.
#   0  what 0 does
#   1  what 1 does
# @setvar! config__{snake}_example 1


{wait}


{timer}


{state}


{setup}


{loop}
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
    sections = {s: rule('#@ ' + s) for s in MODULE_SECTIONS}
    text = TEMPLATE.format(snake=name.replace('-', '_'), title=name.replace('-', ' ').upper(), **sections)
    path.write_bytes(text_of(text.rstrip('\n').split('\n')).encode())
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
        for path in paths:
            if not path.is_file() or REPO not in path.parents:
                raise BuildError('%s is not a recipe file in this repository' % path)
        if '--settings' in flags:
            print('\n\n\n'.join(settings_text(path, modules, owner) for path in paths))
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
