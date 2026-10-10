// Conditional field-duel model. This is not a Razor/game-server emulator.
//
// Run: node util/pvp-sim.mjs --trials 2000 --output tmp/pvp-analysis/results.json
// Test: node --test util/pvp-sim.test.mjs
// Official numerical inputs and unmeasured policy assumptions are kept separate.
//
// Ported from the Python version with the same numbers out for the same seed: the random
// stream is CPython's Mersenne Twister, and rounding, sums and number formatting follow
// CPython (round half even, compensated float sums, int and float kept apart in the JSON).

import {mkdirSync, realpathSync, writeFileSync} from "node:fs";
import {basename, dirname} from "node:path";
import {pathToFileURL} from "node:url";

const DESCRIPTION = `Conditional field-duel model. This is not a Razor/game-server emulator.

Run: node util/pvp-sim.mjs --trials 2000 --output tmp/pvp-analysis/results.json
Official numerical inputs and unmeasured policy assumptions are kept separate.`;

export const PLAYER_SKILLS = {
    Lumberjacking: 120, Swordsmanship: 100, Tactics: 100,
    Magery: 80, Tracking: 80, Resist: 80, Anatomy: 80, Healing: 80,
};
export const MAGE_SKILLS = {
    Magery: 100, Eval: 100, Meditation: 100, Wrestling: 100,
    Resist: 100, Tracking: 100, Alchemy: 120,
};
// name: [mana cost, cast seconds, travel seconds, circle]
export const SPELLS = {
    ma: [4, 0.5, 0.5, 1], tk: [9, 1, 0, 3],
    explosion: [20, 1.75, 2.5, 6], eb: [20, 1.75, 0.5, 6],
    gh: [11, 1.25, 0, 4], heal: [4, 0.5, 0, 1], ra: [4, 0.5, 0, 1],
};
const SOURCES = {
    weapons: "https://wiki.uooutlands.com/Swordsmanship",
    swing: "https://wiki.uooutlands.com/Swing_Speed",
    damage_cap: "https://wiki.uooutlands.com/PvP_Damage_Cap",
    magery: "https://wiki.uooutlands.com/Magery",
    resist: "https://wiki.uooutlands.com/Resisting_Spells",
    healing: "https://wiki.uooutlands.com/Healing",
    alchemy: "https://wiki.uooutlands.com/Alchemy",
    armor: "https://wiki.uooutlands.com/Armor_%26_Weapons",
    meditation: "https://wiki.uooutlands.com/Meditation",
    anatomy: "https://wiki.uooutlands.com/Anatomy",
    tk: "https://uooutlands.com/news/patch-september-28-murderer-and-pvp-overhaul-general-changes/",
    mushroom: "https://uooutlands.com/news/patch-march-5-wizards-grimoire-new-player-rental-credit-deeds-society-job-updates/",
};

// ----------------------------------------------------------------------------------------
// CPython random.Random
// ----------------------------------------------------------------------------------------

const MT_N = 624;
const MT_M = 397;

/**
 * random.Random from CPython: MT19937 seeded from an int the way random.seed does it, and
 * the few methods this model calls, each with CPython's own algorithm.
 */
export class PyRandom {
    constructor(seed) {
        this.state = new Uint32Array(MT_N);
        this.index = MT_N + 1;
        this.seed(seed);
    }

    /** random.seed(int): the absolute value, split into 32-bit words, low word first. */
    seed(seed) {
        let rest = BigInt(seed);

        if (rest < 0n) {
            rest = -rest;
        }

        const key = [];

        while (rest > 0n) {
            key.push(Number(rest & 0xffffffffn));
            rest >>= 32n;
        }

        if (key.length === 0) {
            key.push(0);
        }

        this.initByArray(key);
    }

    initGenrand(seed) {
        const mt = this.state;

        mt[0] = seed >>> 0;

        for (let i = 1; i < MT_N; i++) {
            mt[i] = (Math.imul(1812433253, mt[i - 1] ^ (mt[i - 1] >>> 30)) + i) >>> 0;
        }

        this.index = MT_N;
    }

    initByArray(key) {
        const mt = this.state;
        let i = 1;
        let j = 0;

        this.initGenrand(19650218);

        for (let k = Math.max(MT_N, key.length); k > 0; k--) {
            mt[i] = ((mt[i] ^ Math.imul(mt[i - 1] ^ (mt[i - 1] >>> 30), 1664525)) + key[j] + j) >>> 0;
            i++;
            j++;

            if (i >= MT_N) {
                mt[0] = mt[MT_N - 1];
                i = 1;
            }

            if (j >= key.length) {
                j = 0;
            }
        }

        for (let k = MT_N - 1; k > 0; k--) {
            mt[i] = ((mt[i] ^ Math.imul(mt[i - 1] ^ (mt[i - 1] >>> 30), 1566083941)) - i) >>> 0;
            i++;

            if (i >= MT_N) {
                mt[0] = mt[MT_N - 1];
                i = 1;
            }
        }

        mt[0] = 0x80000000;
    }

    /** genrand_uint32: the next tempered 32-bit word, regenerating the table when used up. */
    nextUint32() {
        const mt = this.state;

        if (this.index >= MT_N) {
            for (let kk = 0; kk < MT_N; kk++) {
                const y = (mt[kk] & 0x80000000) | (mt[(kk + 1) % MT_N] & 0x7fffffff);

                mt[kk] = mt[(kk + MT_M) % MT_N] ^ (y >>> 1) ^ (y & 1 ? 0x9908b0df : 0);
            }

            this.index = 0;
        }

        let y = mt[this.index++];

        y ^= y >>> 11;
        y ^= (y << 7) & 0x9d2c5680;
        y ^= (y << 15) & 0xefc60000;
        y ^= y >>> 18;

        return y >>> 0;
    }

    /** random(): 53 bits from two words, a 27-bit and a 26-bit part. */
    random() {
        const high = this.nextUint32() >>> 5;
        const low = this.nextUint32() >>> 6;

        return (high * 67108864 + low) * (1 / 9007199254740992);
    }

    /** getrandbits(k) for k up to 32, the only widths randint needs here. */
    getrandbits(bits) {
        if (bits === 0) {
            return 0;
        }

        if (bits > 32) {
            throw new RangeError("getrandbits is only ported for up to 32 bits");
        }

        return this.nextUint32() >>> (32 - bits);
    }

    /** _randbelow_with_getrandbits: draw n.bit_length() bits until the value is below n. */
    randbelow(limit) {
        const bits = limit.toString(2).length;
        let value = this.getrandbits(bits);

        while (value >= limit) {
            value = this.getrandbits(bits);
        }

        return value;
    }

    randint(low, high) {
        const width = high + 1 - low;

        if (width <= 0) {
            throw new RangeError(`empty range in randint(${low}, ${high})`);
        }

        return low + this.randbelow(width);
    }

    uniform(low, high) {
        return low + (high - low) * this.random();
    }

    expovariate(rate) {
        return -Math.log(1 - this.random()) / rate;
    }
}

// ----------------------------------------------------------------------------------------
// CPython numbers: round, repr, format and sum
// ----------------------------------------------------------------------------------------

const float_view = new DataView(new ArrayBuffer(8));

/**
 * The exact value of a finite double as digits / 10 ** scale. Every double has a finite
 * decimal expansion, so the rounding below works on the true value, as CPython's dtoa does.
 */
const exactDecimal = (value) => {
    float_view.setFloat64(0, value);

    const high = float_view.getUint32(0);
    const low = float_view.getUint32(4);
    const biased = (high >>> 20) & 0x7ff;
    let mantissa = (BigInt(high & 0xfffff) << 32n) | BigInt(low);
    let exponent = -1074;

    if (biased !== 0) {
        mantissa |= 1n << 52n;
        exponent = biased - 1075;
    }

    const negative = high >>> 31 === 1;

    if (exponent >= 0) {
        return {negative, digits: mantissa << BigInt(exponent), scale: 0};
    }

    return {negative, digits: mantissa * 5n ** BigInt(-exponent), scale: -exponent};
};

/** digits / 10 ** scale rounded to `places` decimals, half to even. The result is over 10 ** places. */
const roundDigits = (digits, scale, places) => {
    const shift = scale - places;

    if (shift <= 0) {
        return digits * 10n ** BigInt(-shift);
    }

    const divisor = 10n ** BigInt(shift);
    let quotient = digits / divisor;
    const twice = (digits % divisor) * 2n;

    if (twice > divisor || (twice === divisor && (quotient & 1n) === 1n)) {
        quotient += 1n;
    }

    return quotient;
};

/** Python round(x, places) for a float: the double nearest the correctly rounded decimal. */
export const pyRound = (value, places) => {
    if (!Number.isFinite(value) || value === 0) {
        return value;
    }

    const {negative, digits, scale} = exactDecimal(value);

    if (scale <= places) {
        return value;
    }

    return Number(`${negative ? "-" : ""}${roundDigits(digits, scale, places)}e-${places}`);
};

/** Python round(x) for a float: the nearest int, half to even. */
const pyRoundToInt = (value) => {
    const floor = Math.floor(value);
    const fraction = value - floor;

    if (fraction > 0.5 || (fraction === 0.5 && floor % 2 !== 0)) {
        return floor + 1;
    }

    return floor;
};

/** The shortest digits that read back as the value, and the power of ten of the first one. */
const shortestDigits = (value) => {
    const [mantissa, exponent] = Math.abs(value).toExponential().split("e");

    return {digits: mantissa.replace(".", ""), exponent: Number(exponent)};
};

const exponentText = (exponent) => `e${exponent < 0 ? "-" : "+"}${String(Math.abs(exponent)).padStart(2, "0")}`;

/** Python repr(float): fixed between 1e-4 and 1e16 with at least one decimal, else 1e-05. */
export const pyRepr = (value) => {
    if (Number.isNaN(value)) {
        return "nan";
    }

    if (!Number.isFinite(value)) {
        return value < 0 ? "-inf" : "inf";
    }

    if (value === 0) {
        return Object.is(value, -0) ? "-0.0" : "0.0";
    }

    const sign = value < 0 ? "-" : "";
    const {digits, exponent} = shortestDigits(value);

    if (exponent < -4 || exponent >= 16) {
        const fraction = digits.length > 1 ? `.${digits.slice(1)}` : "";

        return `${sign}${digits[0]}${fraction}${exponentText(exponent)}`;
    }

    if (exponent < 0) {
        return `${sign}0.${"0".repeat(-exponent - 1)}${digits}`;
    }

    const whole = digits.slice(0, exponent + 1).padEnd(exponent + 1, "0");
    const fraction = digits.slice(exponent + 1) || "0";

    return `${sign}${whole}.${fraction}`;
};

/** Python format(x, ".Nf"): fixed decimals, half to even on the exact value. */
const formatFixed = (value, places) => {
    if (Number.isNaN(value)) {
        return "nan";
    }

    if (!Number.isFinite(value)) {
        return value < 0 ? "-inf" : "inf";
    }

    const {negative, digits, scale} = exactDecimal(value);
    const text = roundDigits(digits, scale, places).toString().padStart(places + 1, "0");
    const whole = text.slice(0, text.length - places);
    const fraction = places > 0 ? `.${text.slice(text.length - places)}` : "";

    return `${negative ? "-" : ""}${whole}${fraction}`;
};

/** Python format(x, ".0%"). */
const formatPercent = (value) => `${formatFixed(value * 100, 0)}%`;

/** Python format(x, "g"): six significant digits, trailing zeros dropped, 1e-05 outside 1e-4..1e6. */
export const formatG = (value, precision = 6) => {
    if (Number.isNaN(value)) {
        return "nan";
    }

    if (!Number.isFinite(value)) {
        return value < 0 ? "-inf" : "inf";
    }

    if (value === 0) {
        return Object.is(value, -0) ? "-0" : "0";
    }

    const significant = Math.max(precision, 1);
    const {negative, digits, scale} = exactDecimal(value);
    const leading = digits.toString().length - 1 - scale;
    let rounded = roundDigits(digits, scale, significant - 1 - leading).toString();
    let exponent = leading;

    if (rounded.length > significant) {
        // Rounding carried into a new digit, as 999999.5 becomes 1e+06.
        rounded = rounded.slice(0, significant);
        exponent += 1;
    }

    const sign = negative ? "-" : "";

    if (exponent >= -4 && exponent < significant) {
        const whole = exponent >= 0 ? rounded.slice(0, exponent + 1) : "0";
        const fraction = (exponent >= 0 ? rounded.slice(exponent + 1) : "0".repeat(-exponent - 1) + rounded).replace(/0+$/, "");

        return `${sign}${whole}${fraction ? `.${fraction}` : ""}`;
    }

    const fraction = rounded.slice(1).replace(/0+$/, "");

    return `${sign}${rounded[0]}${fraction ? `.${fraction}` : ""}${exponentText(exponent)}`;
};

/**
 * Python sum() over a list of [value, isInt] pairs, as CPython 3.12+ adds them: leading ints
 * exactly, then floats with Neumaier compensation, while ints met after a float are added
 * plainly. Returns [total, isInt].
 */
const pySum = (items) => {
    let index = 0;
    let intTotal = 0;

    while (index < items.length && items[index][1]) {
        intTotal += items[index][0];
        index++;
    }

    if (index === items.length) {
        return [intTotal, true];
    }

    let total = intTotal + items[index][0];
    let compensation = 0;

    for (index += 1; index < items.length; index++) {
        const [value, isInt] = items[index];

        if (isInt) {
            total += value;
            continue;
        }

        const next = total + value;

        if (Math.abs(total) >= Math.abs(value)) {
            compensation += total - next + value;
        } else {
            compensation += value - next + total;
        }

        total = next;
    }

    if (compensation !== 0 && Number.isFinite(compensation)) {
        total += compensation;
    }

    return [total, false];
};

/** A number Python holds as a float, so the JSON writes it as one (1.0, not 1). */
class PyFloat {
    constructor(value) {
        this.value = value;
    }
}

const pyFloat = (value) => new PyFloat(value);

/** json.dumps(value, ensure_ascii=False, indent=2) for dicts, lists, str, int, PyFloat. */
const pyJson = (value, depth = 0) => {
    if (value instanceof PyFloat) {
        if (Number.isNaN(value.value)) {
            return "NaN";
        }

        if (!Number.isFinite(value.value)) {
            return value.value < 0 ? "-Infinity" : "Infinity";
        }

        return pyRepr(value.value);
    }

    if (typeof value === "string") {
        return JSON.stringify(value);
    }

    if (typeof value === "number" || typeof value === "bigint" || typeof value === "boolean") {
        return String(value);
    }

    if (value === null) {
        return "null";
    }

    const inner = "  ".repeat(depth + 1);
    const outer = "  ".repeat(depth);

    if (Array.isArray(value)) {
        if (value.length === 0) {
            return "[]";
        }

        return `[\n${value.map((item) => inner + pyJson(item, depth + 1)).join(",\n")}\n${outer}]`;
    }

    const entries = Object.entries(value);

    if (entries.length === 0) {
        return "{}";
    }

    return `{\n${entries.map(([key, item]) => `${inner}${JSON.stringify(key)}: ${pyJson(item, depth + 1)}`).join(",\n")}\n${outer}}`;
};

// ----------------------------------------------------------------------------------------
// Model
// ----------------------------------------------------------------------------------------

// Field order is the JSON order. A field Python holds as a float is listed in float_fields.
const CONFIG_FIELDS = ["contact", "close_bout", "mage_ar", "failed_mana_fraction", "mage_mana_reserve", "potion_fuse", "dt"];
const CONFIG_DEFAULTS = {contact: 0.5, close_bout: 2, mage_ar: 50, failed_mana_fraction: 0, mage_mana_reserve: 11, potion_fuse: 2, dt: 0.05};

/**
 * The frozen Config dataclass. A value that is not a whole number is a float, and so is any
 * field named in `floats`, which is how a whole number read as a float (11.0) is told apart.
 */
export const makeConfig = (fields = {}, {floats = []} = {}) => {
    const config = {...CONFIG_DEFAULTS, ...fields};
    const floatFields = new Set(floats);

    for (const name of CONFIG_FIELDS) {
        const defaultFloat = !(name in fields) && !Number.isInteger(CONFIG_DEFAULTS[name]);

        if (defaultFloat || !Number.isInteger(config[name])) {
            floatFields.add(name);
        }
    }

    return Object.freeze({...config, floatFields});
};

/**
 * One duelist. hp and mana carry whether Python holds them as an int (a whole value set by
 * min/max or the start) or a float, because CPython's sum adds the two kinds differently.
 */
export class Fighter {
    constructor(magery, evaluation, tracking, resist, alchemy, maxMana, manaRegen, {hp = 120, mana = 0, armor = 0, raPool = 0} = {}) {
        this.magery = magery;
        this.evaluation = evaluation;
        this.tracking = tracking;
        this.resist = resist;
        this.alchemy = alchemy;
        this.maxMana = maxMana;
        this.manaRegen = manaRegen;
        this.hp = hp;
        this.hpIsInt = Number.isInteger(hp);
        this.mana = mana;
        this.manaIsInt = Number.isInteger(mana);
        this.armor = armor;
        this.raPool = raPool;
        this.reflect = true;
        this.cast = null;
        this.readyAt = 0;
        this.healPotAt = 0;
        this.bandageAt = null;
        this.bandageSlips = 0;
        this.healRetryAt = 0;
        this.buffRetryAt = 0;
        this.manualMaAt = 8;
        this.tkReadyAt = 30;
        this.tkImmuneAt = 0;
        this.stickyUntil = 30;
        this.bombAt = 15;
        this.stickyUsed = false;
        this.mageOpenerDone = false;
        this.nextAttack = "explosion";
        this.interruptWindows = new Map();
        this.swings = 0;
        this.hits = 0;
        this.interruptions = 0;
    }

    /** hp = min(120, hp + amount) for a float amount. */
    healBy(amount) {
        const next = this.hp + amount;

        this.hp = next < 120 ? next : 120;
        this.hpIsInt = next >= 120;
    }

    /** hp = max(0, hp - amount) for a float amount. */
    hurtBy(amount) {
        const next = this.hp - amount;

        this.hp = next > 0 ? next : 0;
        this.hpIsInt = next <= 0;
    }

    /** mana = max(0, mana - cost). */
    spendMana(cost, costIsInt) {
        const next = this.mana - cost;

        this.mana = next > 0 ? next : 0;
        this.manaIsInt = next > 0 ? this.manaIsInt && costIsInt : true;
    }

    /** mana = min(max_mana, mana + amount) for a float amount. */
    regainMana(amount) {
        const next = this.mana + amount;

        this.mana = next < this.maxMana ? next : this.maxMana;
        this.manaIsInt = next >= this.maxMana;
    }
}

export const weaponRoll = (weapon, rng) => {
    const [base, sides] = weapon === "great" ? [16, 6] : [8, 3];
    let total = 0;

    for (let die = 0; die < 5; die++) {
        total += rng.randint(1, sides);
    }

    return base + total;
};

export const swingDelay = (weapon, stamina) => {
    const speed = weapon === "great" ? 25 : 48;

    return 15000 / ((Math.min(stamina, 100) + 100) * speed);
};

export const spellScalar = (magery, evaluation, tracking) => (
    magery / 100 * (0.75 + 0.375 * evaluation / 100 + Math.min(0.10, 0.10 * tracking / 100))
);

export const bandageAmount = (rng, slips) => 0.8 * rng.uniform(40, 60) * 1.16 * Math.max(0, 1 - 0.02 * slips);

export const potionSplit = (amount, close) => (close ? [amount / 2, amount / 2] : [amount, 0]);

export const outcome = (playerHp, mageHp) => {
    if (playerHp <= 0 && mageHp <= 0) {
        return "mutual";
    }

    if (mageHp <= 0) {
        return "win";
    }

    if (playerHp <= 0) {
        return "loss";
    }

    return "undecided";
};

export const startCast = (fighter, name, now) => {
    const [cost, duration] = SPELLS[name];

    if (fighter.cast !== null || now < fighter.readyAt || fighter.mana < cost) {
        return false;
    }

    fighter.cast = [name, now + duration];

    return true;
};

export const interrupt = (fighter, now, config) => {
    if (fighter.cast === null) {
        return;
    }

    const [name] = fighter.cast;

    fighter.spendMana(SPELLS[name][0] * config.failed_mana_fraction, !config.floatFields.has("failed_mana_fraction"));
    fighter.cast = null;
    fighter.readyAt = now + 0.2;
    fighter.interruptions += 1;
};

export const lowCircleInterrupt = (fighter, circle, now, config) => {
    const allowed = now >= (fighter.interruptWindows.get(circle) ?? -1);

    fighter.interruptWindows.set(circle, now + 5);

    if (allowed) {
        interrupt(fighter, now, config);
    }
};

export const damage = (fighter, amount, now, config, circle = null) => {
    fighter.hurtBy(amount);

    if (fighter.bandageAt !== null && amount > 0) {
        fighter.bandageSlips += 1;
    }

    if (circle === null || circle >= 4) {
        interrupt(fighter, now, config);
    } else {
        lowCircleInterrupt(fighter, circle, now, config);
    }
};

/**
 * The state at one moment. Which numbers Python holds as ints rides along out of sight
 * (pyInts, not enumerable), for the sums in aggregate.
 */
export const snapshot = (player, mage, now) => {
    const row = {
        outcome: outcome(player.hp, mage.hp), at: pyRound(now, 2),
        player_hp: player.hpIsInt ? player.hp : pyRound(player.hp, 2),
        mage_hp: mage.hpIsInt ? mage.hp : pyRound(mage.hp, 2),
        player_mana: player.manaIsInt ? player.mana : pyRound(player.mana, 2),
        mage_mana: mage.manaIsInt ? mage.mana : pyRound(mage.mana, 2),
        swings: player.swings, hits: player.hits,
        player_interruptions: player.interruptions, mage_interruptions: mage.interruptions,
    };
    const pyInts = new Set(["swings", "hits", "player_interruptions", "mage_interruptions"]);

    for (const [key, isInt] of [["player_hp", player.hpIsInt], ["mage_hp", mage.hpIsInt], ["player_mana", player.manaIsInt], ["mage_mana", mage.manaIsInt]]) {
        if (isInt) {
            pyInts.add(key);
        }
    }

    Object.defineProperty(row, "pyInts", {value: pyInts, enumerable: false});

    return row;
};

/** A min-heap of [at, id, kind, source, value], ordered like Python tuples by at, then id. */
class EventQueue {
    constructor() {
        this.items = [];
    }

    get size() {
        return this.items.length;
    }

    peek() {
        return this.items[0];
    }

    static before(a, b) {
        return a[0] < b[0] || (a[0] === b[0] && a[1] < b[1]);
    }

    push(event) {
        const items = this.items;
        let child = items.push(event) - 1;

        while (child > 0) {
            const parent = (child - 1) >> 1;

            if (!EventQueue.before(items[child], items[parent])) {
                break;
            }

            [items[child], items[parent]] = [items[parent], items[child]];
            child = parent;
        }
    }

    pop() {
        const items = this.items;
        const top = items[0];
        const last = items.pop();

        if (items.length > 0) {
            items[0] = last;

            let parent = 0;

            for (;;) {
                const left = 2 * parent + 1;
                const right = left + 1;
                let smallest = parent;

                if (left < items.length && EventQueue.before(items[left], items[smallest])) {
                    smallest = left;
                }

                if (right < items.length && EventQueue.before(items[right], items[smallest])) {
                    smallest = right;
                }

                if (smallest === parent) {
                    break;
                }

                [items[parent], items[smallest]] = [items[smallest], items[parent]];
                parent = smallest;
            }
        }

        return top;
    }
}

// round(step * dt, 6) for every tick, kept per dt: the rounding is exact and not cheap.
const tick_time_cache = new Map();

const tickTimes = (dt, steps) => {
    if (!tick_time_cache.has(dt)) {
        tick_time_cache.set(dt, Array.from({length: steps + 1}, (_, step) => pyRound(step * dt, 6)));
    }

    return tick_time_cache.get(dt);
};

export const trial = (config, seed) => {
    const rng = new PyRandom(seed);
    const player = new Fighter(80, 0, 80, 80, 0, 45, 0.5, {mana: 36, armor: 47, raPool: 20});
    const mage = new Fighter(100, 100, 100, 100, 120, 100, 1, {mana: 91, armor: config.mage_ar, raPool: 25});
    const fighters = [player, mage];

    player.readyAt = mage.readyAt = 0.2;
    // Both initial TK casts have completed at t=0, costing 9 mana each.
    // Both opening potions are attached at t=.2. One potion per successful TK.
    const events = new EventQueue();
    let eventId = 0;

    const enqueue = (at, kind, source, value = null) => {
        eventId += 1;
        events.push([at, eventId, kind, source, value]);
    };

    const throwBomb = (source, now) => {
        const caster = fighters[source];
        const victim = fighters[1 - source];

        if (caster.stickyUsed || now >= caster.stickyUntil || now < caster.bombAt) {
            return;
        }

        caster.stickyUsed = true;
        caster.bombAt = now + 15;
        victim.tkImmuneAt = now + 30;
        caster.readyAt = Math.max(caster.readyAt, now + 0.2);

        const amount = rng.uniform(15, 25) * (1 + 0.5 * caster.alchemy / 100);

        enqueue(now + config.potion_fuse, "bomb", source, amount);
    };

    for (const source of [0, 1]) {
        fighters[source].bombAt = 0;
        enqueue(0.2, "throw", source);
    }

    let close = rng.random() < config.contact;
    let contactChange;

    if (config.contact === 0 || config.contact === 1) {
        contactChange = Infinity;
    } else {
        const mean = close ? config.close_bout : config.close_bout * (1 - config.contact) / config.contact;

        contactChange = rng.expovariate(1 / mean);
    }

    let lastSwing = -3;
    const results = {};
    const steps = pyRoundToInt(60 / config.dt);
    const times = tickTimes(config.dt, steps);

    const finish = (now) => {
        const terminal = snapshot(player, mage, now);

        if (!(30 in results)) {
            results[30] = terminal;
        }

        results[60] = terminal;
    };

    for (let step = 0; step <= steps; step++) {
        const now = times[step];

        if (now >= contactChange) {
            close = !close;

            const mean = close ? config.close_bout : config.close_bout * (1 - config.contact) / config.contact;

            contactChange = now + rng.expovariate(1 / mean);
        }

        if (step) {
            for (const actor of fighters) {
                actor.regainMana(actor.manaRegen * config.dt);
                actor.healBy(0.25 * config.dt);
            }
        }

        // Completing casts precede damage at an exact tick tie, a model convention.
        for (const [source, actor] of fighters.entries()) {
            if (actor.cast === null || now < actor.cast[1]) {
                continue;
            }

            const [name] = actor.cast;

            actor.cast = null;
            actor.readyAt = now + 0.2;
            actor.spendMana(SPELLS[name][0], true);

            if (name === "gh" || name === "heal") {
                const [low, high] = name === "gh" ? [40, 50] : [6, 9];

                actor.healBy(rng.uniform(low, high) * actor.magery / 100);
            } else if (name === "ra") {
                actor.raPool = 25 * actor.magery / 100;
            } else if (name === "tk") {
                actor.stickyUntil = now + 30;
                actor.stickyUsed = false;
                actor.tkReadyAt = now + 30;
                fighters[1 - source].tkImmuneAt = now + 30;
                enqueue(now, "throw", source);
                enqueue(now, "tk", source);
            } else {
                enqueue(now + SPELLS[name][2], "spell", source, name);
            }
        }

        // Process both bombs/delayed spells before checking terminal outcomes.
        while (events.size > 0 && events.peek()[0] <= now) {
            const [, , kind, source, value] = events.pop();
            const caster = fighters[source];
            let victim = fighters[1 - source];

            if (kind === "throw") {
                throwBomb(source, now);
            } else if (kind === "bomb") {
                const [outgoing, splash] = potionSplit(value, close);

                damage(victim, outgoing, now, config);

                if (splash) {
                    damage(caster, splash, now, config);
                }
            } else if (kind === "tk") {
                // TK does not consume Reflection in the user's recorded field test.
                lowCircleInterrupt(victim, 3, now, config);
            } else if (kind === "spell") {
                if (victim.reflect) {
                    victim.reflect = false;
                    victim = caster; // One bounce, no infinite mirror chain.
                }

                const [low, high] = value === "ma" ? [5, 7] : [28, 36];
                const reduction = rng.uniform(0.125, 0.375) * victim.resist / 100;
                const amount = rng.uniform(low, high) * spellScalar(caster.magery, caster.evaluation, caster.tracking) * (1 - reduction);

                damage(victim, amount, now, config, SPELLS[value][3]);
            }
        }

        if (player.hp > 0 && player.bandageAt !== null && now >= player.bandageAt) {
            player.healBy(bandageAmount(rng, player.bandageSlips));
            player.bandageAt = null;
        }

        if (outcome(player.hp, mage.hp) !== "undecided") {
            finish(now);
            break;
        }

        for (const actor of fighters) {
            if (actor.cast === null && now >= actor.readyAt) {
                if (120 - actor.hp >= 35 && now >= actor.healPotAt) {
                    actor.healBy(rng.uniform(19, 26) * (1 + 0.25 * actor.alchemy / 100));
                    actor.healPotAt = now + 10;
                    actor.readyAt = now + 0.2;
                }
            }
        }

        if (player.cast === null && now >= player.readyAt) {
            if (player.bandageAt === null && player.hp < 120) {
                player.bandageAt = now + 10;
                player.bandageSlips = 0;
                player.readyAt = now + 0.2;
            } else if (120 - player.hp >= 45 && now >= player.healRetryAt && player.mana >= 11) {
                player.healRetryAt = now + 2.5;
                startCast(player, "gh", now);
            } else if (!player.raPool && player.hp > 105 && now >= player.buffRetryAt && player.mana >= 4) {
                player.buffRetryAt = now + 5;
                startCast(player, "ra", now);
            } else if (now >= Math.max(player.tkReadyAt, mage.tkImmuneAt) && player.mana >= 29) {
                startCast(player, "tk", now);
            } else if (!player.mageOpenerDone || (!close && now >= player.manualMaAt && player.mana >= 24)) {
                if (startCast(player, "ma", now)) {
                    player.mageOpenerDone = true;
                    player.manualMaAt = now + 8;
                }
            }
        }

        if (mage.cast === null && now >= mage.readyAt) {
            if (mage.hp <= 85 && mage.mana >= 11) {
                startCast(mage, "gh", now);
            } else if (!mage.raPool && mage.mana >= 4) {
                startCast(mage, "ra", now);
            } else if (now >= Math.max(mage.tkReadyAt, player.tkImmuneAt) && mage.mana >= 9 + config.mage_mana_reserve) {
                startCast(mage, "tk", now);
            } else if (!mage.mageOpenerDone) {
                if (startCast(mage, "ma", now)) {
                    mage.mageOpenerDone = true;
                }
            } else if (mage.mana >= 20 + config.mage_mana_reserve && startCast(mage, mage.nextAttack, now)) {
                mage.nextAttack = mage.nextAttack === "explosion" ? "eb" : "explosion";
            } else if (mage.mana >= 4 + config.mage_mana_reserve) {
                // Low-mana harassment is also conditional on this policy, not optimal play.
                startCast(mage, "ma", now);
            }
        }

        if (close && player.cast === null && now >= player.readyAt) {
            const elapsed = now - lastSwing;
            const weapon = elapsed >= swingDelay("great", 100) ? "great" : "norse";

            if (elapsed >= swingDelay(weapon, 100)) {
                lastSwing = now; // Misses also consume a swing.
                player.swings += 1;

                if (rng.random() < 0.5) {
                    player.hits += 1;

                    let amount = weaponRoll(weapon, rng) * 1.36;

                    amount *= 1 - rng.uniform(mage.armor * 0.00333, mage.armor * 0.00666);

                    const absorbed = Math.min(mage.raPool, amount * 0.2);

                    mage.raPool -= absorbed;
                    damage(mage, amount - absorbed, now, config);
                }
            }
        }

        if (outcome(player.hp, mage.hp) !== "undecided") {
            finish(now);
            break;
        }

        if (now === 30 || now === 60) {
            results[now] = snapshot(player, mage, now);
        }
    }

    return results;
};

const OUTCOMES = ["win", "loss", "mutual", "undecided"];
const MEAN_KEYS = ["player_hp", "mage_hp", "player_mana", "mage_mana", "hits", "mage_interruptions"];

export const aggregate = (config, trials, seed) => {
    const first = BigInt(seed);
    const samples = Array.from({length: trials}, (_, n) => trial(config, first + BigInt(n)));
    const asdict = Object.fromEntries(CONFIG_FIELDS.map((name) => [name, config.floatFields.has(name) ? pyFloat(config[name]) : config[name]]));
    const result = {config: asdict, trials, seed: first, durations: {}};

    for (const duration of [30, 60]) {
        const rows = samples.map((sample) => sample[duration]);
        const counts = Object.fromEntries(OUTCOMES.map((key) => [key, 0]));

        for (const row of rows) {
            counts[row.outcome] += 1;
        }

        result.durations[duration] = {
            counts: Object.fromEntries(OUTCOMES.map((key) => [key, counts[key]])),
            percent: Object.fromEntries(OUTCOMES.map((key) => [key, pyFloat(pyRound(100 * counts[key] / trials, 1))])),
            means_all_trials: Object.fromEntries(MEAN_KEYS.map((key) => {
                const [total] = pySum(rows.map((row) => [row[key], row.pyInts.has(key)]));

                return [key, pyFloat(pyRound(total / trials, 1))];
            })),
        };
    }

    return result;
};

// ----------------------------------------------------------------------------------------
// Command line, shaped like the argparse one
// ----------------------------------------------------------------------------------------

const OPTIONS = [
    {flag: "--trials", dest: "trials", type: "int"},
    {flag: "--seed", dest: "seed", type: "int"},
    {flag: "--mage-reserve", dest: "mage_reserve", type: "float"},
    {flag: "--potion-fuse", dest: "potion_fuse", type: "float"},
    {flag: "--output", dest: "output", type: "path"},
];

const helpWidth = () => Math.max(Number(process.env.COLUMNS) || process.stdout.columns || 80, 13) - 2;

const usageText = (prog) => {
    const parts = ["[-h]", ...OPTIONS.map((option) => `[${option.flag} ${option.dest.toUpperCase()}]`)];
    const prefix = `usage: ${prog} `;
    const width = helpWidth();

    if (prefix.length + parts.join(" ").length <= width) {
        return `${prefix}${parts.join(" ")}\n`;
    }

    const lines = [];
    let line = [];
    let length = prefix.length - 1;

    for (const part of parts) {
        if (length + 1 + part.length > width && line.length > 0) {
            lines.push(line.join(" "));
            line = [];
            length = prefix.length - 1;
        }

        line.push(part);
        length += part.length + 1;
    }

    lines.push(line.join(" "));

    return `${prefix}${lines.join(`\n${" ".repeat(prefix.length)}`)}\n`;
};

const fillText = (text, width) => {
    const lines = [];
    let line = "";

    for (const word of text.split(/\s+/).filter(Boolean)) {
        if (line && line.length + 1 + word.length > width) {
            lines.push(line);
            line = word;
        } else {
            line = line ? `${line} ${word}` : word;
        }
    }

    return [...lines, line].join("\n");
};

const helpText = (prog) => [
    usageText(prog),
    `${fillText(DESCRIPTION, helpWidth())}\n`,
    "options:",
    "  -h, --help            show this help message and exit",
    ...OPTIONS.map((option) => `  ${option.flag} ${option.dest.toUpperCase()}`),
    "",
].join("\n");

const fail = (prog, message) => {
    process.stderr.write(`${usageText(prog)}${prog}: error: ${message}\n`);
    process.exit(2);
};

const parseInt10 = (text) => (/^\s*[+-]?\d+(?:_\d+)*\s*$/.test(text) ? BigInt(text.trim().replaceAll("_", "")) : null);

const parseFloat10 = (text) => {
    const trimmed = text.trim();
    const special = /^([+-]?)(inf|infinity|nan)$/i.exec(trimmed);

    if (special) {
        return special[2].toLowerCase() === "nan" ? NaN : (special[1] === "-" ? -Infinity : Infinity);
    }

    const digits = String.raw`\d(?:_?\d)*`;
    const number = new RegExp(String.raw`^[+-]?(?:${digits}(?:\.(?:${digits})?)?|\.${digits})(?:[eE][+-]?${digits})?$`);

    return number.test(trimmed) ? Number(trimmed.replaceAll("_", "")) : null;
};

/** argparse rules this script meets: --flag value, --flag=value, unique prefixes, -h. */
const parseArgs = (argv, prog) => {
    const args = {trials: 2000n, seed: 410n, mage_reserve: 11, potion_fuse: 2, output: null};
    const given = new Set();
    const unknown = [];
    const looksLikeNegativeNumber = (text) => /^-\d+$|^-\d*\.\d+$/.test(text);

    for (let index = 0; index < argv.length; index++) {
        const arg = argv[index];

        // Everything from a bare -- on is positional, and this script takes none. argparse
        // lists the -- itself among the unrecognized arguments too.
        if (arg === "--") {
            unknown.push(...argv.slice(index));
            break;
        }

        if (arg === "-h" || (arg.startsWith("--h") && "--help".startsWith(arg))) {
            process.stdout.write(helpText(prog));
            process.exit(0);
        }

        if (!arg.startsWith("-") || arg === "-" || looksLikeNegativeNumber(arg)) {
            unknown.push(arg);
            continue;
        }

        const [name, inline] = arg.includes("=") ? [arg.slice(0, arg.indexOf("=")), arg.slice(arg.indexOf("=") + 1)] : [arg, null];
        const matches = OPTIONS.filter((option) => option.flag === name || (name.startsWith("--") && name.length > 2 && option.flag.startsWith(name)));
        const option = matches.find((candidate) => candidate.flag === name) ?? (matches.length === 1 ? matches[0] : null);

        if (option === null) {
            if (matches.length > 1) {
                fail(prog, `ambiguous option: ${name} could match ${matches.map((candidate) => candidate.flag).join(", ")}`);
            }

            unknown.push(arg);
            continue;
        }

        let text = inline;

        if (text === null) {
            const next = argv[index + 1];

            if (next === undefined || (next.startsWith("-") && next !== "-" && !looksLikeNegativeNumber(next))) {
                fail(prog, `argument ${option.flag}: expected one argument`);
            }

            text = next;
            index++;
        }

        let value = text;

        if (option.type === "int") {
            value = parseInt10(text);
        } else if (option.type === "float") {
            value = parseFloat10(text);
        }

        if (value === null) {
            fail(prog, `argument ${option.flag}: invalid ${option.type} value: '${text}'`);
        }

        args[option.dest] = value;
        given.add(option.dest);
    }

    if (unknown.length > 0) {
        fail(prog, `unrecognized arguments: ${unknown.join(" ")}`);
    }

    return {args, given};
};

const summaryText = (durations) => {
    const parts = Object.entries(durations).map(([duration, row]) => {
        const percent = Object.entries(row.percent).map(([key, value]) => `'${key}': ${pyRepr(value.value)}`);

        return `${duration}: {${percent.join(", ")}}`;
    });

    return `{${parts.join(", ")}}`;
};

const main = () => {
    // A reader that stops early (| head) closes the pipe: that is not an error.
    process.stdout.on("error", (error) => {
        if (error.code !== "EPIPE") {
            throw error;
        }

        process.exit(0);
    });

    const prog = basename(process.argv[1]);
    const {args, given} = parseArgs(process.argv.slice(2), prog);

    if (args.trials < 1n) {
        fail(prog, "trials must be positive");
    }

    if (args.mage_reserve < 0 || args.potion_fuse < 0) {
        fail(prog, "reserve and fuse cannot be negative");
    }

    // A value read off the command line is a float, a default stays an int.
    const floats = ["mage_reserve", "potion_fuse"].filter((name) => given.has(name)).map((name) => (name === "mage_reserve" ? "mage_mana_reserve" : name));
    const trials = Number(args.trials);
    const cases = [];

    for (const failedCost of [0, 1]) {
        for (const contact of [0.25, 0.5, 0.75]) {
            const config = makeConfig({
                contact, failed_mana_fraction: failedCost,
                mage_mana_reserve: args.mage_reserve, potion_fuse: args.potion_fuse,
            }, {floats});

            cases.push(aggregate(config, trials, args.seed));
        }
    }

    const result = {
        model: "conditional-policy-v1", player_skills: PLAYER_SKILLS, mage_skills: MAGE_SKILLS,
        sources: SOURCES, assumptions: {
            initial: "HP120, full mana minus TK9, RA/Reflect/Protection/Strength/Agility/Siphon prepared",
            gear: "Player GM leather+Protection AR47, mage total AR50, mundane axes, sufficient supplies",
            contact: "Alternating exponential close/far bouts, close mean2s, melee stamina100 maintained",
            distributions: "Uniform armor mitigation, resist mitigation and stated heal/spell ranges",
            opening: "Both TK land at0, both throw at.2, both begin MA at.4, mage then alternates Ex/EB attempts",
            policy: "Player bandage+pot/GH deficit45, RA retry5s; manual MA far every8s leaves20mana; TK also leaves20",
            mage_policy: `Potion deficit35, GH HP85, RA empty; offensive TK/Ex/EB/MA leave${formatG(args.mage_reserve)}mana`,
            timing: `Recovery/items.2s, tick.05s, cast completion wins exact tie, bomb fuse${formatG(args.potion_fuse)}s, close means splashback`,
            mana: "Passive regeneration while casting; interrupted cost varied0/100%, completed spells full cost",
            excluded: "Poison, Curse, Paralyze, weapon disarm, active meditation, terrain/LOS, escape, lag, mushroom, PvM effects",
            limits: "Not calibrated against duel logs or server. Contact, decision timing, distributions and fuse are assumptions.",
            termination: "Stop at first death; mutual counts only same-tick damage, no future post-death explosion resolution",
        }, cases,
    };

    if (args.output !== null) {
        mkdirSync(dirname(args.output), {recursive: true});
        writeFileSync(args.output, `${pyJson(result)}\n`);
    }

    for (const entry of cases) {
        const config = entry.config;
        const contact = config.contact instanceof PyFloat ? config.contact.value : config.contact;
        const failed = config.failed_mana_fraction instanceof PyFloat ? config.failed_mana_fraction.value : config.failed_mana_fraction;

        process.stdout.write(`contact=${formatPercent(contact)} failed-mana=${formatPercent(failed)} ${summaryText(entry.durations)}\n`);
    }
};

if (process.argv[1] && import.meta.url === pathToFileURL(realpathSync(process.argv[1])).href) {
    main();
}
