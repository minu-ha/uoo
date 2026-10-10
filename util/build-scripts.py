#!/usr/bin/env python3
"""Assemble Razor loops from module/ and recipe/ (design: blueprint/modules.html).

    util/build-scripts.py                         build every recipe and rewrite it in its tidy form
    util/build-scripts.py recipe/x-recipe.razor   just that one
    util/build-scripts.py --check                 fail if a loop or a recipe is out of date
    util/build-scripts.py --settings recipe/x-recipe.razor
                                                  every setting of that loop: its value, what it
                                                  does, the blocks that read it, file and line
    util/build-scripts.py --new-module <folder>/<name>
                                                  write an empty module to fill in

Both kinds of file are made of boxes: a "#" rule line, the "#@" line and what explains it, a
"#" rule line, then the lines it explains.

Module: module/<folder>/<name>.razor, called <folder>/<name>. One block of a loop, the folder
says what it looks after. module/base.razor is the frame of every loop.
    head box             what the block does (the first line is a summary), "#@ hotkeys A, B"
    #@ config box        config__ settings: in the box "#   name" and "#      what it does" for
                         each, under the box the @setvar! lines with the defaults, joined up
    #@ wait box          wait__ and cooldown__ values, the same in every loop, written the same way
    #@ timer box         one "timer__x <start>" per line under the box, the start a cooldown__
                         name or 0. Describing them in the box is optional
    #@ state box         var__ state, written the same way. Guards (if not varexist) may wrap them
    #@ setup, loop, end  code, under a box with only the "#@" line. end is base only
Every name a section declares is described in its box, and each name belongs to one module.
A block may use the names of any module the loop has. The builder works out which those are.

Recipe: recipe/<loop>-recipe.razor, one loop.
    #@ output            the loop file it builds, before the first box
    #@ header box        the comment block at the top of the loop
    #@ blocks box        one box per block, in the order they run, base first: the
                         "#@ use <module>  note" line and the settings it changes (what each
                         does, its default, the other blocks that read it, "> " reason lines),
                         then under the box the @setvar! lines of those settings. The builder
                         writes the box. Only the "#@ use" line, the "> " lines and the @setvar!
                         lines are the reader's, and a "#" line right above an @setvar! line is
                         its reason
    #@ state box         loop-only state, or another start value for a module's state (optional)
    #@ setup box         loop-only setup: loot pouch, resume list, loaded message (optional)

Output: header with Hotkeys and Generated lines, CONFIG, WAIT AND COOLDOWN, TIMER, STATE,
setup, MAIN LOOP. Each part takes base first, then the blocks in order, then the recipe, each
piece in a box naming the file it came from. CRLF line ends. Needs only the Python standard library.
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
WIDTH = 100
BOX = '# ' + '#' * (WIDTH - 2)
BOX_RULE = re.compile(r'^# #{%d}\s*$' % (WIDTH - 2))
SECTION = re.compile(r'^#@\s*([a-z]+)\s*-*\s*$')
NAME = re.compile(r'\b(?:config|wait|cooldown|timer|var)__[A-Za-z0-9_]+')
FULL_NAME = re.compile(r'^(?:config|wait|cooldown|timer|var)__[A-Za-z0-9_]+$')
SETVAR = re.compile(r'^\s*@?setvar!?\s+(\S+)\s*(.*)$')
TIMER = re.compile(r'^(timer__[A-Za-z0-9_]+)\s+(0|(?:cooldown|wait)__[A-Za-z0-9_]+)$')
GUARD = re.compile(r'^\s*(if not varexist var__[A-Za-z0-9_]+|endif)\s*$')
DESC_NAMES = re.compile(r'^#   (\S.*)$')
DESC_TEXT = re.compile(r'^#      (.*)$')
BOX_SETTING = re.compile(r'^#\s+([a-z0-9_]+) \(default ')
TEXT = '#      '
BLOCKS_GUIDE = ['#   One box per block, in the order the blocks run, base first. The builder writes the boxes.',
                '#   To change a setting, write its @setvar! line under any box, with the reason as a "#" line',
                '#   right above it. The builder moves both under the box of the module that has the setting,',
                '#   the reason as a "> " line in the box. In a box only the "> " lines are yours.']
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


def banner(name):
    return [BOX, '# # ' + name, BOX]


def parse(path, kind):
    """Directives, notes and section lines. Box rule lines only shape the file, so they are
    dropped, except under a recipe's #@ blocks where they close a block's box."""
    allowed = MODULE_SECTIONS if kind == 'module' else RECIPE_SECTIONS
    unit = {'path': path, 'notes': [], 'hotkeys': [], 'output': None, 'blocks': [], 'sections': {}}
    current = None
    for number, line in enumerate(read_lines(path), 1):
        where = '%s:%d' % (rel(path), number)
        section = SECTION.match(line)
        if section and section.group(1) in allowed:
            if section.group(1) in unit['sections']:
                raise BuildError('%s: a second #@ %s' % (where, section.group(1)))
            current = section.group(1)
            unit['sections'][current] = []
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
                raise BuildError('%s: a recipe has no #@ config. A setting goes under the box of its block' % where)
            else:
                raise BuildError('%s: unknown or misplaced directive: %s' % (where, line.strip()))
        elif kind == 'recipe' and current == 'blocks':
            unit['blocks'].append(('line', number, line))
        elif BOX_RULE.match(line):
            continue
        elif current is None:
            unit['notes'].append(line)
        else:
            unit['sections'][current].append((number, line))
    return unit


def lines_of(unit, section):
    return [line for _, line in unit['sections'].get(section, [])]


def split_box(module, section):
    """A declaring section as its box (the comment lines first) and its code (the rest). The box
    reads as entries: "#   name, name" lines, then "#      text" lines describing them."""
    name, lines = rel(module['path']), module['sections'].get(section, [])
    box, code, entries = [], [], []
    for number, line in lines:
        if code and not is_code(line) and line.strip():
            raise BuildError('%s:%d: describe names in the box above them, not between them' % (name, number))
        if is_code(line):
            code.append((number, line))
        elif line.strip():
            box.append((number, line))
    for number, line in box:
        text, names = DESC_TEXT.match(line), DESC_NAMES.match(line)
        if line.strip() == '#':
            continue
        if text and entries and entries[-1]['names']:
            entries[-1]['description'].append(text.group(1).rstrip())
        elif names and all(FULL_NAME.match(n.strip()) for n in names.group(1).rstrip(',').split(',')):
            if not entries or entries[-1]['description']:
                entries.append({'names': [], 'description': [], 'number': number})
            entries[-1]['names'] += [n.strip() for n in names.group(1).rstrip(',').split(',')]
        else:
            raise BuildError('%s:%d: in a box, write "#   name, name" and under it "#      what they do"'
                             % (name, number))
    return [line for _, line in box], code, entries


def load_module(path):
    ident = path.relative_to(MODULE_DIR).with_suffix('').as_posix()
    module = parse(path, 'module')
    module['ident'] = ident
    name = rel(path)
    description = [comment_text(l) for l in module['notes'] if l.strip()]
    if not description or any(is_code(l) for l in module['notes']):
        raise BuildError('%s: say what the block does in "#" lines before the first section' % name)
    module['description'] = description
    if 'end' in module['sections'] and ident != BASE:
        raise BuildError('%s: only module/base.razor has #@ end' % name)

    declared, module['entries'], module['code'], described = {}, {}, {}, {}
    for section, prefixes in DECLARES.items():
        if section not in module['sections']:
            continue
        box, code, entries = split_box(module, section)
        module['entries'][section], module['code'][section] = entries, [line for _, line in code]
        for number, line in code:
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
                    raise BuildError('%s: only @setvar! lines go under the #@ %s box' % (where, section))
                if section != 'state' and not match.group(2).strip():
                    raise BuildError('%s: %s needs a value' % (where, match.group(1)))
            declared_name = match.group(1)
            if not declared_name.startswith(prefixes):
                raise BuildError('%s: #@ %s holds %s names, not %s'
                                 % (where, section, ' and '.join(p + '*' for p in prefixes), declared_name))
            if declared_name in declared:
                raise BuildError('%s: %s is declared twice' % (where, declared_name))
            declared[declared_name] = number
        for entry in entries:
            for n in entry['names']:
                if n not in declared or not n.startswith(prefixes):
                    raise BuildError('%s:%d: the #@ %s box describes %s, which it does not declare'
                                     % (name, entry['number'], section, n))
                described[n] = entry['description']
        if section != 'timer':
            for n, number in declared.items():
                if n.startswith(prefixes) and n not in described:
                    raise BuildError('%s:%d: describe %s in the #@ %s box above it' % (name, number, n, section))
    for section in ('setup', 'loop', 'end'):
        for number, line in module['sections'].get(section, []):
            match = SETVAR.match(line) if is_code(line) else None
            if match and match.group(1).startswith('config__'):
                raise BuildError('%s:%d: a block never changes a setting. A recipe does, under the box of the block'
                                 % (name, number))
    module['declared'] = declared
    module['settings'] = [{'name': SETVAR.match(l).group(1), 'value': SETVAR.match(l).group(2).strip(),
                           'number': declared[SETVAR.match(l).group(1)], 'description': described[SETVAR.match(l).group(1)]}
                          for l in module['code'].get('config', [])]
    module['refs'] = references(module, MODULE_SECTIONS)
    module['used'] = module['refs'] - set(declared)
    return module


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
    config__ name -> value, reason lines, line number. In a block's box only the "> " lines are
    the reader's. A comment right above an @setvar! line is a reason too, and moves into the box."""
    entries, over, reasons, pending = [], {}, {}, []
    box, setting = False, None

    def settle():
        if pending:
            raise BuildError('%s:%d: a reason goes right above its @setvar! line, or as a "> " line in the box'
                             % (name, pending[0][1]))

    for item in recipe['blocks']:
        if item[0] == 'line' and not entries:
            continue  # the #@ blocks box: the builder's own guide
        if item[0] == 'use':
            settle()
            entries.append({'ident': item[2], 'note': item[3], 'number': item[1]})
            box, setting = True, None
            continue
        _, number, line = item
        text = line.strip()
        if not text:
            settle()
            continue
        if BOX_RULE.match(text):
            settle()
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
    settle()
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
            raise BuildError('%s:%d: a recipe sets var__ state only. A setting goes under the box of its block'
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


def wrapped(text):
    return textwrap.wrap(text, WIDTH, initial_indent=TEXT, subsequent_indent=TEXT + '   ')


def block_box(loop, modules, entry, width):
    """One block of #@ blocks: its box, then the @setvar! lines of the settings it changes."""
    module, over = modules[entry['ident']], loop['over']
    changed = [s for s in module['settings'] if s['name'] in over]
    out = [BOX, ('#@ use %-*s  %s' % (width, entry['ident'], entry['note'])).rstrip()]
    if 'setup' in module['sections'] and 'loop' not in module['sections']:
        out.append('#   Runs once, before the loop.')
    for setting in changed:
        value = over[setting['name']]
        same = ', the same value' if value['value'] == setting['value'] else ''
        out += ['#', '#   %s (default %s%s)' % (setting['name'][len('config__'):], setting['value'], same)]
        out += [(TEXT + d).rstrip() for d in setting['description']]
        if read_by(loop, setting['name']):
            out += wrapped(read_by(loop, setting['name']))
        out += [TEXT + '> ' + n for n in value['notes']]
    out.append(BOX)
    out += ['@setvar! %s %s' % (s['name'], over[s['name']]['value']) for s in changed]
    return out


def recipe_text(loop, modules):
    """The recipe as the builder writes it back: notes, output, then one box per section, the
    blocks as one box each with each change under the box of the module that has it."""
    recipe = loop['recipe']
    width = max(len(e['ident']) for e in loop['entries'])
    out = trim(recipe['notes']) + ['#@ output ' + recipe['output']]
    for section in RECIPE_SECTIONS:
        if section not in recipe['sections']:
            continue
        if section == 'blocks':
            body = join([block_box(loop, modules, e, width) for e in loop['entries']])
            out += ['', '', BOX, '#@ blocks'] + BLOCKS_GUIDE + [BOX, ''] + body
        else:
            out += ['', '', BOX, '#@ ' + section, BOX, ''] + trim(lines_of(recipe, section))
    return text_of(out)


def source_box(source, box=()):
    return [BOX, '# ' + source] + list(box) + [BOX]


def entry_lines(entry, notes=()):
    """One entry of a box: a blank comment line, the names, what they do, then any notes."""
    out, line = ['#'], '#   '
    for i, name in enumerate(entry['names']):
        piece = name + (',' if i < len(entry['names']) - 1 else '')
        if len(line) + len(piece) > WIDTH and line.strip() != '#':
            out.append(line.rstrip())
            line = '#   '
        line += piece + ' '
    out.append(line.rstrip())
    return out + [(TEXT + d).rstrip() for d in entry['description']] + list(notes)


def config_part(loop, module):
    """A module's settings in CONFIG: its box with this loop's values and reasons, then the values."""
    over = loop['over']
    defaults = {s['name']: s['value'] for s in module['settings']}
    box = []
    for entry in module['entries']['config']:
        notes = []
        for name in entry['names']:
            if name in over:
                same = ', the default' if over[name]['value'] == defaults[name] else ' (default %s)' % defaults[name]
                notes.append(TEXT + '> This loop: %s %s%s.' % (name, over[name]['value'], same))
                notes += [TEXT + '> ' + n for n in over[name]['notes']]
        box += entry_lines(entry, notes)
    values = []
    for line in module['code']['config']:
        name = SETVAR.match(line).group(1)
        values.append('@setvar! %s %s' % (name, over[name]['value']) if name in over else line)
    return source_box(module_path(module['ident']), box) + values


def timer_lines(unit):
    """A module's timers, each made if missing and set to its start value."""
    out = []
    for line in unit.get('code', {}).get('timer', []):
        timer, start = TIMER.match(line.strip()).groups()
        out += ([''] if out else []) + ['if not timerexists "%s"' % timer, '    createtimer "%s"' % timer, 'endif',
                                        'settimer "%s" %s' % (timer, start)]
    return out


def build(path, modules, owner):
    """The recipe text and the loop text, both as they should be on disk."""
    loop = prepare(path, modules, owner)
    recipe, name = loop['recipe'], loop['name']
    units = [(module_path(ident), modules[ident]) for ident in loop['order']]

    def declaring(section, with_recipe=False):
        found = []
        for source, unit in units:
            if section not in unit['sections']:
                continue
            code = timer_lines(unit) if section == 'timer' else trim(unit['code'][section])
            if code:
                box = [l for e in unit['entries'][section] for l in entry_lines(e)]
                found.append(source_box(source, box) + code)
        if with_recipe and trim(lines_of(recipe, section)):
            found.append(source_box(name) + trim(lines_of(recipe, section)))
        return found

    def code_parts(section, indent=''):
        found = []
        for source, unit in units + [(name, recipe)]:
            lines = trim(lines_of(unit, section))
            if lines and unit is recipe and section != 'setup':
                continue
            if lines:
                found.append(([indent + '# ' + source] if indent else source_box(source)) + lines)
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

    config = [config_part(loop, unit) for _, unit in units if unit['code'].get('config')]
    sections = [('CONFIG', join(config)),
                ('WAIT AND COOLDOWN', join(declaring('wait'))),
                ('TIMER', join(declaring('timer'))),
                ('STATE', join(declaring('state', True)))]
    for title, lines in sections:
        if lines:
            out += ['', ''] + banner(title) + [''] + lines
    if code_parts('setup'):
        out += ['', ''] + join(code_parts('setup'))
    out += ['', ''] + banner('MAIN LOOP') + ['while not dead']
    out += join(code_parts('loop', INDENT) + code_parts('end', INDENT)) + ['endwhile']

    for line in out:
        if line.strip().startswith('#') and ';' in line:
            raise BuildError('%s: a comment has ";" (blueprint/razor.html part 3): %s' % (name, line.strip()))
    return [(path, recipe_text(loop, modules)), (REPO / recipe['output'], text_of(out))]


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


TEMPLATE = """{box}
# One line on what this block does. It shows in --settings.
# More lines when the block needs them: what it waits for, why it works this way.
#@ hotkeys
{box}


{box}
#@ config
#
#   config__{snake}_example
#      What this setting changes. Each name the section declares is described here.
#        0  what 0 does
#        1  what 1 does
{box}
@setvar! config__{snake}_example 1


{box}
#@ loop
{box}
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
    text = TEMPLATE.format(box=BOX, snake=name.replace('-', '_'), title=name.replace('-', ' ').upper())
    path.write_bytes(text_of(text.rstrip('\n').split('\n')).encode())
    print('wrote %s. Add a box with "#@ use %s" to the recipe that runs it.' % (rel(path), ident))


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
