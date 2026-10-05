"""Numerical and scheduling checks, not a Razor or game-server emulator."""

import importlib.util
from pathlib import Path
import random
import sys
import unittest

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("pvp_sim", Path(__file__).with_name("pvp-sim.py"))
sim = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = sim
spec.loader.exec_module(sim)


class CombatModelTests(unittest.TestCase):
  def test_weapon_dice_bounds(self):
    rng = random.Random(12)
    for _ in range(1000):
      self.assertTrue(21 <= sim.weapon_roll("great", rng) <= 46)
      self.assertTrue(13 <= sim.weapon_roll("norse", rng) <= 23)

  def test_shared_swing_timing(self):
    self.assertEqual(sim.swing_delay("great", 100), 3)
    self.assertEqual(sim.swing_delay("norse", 100), 1.5625)
    self.assertEqual(sim.swing_delay("great", 120), 3)

  def test_skill_totals_and_scalar(self):
    self.assertEqual(sum(sim.PLAYER_SKILLS.values()), 720)
    self.assertEqual(sum(sim.MAGE_SKILLS.values()), 720)
    self.assertAlmostEqual(sim.spell_scalar(80, 0, 80), .664)
    self.assertAlmostEqual(sim.spell_scalar(100, 100, 100), 1.225)

  def test_bandage_slips_reduce_healing(self):
    clean = sim.bandage_amount(random.Random(1), 0)
    slipped = sim.bandage_amount(random.Random(1), 5)
    self.assertAlmostEqual(slipped, clean * .9)
    self.assertTrue(37.12 <= clean <= 55.68)

  def test_defeat_and_undecided_are_distinct(self):
    self.assertEqual(sim.outcome(80, 70), "undecided")
    self.assertEqual(sim.outcome(80, 0), "win")
    self.assertEqual(sim.outcome(0, 80), "loss")
    self.assertEqual(sim.outcome(0, 0), "mutual")

  def test_splashback_conserves_damage(self):
    self.assertEqual(sim.potion_split(32, True), (16, 16))
    self.assertEqual(sim.potion_split(32, False), (32, 0))

  def test_reproducible_trial_and_mana_bounds(self):
    config = sim.Config(contact=.5)
    one = sim.trial(config, 82)
    two = sim.trial(config, 82)
    self.assertEqual(one, two)
    for row in one.values():
      self.assertTrue(0 <= row["player_mana"] <= 45)
      self.assertTrue(0 <= row["mage_mana"] <= 100)

  def test_terminal_outcome_stays_terminal_at_60(self):
    for seed in range(30):
      result = sim.trial(sim.Config(contact=1), seed)
      if result[30]["outcome"] != "undecided":
        self.assertEqual(result[30], result[60])

  def test_low_circle_hits_restart_interrupt_window(self):
    fighter = sim.Fighter(100, 100, 100, 100, 0, 100, 1, mana=100)
    config = sim.Config()
    for at in (0, 4, 6):
      fighter.cast = ("gh", at + 1.25)
      sim.damage(fighter, 1, at, config, circle=1)
    self.assertEqual(fighter.interruptions, 1)
    self.assertEqual(fighter.interrupt_windows[1], 11)

  def test_duel_cannot_gain_free_swings_from_weapon_swaps(self):
    for seed in range(20):
      result = sim.trial(sim.Config(contact=1), seed)
      for duration, row in result.items():
        self.assertLessEqual(row["swings"], 1 + int(duration / 1.5625))
        self.assertLessEqual(row["hits"], row["swings"])


if __name__ == "__main__":
  unittest.main()
