// Numerical and scheduling checks, not a Razor or game-server emulator.
//
// Run: node --test util/pvp-sim.test.mjs

import assert from "node:assert/strict";
import {test} from "node:test";
import {
    bandageAmount, damage, Fighter, formatG, MAGE_SKILLS, makeConfig, outcome, PLAYER_SKILLS, potionSplit,
    PyRandom, pyRepr, pyRound, spellScalar, swingDelay, trial, weaponRoll,
} from "./pvp-sim.mjs";

const assertAlmostEqual = (actual, expected) => assert.ok(Math.abs(actual - expected) < 5e-8, `${actual} is not about ${expected}`);
const sum = (values) => values.reduce((total, value) => total + value, 0);

test("weapon dice bounds", () => {
    const rng = new PyRandom(12);

    for (let roll = 0; roll < 1000; roll++) {
        const great = weaponRoll("great", rng);
        const norse = weaponRoll("norse", rng);

        assert.ok(great >= 21 && great <= 46);
        assert.ok(norse >= 13 && norse <= 23);
    }
});

test("shared swing timing", () => {
    assert.equal(swingDelay("great", 100), 3);
    assert.equal(swingDelay("norse", 100), 1.5625);
    assert.equal(swingDelay("great", 120), 3);
});

test("skill totals and scalar", () => {
    assert.equal(sum(Object.values(PLAYER_SKILLS)), 720);
    assert.equal(sum(Object.values(MAGE_SKILLS)), 720);
    assertAlmostEqual(spellScalar(80, 0, 80), 0.664);
    assertAlmostEqual(spellScalar(100, 100, 100), 1.225);
});

test("bandage slips reduce healing", () => {
    const clean = bandageAmount(new PyRandom(1), 0);
    const slipped = bandageAmount(new PyRandom(1), 5);

    assertAlmostEqual(slipped, clean * 0.9);
    assert.ok(clean >= 37.12 && clean <= 55.68);
});

test("defeat and undecided are distinct", () => {
    assert.equal(outcome(80, 70), "undecided");
    assert.equal(outcome(80, 0), "win");
    assert.equal(outcome(0, 80), "loss");
    assert.equal(outcome(0, 0), "mutual");
});

test("splashback conserves damage", () => {
    assert.deepEqual(potionSplit(32, true), [16, 16]);
    assert.deepEqual(potionSplit(32, false), [32, 0]);
});

test("reproducible trial and mana bounds", () => {
    const config = makeConfig({contact: 0.5});
    const one = trial(config, 82);
    const two = trial(config, 82);

    assert.deepEqual(one, two);

    for (const row of Object.values(one)) {
        assert.ok(row.player_mana >= 0 && row.player_mana <= 45);
        assert.ok(row.mage_mana >= 0 && row.mage_mana <= 100);
    }
});

test("terminal outcome stays terminal at 60", () => {
    for (let seed = 0; seed < 30; seed++) {
        const result = trial(makeConfig({contact: 1}), seed);

        if (result[30].outcome !== "undecided") {
            assert.deepEqual(result[30], result[60]);
        }
    }
});

test("low circle hits restart the interrupt window", () => {
    const fighter = new Fighter(100, 100, 100, 100, 0, 100, 1, {mana: 100});
    const config = makeConfig();

    for (const at of [0, 4, 6]) {
        fighter.cast = ["gh", at + 1.25];
        damage(fighter, 1, at, config, 1);
    }

    assert.equal(fighter.interruptions, 1);
    assert.equal(fighter.interruptWindows.get(1), 11);
});

test("a duel cannot gain free swings from weapon swaps", () => {
    for (let seed = 0; seed < 20; seed++) {
        const result = trial(makeConfig({contact: 1}), seed);

        for (const [duration, row] of Object.entries(result)) {
            assert.ok(row.swings <= 1 + Math.trunc(Number(duration) / 1.5625));
            assert.ok(row.hits <= row.swings);
        }
    }
});

// The port has to give CPython's numbers. These values were read off CPython 3.13.

test("the random stream matches CPython for the same seed", () => {
    const rng = new PyRandom(410);

    assert.equal(rng.random(), 0.14708406988922706);
    assert.equal(rng.randint(1, 6), 3);
    assert.equal(rng.uniform(15, 25), 15.176390833207456);
    // expovariate goes through the C library log, which may differ in the last bit.
    assertAlmostEqual(rng.expovariate(0.5), 0.7964791406740526);
});

test("round, repr and format follow CPython", () => {
    assert.equal(pyRound(12.25, 1), 12.2);
    assert.equal(pyRound(0.125, 2), 0.12);
    assert.equal(pyRound(0.375, 2), 0.38);
    assert.equal(pyRound(30.000000000000004, 6), 30);
    assert.equal(pyRepr(50), "50.0");
    assert.equal(pyRepr(1e-5), "1e-05");
    assert.equal(pyRepr(1e16), "1e+16");
    assert.equal(pyRepr(0.0001), "0.0001");
    assert.equal(formatG(11), "11");
    assert.equal(formatG(1234565), "1.23456e+06");
    assert.equal(formatG(999999.5), "1e+06");
    assert.equal(formatG(0.00001), "1e-05");
});
