"""Conditional field-duel model. This is not a Razor/game-server emulator.

Run: python3 util/pvp-sim.py --trials 2000 --output tmp/pvp-analysis/results.json
Official numerical inputs and unmeasured policy assumptions are kept separate.
"""

import argparse
from collections import Counter
from dataclasses import asdict, dataclass, field
import heapq
import json
from pathlib import Path
import random

PLAYER_SKILLS = dict(Lumberjacking=120, Swordsmanship=100, Tactics=100,
          Magery=80, Tracking=80, Resist=80, Anatomy=80, Healing=80)
MAGE_SKILLS = dict(Magery=100, Eval=100, Meditation=100, Wrestling=100,
         Resist=100, Tracking=100, Alchemy=120)
SPELLS = {
  "ma": (4, .5, .5, 1), "tk": (9, 1, 0, 3),
  "explosion": (20, 1.75, 2.5, 6), "eb": (20, 1.75, .5, 6),
  "gh": (11, 1.25, 0, 4), "heal": (4, .5, 0, 1), "ra": (4, .5, 0, 1),
}
SOURCES = {
  "weapons": "https://wiki.uooutlands.com/Swordsmanship",
  "swing": "https://wiki.uooutlands.com/Swing_Speed",
  "damage_cap": "https://wiki.uooutlands.com/PvP_Damage_Cap",
  "magery": "https://wiki.uooutlands.com/Magery",
  "resist": "https://wiki.uooutlands.com/Resisting_Spells",
  "healing": "https://wiki.uooutlands.com/Healing",
  "alchemy": "https://wiki.uooutlands.com/Alchemy",
  "armor": "https://wiki.uooutlands.com/Armor_%26_Weapons",
  "meditation": "https://wiki.uooutlands.com/Meditation",
  "anatomy": "https://wiki.uooutlands.com/Anatomy",
  "tk": "https://uooutlands.com/news/patch-september-28-murderer-and-pvp-overhaul-general-changes/",
  "mushroom": "https://uooutlands.com/news/patch-march-5-wizards-grimoire-new-player-rental-credit-deeds-society-job-updates/",
}


@dataclass(frozen=True)
class Config:
  contact: float = .5
  close_bout: float = 2
  mage_ar: float = 50
  failed_mana_fraction: float = 0
  mage_mana_reserve: float = 11
  potion_fuse: float = 2
  dt: float = .05


@dataclass
class Fighter:
  magery: float
  evaluation: float
  tracking: float
  resist: float
  alchemy: float
  max_mana: float
  mana_regen: float
  hp: float = 120
  mana: float = 0
  armor: float = 0
  ra_pool: float = 0
  reflect: bool = True
  cast: tuple | None = None
  ready_at: float = 0
  heal_pot_at: float = 0
  bandage_at: float | None = None
  bandage_slips: int = 0
  heal_retry_at: float = 0
  buff_retry_at: float = 0
  manual_ma_at: float = 8
  tk_ready_at: float = 30
  tk_immune_at: float = 0
  sticky_until: float = 30
  bomb_at: float = 15
  sticky_used: bool = False
  mage_opener_done: bool = False
  next_attack: str = "explosion"
  interrupt_windows: dict = field(default_factory=dict)
  swings: int = 0
  hits: int = 0
  interruptions: int = 0


def weapon_roll(weapon, rng):
  base, sides = (16, 6) if weapon == "great" else (8, 3)
  return base + sum(rng.randint(1, sides) for _ in range(5))


def swing_delay(weapon, stamina):
  speed = 25 if weapon == "great" else 48
  return 15000 / ((min(stamina, 100) + 100) * speed)


def spell_scalar(magery, evaluation, tracking):
  return magery / 100 * (.75 + .375 * evaluation / 100 + min(.10, .10 * tracking / 100))


def bandage_amount(rng, slips):
  return .8 * rng.uniform(40, 60) * 1.16 * max(0, 1 - .02 * slips)


def potion_split(damage, close):
  return (damage / 2, damage / 2) if close else (damage, 0)


def outcome(player_hp, mage_hp):
  if player_hp <= 0 and mage_hp <= 0:
    return "mutual"
  if mage_hp <= 0:
    return "win"
  if player_hp <= 0:
    return "loss"
  return "undecided"


def start_cast(fighter, name, now):
  cost, duration, _, _ = SPELLS[name]
  if fighter.cast is not None or now < fighter.ready_at or fighter.mana < cost:
    return False
  fighter.cast = (name, now + duration)
  return True


def interrupt(fighter, now, config):
  if fighter.cast is None:
    return
  name, _ = fighter.cast
  fighter.mana = max(0, fighter.mana - SPELLS[name][0] * config.failed_mana_fraction)
  fighter.cast = None
  fighter.ready_at = now + .2
  fighter.interruptions += 1


def damage(fighter, amount, now, config, circle=None):
  fighter.hp = max(0, fighter.hp - amount)
  if fighter.bandage_at is not None and amount > 0:
    fighter.bandage_slips += 1
  if circle is None or circle >= 4:
    interrupt(fighter, now, config)
  else:
    low_circle_interrupt(fighter, circle, now, config)


def low_circle_interrupt(fighter, circle, now, config):
  allowed = now >= fighter.interrupt_windows.get(circle, -1)
  fighter.interrupt_windows[circle] = now + 5
  if allowed:
    interrupt(fighter, now, config)


def snapshot(player, mage, now):
  return {
    "outcome": outcome(player.hp, mage.hp), "at": round(now, 2),
    "player_hp": round(player.hp, 2), "mage_hp": round(mage.hp, 2),
    "player_mana": round(player.mana, 2), "mage_mana": round(mage.mana, 2),
    "swings": player.swings, "hits": player.hits,
    "player_interruptions": player.interruptions, "mage_interruptions": mage.interruptions,
  }


def trial(config, seed):
  rng = random.Random(seed)
  player = Fighter(80, 0, 80, 80, 0, 45, .5, mana=36, armor=47, ra_pool=20)
  mage = Fighter(100, 100, 100, 100, 120, 100, 1, mana=91,
         armor=config.mage_ar, ra_pool=25)
  fighters = (player, mage)
  player.ready_at = mage.ready_at = .2
  # Both initial TK casts have completed at t=0, costing 9 mana each.
  # Both opening potions are attached at t=.2. One potion per successful TK.
  events = []
  event_id = 0

  def enqueue(at, kind, source, value=None):
    nonlocal event_id
    event_id += 1
    heapq.heappush(events, (at, event_id, kind, source, value))

  def throw_bomb(source, now):
    caster, victim = fighters[source], fighters[1 - source]
    if caster.sticky_used or now >= caster.sticky_until or now < caster.bomb_at:
      return
    caster.sticky_used = True
    caster.bomb_at = now + 15
    victim.tk_immune_at = now + 30
    caster.ready_at = max(caster.ready_at, now + .2)
    amount = rng.uniform(15, 25) * (1 + .5 * caster.alchemy / 100)
    enqueue(now + config.potion_fuse, "bomb", source, amount)

  for source in (0, 1):
    fighters[source].bomb_at = 0
    enqueue(.2, "throw", source)
  close = rng.random() < config.contact
  if config.contact in (0, 1):
    contact_change = float("inf")
  else:
    mean = config.close_bout if close else config.close_bout * (1 - config.contact) / config.contact
    contact_change = rng.expovariate(1 / mean)
  last_swing = -3
  results = {}
  steps = round(60 / config.dt)

  for step in range(steps + 1):
    now = round(step * config.dt, 6)
    if now >= contact_change:
      close = not close
      mean = config.close_bout if close else config.close_bout * (1 - config.contact) / config.contact
      contact_change = now + rng.expovariate(1 / mean)
    if step:
      for actor in fighters:
        actor.mana = min(actor.max_mana, actor.mana + actor.mana_regen * config.dt)
        actor.hp = min(120, actor.hp + .25 * config.dt)

    # Completing casts precede damage at an exact tick tie, a model convention.
    for source, actor in enumerate(fighters):
      if actor.cast is None or now < actor.cast[1]:
        continue
      name, _ = actor.cast
      actor.cast = None
      actor.ready_at = now + .2
      actor.mana = max(0, actor.mana - SPELLS[name][0])
      if name in ("gh", "heal"):
        low, high = (40, 50) if name == "gh" else (6, 9)
        actor.hp = min(120, actor.hp + rng.uniform(low, high) * actor.magery / 100)
      elif name == "ra":
        actor.ra_pool = 25 * actor.magery / 100
      elif name == "tk":
        actor.sticky_until = now + 30
        actor.sticky_used = False
        actor.tk_ready_at = now + 30
        fighters[1 - source].tk_immune_at = now + 30
        enqueue(now, "throw", source)
        enqueue(now, "tk", source)
      else:
        enqueue(now + SPELLS[name][2], "spell", source, name)

    # Process both bombs/delayed spells before checking terminal outcomes.
    while events and events[0][0] <= now:
      _, _, kind, source, value = heapq.heappop(events)
      caster, victim = fighters[source], fighters[1 - source]
      if kind == "throw":
        throw_bomb(source, now)
      elif kind == "bomb":
        outgoing, splash = potion_split(value, close)
        damage(victim, outgoing, now, config)
        if splash:
          damage(caster, splash, now, config)
      elif kind == "tk":
        # TK does not consume Reflection in the user's recorded field test.
        low_circle_interrupt(victim, 3, now, config)
      elif kind == "spell":
        if victim.reflect:
          victim.reflect = False
          victim = caster  # One bounce, no infinite mirror chain.
        low, high = (5, 7) if value == "ma" else (28, 36)
        reduction = rng.uniform(.125, .375) * victim.resist / 100
        amount = rng.uniform(low, high) * spell_scalar(
          caster.magery, caster.evaluation, caster.tracking) * (1 - reduction)
        damage(victim, amount, now, config, SPELLS[value][3])

    if player.hp > 0 and player.bandage_at is not None and now >= player.bandage_at:
      player.hp = min(120, player.hp + bandage_amount(rng, player.bandage_slips))
      player.bandage_at = None
    if outcome(player.hp, mage.hp) != "undecided":
      terminal = snapshot(player, mage, now)
      results.setdefault(30, terminal)
      results[60] = terminal
      break

    for actor in fighters:
      if actor.cast is None and now >= actor.ready_at:
        if 120 - actor.hp >= 35 and now >= actor.heal_pot_at:
          actor.hp = min(120, actor.hp + rng.uniform(19, 26) * (1 + .25 * actor.alchemy / 100))
          actor.heal_pot_at = now + 10
          actor.ready_at = now + .2
    if player.cast is None and now >= player.ready_at:
      if player.bandage_at is None and player.hp < 120:
        player.bandage_at = now + 10
        player.bandage_slips = 0
        player.ready_at = now + .2
      elif 120 - player.hp >= 45 and now >= player.heal_retry_at and player.mana >= 11:
        player.heal_retry_at = now + 2.5
        start_cast(player, "gh", now)
      elif not player.ra_pool and player.hp > 105 and now >= player.buff_retry_at and player.mana >= 4:
        player.buff_retry_at = now + 5
        start_cast(player, "ra", now)
      elif now >= max(player.tk_ready_at, mage.tk_immune_at) and player.mana >= 29:
        start_cast(player, "tk", now)
      elif not player.mage_opener_done or (not close and now >= player.manual_ma_at and player.mana >= 24):
        if start_cast(player, "ma", now):
          player.mage_opener_done = True
          player.manual_ma_at = now + 8

    if mage.cast is None and now >= mage.ready_at:
      if mage.hp <= 85 and mage.mana >= 11:
        start_cast(mage, "gh", now)
      elif not mage.ra_pool and mage.mana >= 4:
        start_cast(mage, "ra", now)
      elif now >= max(mage.tk_ready_at, player.tk_immune_at) and mage.mana >= 9 + config.mage_mana_reserve:
        start_cast(mage, "tk", now)
      elif not mage.mage_opener_done:
        if start_cast(mage, "ma", now):
          mage.mage_opener_done = True
      elif mage.mana >= 20 + config.mage_mana_reserve and start_cast(mage, mage.next_attack, now):
        mage.next_attack = "eb" if mage.next_attack == "explosion" else "explosion"
      elif mage.mana >= 4 + config.mage_mana_reserve:
        # Low-mana harassment is also conditional on this policy, not optimal play.
        start_cast(mage, "ma", now)

    if close and player.cast is None and now >= player.ready_at:
      elapsed = now - last_swing
      weapon = "great" if elapsed >= swing_delay("great", 100) else "norse"
      if elapsed >= swing_delay(weapon, 100):
        last_swing = now  # Misses also consume a swing.
        player.swings += 1
        if rng.random() < .5:
          player.hits += 1
          amount = weapon_roll(weapon, rng) * 1.36
          amount *= 1 - rng.uniform(mage.armor * .00333, mage.armor * .00666)
          absorbed = min(mage.ra_pool, amount * .2)
          mage.ra_pool -= absorbed
          damage(mage, amount - absorbed, now, config)
    if outcome(player.hp, mage.hp) != "undecided":
      terminal = snapshot(player, mage, now)
      results.setdefault(30, terminal)
      results[60] = terminal
      break
    if now in (30, 60):
      results[int(now)] = snapshot(player, mage, now)
  return results


def aggregate(config, trials, seed):
  samples = [trial(config, seed + n) for n in range(trials)]
  result = {"config": asdict(config), "trials": trials, "seed": seed, "durations": {}}
  for duration in (30, 60):
    rows = [sample[duration] for sample in samples]
    counts = Counter(row["outcome"] for row in rows)
    result["durations"][duration] = {
      "counts": {key: counts[key] for key in ("win", "loss", "mutual", "undecided")},
      "percent": {key: round(100 * counts[key] / trials, 1) for key in ("win", "loss", "mutual", "undecided")},
      "means_all_trials": {key: round(sum(row[key] for row in rows) / trials, 1) for key in
                ("player_hp", "mage_hp", "player_mana", "mage_mana", "hits", "mage_interruptions")},
    }
  return result


def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument("--trials", type=int, default=2000)
  parser.add_argument("--seed", type=int, default=410)
  parser.add_argument("--mage-reserve", type=float, default=11)
  parser.add_argument("--potion-fuse", type=float, default=2)
  parser.add_argument("--output", type=Path)
  args = parser.parse_args()
  if args.trials < 1:
    parser.error("trials must be positive")
  if args.mage_reserve < 0 or args.potion_fuse < 0:
    parser.error("reserve and fuse cannot be negative")
  cases = []
  for failed_cost in (0, 1):
    for contact in (.25, .5, .75):
      config = Config(contact=contact, failed_mana_fraction=failed_cost,
              mage_mana_reserve=args.mage_reserve, potion_fuse=args.potion_fuse)
      cases.append(aggregate(config, args.trials, args.seed))
  result = {
    "model": "conditional-policy-v1", "player_skills": PLAYER_SKILLS, "mage_skills": MAGE_SKILLS,
    "sources": SOURCES, "assumptions": {
      "initial": "HP120, full mana minus TK9, RA/Reflect/Protection/Strength/Agility/Siphon prepared",
      "gear": "Player GM leather+Protection AR47, mage total AR50, mundane axes, sufficient supplies",
      "contact": "Alternating exponential close/far bouts, close mean2s, melee stamina100 maintained",
      "distributions": "Uniform armor mitigation, resist mitigation and stated heal/spell ranges",
      "opening": "Both TK land at0, both throw at.2, both begin MA at.4, mage then alternates Ex/EB attempts",
      "policy": "Player bandage+pot/GH deficit45, RA retry5s; manual MA far every8s leaves20mana; TK also leaves20",
      "mage_policy": f"Potion deficit35, GH HP85, RA empty; offensive TK/Ex/EB/MA leave{args.mage_reserve:g}mana",
      "timing": f"Recovery/items.2s, tick.05s, cast completion wins exact tie, bomb fuse{args.potion_fuse:g}s, close means splashback",
      "mana": "Passive regeneration while casting; interrupted cost varied0/100%, completed spells full cost",
      "excluded": "Poison, Curse, Paralyze, weapon disarm, active meditation, terrain/LOS, escape, lag, mushroom, PvM effects",
      "limits": "Not calibrated against duel logs or server. Contact, decision timing, distributions and fuse are assumptions.",
      "termination": "Stop at first death; mutual counts only same-tick damage, no future post-death explosion resolution",
    }, "cases": cases,
  }
  if args.output:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
  for case in cases:
    cfg = case["config"]
    summary = {duration: row["percent"] for duration, row in case["durations"].items()}
    print(f"contact={cfg['contact']:.0%} failed-mana={cfg['failed_mana_fraction']:.0%}", summary)


if __name__ == "__main__":
  main()
