# PvP 규칙

템플릿과 무관한 PvP 서버 규칙과 숫자. 위키와 패치노트 원문을 인용하고, 해석은 인용문 아래에 적는다.
인게임에서 확인된 것은 그렇게 적었고, 확인되지 않은 것은 "확인되지 않았다" 로 남겼다.

- Bard Necro 가 이 규칙으로 내린 판단 (Defensive Barding, 도주냐 반격이냐, Herding 대신 Resist)은 [bard-necro-handbook.md](bard-necro-handbook.md) 6절.
- PvP 에서 막히는 스크립트 명령은 [razor.md](razor.md) 7절.

## 목차

1. [공격적 행동과 Heat of Battle](#1-공격적-행동과-heat-of-battle)
    - 1.1 [무엇이 켜는가](#11-무엇이-켜는가)
    - 1.2 [지속시간](#12-지속시간)
    - 1.3 [던전에서는 리콜로 도주할 수 없다](#13-던전에서는-리콜로-도주할-수-없다)
2. [명중률](#2-명중률)
    - 2.1 [스킬 대 스킬, 명중 보너스 0](#21-스킬-대-스킬-명중-보너스-0)
    - 2.2 [내가 칠 때](#22-내가-칠-때)
    - 2.3 [PK 가 나를 칠 때, PK 무기 100](#23-pk-가-나를-칠-때-pk-무기-100)
    - 2.4 [명중 보너스](#24-명중-보너스)
    - 2.5 [메이지가 레슬링을 드는 이유](#25-메이지가-레슬링을-드는-이유)
3. [Hamstring](#3-hamstring)
4. [Telekinesis 와 폭발 포션](#4-telekinesis-와-폭발-포션)
    - 4.1 [규칙](#41-규칙)
    - 4.2 [TK 순서](#42-tk-순서)
5. [주문으로 싸울 때](#5-주문으로-싸울-때)
6. [소환수로 싸울 때](#6-소환수로-싸울-때)
    - 6.1 [PvM 에서 받던 강화가 빠진다](#61-pvm-에서-받던-강화가-빠진다)
    - 6.2 [소환수별 비교](#62-소환수별-비교)
7. [Parrying](#7-parrying)
    - 7.1 [패리 메이지가 있는 이유](#71-패리-메이지가-있는-이유)
8. [Resisting Spells](#8-resisting-spells)
9. [근접 반격력](#9-근접-반격력)
10. [Tracking](#10-tracking)
    - 10.1 [Hunting 모드](#101-hunting-모드)
11. [자주 틀렸던 것](#11-자주-틀렸던-것)
12. [참고 링크](#12-참고-링크)

---

## 1. 공격적 행동과 Heat of Battle

**다른 플레이어에게 공격적 행동을 하면 Heat of Battle 이 켜지고, 그동안 리콜·문게이트를 못 쓴다.**
바드는 여기에 Defensive Barding 까지 같이 잃는다 ([bard-necro-handbook.md](bard-necro-handbook.md) 6.1절). 아래 숫자는 전부 이 조건에서 갈린다.

### 1.1 무엇이 켜는가

> "Heat of Battle will be triggered by performing an aggressive action against another player regardless of notoriety, or when interacting with various faction content events or wayposts."
> "Aggressive actions include attacking or stealing from a player"
> "Aggressive actions do not include retaliatory empty-handed wrestling attacks or weapon swings your character makes when someone attacks you"
> "However, it is an aggressive action to re-target your attacker (for example, to avoid attacking monsters instead of the attacking player)
> "
> "Note also that using harmful spells (such as Weaken, Telekinesis, or Energy Bolt) will trigger Heat of Battle, even when used against an attacker"
> "Heat of battle will prevent the player from utilizing any moongates, recalling, or entering an inn room while it is active"

### 1.2 지속시간

지속시간은 위키 문서에 없고 2020-09-28 패치 원문에 있다.

> "When any player commits a hostile action (including stealing) to another player, but the action is not considered a criminal action (such as attacking or stealing from a Red, Grey, or Orange
> player) they will have a 30 second Heat of Battle timer started"
> "When any player commits any Criminal action, they have will have a 2 minute Heat of Battle timer started that matches their Criminal Timer duration"
> "Heat of Battle now has a maximum duration of 5 minutes, regardless of circumstance"

| 내 행동                                               | Heat of Battle                  |
|-------------------------------------------------------|---------------------------------|
| PK 가 나를 칠 때 내 캐릭터가 자동으로 되받아치는 스윙 | **안 켜짐**                     |
| 몹을 치던 중 PK 로 타겟을 바꿈                        | **켜짐.** 위키 예시가 이 경우다 |
| 해로운 주문 (Energy Bolt, Weaken, Telekinesis ...)    | **켜짐.** 상대가 먼저 쳤어도    |
| 빨강 / 회색 / 주황 플레이어에게 공격적 행동           | 켜짐, 할 때마다 **30초** 타이머 |
| 파랑 공격 (Criminal)                                  | 켜짐, **2분**                   |
| 햄스트링을 켜 둔 자동 반격 스윙                       | 확인되지 않았다                 |

**"반격은 안 켜진다" 는 자동 스윙에만 맞다.** 사냥 중에는 몹을 치고 있으므로 PK 를 치려면 타겟을 바꿔야 하고,
그 순간 켜진다. 거리를 두고 주문을 쓰는 메이지 PK 에게는 자동 스윙이 나갈 일 자체가 없다.

### 1.3 던전에서는 리콜로 도주할 수 없다

> "Within dungeons, players may only cast Recall within 8 tiles of a Golden Moongate" -- Magery (Recall)
> "Any character can cast this spell from a scroll in a rune book or rune tome, or from a scroll onto a loose marked rune, even with 0 Magery skill" -- Magery (Recall)
> "When a player is in the Heat of Battle they are unable to cast Recall, Gate, or use any Moongates" -- Magery

- 룬북 리콜은 Magery 0 이어도 된다. 하지만 **던전 안에서는 Golden Moongate 8타일 안에서만 된다.**
- 던전에서 PK 를 만나면 도주 플랜은 "문게이트까지 뛰기" 다. 그 사이에 맞으면 **printed 방어로 버텨야 한다.**

## 2. 명중률

> "The chance to hit with a mace class weapon is equal to (attacker's mace fighting skill + 50) / ((defender's weapon or wrestling skill + 50) * 2) plus any relevant accuracy bonuses" -- Mace Fighting
> "The chance to hit and defend with fists (avoiding interrupts while casting) is equal to (attacker's wrestling skill + 50) / ((defender's weapon or wrestling skill + 50) * 2) plus any relevant
> accuracy bonuses." -- Wrestling
> "Due to Wrestling's defense bonus being active when unarmed (or when holding a spellbook) it can be used to defend against melee attacks while casting spells." -- Wrestling

Swordsmanship 도 같은 형태다.

```
명중률 = (공격자 스킬 + 50) / ((방어자 스킬 + 50) x 2)
```

**양쪽 다 지금 손에 든 것의 스킬 하나만 쓴다.** 가진 다른 스킬은 판정에 안 들어간다.

|        | 쓰이는 스킬                                       |
|--------|---------------------------------------------------|
| 공격자 | 든 무기의 스킬. 맨손·레슬링 무기일 때만 Wrestling |
| 방어자 | 든 무기의 스킬. 맨손·스펠북이면 Wrestling         |

### 2.1 스킬 대 스킬, 명중 보너스 0

| 공격 \ 방어 | 0    | 50  | 80    | 100   |
|-------------|------|-----|-------|-------|
| **0**       | 50%  | 25% | 19.2% | 16.7% |
| **50**      | 100% | 50% | 38.5% | 33.3% |
| **80**      | 100% | 65% | 50%   | 43.3% |
| **100**     | 100% | 75% | 57.7% | 50%   |

- **같은 숫자끼리는 항상 50%.**
- 방어 0 에 공격 50 이상은 공식값이 1 을 넘는다 (130%, 150%). 100% 로 적었다.

### 2.2 내가 칠 때

| 나 (손에 든 것)        | 상대 (손에 든 것)                           | 계산      | 명중                         |
|------------------------|---------------------------------------------|-----------|------------------------------|
| 메이스 100             | 무기 100                                    | 150 / 300 | 50%                          |
| 맨손, 레슬링 100       | 맨손, 레슬링 100                            | 150 / 300 | 50%                          |
| 맨손, 레슬링 0         | 맨손, 레슬링 100                            | 50 / 300  | 16.7%                        |
| 맨손, 레슬링 100       | 맨손, 레슬링 0                              | 150 / 100 | 100%                         |
| 맨손, 레슬링 0         | 무기 100                                    | 50 / 300  | 16.7%                        |
| 레슬링 무기, 레슬링 80 | 메이지 PK (스펠북, 레슬링 100, 무기 0)      | 130 / 300 | **43.3%**                    |
| 메이스 100, 레슬링 0   | 메이지 PK (스펠북, 레슬링 100)              | 150 / 300 | **50%**                      |
| 메이스 80              | 메이지 PK (스펠북, 레슬링 100)              | 130 / 300 | **43.3%**                    |
| 메이스 100             | 무기 100 + 레슬링 100, **무기를 든 상태**   | 150 / 300 | 50%. 상대 레슬링은 안 쓰인다 |
| 메이스 100             | 무기 100 + 레슬링 100, **스펠북을 든 상태** | 150 / 300 | 50%                          |
| 메이스 100             | 무기 100 + 레슬링 0, **스펠북을 든 상태**   | 150 / 100 | 100%                         |

- **메이지 PK 상대 명중률은 내 무기 스킬만 정한다.** 내 레슬링은 내가 레슬링으로 칠 때만 들어간다.
- 80 으로 치면 메이스든 레슬링 무기든 똑같이 43.3% 다.
- 무기와 레슬링을 둘 다 가진 상대는 **지금 든 쪽**으로 방어한다.

### 2.3 PK 가 나를 칠 때, PK 무기 100

| 내 손                          | Defensive Barding 켜짐            | Heat of Battle 중 |
|--------------------------------|-----------------------------------|-------------------|
| 맨손, printed 레슬링 0         | 50% (Effective 100)               | **100%**          |
| 맨손, printed 레슬링 80        | 50% (Effective 100)               | 57.7%             |
| 레슬링 무기, printed 레슬링 80 | 확인되지 않았다 ("while unarmed") | 57.7%             |
| 메이스 80                      | 57.7%                             | 57.7%             |
| 메이스 100                     | 50%                               | 50%               |

무기를 들면 방어는 그 무기의 스킬이다. **Effective Wrestling 이 끼어드는 것은 맨손일 때다.**

### 2.4 명중 보너스

> "Accuracy bonuses to melee weapons from items (Colored Materials, Magical Properties, Aspects, Mastery Chains, etc) are now capped by a player's base melee skill for that weapon." -- Armor & Weapons
> "Players will receive bonuses against creatures based on what "setup" they have for weapons/shields occupying their hands" -- Wrestling

- 위 표는 보너스 0 기준이다. **보너스가 곱해지는지 더해지는지는 위키에 없다.**
- Weapon Setup 보너스 (한손 무방패 Accuracy 등)는 크리처 상대 보너스라서 PvP 에는 안 붙는다.

### 2.5 메이지가 레슬링을 드는 이유

> "Wrestling is very important to mage-types, as taking a melee hit will interrupt a spellcast in progress." -- Wrestling

**메이지 PK 는 한 대 맞으면 시전이 끊긴다.** 메이지가 레슬링 100 을 드는 이유이고, 이쪽이 무기 스킬을 올려야 하는 이유다.

Arcane Staff 를 든 메이지는 방어 스킬이 다르다.

> "A players chance to hit/defend with an Arcane Staff is based on their Arcane skill, but is also capped by the lower printed value of Magery or Wrestling" -- Arcane Staff
> "PvP-based interrupts while casting with an Arcane Staff equipped will be resolved as normal using the player's Wrestling skill" -- Arcane Staff

## 3. Hamstring

PvP 요구조건. 첫 줄을 채우고 나머지 둘 중 하나를 채운다.

> "80.0 or higher attacking weapon skill in Dual Wielding, Fencing, Mace Fighting, Swordsmanship, or Wrestling"
> "two of the following skills at 80.0 or higher; Anatomy, Arms Lore, Chivalry, Forensic Evaluation, Tracking, Wrestling"
> "two of the following weapon skills at 80.0 or higher (including attacking weapon skill); Archery, Dual Wielding, Fencing, Mace Fighting, Swordsmanship"

> "if Hamstring is toggled for a player, on a missed attack they will not be able to make another Hamstring attempt for 15 seconds"
> "On a successful hit when Hamstring is toggled, a player will have a cooldown of 30-53 seconds (100-25 dex) before they may make another Hamstring attempt to any target"
> "When a player is hit by a Hamstring effect, they will be reduced to 0 Stamina for 3 seconds (forcing them to walk), after which their stamina will return to its previous amount"
> "Once hamstrung, a player or creature cannot be affected by another hamstring effect for another 30 seconds"

- **빗나가면 15초 잠긴다.** 햄스트링을 켠 첫 스윙의 명중률이 곧 성공률이다. 레슬링 100 메이지 상대로 무기 80 이면 43.3%, 100 이면 50%.
- 걸려도 3초이고 다음 시도는 30~53초 뒤다. **한 교전에 한 번**이라고 보는 게 맞다.
- Wrestling 80 + Anatomy 80 은 두 번째 줄 (목록에서 두 개)을 채운다. 공격 스킬인 Wrestling 을 목록에서 다시 세지 말라는 문구는 없다.
- 메이스로 하려면 Mace 80 + 목록에서 두 개. Anatomy + Tracking 도 된다.
- 세 번째 줄 (무기 두 개)의 PvP 목록에는 Wrestling 이 없다. PvM 목록에는 있다.

## 4. Telekinesis 와 폭발 포션

### 4.1 규칙

메이지 PK 의 흔한 진입이다. 규칙은 2020-09-28 패치 원문에 있고, 위키 Alchemy 문서에는
"Telekinesis is always required for sticking explosion potions to players regardless of skill level" 만 남아 있다.

> "If a player casts Telekinesis and successfully targets another player, it will apply a "Sticky" effect to the target player lasting 30 seconds"
> "If the same player that casted Telekinesis against a player throws an Explosive Potion at them within 30 seconds of the spellcast, the explosion potion will follow the movement of the target
> player, and when exploding will only damage the target player (and not other nearby players or creatures)"
> "If a "Stuck" potion on a player explodes, and both the thrower and the target player are within the radius of the blast, the damage from the potion will be split equally between the two players,
> instead of being dealt entirely to the target"
> "In some cases, players "stuck" with a explosive potion should consider "running the potion back" to the target to trigger the Splashback mechanic, both to reduce the damage on the explosion potion,
> but to also damage the thrower and potentially interrupt a spellcast if the thrower is currently casting"
> "Players can also cast Telekinesis on themselves as a defensive measure, since once Telekinesis is cast onto a player, no other player will be able to cast the spell on them for 30 seconds, and only
> the caster of the spell is allowed to stick potions onto a target that has Telekinesis active on them"
> "Telekinesis is a 3rd circle spell, requiring a minimum of 30 Magery to cast and 50 Magery to cast with 100% success"

위키 Explosion Potion 문서 (삭제 표시가 붙어 있다):

> "Explosion Potions stuck to another player with Telekinesis will now follow their target even if they change regions, such as crossing dungeon levels, exiting dungeons, recalling/gating/hiking, or
> using moongates"

- **붙은 포션은 리콜해도 따라온다.** 리콜로 이 콤보를 피할 수 없다.
- **던진 사람 곁에서 터지면 데미지가 반으로 나뉘고, 상대 시전이 끊길 수 있다.** 붙어서 싸우는 플랜과 방향이 같다.
- 자기 자신에게 TK 를 거는 방어는 Magery 30 이 있어야 한다.

지금 위키 Magery 주문표도 자기 TK 방어를 적고 있다.

> "Players can cast the Telekinesis spell onto another player (PvP) to make the player "Sticky" for explosion potions for the next 30 seconds" -- Magery (Telekinesis)
> "or on themselves to block it from being cast on them." -- Magery (Telekinesis)

TK 쿨다운 제약 (2020-09-28 패치 원문. 지금 위키에는 없다):

> "Each player has a global cooldown for casting Telekinesis in PvP, and can only successfuly apply it at most once every 30 seconds to any player (similar to Wall of Stone casting cooldowns)"
> "A player can only be hit by the Telekinesis spell (from all players) at most once every 30 seconds"
> "Whenever an Explosion Potion is "stuck" to a player, it immediately resets the 30 second Telekinesis casting cooldown against them (i.e other players cannot cast Telekinesis against that player for
> another 30 seconds after that point)"

- **자기 TK 는 상대 TK 보다 먼저 걸려야 한다.** 상대 TK 가 먼저 맞으면 30초 동안 Sticky 이고, 그동안은 내 TK 도 나에게 안 걸린다.
- 자기 TK 가 막는 것은 **붙는 것**이다. 던지는 것 자체는 막지 않는다. 안 붙은 포션은 나를 따라오지 않는다.
- **자기 TK 와 역콤보 TK 는 30초 안에 둘 다 못 쓸 수 있다.** "to any player" 에 자기 자신이 들어가는지는 확인되지 않았다.
- **상대가 자기 TK 를 걸어 두었으면 내 TK 는 안 걸린다.** 걸려 있는 동안 포션을 붙일 수 있는 것은 건 사람뿐이다.
- 자기에게 거는 TK 는 "against another player" 가 아니므로 위키 정의상 Heat of Battle 조건이 아니다. 인게임 확인은 안 됐다.

### 4.2 TK 순서

시전자 글로벌 쿨 "at most once every 30 seconds to any player" 에 자기 자신이 들어가면
자기 TK 와 공격 TK 는 30초 안에 하나만 된다 (미확인, 길드원에게 시험하면 바로 안다).

| 상황                     | 행동            | 왜                                                                                         |
|--------------------------|-----------------|--------------------------------------------------------------------------------------------|
| 내가 먼저 움직일 수 있다 | **자기 TK**     | 30초 동안 상대 폭탄이 안 붙는다. 붙지 않은 포션은 걸어서 피한다                            |
| 이미 상대 TK 에 맞았다   | **상대에게 TK** | 자기 TK 는 어차피 안 걸린다 (한 사람은 30초에 한 번만 맞는다). 내 글로벌 쿨은 아직 안 썼다 |
| 30초 지남                | 다시 위 판단    | 싸움은 보통 30초를 넘긴다                                                                  |

막는 범위는 4.1 끝의 목록.

## 5. 주문으로 싸울 때

메이지 계열 템플릿을 PvP 기준으로 볼 때 필요한 숫자다.

> "All hostile spells from 4th, 5th, 6th, 7th, and 8th circles will interrupt other players 100% of the time" -- Magery
> "Casting a hostile 1st circle spell against another player will at first have an interrupt chance of 100%" -- Magery
> "Afterwards, a 5 second window starts where all subsequent 1st circle hostile spells against the target have a 0% interrupt chance" -- Magery

2서클과 3서클도 같은 규칙이고, 창은 서클마다 따로 돈다.

> "PvP - Deals ((28 to 36) * (Magery / 100) * (.75 + (.375 * (Eval Int / 100)))) damage to target player" -- Energy Bolt, Explosion 공통
> "Modifies base spell damage against players by (0.75 + (0.375 * (Eval/100)))" -- Evaluating Intelligence
> "There is a 10% spell damage cap on supplemental skills (Tracking, Camping, Inscription, etc)" -- Evaluating Intelligence

| Eval | PvP 배율 | Energy Bolt / Explosion (Magery 100) |
|------|----------|--------------------------------------|
| 80   | x1.05    | 29.4 ~ 37.8                          |
| 100  | x1.125   | 31.5 ~ 40.5                          |

- Explosion 은 "damage delay of 2.5 seconds", Energy Bolt 는 0.5초다.

**레슬링:**

- 메이지는 근접 한 대에 시전이 끊긴다 (2.5절).
- 바드는 도주할 때만 Defensive Barding 이 레슬링을 채운다 ([bard-necro-handbook.md](bard-necro-handbook.md) 6.5절).
- printed 0 이면 무기 100 PK 의 근접은 **100%** 맞고, 한 대마다 시전이 끊긴다.

> "Wrestling will provide a (15% * (Wrestling Skill / 100)) Mana Refund chance when casting spells" -- Wrestling (PvM)

**Magic Reflection 과 Inscription:**

> "PvP - Has a (35% * (Inscription / 100)) chance to stay active and reflect a single additional spell before being nullified" -- Magery (Magic Reflection)
> "Will at most ever reflect 2 spells during PvP" -- Magery (Magic Reflection)
> "Players using a scroll to cast a spell will receive a (10% * (Inscription Skill / 100)) damage bonus against other players (PvP Spell Supplemental Damage Cap 10%)" -- Inscription
> "Increases certain spell's buff durations. Normal duration is 2 minutes and are increased by (400% * (Inscription Skill / 100)), including:" -- Inscription (Protection, Arch Protection, Bless,
> Invisibility)

- Inscription 120 의 PvP 몫은 **리플렉트가 한 번 더 남을 확률 42%** 와 스크롤 시전 딜 +10% (상한) 정도다.
- 나머지는 PvM 이다. 버프 지속 2분 -> 11.6분, 스크롤 환급, Reactive Armor.

**Alchemy (PvP):**

> "Increases Explosion Potion damage by (50% * (Alchemy Skill / 100))" -- Alchemy
> "Increases Healing Potion effectiveness by (25% * (Alchemy Skill / 100))" -- Alchemy
> "Increases Cure Potion chances by (12.5% * (Alchemy Skill / 100))" -- Alchemy
> "In PvP the base damage range is 15-25, scaled with a player's alchemy skill" -- Alchemy (Greater Explosion)

- 80 이면 폭발 포션 +40%, 힐 포션 +20%, 큐어 포션 +10%. Greater Explosion 쿨다운은 15초 (위키 포션표).

**마나:**

> "The baseline Mana Regen rate is 1 mana restored every 2 seconds (i.e., 0.5 mana per second)." -- Meditation
> "The Mana Regen rate is increased by (100% * (Meditation skill / 100))" -- Meditation

- Meditation 0 이면 초당 0.5 다. PvP 에서 오래 싸우는 구성이 아니다.

**PvM 에서 인터럽트:**

> "Provides players with a (Effective Magic Resist Skill / 100%)) chance to avoid Spell Interruption from Creature/Environment Damage" -- Resisting Spells
> "Players will have an (Effective Inscription Skill / 100%)) chance to avoid Spell Interruption from Creature/Environment Damage" -- Inscription

- 크리처 인터럽트 회피가 Resist 와 Inscription 에 같은 형태로 있다. 둘이 합산되는지는 확인되지 않았다. **Resist 100 이면 이것만으로 100% 다.**
- 바드의 Defensive Barding 은 PvM 보너스를 주지 않으므로 이 효과는 printed Resist 로만 받는다.

Wizard's Grimoire:

> "Players must have at least 80 Magery skill and at least 80 Meditation or 80 Eval Int skill to benefit from the Wizard's Grimoire" -- Wizard's Grimoire

**주문 데미지 보너스 합산:**

> "Instead, having the Necromancy skill during PvP will provide the player with a (10% * (Necromancy Skill / 100)) Supplemental PvP Spell Damage bonus" -- Necromancy
> "However, you could have 100 Evaluating Intelligence and 100 Tracking and gain 22.5% spell damage increase" -- Evaluating Intelligence

- Eval 과 보조 스킬 보너스는 **더해진다** (위키 예시: 12.5% + 10% = 22.5%).

| 구성                                               | Eval 배율 | 보조 스킬 (상한 10%)         | PvP 주문 합계 |
|----------------------------------------------------|-----------|------------------------------|---------------|
| Bard Necro (Eval 80, Necro 100)                    | +5%       | +10% (Necromancy)            | **+15%**      |
| Bard Mage (Eval 100, 보조 없음)                    | +12.5%    | 0                            | +12.5%        |
| Bard Mage (Eval 100, Inscription 120, 스크롤 시전) | +12.5%    | +10% (Inscription, 스크롤만) | +22.5%        |

## 6. 소환수로 싸울 때

### 6.1 PvM 에서 받던 강화가 빠진다

**"소환수는 PvP 에서 약하다" 에는 근거가 있다.** PvM 에서 받던 강화가 PvP 에서 빠진다.

> "If a player gets PvP flagged their summons' stats and skills will be automatically adjusted to their printed spirit speak skill" -- Spirit Speak
> "Additionally Summoner Tome upgrades will not apply against players" -- Spirit Speak
> "Necromancy Abilities will NOT work in PvP" -- Necromancy
> "Abilities that increase the Health and Damage of Summoned Followers will follow the same handling that bonuses earned from Spirit Speak follow in PvP" -- Necromancy
> "When a player attempts to Dispel another player's summoned follower (with the Dispel or Mass Dispel spell) there is a (50% * (Controller's Printed Spirit Speak Skill / 100)) chance the Summoned
> Follower will ignore the dispel attempt (this applies to normal and Undead summons)" -- Spirit Speak
> "Summoning Spells take 5 seconds to cast" -- Spirit Speak
> "Players cannot receive Mana Refunds from casting any Summoning Spells" -- Spirit Speak
> "Magic Resist potions work against pets in PvP" -- Alchemy
> "Lesser, Regular, and Greater Magic Resist potions reduce spell damage taken from creatures by 10/20/30% for 2 minutes" -- Alchemy

| 항목                       | PvM                                       | PvP                                                                             |
|----------------------------|-------------------------------------------|---------------------------------------------------------------------------------|
| 소환수 스탯                | Effective Spirit Speak (장비 보너스 포함) | **printed Spirit Speak 만**                                                     |
| Summoner's Tome 업그레이드 | 적용                                      | **플레이어 상대로 안 됨**                                                       |
| Necromancy 어빌리티        | 적용                                      | **안 됨**                                                                       |
| 소환수 주문 데미지         | 그대로                                    | PK 가 Magic Resist 포션을 마시면 **-10 / 20 / 30%**                             |
| 상대 Dispel                | --                                        | Spirit Speak 120 이면 **60% 무시, 40% 로 지워진다**                             |
| 다시 부르기                | --                                        | 5초 시전 (`item-list.txt` 는 6.00초), 마나 환급 없음, 상대 4서클+ 주문에 끊긴다 |

Herding 이 PvP 에서 대신 주는 것 (Necromancy 의 주문 보너스는 5절):

> "Tamed and summoned creatures deal (11% * (Effective Herding Skill / 100)) additional damage against players while their controller has an active shepherd's crook." -- Herding
> "Tamed and summoned receive (5.5% * (Effective Herding Skill)) Damage Resistance against all players" -- Herding

- Herding 80 이면 소환수 딜 +8.8%. 저항 공식은 원문에 `/ 100` 이 빠져 있어 값을 그대로 읽을 수 없다.

**확인되지 않은 것:**

- **소환수가 PK 를 치면 내 Heat of Battle 이 켜지는지.** 위키 정의는 "performing an aggressive action against another player" 뿐이다. 켜지지 않는다면 "소환수가 싸우고 나는 자기 대상 주문 (자기 TK, 힐, 큐어)만 쓴다" 는 플랜이 Defensive Barding 과 리콜을 지킨다.
  Heat of Battle 은 버프바에 뜨므로 ("The Heat of Battle flag is now a visible buff on players in the Buff Bar") 실전에서 소환수가 공격을 시작한 직후 버프바를 보면 확인된다.
- **소환수 데미지가 Resisting Spells 의 "Creature/Environment Damage" 에 들어가는지.** 들어간다면 Resist 100 PK 는 소환수에게 맞아도 시전이 끊기지 않는다. 그러면 PK 의 콤보를 끊는 것은 **내 주문뿐**이다.

### 6.2 소환수별 비교

> "Any summon that is cast while the Necromancy "Vengeful Spirit" ability is active will be summoned as an undead summon with the same stats, skills and abilities as their normal counterparts." --
> Spirit Speak
> "Like the Energy Vortex, the Jackal Spirit are now "non-hostile" to players and tamed creatures and will never attack them" -- Jackal Spirit
> "Like Blade Spirits, Skeletal Husks are now "non-hostile" to players and tamed creatures and will never attack them" -- Skeletal Husk
> "Mana Drain - Casting on a monster will reduce its magic resistance by 20 * Magery/100 (halved in PvP)" -- Magery

팔로워 PvP 규칙 (Animal Taming. "Tamed/Summoned" 로 적힌 것만 옮겼다):

> "Tamed/Summoned follower PvP damage scalar has been increased to 30% (previously was 25%)"
> "Tamed/Summoned follower maximum melee hit chance in PvP is now 66%. (previously was 50%)"
> "Tamed/Summoned followers now have a 60% reduced chance in PvP to trigger abilities against players (previously was 90% reduction)"
> "Tamed/Summoned follower ability cooldowns in PvP are now only increased by 50% (previously were increased by 100%)"
> "Capped at inflicting at most 10 Damage Per Control Slot over a 3 second window to individual players in PvP" -- 근접
> "Capped at inflicting at most 7 Damage Per Control Slot over a 3 second window to individual players in PvP. Capped at 8 tiles distance." -- 원거리 / 주문
> "Player pets move at 80% speed while attacking a player target" -- 소환수에도 해당하는지는 적혀 있지 않다

위키 소환수 데이터 (`Module:SummonableCreatureData`. 기본 스탯이라 SS 120 스케일 전 값이다):

| 언데드 (원본)                   | 슬롯 | 공격 | HP      | 데미지 | Wrestling | AR | MR      | 능력                    | PvP                    |
|---------------------------------|------|------|---------|--------|-----------|----|---------|-------------------------|------------------------|
| Lich (Fire Elemental)           | 2    | 주문 | 400     | 28-34  | 85        | 25 | 100     | Epic Barrage            | 가장 약하다            |
| Vampire Thrall (Daemon)         | 2    | 주문 | **600** | 26-32  | 95        | 50 | 100     | Fury (3분에 +30%)       |                        |
| Rag Witch (Water Elemental)     | 2    | 주문 | 550     | 24-30  | 100       | 50 | **150** | Mirror, Flux (parry 25) | 주문에 가장 강하다     |
| Ancient Mummy (Earth Elemental) | 2    | 근접 | 550     | 30-36  | 95        | 75 | 50      | Rooted                  | 따라가야 한다          |
| Skeletal Fiend (Air Elemental)  | 2    | 근접 | 500     | 34-40  | 100       | 50 | 100     | Cleave                  | 따라가야 한다          |
| Jackal Spirit (Energy Vortex)   | 2    | 근접 | 500     | 38-46  | 105       | 50 | 100     | Discharge               | **플레이어를 안 친다** |
| Skeletal Husk (Blade Spirit)    | 1    | 근접 | 250     | 20-24  | 90        | 50 | 100     | Diversion               | **플레이어를 안 친다** |

- **PvP 에서는 소환수끼리 딜 차이가 줄어든다.** 2슬롯 소환수 하나가 플레이어에게 넣는 양은 3초에 주문 14 · 근접 20 이 상한이다.
- **Lich 를 PvM 기본으로 쓰는 이유가 PvP 에서는 사라진다.** Hex 는 Fire Tome 업그레이드이고 Tome 은 플레이어 상대로 적용되지 않는다. Mana Drain 도 절반이다.
- 그러면 남는 차이는 **버티는 힘**이다. Vampire (HP 600) 와 Rag Witch (MR 150) 가 Lich (HP 400, AR 25) 보다 낫다.
- 주문형 소환수는 PK 의 Magic Resist 포션 (-10 / 20 / 30%) 에 깎인다. 근접형은 안 깎이지만, 거리를 두는 메이지 PK 에게 붙어야 딜이 들어간다.
- Dispel 은 어느 소환수든 같은 확률로 막는다 (Spirit Speak 120 이면 60%).
- **PK 앞에서 다시 부를 수는 없다고 본다.** 5초 시전에 상대 4서클 이상 주문은 100% 끊고, Vengeful Spirit 도 다시 켜야 한다. 그러므로 PK 전에 쓰는 소환수는 **사냥하던 소환수**다.

## 7. Parrying

> "Players may parry melee attacks with shields, two-handed weapons, paired weapons (wrestling/dual wielding) and parry daggers."
> "Chance to parry a melee attack is (50% * (Parrying Skill / 100))"
> "Successfully parrying an attack from another player or creature will reduce its damage by 75%"
> "Successfully parrying an attack from another player, while wielding a two-handed weapon, will reduce its damage by only 50% however"
> "You cannot parry spells in PVP"
> "Provides a (50% * (Effective Parry Skill / 100)) reduction to Stamina losses that occur due to taking damage"

| Parrying | 근접 막기 | 막으면                  | 피격 스태미나 손실 |
|----------|-----------|-------------------------|--------------------|
| 80       | 40%       | -75% (양손 무기면 -50%) | -40%               |
| 100      | 50%       | 같음                    | -50%               |

- **PvP 주문은 못 막는다.** 메이지 PK 상대로 남는 것은 스태미나 손실 감소뿐이다.
- 레슬링 무기는 무기표에 **2H** 로 적혀 있다. PvP 패링 감소가 -50% 로 줄어드는지는 확인되지 않았다.

PvP 근접 데미지 기대 감소 = 막을 확률 x 감소율.

| Parrying | 방패 · paired           | 양손 무기         |
|----------|-------------------------|-------------------|
| 80       | `40% x 75% =` **30%**   | `40% x 50% =` 20% |
| 100      | `50% x 75% =` **37.5%** | `50% x 50% =` 25% |

### 7.1 패리 메이지가 있는 이유

주문 방어가 아니라 **근접 방어와 방패**다.

> "Players with both 80 Magery and 80 Parrying or greater may cast spells and meditate with a shield (meditation rate will still be affected by the shield's meditation penalty)" -- Parrying
> "Armor rating provided from shields is (50% * Shield Base AR) + (50% * Shield Base AR * (Parrying Skill / 100))" -- Parrying
> "Hits from a Macing-skill weapon against another player have a (100% * (Damage / 50)) chance to cause the player to lose 5 Stamina" -- Mace Fighting
> "Dexterity Penalties have been removed from armor and shields and replaced with a Stamina Fatigue Penalty that increases the amount of stamina the player loses when taking damage" -- Armor & Weapons

- 메이지는 **Magery 80 + Parrying 80 이 있어야 방패를 든 채 시전한다.** 방패 AR 도 Parrying 에 비례한다.
- PvP 에서 하는 일은 덱서의 근접을 막고, 맞을 때 잃는 스태미나를 줄이는 것이다.
  스태미나가 0 이면 걷게 된다 (Hamstring 원문 "reduced to 0 Stamina ... forcing them to walk").
- PvM 에서 하는 일이 더 많다. 크리처 주문 패링 (`25% x (Parrying / 100)`, -75%), Taunt, Parry Codex.
- Parry Codex 에는 Mirror ("reduces Spell Damage taken by 6% per rank") 같은 스탠스가 있다.
  하지만 Codex 문서 분류는 PvM 이고 XP 도 크리처를 잡아야 오른다. **PvP 에 적용되는지는 적혀 있지 않다.**
- 위키 메이지 템플릿 페이지에 패리 메이지는 없다. Parry Codex 를 요구하는 메이지는 New Player 페이지의 Arcane Mage 하나다.

**메이지 PK 상대로 패링이 막는 것은 없다.** 근접 PK 나 무기를 든 하이브리드 상대로는 위 30% 가 그대로 산다.

## 8. Resisting Spells

> "Spell damage taken is reduced by a minimum of (12.5% * (Magic Resist Skill / 100)) (PvM/PvP)"
> "Spell damage taken is reduced by a maximum of (37.5% * (Magic Resist Skill / 100)) (PvM/PvP)"
> "The chance to resist any hostile spell with a non-damaging effect such as Curse or Poison is ((40% - (Spell Circle * 5%)) * (Magic Resist Skill / 100))"

위키 표 (발췌). 서클 칸은 비데미지 주문 저항 확률이다.

| Resist | 데미지 감소  | 1서클 | 2서클 | 3서클 | 4서클 | 5서클 | 6서클 | 7서클 | 8서클 |
|--------|--------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 80     | 10 ~ 30%     | 28%   | 24%   | N/A   | 16%   | 12%   | 8%    | 4%    | N/A   |
| 100    | 12.5 ~ 37.5% | 35%   | 30%   | N/A   | 20%   | 15%   | 10%   | 5%    | N/A   |

- 서클 (위키 Magery 주문표): Weaken 1, **Poison · Telekinesis 3**, Curse 4, Paralyze 5, **Energy Bolt · Explosion 6**, Mana Vampire 7.
- 위키 표는 3서클을 N/A 로 적는데 본문은 3서클인 Poison 을 예로 든다. 서로 맞지 않는다. 확인되지 않았다.
- 바드는 **Defensive Barding 이 켜져 있으면 100 행, Heat of Battle 중이면 printed 행이다** ([bard-necro-handbook.md](bard-necro-handbook.md) 6.1절).

## 9. 근접 반격력

> "Unarmed Wrestling base damage against players is 1-4" -- Wrestling
> "Damage from Wrestling Weapons in PvP will scale based on the player's Raw Dex stat as a % (without any adjustments for Dex bonuses or penalties from Potions, Bless, Weaken, other effects)" --
> Wrestling
> "Wrestling Weapons can be disarmed, which will result in the player dealing standard "Unarmed" 1-2 damage during that time" -- Wrestling
> "Wrestling Weapons receive a +20% Melee Damage bonus towards creatures that is applied to Two-Handed Weapons (since players cannot equip shields while using Wrestling Weapons)" -- Wrestling

위키 무기표의 Grinding (Light) 행:

| 계열          | 초/스윙 | 데미지  | 평균 | DPS       | 무기                                            |
|---------------|---------|---------|------|-----------|-------------------------------------------------|
| Wrestling     | 1.67    | 13 ~ 31 | 22   | **13.17** | Martial Manual, Cestus, Fistblade               |
| Swordsmanship | 1.56    | 13 ~ 23 | 18   | 11.54     | Longswords, Broadsword, Viking Sword, Norse Axe |
| Mace Fighting | 1.63    | 12 ~ 24 | 18   | 11.04     | Mace, Maul, War Mace, Flanged Mace, Flail       |
| Throwing      | 1.88    | 14 ~ 24 | 19   | 10.11     | Throwing Dagger, Throwing Star                  |
| Archery       | 2.21    | 13 ~ 25 | 19   | 8.6       | Bow, Hunting Bow, Recurve Bow                   |

- **맨손은 PvP 에서 1~4 다.** 레슬링으로 싸우려면 레슬링 무기가 전제다.
- 레슬링 무기의 PvP 데미지는 **raw Dex 비율**이다. raw Dex 100 이면 100%, 50 이면 50%. 포션·Bless 는 안 친다.
- 레슬링 무기는 방패를 못 든다. 패링은 무기 자체로 한다 (7절).

## 10. Tracking

> "A downside of Bard Templates is clear lack to fight back Pks / Griefers. Through Defensive Barding they are tough to kill but lack the offensive to fight back." -- TemplatesBard
> "Consider squeezing 80-100 Tracking into a template to passively track hostile players (PK's) so you can avoid them." -- TemplatesBard
> "On a successful tracking attempt, players can see a list of non-hidden targets within (20 + (80 * (Tracking Skill / 100))) tiles"
> "Inside dungeons, this tracking distance is halved (20 + (80 * (Tracking Skill / 100))) / 2 tiles"
> "Increases Effective Barding skill by (10 * (Tracking Skill / 100))"
> "When attacking any creature add Base Weapon Damage * (25% * (Tracking Skill / 100)) supplemental bonus damage per weapon hit."
> "When attacking any player, add Base Weapon Damage * (10% * (Tracking Skill / 100)) supplemental bonus damage per weapon hit"

| Tracking | 탐지 거리 야외 / 던전 | Effective Barding | 무기 딜 PvM / PvP |
|----------|-----------------------|-------------------|-------------------|
| 80       | 84 / 42 타일          | +8                | +20% / +8%        |
| 100      | 100 / 50 타일         | +10               | +25% / +10%       |

- 바드에게 주는 Effective Barding 보너스와 Hunting 이 바드 스킬 쿨에 끼치는 영향은 [bard-necro-handbook.md](bard-necro-handbook.md) 6.6절.
- Hunting 모드를 "Murderer Players" 로 켜는 코드가 이미 있다: `script/gather/mining.razor:195`.
- Hamstring 두 번째 줄 목록에 들어 있다 (3절).

### 10.1 Hunting 모드

> "Players can activate and deactivate a "Hunting" mode from the Tracking window to automatically make Tracking skill checks at various intervals (still requiring the normal 5 second skill cooldown)
> against a specific type of player/creature"
> "Players will always receive their bonuses to Damage and Barding Skill from the Tracking skill even if they are not currently Hunting"
> "Tracking success chance is (100% * (Tracking Skill / 100))"

- **딜·바딩 보너스는 Hunting 을 안 켜도 붙는다.** PK 조기 발견에만 Hunting 이 필요하다.
- 판정 한 번의 성공률은 Tracking 80 이면 80% 다.
- **Hunting 의 자동 판정도 5초 스킬 쿨을 쓴다.** 서버 스킬 게이트가 하나라 다른 스킬과 부딪칠 수 있다.
- 판정 빈도는 Hunt Frequency 로 고른다. "New When No Arrow" 와 "New When No Target" 은 화살표가 없을 때만 판정한다.
  주변에 Murderer 가 없으면 화살표가 없으므로 계속 판정한다.

## 11. 자주 틀렸던 것

| 틀린 생각                                              | 사실                                                                                                          |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| 레슬링이 0 이면 PvP 에서 못 때린다                     | **아니다.** 공격은 든 무기의 스킬로 판정한다. 레슬링은 맨손·레슬링 무기로 칠 때만 쓴다                        |
| 레슬링 100 이면 명중 50%                               | **스킬이 같으면 50% 다.** 100 대 100 이라서 50% 다                                                            |
| 메이지 PK 를 맞히려면 내 레슬링이 필요하다             | **내 무기 스킬 대 상대 레슬링이다.** 메이스 100 이면 50%, 80 이면 43.3%                                       |
| PK 가 먼저 쳤으면 반격해도 Heat of Battle 이 안 켜진다 | **자동 반격 스윙만 예외다.** 타겟을 바꾸거나 해로운 주문을 쓰면 켜진다                                        |
| 레슬링 무기 데미지는 4~13 이다                         | **13~31, 평균 22.** 무기표의 DiceMax(4) 와 MinDmg(13) 칸을 데미지로 잘못 읽은 값이었다                        |
| 붙은 폭발 포션은 리콜로 피한다                         | **따라온다.** 던진 사람 곁으로 가면 데미지가 반으로 나뉜다                                                    |
| 패링으로 PK 의 주문을 막는다                           | **못 막는다.** "You cannot parry spells in PVP". 패리 메이지의 이유는 근접 방어와 방패 시전이다               |
| 던전에서도 룬북으로 도망친다                           | **Golden Moongate 8타일 안에서만 리콜된다**                                                                   |
| Summoner's Tome 투자는 PvP 에서도 소환수를 세게 한다   | **안 한다.** "Summoner Tome upgrades will not apply against players". 스탯도 printed Spirit Speak 로 돌아간다 |
| 자기 TK 는 PK 가 나타난 뒤 아무 때나 걸면 된다         | **상대 TK 보다 먼저여야 한다.** 한 사람은 30초에 한 번만 TK 에 맞는다                                         |

## 12. 참고 링크

- [Heat of Battle](https://wiki.uooutlands.com/Heat_of_Battle) -- 공격적 행동의 정의, 자동 반격 예외
- [PATCH: Murderer and PvP Overhaul (2020-09-28)](https://forums.uooutlands.com/index.php?threads/patch-murderer-and-pvp-overhaul-general-changes.3232/) -- Heat of Battle 지속시간, Telekinesis 포션
- [Wrestling](https://wiki.uooutlands.com/Wrestling) / [Mace Fighting](https://wiki.uooutlands.com/Mace_Fighting) -- 명중 공식, 레슬링 무기
- [Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons) -- 무기표, 명중 보너스 상한
- [Arcane Staff](https://wiki.uooutlands.com/Arcane_Staff)
- [Hamstring](https://wiki.uooutlands.com/Hamstring)
- [Alchemy](https://wiki.uooutlands.com/Alchemy) -- Sticky Potions, 포션 보너스
- [Magery](https://wiki.uooutlands.com/Magery) -- 인터럽트, Recall 제한, Telekinesis, Magic Reflection
- [Evaluating Intelligence](https://wiki.uooutlands.com/Evaluating_Intelligence) -- PvP 배율, 보조 스킬 상한
- [Inscription](https://wiki.uooutlands.com/Inscription)
- [Meditation](https://wiki.uooutlands.com/Meditation)
- [Wizard's Grimoire](https://wiki.uooutlands.com/Wizard%27s_Grimoire)
- [Spirit Speak](https://wiki.uooutlands.com/Spirit_Speak) -- PvP 소환수 스탯, Dispel
- [Necromancy](https://wiki.uooutlands.com/Necromancy) -- PvP 에서 능력이 안 먹는 것
- [Herding](https://wiki.uooutlands.com/Herding)
- [Animal Taming](https://wiki.uooutlands.com/Animal_Taming) -- 팔로워 PvP 규칙
- [Parrying](https://wiki.uooutlands.com/Parrying)
- [Resisting Spells](https://wiki.uooutlands.com/Resisting_Spells)
- [Tracking](https://wiki.uooutlands.com/Tracking)
- [TemplatesBard](https://wiki.uooutlands.com/TemplatesBard)
