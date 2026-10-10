#!/usr/bin/env node
/**
 * Assemble Razor loops from module/ and recipe/ (design: blueprint/modules.md).
 * Usage: the USAGE lines below, also printed on a wrong flag.
 *
 * Both kinds of file are made of boxes: a rule, the "# @" line, a blank "#" line and the "#" lines
 * explaining what follows, a rule, then the lines it explains, joined up. Rules are "-", and "=" for
 * the four parts of a recipe. "#@" still reads as "# @".
 *
 * Module: module/<folder>/<name>.razor, called <folder>/<name>. One block of a loop, the folder
 * says what it looks after. module/base.razor is the frame of every loop.
 *     head box               what the block does (the first line is the summary), "# @ hotkeys A, B"
 *     # @ config box         "#   name" and "#      what it does" for each config__ setting, then
 *                            under the box the @setvar! lines with the defaults, joined up
 *     # @ wait box           wait__, interval__ and cooldown__ values, the same in every loop
 *     # @ timer box          one "timer__x <start>" line per timer, the start an interval__ or config__ name, or 0.
 *                            Describing them is optional
 *     # @ state box          var__ state, written the same way. Guards (if not varexist) may wrap them
 *     # @ setup, loop, end   code under a box with only the "# @" line. end is base only. A loop or
 *                            end block starts with its "-" banner: the title, what it does, a rule.
 *                            The built loop keeps the rules and the title, with the module path
 * Every name a section declares is described in its box, and each name belongs to one module.
 * A block may use the names of any module the loop has. The builder works out which those are.
 *
 * Recipe: recipe/<loop>-recipe.razor, one loop.
 *     # @ output             the loop file it builds, before the first part
 *     # @ header box         the comment block at the top of the loop
 *     # @ blocks box         one box per block, in the order they run, base first: the
 *                            "# @ use <module>" line, then the builder writes the module's summary
 *                            and the settings this loop changes (what each does, its default, the
 *                            other blocks that read it). The reader writes "> " lines (a note on the
 *                            block, or under a setting the reason for its value) and, under the box,
 *                            the @setvar! lines. A "#" line right above an @setvar! line is its reason
 *     # @ state box          loop-only state, or another start value for a module's state (optional)
 *     # @ setup box          loop-only setup: loot pouch, resume list, loaded message (optional)
 *
 * Output: header with Hotkeys and Generated lines, CONFIG, WAIT AND COOLDOWN, TIMER, STATE,
 * setup, MAIN LOOP. Each part takes base first, then the blocks in order, then the recipe, each
 * piece under a box naming the file it came from. CRLF line ends. Needs only Node 22, no packages.
 */
import {existsSync, readFileSync, readdirSync, realpathSync, statSync, writeFileSync} from "node:fs";
import {dirname, join, relative, resolve, sep} from "node:path";
import {fileURLToPath} from "node:url";

const USAGE = `    node util/build-scripts.mjs                         build every recipe and rewrite it in its tidy form
    node util/build-scripts.mjs recipe/x-recipe.razor   just that one
    node util/build-scripts.mjs --check                 fail if a loop or a recipe is out of date
    node util/build-scripts.mjs --settings recipe/x-recipe.razor
                                                        every setting of that loop: its value, what it
                                                        does, the blocks that read it, file and line
    node util/build-scripts.mjs --new-module <folder>/<name>
                                                        write an empty module to fill in`;

const REPO = realpathSync(resolve(dirname(fileURLToPath(import.meta.url)), ".."));
const MODULE_DIR = join(REPO, "module");
const BASE = "base";
const MODULE_SECTIONS = ["config", "wait", "timer", "state", "setup", "loop", "end"];
const RECIPE_SECTIONS = ["header", "blocks", "state", "setup"];
const DECLARES = {config: ["config__"], wait: ["wait__", "interval__", "cooldown__"], timer: ["timer__"], state: ["var__"]};
const WIDTH = 90;
const BOX = `# ${"-".repeat(WIDTH - 2)}`;
const PART = `# ${"=".repeat(WIDTH - 2)}`;
const SECTION = /^#\s?@\s*([a-z]+)\s*[-=]*\s*$/;
const DIRECTIVE = /^#\s?@\s*([a-z]+)\b\s*(.*)$/;
const RULE_LINE = /^#\s*[-=#]{8,}\s*$/;
const BLOCK_RULE = /^\s+#\s*-{8,}\s*$/;
// A name starts where no letter, digit or "_" comes before it, the way a Unicode \b does.
const NAME = /(?<![\p{L}\p{N}_])(?:config|wait|interval|cooldown|timer|var)__[A-Za-z0-9_]+/gu;
const FULL_NAME = /^(?:config|wait|interval|cooldown|timer|var)__[A-Za-z0-9_]+$/;
const SETVAR = /^\s*@?setvar!?\s+(\S+)\s*(.*)$/;
const TIMER = /^(timer__[A-Za-z0-9_]+)\s+(0|(?:interval|cooldown|wait|config)__[A-Za-z0-9_]+)$/;
const GUARD = /^\s*(if not varexist var__[A-Za-z0-9_]+|endif)\s*$/;
const DESC_NAMES = /^# {3}(\S.*)$/;
const DESC_TEXT = /^# {6}(.*)$/;
const BOX_SETTING = /^#\s+([a-z0-9_]+) \(default /;
const TEXT = "#      ";
const INDENT = "    ";
const GROUPS = ["when", "otherwise", "end", "every"];
const BLOCKS_GUIDE = [
    "#   One box per block, in the order the blocks run, base first. The builder writes the box.",
    '#   Yours are the "> " lines in it (a note on the block, or under a setting the reason for',
    "#   its value) and the @setvar! lines under it. Write a new @setvar! line under any box, its",
    '#   reason as a "#" line right above it: the builder moves both to the box it belongs to.',
];

class BuildError extends Error {}

const readLines = (path) => readFileSync(path, "utf8").replaceAll("\r\n", "\n").replace(/\n+$/, "").split("\n");

const textOf = (lines) => `${lines.join("\r\n")}\r\n`;

const rel = (path) => relative(REPO, path).split(sep).join("/");

const modulePath = (ident) => `module/${ident}.razor`;

const isFile = (path) => existsSync(path) && statSync(path).isFile();

// Lengths count characters, not UTF-16 units, so a wide character pads like any other.
const charCount = (text) => [...text].length;

const padEnd = (text, width) => text + " ".repeat(Math.max(0, width - charCount(text)));

const splitWords = (text) => text.split(/\s+/).filter(Boolean);

const stripDashes = (text) => text.replace(/^[ =-]+|[ =-]+$/g, "");

const trimLines = (lines) => {
    let start = 0;
    let end = lines.length;
    while (start < end && !lines[start].trim()) start += 1;
    while (end > start && !lines[end - 1].trim()) end -= 1;
    return lines.slice(start, end);
};

/**
 * Parts one after another, gap blank lines between them.
 */
const joinParts = (parts, gap = 1) => {
    const result = [];
    for (const part of parts) {
        if (result.length) result.push(...Array(gap).fill(""));
        result.push(...part);
    }
    return result;
};

const isCode = (line) => Boolean(line.trim()) && !line.trim().startsWith("#");

const commentText = (line) => {
    const text = line.trim().slice(1);
    return text.startsWith(" ") ? text.slice(1) : text;
};

/**
 * A part of the loop file (CONFIG, MAIN LOOP): a "=" box at the left edge.
 */
const banner = (name) => [PART, `# ${name}`, PART];

/**
 * A block in the loop starts with its "-" banner, and a block with steps has one more
 * banner per step. The built loop keeps only the rules and the title of each, with the file
 * the block came from on the right of the first title: what the block does is written in
 * that file. Inside a group the block moves in by four spaces a level and its rules are
 * shortened to keep the width.
 */
const blockBanner = (blockLines, source, depth = 0) => {
    const lines = blockLines.map((line) => (line.trim() ? " ".repeat(4 * depth) + line : line));
    const indent = lines[0].slice(0, lines[0].length - lines[0].trimStart().length);
    const rule = `${indent}# ${"-".repeat(WIDTH - indent.length - 2)}`;
    // The indent is whitespace only, which needs no escaping in a pattern.
    const titleLine = new RegExp(`^${indent}# [A-Z][A-Z0-9 /&,.'()+:-]*$`);
    const starts = new Set([0]);
    for (let i = 0; i < lines.length - 1; i += 1) {
        if (BLOCK_RULE.test(lines[i]) && lines[i].startsWith(`${indent}#`) && titleLine.test(lines[i + 1].trimEnd())) {
            starts.add(i);
        }
    }
    for (const start of [...starts].sort((a, b) => b - a)) {
        let closing = start + 2;
        while (closing < lines.length && !BLOCK_RULE.test(lines[closing])) closing += 1;
        if (closing === lines.length) {
            throw new BuildError(`${source}: the banner at "${lines[start + 1].trim()}" has no closing rule`);
        }
        lines.splice(start, closing - start + 1, rule, lines[start + 1].trimEnd(), rule);
    }
    const title = lines[1].trimEnd();
    lines[1] = title + " ".repeat(Math.max(2, WIDTH - charCount(title) - charCount(source))) + source;
    return lines;
};

/**
 * Directives, notes and section lines. Rule lines only shape the file and are dropped,
 * except under a recipe's # @ blocks, where the rule under a # @ use line closes its box.
 */
const parse = (path, kind) => {
    const allowed = kind === "module" ? MODULE_SECTIONS : RECIPE_SECTIONS;
    const unit = {path, notes: [], hotkeys: [], output: null, blocks: [], sections: {}};
    let current = null;
    readLines(path).forEach((line, index) => {
        const number = index + 1;
        const where = `${rel(path)}:${number}`;
        const section = SECTION.exec(line);
        if (section && allowed.includes(section[1])) {
            if (Object.hasOwn(unit.sections, section[1])) throw new BuildError(`${where}: a second # @ ${section[1]}`);
            current = section[1];
            unit.sections[current] = [];
            return;
        }
        const directive = DIRECTIVE.exec(line);
        if (directive) {
            const word = directive[1];
            const words = [word, ...splitWords(directive[2])];
            if (word === "hotkeys" && kind === "module" && current === null) {
                unit.hotkeys.push(...words.slice(1).join(" ").split(",").map((hotkey) => hotkey.trim()).filter(Boolean));
            } else if (word === "output" && kind === "recipe" && current === null) {
                unit.output = words.slice(1).join(" ");
            } else if (word === "use" && kind === "recipe" && current === "blocks" && words.length > 1) {
                unit.blocks.push({type: "use", number, ident: words[1], note: stripDashes(words.slice(2).join(" "))});
            } else if (GROUPS.includes(word) && kind === "recipe" && current === "blocks") {
                unit.blocks.push({type: "group", number, word, rest: stripDashes(directive[2])});
            } else if (word === "config" && kind === "recipe") {
                throw new BuildError(`${where}: a recipe has no # @ config. A setting goes under the # @ use line of its block`);
            } else {
                throw new BuildError(`${where}: unknown or misplaced directive: ${line.trim()}`);
            }
        } else if (kind === "recipe" && current === "blocks") {
            unit.blocks.push({type: "line", number, line});
        } else if (RULE_LINE.test(line)) {
            // a rule only shapes the file
        } else if (current === null) {
            unit.notes.push(line);
        } else {
            unit.sections[current].push({number, line});
        }
    });
    return unit;
};

const linesOf = (unit, section) => (unit.sections[section] ?? []).map((entry) => entry.line);

/**
 * A declaring section as its descriptions (the comment lines first) and its code (the rest).
 * The descriptions read as entries: "#   name, name" lines, then "#      text" lines.
 */
const splitBox = (module, section) => {
    const name = rel(module.path);
    const code = [];
    const entries = [];
    for (const {number, line} of module.sections[section] ?? []) {
        if (isCode(line)) {
            code.push({number, line});
            continue;
        }
        if (!line.trim() || line.trim() === "#") continue;
        if (code.length) throw new BuildError(`${name}:${number}: describe names above them, not between them`);
        const text = DESC_TEXT.exec(line);
        const names = DESC_NAMES.exec(line);
        const listed = names ? names[1].replace(/,+$/, "").split(",").map((n) => n.trim()) : [];
        if (text && entries.length && entries.at(-1).names.length) {
            entries.at(-1).description.push(text[1].trimEnd());
        } else if (names && listed.every((n) => FULL_NAME.test(n))) {
            if (!entries.length || entries.at(-1).description.length) entries.push({names: [], description: [], number});
            entries.at(-1).names.push(...listed);
        } else {
            throw new BuildError(`${name}:${number}: describe names as "#   name, name" with "#      what they do" under it`);
        }
    }
    return {code, entries};
};

/**
 * Names the code of these sections mentions, without the name each declaring line declares.
 */
const references = (unit, sections) => {
    const found = new Set();
    for (const section of sections) {
        for (const {line} of unit.sections[section] ?? []) {
            if (!isCode(line)) continue;
            let text = line;
            if (Object.hasOwn(DECLARES, section)) {
                const match = section === "timer" ? TIMER.exec(line.trim()) : SETVAR.exec(line);
                if (match) text = line.replace(match[1], "");
            }
            for (const name of text.match(NAME) ?? []) found.add(name);
        }
    }
    return found;
};

const loadModule = (path) => {
    const ident = rel(path).slice("module/".length, -".razor".length);
    const module = parse(path, "module");
    module.ident = ident;
    const name = rel(path);
    const description = trimLines(module.notes.filter((line) => line.trim()).map(commentText));
    if (!description.length || module.notes.some(isCode)) {
        throw new BuildError(`${name}: say what the block does in "#" lines before the first section`);
    }
    module.description = description;
    if (charCount(description[0]) > WIDTH - 4) {
        throw new BuildError(`${name}: the first line is the summary the recipe shows, keep it to ${WIDTH - 4} characters`);
    }
    if (Object.hasOwn(module.sections, "end") && ident !== BASE) throw new BuildError(`${name}: only module/base.razor has # @ end`);

    const declared = new Map();
    const described = new Map();
    module.entries = {};
    module.code = {};
    for (const [section, prefixes] of Object.entries(DECLARES)) {
        if (!Object.hasOwn(module.sections, section)) continue;
        const {code, entries} = splitBox(module, section);
        module.entries[section] = entries;
        module.code[section] = code.map((entry) => entry.line);
        const hasPrefix = (n) => prefixes.some((prefix) => n.startsWith(prefix));
        for (const {number, line} of code) {
            const where = `${name}:${number}`;
            let match;
            if (section === "timer") {
                match = TIMER.exec(line.trim());
                if (!match) throw new BuildError(`${where}: write a timer as "timer__<name> <interval__ name or 0>"`);
            } else {
                match = SETVAR.exec(line);
                if (!match) {
                    if (section === "state" && GUARD.test(line)) continue;
                    throw new BuildError(`${where}: only @setvar! lines go under # @ ${section}`);
                }
                if (section !== "state" && !match[2].trim()) throw new BuildError(`${where}: ${match[1]} needs a value`);
            }
            const declaredName = match[1];
            if (!hasPrefix(declaredName)) {
                const kinds = prefixes.map((prefix) => `${prefix}*`).join(" and ");
                throw new BuildError(`${where}: # @ ${section} holds ${kinds} names, not ${declaredName}`);
            }
            if (declared.has(declaredName)) throw new BuildError(`${where}: ${declaredName} is declared twice`);
            declared.set(declaredName, number);
        }
        for (const entry of entries) {
            for (const n of entry.names) {
                if (!declared.has(n) || !hasPrefix(n)) {
                    throw new BuildError(`${name}:${entry.number}: # @ ${section} describes ${n}, which it does not declare`);
                }
                described.set(n, entry.description);
            }
        }
        if (section !== "timer") {
            for (const [n, number] of declared) {
                if (hasPrefix(n) && !described.has(n)) throw new BuildError(`${name}:${number}: describe ${n} under # @ ${section}`);
            }
        }
    }
    for (const section of ["loop", "end"]) {
        const code = trimLines(linesOf(module, section));
        let closing = code.findIndex((line, i) => i >= 2 && !line.trim().startsWith("#"));
        if (closing === -1) closing = code.length;
        const banners = code.length > 2 && BLOCK_RULE.test(code[0]) && code[1].trim().startsWith("# ")
            && code.slice(2, closing).some((line) => BLOCK_RULE.test(line));
        if (code.length && !banners) {
            throw new BuildError(`${name}: # @ ${section} starts with its banner: a "-" rule, "# TITLE", what the block does, a "-" rule`);
        }
    }
    for (const section of ["setup", "loop", "end"]) {
        for (const {number, line} of module.sections[section] ?? []) {
            const match = isCode(line) ? SETVAR.exec(line) : null;
            if (match && match[1].startsWith("config__")) throw new BuildError(`${name}:${number}: a block never changes a setting. A recipe does`);
        }
    }
    module.declared = declared;
    module.settings = (module.code.config ?? []).map((line) => {
        const [, setting, value] = SETVAR.exec(line);
        return {name: setting, value: value.trim(), number: declared.get(setting), description: described.get(setting)};
    });
    module.refs = references(module, MODULE_SECTIONS);
    module.used = new Set([...module.refs].filter((n) => !declared.has(n)));
    return module;
};

/**
 * Paths in the order Python's sorted() gives pathlib paths: part by part, so "a/x" comes before "a-b/x".
 */
const byParts = (a, b) => {
    const left = a.split(sep);
    const right = b.split(sep);
    for (let i = 0; i < Math.min(left.length, right.length); i += 1) {
        if (left[i] !== right[i]) return left[i] < right[i] ? -1 : 1;
    }
    return left.length - right.length;
};

const loadModules = () => {
    const modules = new Map();
    const files = readdirSync(MODULE_DIR, {recursive: true}).filter((file) => file.endsWith(".razor")).sort(byParts);
    for (const file of files) {
        const module = loadModule(join(MODULE_DIR, file));
        modules.set(module.ident, module);
    }
    if (!modules.has(BASE)) throw new BuildError("module/base.razor is missing");
    const owner = new Map();
    for (const [ident, module] of modules) {
        for (const name of module.declared.keys()) {
            if (owner.has(name)) {
                throw new BuildError(`${name} is declared by both ${modulePath(owner.get(name))} and ${modulePath(ident)}. A name belongs to one module`);
            }
            owner.set(name, ident);
        }
    }
    return {modules, owner};
};

/**
 * # @ blocks as entries and the settings written under them: config__ name -> value, reason
 * lines, line number. Each block is a box: a rule, the # @ use line, the builder's lines, a rule,
 * then the @setvar! lines. In the box only the "> " lines are the reader's: a note on the block,
 * or under a setting the reason for its value. A comment right above an @setvar! line is a reason too.
 */
const readBlocks = (recipe, name) => {
    const entries = [];
    const over = new Map();
    const reasons = new Map();
    const pending = [];
    const loose = [];
    const layout = [];
    const openGroups = [];
    let box = false;
    let setting = null;

    const settle = () => {
        if (pending.length) throw new BuildError(`${name}:${pending[0].number}: a reason goes right above its @setvar! line, or as a "> " line`);
    };

    for (const item of recipe.blocks) {
        if (item.type === "line" && !entries.length) continue; // the guide under # @ blocks is the builder's
        if (item.type === "group") {
            settle();
            loose.length = 0;
            box = false;
            setting = null;
            const {number, word, rest} = item;
            if ((word === "when" || word === "every") && !rest) {
                throw new BuildError(`${name}:${number}: # @ ${word} needs ${word === "when" ? "a condition" : "an interval__ name"}`);
            }
            if (word === "otherwise" && (!openGroups.length || openGroups.at(-1).word !== "when")) {
                throw new BuildError(`${name}:${number}: # @ otherwise goes inside a # @ when`);
            }
            if (word === "end" && !openGroups.length) throw new BuildError(`${name}:${number}: # @ end has no group to close`);
            if (!entries.length) throw new BuildError(`${name}:${number}: groups come after # @ use base`);
            if (word === "when" || word === "every") {
                openGroups.push({word, number});
            } else if (word === "otherwise") {
                openGroups[openGroups.length - 1] = {word: "otherwise", number: openGroups.at(-1).number};
            } else {
                openGroups.pop();
            }
            layout.push({kind: word, rest, number});
            continue;
        }
        if (item.type === "use") {
            settle();
            loose.length = 0;
            entries.push({ident: item.ident, number: item.number, old: [], notes: item.note ? [item.note] : [], kind: "use"});
            layout.push(entries.at(-1));
            box = true;
            setting = null;
            continue;
        }
        const {number, line} = item;
        const text = line.trim();
        if (!text || RULE_LINE.test(text)) {
            settle();
            box = false;
            loose.length = 0;
            continue;
        }
        if (text.startsWith("#")) {
            if (text.includes(";")) throw new BuildError(`${name}:${number}: no ";" in a comment (blueprint/razor.md part 3)`);
            const body = commentText(line).trim();
            const reason = body.startsWith(">") ? body.slice(1).trim() : null;
            if (!body && box) continue;
            if (!box) {
                pending.push({text: reason ?? body, number});
                continue;
            }
            if (reason === null && !line.startsWith("#   ")) {
                // Not a shape the builder writes. Right above an @setvar! line it is that setting's
                // reason (a box not yet closed by its rule), otherwise it is dropped with a warning.
                entries.at(-1).old.push({number, line: line.trimEnd()});
                loose.push({text: body, number});
                continue;
            }
            loose.length = 0;
            const boxSetting = BOX_SETTING.exec(text);
            if (boxSetting) {
                setting = `config__${boxSetting[1]}`;
            } else if (reason !== null && setting) {
                if (!reasons.has(setting)) reasons.set(setting, []);
                reasons.get(setting).push(reason);
            } else if (reason !== null) {
                entries.at(-1).notes.push(reason);
            }
            continue;
        }
        const match = SETVAR.exec(line);
        if (!match || !match[1].startsWith("config__") || !match[2].trim()) {
            throw new BuildError(`${name}:${number}: under # @ blocks go "# @ use" lines and, under each, "@setvar! config__<name> <value>" lines`);
        }
        if (!entries.length) throw new BuildError(`${name}:${number}: a setting goes under the # @ use line of its block`);
        if (over.has(match[1])) throw new BuildError(`${name}:${number}: ${match[1]} is set twice`);
        if (box && loose.length) {
            const taken = new Set(loose.map((entry) => entry.number));
            entries.at(-1).old = entries.at(-1).old.filter((entry) => !taken.has(entry.number));
            pending.push(...loose);
        }
        box = false;
        over.set(match[1], {value: match[2].trim(), number, notes: pending.map((entry) => entry.text)});
        pending.length = 0;
        loose.length = 0;
    }
    settle();
    if (openGroups.length) {
        const {word, number} = openGroups.at(-1);
        throw new BuildError(`${name}:${number}: this # @ ${word} has no # @ end`);
    }
    for (const [key, value] of over) value.notes = [...(reasons.get(key) ?? []), ...value.notes];
    return {entries, over, layout};
};

/**
 * Read a recipe and check it against the modules it lists.
 */
const prepare = (path, modules, owner) => {
    const recipe = parse(path, "recipe");
    const name = rel(path);
    if (!recipe.output) throw new BuildError(`${name}: no # @ output`);
    if (!Object.hasOwn(recipe.sections, "blocks")) throw new BuildError(`${name}: no # @ blocks`);
    const {entries, over, layout} = readBlocks(recipe, name);
    if (!entries.length || entries[0].ident !== BASE) throw new BuildError(`${name}: the first block is always "# @ use base"`);

    const order = [];
    for (const entry of entries) {
        const where = `${name}:${entry.number}`;
        if (!modules.has(entry.ident)) throw new BuildError(`${where}: there is no ${modulePath(entry.ident)}`);
        if (order.includes(entry.ident)) throw new BuildError(`${where}: ${entry.ident} is listed twice`);
        order.push(entry.ident);
    }

    const own = new Set();
    for (const {number, line} of recipe.sections.state ?? []) {
        const match = isCode(line) ? SETVAR.exec(line) : null;
        if (match && !match[1].startsWith("var__")) {
            throw new BuildError(`${name}:${number}: a recipe sets var__ state only. A setting goes under the # @ use line of its block`);
        }
        if (match) own.add(match[1]);
    }
    const recipeRefs = references(recipe, ["state", "setup"]);

    const check = (user, names) => {
        for (const used of [...names].sort()) {
            if (order.includes(owner.get(used)) || (!owner.has(used) && own.has(used))) continue;
            if (!owner.has(used)) throw new BuildError(`${user} uses ${used}, which no module declares`);
            throw new BuildError(`${user} uses ${used} from ${modulePath(owner.get(used))}. Add "# @ use ${owner.get(used)}" to ${name}`);
        }
    };

    for (const ident of order) check(modulePath(ident), modules.get(ident).used);
    check(name, [...recipeRefs].filter((n) => !own.has(n)));

    // A group reads names like any block, and an every group gets a timer of its own.
    const clocks = [];
    for (const item of layout) {
        const where = `${name}:${item.number}`;
        if (item.kind === "when") {
            check(where, new Set(item.rest.match(NAME) ?? []));
        } else if (item.kind === "every") {
            const interval = item.rest;
            if (!/^interval__\w+$/.test(interval)) throw new BuildError(`${where}: # @ every takes one interval__ name`);
            check(where, [interval]);
            const timer = `timer__${interval.slice("interval__".length)}`;
            if (owner.has(timer)) {
                throw new BuildError(`${where}: ${timer} belongs to ${modulePath(owner.get(timer))}. Pick an interval whose timer no module declares`);
            }
            item.timer = timer;
            clocks.push([timer, interval]);
        }
    }

    for (const [setting, value] of over) {
        const where = `${name}:${value.number}`;
        if (!owner.has(setting)) {
            throw new BuildError(`${where}: no module has ${setting}. Run node util/build-scripts.mjs --settings ${name} for the list`);
        }
        if (!order.includes(owner.get(setting))) {
            throw new BuildError(`${where}: ${setting} belongs to ${owner.get(setting)}, which this loop does not use`);
        }
    }

    const readers = new Map();
    const addReader = (used, reader) => {
        if (!readers.has(used)) readers.set(used, []);
        readers.get(used).push(reader);
    };
    for (const ident of order) {
        for (const used of modules.get(ident).refs) addReader(used, ident);
    }
    for (const used of recipeRefs) addReader(used, "this recipe");
    return {recipe, name, order, entries, layout, clocks, over, readers, owner};
};

/**
 * Which other blocks of the loop read a setting, besides the module that has it.
 */
const readBy = (loop, setting) => {
    const found = loop.readers.get(setting) ?? [];
    const others = found.filter((reader) => reader !== loop.owner.get(setting));
    if (!found.length) return "No block of this loop reads it.";
    if (!others.length) return "";
    return `${others.length < found.length ? "Also read by " : "Read by "}${others.join(", ")}.`;
};

/**
 * Python's textwrap.wrap(text, WIDTH, initial_indent=first, subsequent_indent=rest,
 * break_long_words=False, break_on_hyphens=False), which every recipe box was written with:
 * words split on whitespace only, and a word longer than the line gets a line of its own.
 */
const wrapped = (text, first = "#   ", rest = first) => {
    // Tabs go to the next multiple of 8 and other whitespace becomes a space. Text is one line.
    let column = 0;
    const munged = [...text].map((char) => {
        if (char === "\t") {
            const spaces = 8 - (column % 8);
            column += spaces;
            return " ".repeat(spaces);
        }
        column += 1;
        return /[\n\v\f\r]/.test(char) ? " " : char;
    }).join("");
    const chunks = munged.split(/([\t\n\v\f\r ]+)/).filter(Boolean).reverse();
    const lines = [];
    while (chunks.length) {
        const indent = lines.length ? rest : first;
        const width = WIDTH - charCount(indent);
        // A line other than the first never starts with whitespace.
        if (!chunks.at(-1).trim() && lines.length) chunks.pop();
        const line = [];
        let length = 0;
        while (chunks.length && length + charCount(chunks.at(-1)) <= width) {
            length += charCount(chunks.at(-1));
            line.push(chunks.pop());
        }
        if (chunks.length && charCount(chunks.at(-1)) > width && !line.length) line.push(chunks.pop());
        if (line.length && !line.at(-1).trim()) line.pop();
        if (line.length) lines.push(indent + line.join(""));
    }
    return lines;
};

/**
 * One block of # @ blocks: its # @ use line, the summary, notes and changed settings under
 * it, then the @setvar! lines of those settings.
 */
const blockLines = (loop, modules, entry) => {
    const module = modules.get(entry.ident);
    const {over} = loop;
    const changed = module.settings.filter((setting) => over.has(setting.name));
    const out = [BOX, `# @ use ${entry.ident}`, "#", ...wrapped(module.description[0])];
    if (Object.hasOwn(module.sections, "setup") && !Object.hasOwn(module.sections, "loop")) out.push("#   Runs once, before the loop.");
    out.push(...entry.notes.map((note) => `#   > ${note}`));
    for (const setting of changed) {
        const value = over.get(setting.name);
        const same = value.value === setting.value ? ", the same value" : "";
        out.push("#", `#   ${setting.name.slice("config__".length)} (default ${setting.value}${same})`);
        out.push(...setting.description.map((line) => (TEXT + line).trimEnd()));
        const readers = readBy(loop, setting.name);
        if (readers) out.push(...wrapped(readers, TEXT, `${TEXT}   `));
        out.push(...value.notes.map((note) => `${TEXT}> ${note}`));
    }
    return [...out, BOX, ...changed.map((setting) => `@setvar! ${setting.name} ${over.get(setting.name).value}`)];
};

/**
 * The recipe as the builder writes it back: notes, output, then each part in a "=" box,
 * every block in a "-" box with each change under the box of the block it belongs to.
 */
const recipeText = (loop, modules) => {
    const {recipe} = loop;
    const out = [...trimLines(recipe.notes), `# @ output ${recipe.output}`];
    const blocks = loop.entries.map((entry) => blockLines(loop, modules, entry));
    const parts = loop.layout.map((item) => (item.kind === "use"
        ? blocks[loop.entries.indexOf(item)]
        : [PART, `# @ ${item.kind} ${item.rest}`.trimEnd(), PART]));
    loop.entries.forEach((entry, i) => {
        const kept = new Set(blocks[i]);
        for (const {number, line} of entry.old) {
            if (!kept.has(line)) {
                console.error(`build-scripts: ${loop.name}:${number}: dropped a line under # @ use ${entry.ident} that the builder did not write. `
                    + `Write your own lines as "> " lines: ${line}`);
            }
        }
    });
    for (const section of RECIPE_SECTIONS) {
        if (!Object.hasOwn(recipe.sections, section)) continue;
        if (section === "blocks") {
            out.push("", "", PART, "# @ blocks", "#", ...BLOCKS_GUIDE, PART, "", ...joinParts(parts));
        } else {
            out.push("", "", PART, `# @ ${section}`, PART, "", ...trimLines(linesOf(recipe, section)));
        }
    }
    return textOf(out);
};

/**
 * The box over a piece of the loop: the file it came from, where its names are explained.
 */
const sourceBox = (source) => [BOX, `# ${source}`, BOX];

/**
 * A module's settings in CONFIG, with this loop's values. What they do and why the loop
 * changes them stay in the module and the recipe.
 */
const configPart = (loop, module) => {
    const values = module.code.config.map((line) => {
        const name = SETVAR.exec(line)[1];
        return loop.over.has(name) ? `@setvar! ${name} ${loop.over.get(name).value}` : line;
    });
    return [...sourceBox(modulePath(module.ident)), ...values];
};

/**
 * A module's timers, each made if missing and set to its start value.
 */
const timerLines = (unit) => {
    const out = [];
    for (const line of unit.code.timer ?? []) {
        const [, timer, start] = TIMER.exec(line.trim());
        if (out.length) out.push("");
        out.push(`if not timerexists "${timer}"`, `    createtimer "${timer}"`, "endif", `settimer "${timer}" ${start}`);
    }
    return out;
};

/**
 * The recipe text and the loop text, both as they should be on disk.
 */
const build = (path, modules, owner) => {
    const loop = prepare(path, modules, owner);
    const {recipe, name} = loop;
    const units = loop.order.map((ident) => [modulePath(ident), modules.get(ident)]);

    const declaring = (section, withRecipe = false) => {
        const found = [];
        for (const [source, unit] of units) {
            if (!Object.hasOwn(unit.sections, section)) continue;
            const code = section === "timer" ? timerLines(unit) : trimLines(unit.code[section]);
            if (code.length) found.push([...sourceBox(source), ...code]);
        }
        const own = trimLines(linesOf(recipe, section));
        if (withRecipe && own.length) found.push([...sourceBox(name), ...own]);
        if (section === "timer" && loop.clocks.length) {
            found.push([...sourceBox(name), ...timerLines({code: {timer: loop.clocks.map((clock) => clock.join(" "))}})]);
        }
        return found;
    };

    /**
     * The pass: each block's loop part in recipe order, groups wrapped in if and else.
     */
    const loopLines = () => {
        const out = [];
        let depth = 0;
        let gap = false;
        for (const item of loop.layout) {
            const pad = INDENT + "    ".repeat(depth);
            if (item.kind === "use") {
                const lines = trimLines(linesOf(modules.get(item.ident), "loop"));
                if (lines.length) {
                    if (gap) out.push("");
                    out.push(...blockBanner(lines, modulePath(item.ident), depth));
                    gap = true;
                }
                continue;
            }
            if (item.kind === "when") {
                if (gap) out.push("");
                out.push(`${pad}if ${item.rest}`);
                depth += 1;
            } else if (item.kind === "every") {
                if (gap) out.push("");
                out.push(`${pad}if timer "${item.timer}" >= ${item.rest}`, `${pad}    settimer "${item.timer}" 0`);
                depth += 1;
            } else if (item.kind === "otherwise") {
                out.push(`${INDENT}${"    ".repeat(depth - 1)}else`);
            } else {
                depth -= 1;
                out.push(`${INDENT}${"    ".repeat(depth)}endif`);
            }
            gap = item.kind === "end" || item.kind === "every";
        }
        const end = trimLines(linesOf(modules.get(BASE), "end"));
        return end.length ? [...out, "", ...blockBanner(end, modulePath(BASE))] : out;
    };

    const setupParts = [...units, [name, recipe]]
        .map(([source, unit]) => [source, trimLines(linesOf(unit, "setup"))])
        .filter(([, lines]) => lines.length)
        .map(([source, lines]) => [...sourceBox(source), ...lines]);

    const out = trimLines(linesOf(recipe, "header"));
    const hotkeys = [];
    for (const [, unit] of units) hotkeys.push(...unit.hotkeys.filter((hotkey) => !hotkeys.includes(hotkey)));
    if (hotkeys.length) {
        let line = "# Hotkeys: ";
        hotkeys.forEach((hotkey, i) => {
            const piece = hotkey + (i < hotkeys.length - 1 ? "," : ".");
            if (charCount(line) + charCount(piece) > 100 && line.trim() !== "# Hotkeys:") {
                out.push(line.trimEnd());
                line = "#          ";
            }
            line += `${piece} `;
        });
        out.push(line.trimEnd());
    }
    out.push(`# Generated from ${name} by util/build-scripts.mjs. Edit module/ and recipe/, not this file.`);

    const config = units.filter(([, unit]) => unit.code.config?.length).map(([, unit]) => configPart(loop, unit));
    const sections = [
        ["CONFIG", joinParts(config, 2)],
        ["WAIT AND COOLDOWN", joinParts(declaring("wait"), 2)],
        ["TIMER", joinParts(declaring("timer"), 2)],
        ["STATE", joinParts(declaring("state", true), 2)],
    ];
    for (const [title, lines] of sections) {
        if (lines.length) out.push("", "", ...banner(title), "", ...lines);
    }
    if (setupParts.length) out.push("", "", ...joinParts(setupParts, 2));
    out.push("", "", ...banner("MAIN LOOP"), "while not dead", ...loopLines(), "endwhile");

    for (const line of out) {
        if (line.trim().startsWith("#") && line.includes(";")) {
            throw new BuildError(`${name}: a comment has ";" (blueprint/razor.md part 3): ${line.trim()}`);
        }
    }
    return [[path, recipeText(loop, modules)], [join(REPO, recipe.output), textOf(out)]];
};

/**
 * Every setting of a loop, by module, with its value, meaning, readers, file and line.
 */
const settingsText = (path, modules, owner) => {
    const loop = prepare(path, modules, owner);
    const out = [`Settings of ${loop.name}. "*" marks the ones it changes.`];
    for (const ident of loop.order) {
        const module = modules.get(ident);
        if (!module.settings.length) continue;
        out.push("", "", `${modulePath(ident)}  ${module.description[0]}`);
        for (const setting of module.settings) {
            const value = loop.over.get(setting.name);
            const shown = value ? value.value : setting.value;
            let line = `  ${value ? "*" : " "} ${setting.name} ${shown}`;
            if (value) line += shown !== setting.value ? ` (default ${setting.value})` : " (same as the default)";
            out.push("", `${padEnd(line, 64)} ${modulePath(ident)}:${setting.number}`);
            out.push(...setting.description.map((description) => `        ${description}`));
            const readers = readBy(loop, setting.name);
            if (readers) out.push(`        ${readers}`);
            out.push(...(value ? value.notes : []).map((note) => `        This loop: ${note}`));
        }
    }
    return out.join("\n");
};

const template = ({box, rule, snake, title}) => `${box}
# One line on what this block does, shown in --settings and in the recipes that use it.
# More lines when the block needs them: what it waits for, why it works this way.
# @ hotkeys
${box}


${box}
# @ config
#   config__${snake}_example
#      What this setting changes. Each name a section declares is described in its box.
#        0  what 0 does
#        1  what 1 does
${box}
@setvar! config__${snake}_example 1


${box}
# @ loop
${box}
    # ${rule}
    # ${title}
    # One or two lines on what this block does in the pass.
    # ${rule}
`;

const newModule = (ident) => {
    const folders = readdirSync(MODULE_DIR, {withFileTypes: true}).filter((entry) => entry.isDirectory()).map((entry) => entry.name).sort();
    if (!/^[a-z]+\/[a-z0-9-]+$/.test(ident) || !folders.includes(ident.split("/")[0])) {
        throw new BuildError(`name a module <folder>/<name> in kebab-case. The folders are ${folders.join(", ")}. A new concern gets its own folder: make it first`);
    }
    const path = join(MODULE_DIR, `${ident}.razor`);
    if (existsSync(path)) throw new BuildError(`${rel(path)} already exists`);
    const name = ident.split("/")[1];
    const text = template({
        box: BOX,
        rule: "-".repeat(WIDTH - INDENT.length - 2),
        snake: name.replaceAll("-", "_"),
        title: name.replaceAll("-", " ").toUpperCase(),
    });
    writeFileSync(path, textOf(text.replace(/\n+$/, "").split("\n")));
    console.log(`wrote ${rel(path)}. Add "# @ use ${ident}" to the recipe that runs it.`);
};

const recipeFiles = () => readdirSync(join(REPO, "recipe"))
    .filter((file) => file.endsWith("-recipe.razor"))
    .sort()
    .map((file) => join(REPO, "recipe", file));

const main = (argv) => {
    const flags = argv.filter((arg) => arg.startsWith("--"));
    const args = argv.filter((arg) => !arg.startsWith("--"));
    if (flags.some((flag) => !["--check", "--settings", "--new-module"].includes(flag)) || (flags.includes("--settings") && !args.length)) {
        console.error(USAGE);
        return 2;
    }
    let modules;
    let owner;
    let paths;
    try {
        if (flags.includes("--new-module")) {
            for (const ident of args) newModule(ident);
            return 0;
        }
        ({modules, owner} = loadModules());
        paths = args.length ? args.map((arg) => (existsSync(arg) ? realpathSync(arg) : resolve(arg))) : recipeFiles();
        for (const path of paths) {
            if (!isFile(path) || !path.startsWith(REPO + sep)) throw new BuildError(`${path} is not a recipe file in this repository`);
        }
        if (flags.includes("--settings")) {
            console.log(paths.map((path) => settingsText(path, modules, owner)).join("\n\n\n"));
            return 0;
        }
    } catch (error) {
        if (!(error instanceof BuildError)) throw error;
        console.error(`build-scripts: ${error.message}`);
        return 1;
    }

    const check = flags.includes("--check");
    let failed = false;
    for (const path of paths) {
        let results;
        try {
            results = build(path, modules, owner);
        } catch (error) {
            if (!(error instanceof BuildError)) throw error;
            console.error(`build-scripts: ${error.message}`);
            failed = true;
            continue;
        }
        for (const [target, text] of results) {
            const current = isFile(target) ? readFileSync(target, "utf8") : null;
            if (current === text) continue;
            if (check) {
                console.error(`build-scripts: ${rel(target)} is out of date. Run node util/build-scripts.mjs`);
                failed = true;
            } else {
                writeFileSync(target, text);
                console.log(`wrote ${rel(target)}`);
            }
        }
    }
    if (check && !failed) console.log(`ok: ${paths.length} recipes, ${modules.size} modules`);
    return failed ? 1 : 0;
};

process.exitCode = main(process.argv.slice(2));
