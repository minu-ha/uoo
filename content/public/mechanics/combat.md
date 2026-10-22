---
name: Combat
label: 전투 메커니즘
group: Mechanics
order: 50
---

방어구와 마나 재생, 근접 무기, 붕대, 스탯 포션, Parrying, Resisting Spells, Tracking의 서버 규칙.
PvP 자체의 규칙(Heat of Battle, 명중률, TK)은 [PvP](../game/pvp.md), 템플릿별 선택은 각 템플릿 문서.

## <a id="00"></a>00 한눈에

| 절 | 내용 |
| --- | --- |
| [01](#01) | 방어구 재질별 자연 마나 재생 |
| [02](#02) | 맨손과 레슬링의 반격력. 보조 피해 상한, 스윙 간격, 붕대, 스탯 포션, 방어구 AR |
| [03](#03) | 패링으로 막는 것과 못 막는 것 |
| [04](#04) | PvP에서 Resist의 감소량 |
| [05](#05) | PK 조기 발견 |
| [06](#06) | 자주 틀렸던 생각 |
| [07](#07) | 출처 |

이 문서에 걸린 질문은 [Open items](../questions/open-items.md).

::part[회복]

## <a id="01"></a>01 방어구와 자연 마나 재생

> "The baseline Mana Regen rate is 1 mana restored every 2 seconds (i.e., 0.5 mana per second)." -- Meditation
> "The minimum Mana Regen rate is 1 mana restored every 8 seconds (i.e., 0.125 mana per second)." -- Meditation
> "A player's Total Armor Meditation Penalty is equal to the combined Meditation Penalties of all armor worn" -- Meditation
> "Which would result in a (2 \* 16.3%) = -32.6% effect on their Mana Regen rate." -- Meditation, 스터디드 한 벌과 플레이트 고짓의 예

- [Meditation](https://wiki.uooutlands.com/Meditation) 기본 재생: 2초에 1마나
- 부위 하나의 페널티 = 부위 비율 × 재질 비율. 입은 부위의 합계 × 2 = 재생 감소율
  - 부위: 가슴 35%, 다리 22%, 팔 15%, 머리 14%, 장갑 7%, 목 7%, 방패 35%([Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons))
  - 재질: 가죽 0%, 스터디드 10%, 본 25%, 링 50%, 체인 75%, 플레이트 100%
- Leather = 방어구에 의한 재생 감소 없음. 재생 가산은 아님
- Meditation 0, 가죽, 다른 보정 없음 → 이론상 30초에 15, 60초에 30마나

방패 없이 한 재질로 여섯 부위를 입은 한 벌. 간격은 아래 나누기 식, Meditation 0.

| 한 벌 | 페널티 합계 | 재생 감소 | 1마나 간격 | 120초 재생 |
| --- | --- | --- | --- | --- |
| 가죽 | 0% | 0% | 2초 | 60 |
| 스터디드 | 10% | 20% | 2.4초 | 50 |
| 본 | 25% | 50% | 3초 | 40 |
| 링 | 50% | 100% | 4초 | 30 |
| 체인 | 75% | 150% | 5초 | 24 |
| 플레이트 | 100% | 200% | 6초 | 20 |

- 감소율을 재생에서 빼는지 나누는지는 위키 문장만으로 안 정해짐. 빼면 링 한 벌부터 0 → 최저점 8초
- [outlandsbutler.com](https://www.outlandsbutler.com/) 장비 계산은 나누기: `1마나 간격 = 2초 × (1 + 감소율)`. 체인 한 벌 5초, 플레이트 한 벌 6초. 2026-10-21 사용자 화면
- 위키가 한 벌 효과를 −100%, −150%, −200%로 따로 적는 것과 맞는 쪽은 나누기 → 이 표도 나누기. 실제 간격은 확인되지 않았다
  - 확인 방법: 체인 한 벌, 음식 버프 없이 마나 10이 차는 시간. 나누기면 50초, 빼기면 80초
- 나누기면 갑옷만으로는 최저점(8초)에 닿지 않음. 플레이트 한 벌이 6초
- Butler는 음식 버프의 재생 +25%를 곱함(체인 0.2 → 0.25마나/초). 위키 근거는 확인되지 않았다
- 수동 Meditation 성공 상태 유지는 가정하지 않음. 이동, 행동, 피격으로 끊기는 능동 명상을 추격 중 유지한다고 보지 않음
- 마나가 가득 찬 동안의 재생은 쌓이지 않음. 시전 비용, 시점, 장비 변경에 따라 실제 남는 마나는 다름
- 최대 마나 ≠ 현재 마나. INT 45에서 Earth Elemental의 50마나 비용은 스크롤 성공률 보정으로 해결 불가
- 버프로 늘어난 최대치 ≠ 현재 마나 회복. 템플릿 적용은 [Lumberjack PvP](../templates/lumberjack-pvp.md#04) 04절

::part[근접]

## <a id="02"></a>02 근접 반격력

**맨손은 PvP 데미지 1\~4 → 반격력 없음.** 레슬링으로 싸우려면 레슬링 무기 필요.

> "Unarmed Wrestling base damage against players is 1-4" -- Wrestling
> "Damage from Wrestling Weapons in PvP will scale based on the player's Raw Dex stat as a % (without any adjustments for Dex bonuses or penalties from Potions, Bless, Weaken, other effects)" --
> Wrestling
> "Wrestling Weapons can be disarmed, which will result in the player dealing standard "Unarmed" 1-2 damage during that time" -- Wrestling
> "Wrestling Weapons receive a +20% Melee Damage bonus towards creatures that is applied to Two-Handed Weapons (since players cannot equip shields while using Wrestling Weapons)" -- Wrestling

위키 무기표의 Grinding (Light) 행.

| 계열 | 스윙 간격(초) | 데미지 | 평균 | DPS | 무기 |
| --- | --- | --- | --- | --- | --- |
| Wrestling | 1.67 | 13\~31 | 22 | **13.17** | Martial Manual, Cestus, Fistblade |
| Swordsmanship | 1.56 | 13\~23 | 18 | 11.54 | Longswords, Broadsword, Viking Sword, Norse Axe |
| Mace Fighting | 1.63 | 12\~24 | 18 | 11.04 | Mace, Maul, War Mace, Flanged Mace, Flail |
| Throwing | 1.88 | 14\~24 | 19 | 10.11 | Throwing Dagger, Throwing Star |
| Archery | 2.21 | 13\~25 | 19 | 8.6 | Bow, Hunting Bow, Recurve Bow |

- 레슬링 무기의 PvP 데미지는 **raw Dex 비례.** raw Dex 100이면 100%, 50이면 50%. 포션이나 Bless로 올린 Dex는 제외
- 레슬링 무기를 들면 방패 불가. 패링은 무기 자체로(03절)
- 무장 해제 중 데미지: 원문 "Unarmed" 1-2. 플레이어 상대 맨손 1\~4와 어느 쪽이 맞는지는 확인되지 않았다

### <a id="02.A"></a>02.A 보조 피해 상한과 도끼

> "Total of 20% Damage Bonus from all Supplemental skills" / "Total of 10% Damage Bonus from all Supplemental skills" —
> [PvP Damage Cap](https://wiki.uooutlands.com/PvP_Damage_Cap)

- 근접 보조 피해 상한 20%, 주문 보조 피해 상한 10%. **Tactics와 Anatomy는 근접 상한 밖, Eval은 주문 상한 밖**
- 보조 스킬의 PvP 기본 비율: 스킬 100당 10%. 스킬마다 정한 무기나 주문 조건 필요
- PvP Damage Cap 표: Lumberjacking 보너스는 **도끼만**, Mining 보너스는 메이스 계열만
- Swordsmanship이라고 모두 도끼는 아님. Katana와 Halberd는 Lumberjacking 보너스 대상 아님
- 디스코드의 "arguably it should be all swords"는 의견일 뿐, 현재 적용 범위 아님

> "(-50% + (Tactics Skill / 200))" — [Tactics](https://wiki.uooutlands.com/Tactics)

- Tactics 0\~100의 기본 무기 피해 조정식. 80은 -10%, 100은 0% → 80에서 100으로 올리면 기본 피해 10%p 회복
- 최종 피해가 정확히 10% 늘어난다는 뜻은 아님

> "Base Weapon Damage \* (20% \* (Anatomy Skill / 100))" — [Anatomy](https://wiki.uooutlands.com/Anatomy)

- Anatomy 80이면 기본 무기 피해 +16%, 100이면 +20%. Anatomy만으로 붕대 회복 대체 불가

### <a id="02.B"></a>02.B 현재 스태미나와 무기 교체

> "15000 / (Current Stamina (max 100) + 100) \* Weapon Speed)" —
> [Swing Speed](https://wiki.uooutlands.com/Swing_Speed)

- 원문 식의 괄호 불일치. 같은 페이지 무기표에 맞춘 식: `스윙 간격 = 15000 / ((min(현재 스태미나, 100) + 100) × 무기 Speed)`초
- PvP는 현재 스태미나와 무기 Speed만. PvM의 Aspect나 스킬 공속 보너스 없음
- 현재 스태미나가 간격을 정함 → 맞아서 줄어든 스태미나만큼 느려짐. Speed 20 무기는 스태미나 100에서 3.75초, 60에서 4.69초
- [Quick Switch](https://wiki.uooutlands.com/Combat_Overview)의 기준은 마지막 장착이 아닌 마지막 스윙
- 빠른 무기로 바꾸면 마지막 스윙부터 빠른 무기 간격, 느린 무기로 바꾸면 느린 무기 간격
- 무기별 별도 타이머로 중간에 공짜 한 대를 끼우는 구조 아님

> "increases the amount of stamina the wearer will lose when taking damage" / "A player's Total Stamina Fatigue Penalty is their (Total Armor Meditation Penalty / 2)." —
> [Armor & Weapons의 Stamina Fatigue Penalties](https://wiki.uooutlands.com/Armor_%26_Weapons)

- 방어구가 무거울수록 맞을 때 스태미나를 더 잃음. 위키 식이면 체인 한 벌 37.5%, 플레이트 한 벌 50%(페널티 합계는 01절)
- Butler 화면은 절반이 아닌 합계 그대로(체인 75%, 플레이트 100%). 위키 본문의 체인 예시(80%)도 표와 다름 → 실제 값은 확인되지 않았다

### <a id="02.C"></a>02.C 붕대의 회복량과 시간

> "Bandaging time is 15 - (5 \* (dex - 25) / 75) seconds" — [Healing](https://wiki.uooutlands.com/Healing)

- 자기 붕대 시간은 DEX 100까지만 감소. 식의 DEX는 버프 반영값, 스윙 계산의 현재 스태미나와는 다름

> "Random Value of 40 to 60" — [Healing의 회복식](https://wiki.uooutlands.com/Healing)

- 회복식: `(Healing / 100) × (40~60) × (1 + 0.2 × Anatomy / 100)`
- 슬립 하나마다 회복량 2% 감소. 아래 범위는 슬립, 다른 보정, 정수 반올림 제외

| Healing | Anatomy | 회복량 | 평균 |
| --- | --- | --- | --- |
| 80 | 0 | 32\~48 | 40 |
| 80 | 80 | 37.12\~55.68 | 46.4 |
| 100 | 80 | 46.4\~69.6 | 58 |
| 80 | 100 | 38.4\~57.6 | 48 |

- 붕대 해독: Healing과 Anatomy 각 60 이상. 부활 시도: 각 80 이상
- PvP에서 독 상태로 붕대를 쓰면 PvM처럼 해독과 HP 회복을 함께 한다고 계산하지 않음
  ([Heal through Poison](https://wiki.uooutlands.com/Combat_Overview))

> "Chance to resurrect with less than 100 Healing scales from 24% with 80 Healing skill to 62% with 99 Healing skill." /
> "Players with 100 Healing and 80 Anatomy skill will always have 100% chance to resurrect their target with bandages." —
> [Healing](https://wiki.uooutlands.com/Healing)

> "Bandaging another target takes 5-7.5 seconds, scaled based on Healer's Dexterity (capped at 100 Dexterity)" — [Healing](https://wiki.uooutlands.com/Healing)

- 붕대 부활 확률: Healing 80에서 24%, 99에서 62%, 100이면 늘 성공. 사이 값의 식은 위키에 없음
- 남에게 붕대: 5\~7.5초, DEX 100에서 5초. 부활에 걸리는 시간은 위키에 없음

### <a id="02.D"></a>02.D 스탯 포션과 Bless

> "Increases max strength/hp by 20" / "Increases max dexterity/stamina by 20" —
> [Alchemy의 Greater Strength와 Greater Agility](https://wiki.uooutlands.com/Alchemy)

- Greater Strength: STR과 최대 HP +20. Greater Agility: DEX와 최대 스태미나 +20
- [Bless](https://wiki.uooutlands.com/Template:SpellCircles)의 스탯 보정식 `11 × Magery / 100` → Magery 80이면 8.8
- **포션과 안 겹침.** 힘, 민첩 포션이 걸린 동안 Bless는 STR, DEX를 더 올리지 않음 → 남는 것은 INT(최대 마나). 인게임 확인됨 2026-10-21
- 실제 정수 처리는 확인되지 않았다
- 버프 바로는 포션 판별 불가. 위키 [BuffIcons](https://wiki.uooutlands.com/Template:BuffIcons)는 같은 아이콘을 `Strength Spell / Potion`, `Agility Spell / Potion`으로 표기
- 인게임 확인됨 2026-10-09: Magery 100 Bless는 `Your strength/dexterity/intelligence has changed by 11`, 버프 바에 `Strength`, `Agility`, `Cunning`
- 스탯 포션 버프 이름에도 Potion 없음 → `findbuff 'Strength'`로 보면 내 Bless든 아군 Bless든 걸린 동안 포션을 안 마심
- 포션 루프는 스탯 값으로 판정. Greater 포션을 마신 값(기본 + 20)을 `config__str_potion`, `config__dex_potion`에 두고, 그보다 낮으면 마심
- Bless와 Strength, Agility 주문은 식상 Magery 100에서 11, 120에서도 13.2 → 그 선 아래
- Razor 스크립트는 덧셈 불가 → 기본값이 아닌 기준선을 기록([Razor](../scripting/razor.md#05) 05절)
- 포션마다 재시도 간격. 스탯은 마신 뒤 한 왕복 늦게 오르고, Curse, Weaken, Clumsy는 포션 효과 중에도 스탯을 선 아래로 누름
- 간격이 없으면 거절될 마시기가 패스마다 회복 포션과 같은 아이템 큐로 나감
- Magic Resist 포션은 제 아이콘 `Magic Resist Potion`으로 판정(인게임 확인됨 2026-10-09)
- INT 45에 Bless: 정수 처리 전 최대치 53.8(56 아님). Bless 자체도 9마나
- 최대치 증가 시 현재 마나 증가량은 별도 측정 필요 → 시전 직후 현재 마나 53.8을 약속하지 않음

### <a id="02.E"></a>02.E 방어구를 반영한 근접 계산 예시의 전제

> "Minimum Amount: (.333% \* (Total Armor Value))" / "Maximum Amount: (.666% \* (Total Armor Value))" —
> [Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons)

- 위 공식상 물리 피해 감소 범위: `AR × 0.333%`부터 `AR × 0.666%`. AR 50이면 16.65\~33.30% 감소, 0.667\~0.8335 남음
- 위키의 AR 50 설명은 16.5\~33%로 축약. 여기서는 인용 계수 그대로, 서버 정수 처리는 제외
- 기본 무기 피해에 Tactics, Anatomy, 해당 보조 피해를 적용한 뒤 이 비율로 비교
- Parry, Reactive Armor, 무기 품질, 마법 옵션, 추가 효과, 정수 처리는 별도 조건
- 피해 중간값에 명중률을 곱해도, 접근 실패와 이동 시간을 반영한 실전 DPS는 아님

NPC 판매 방어구의 부위별 AR. [Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons)의 표.

| 부위 | 가죽 | 스터디드 | 본 | 링 | 체인 | 플레이트 |
| --- | --- | --- | --- | --- | --- | --- |
| 가슴 | 9 | 11 | 12 | 14 | 16 | 18 |
| 다리 | 6 | 7 | 8 | 9 | 10 | 11 |
| 팔 | 4 | 5 | 5 | 6 | 7 | 8 |
| 장갑 | 2 | 2 | 2 | 3 | 3 | 4 |
| 목 | 2 | 2 | 2 | 3 | 3 | 4 |
| 머리 | 4 | 4 | 5 | 6 | 6 | 7 |
| 방패 | 4 | 5 | 6 | 7 | 8 | 9 |
| 방패 뺀 여섯 부위 합 | 27 | 31 | 34 | 41 | 45 | 52 |

- 위키의 한 벌 Base Armor(25, 30, 35, 40, 45, 50)와 표의 합이 조금 다름. 이유는 위키에 없음
- AR은 부위 비율 없이 그대로 더함. 부위 비율은 마나 페널티(01절)에만
- 마법과 제작 보정: Defense +20%, GM과 Guarding +40%, Hardening +60%, Fortification +80%, Invulnerability +100%. 부서진 방어구는 AR 50% 감소

::part[스킬]

## <a id="03"></a>03 Parrying

**패링은 근접만 막음.** PvP 주문 방어 불가 → 메이지 PK 상대로는 피격 스태미나 감소 효과만.
근접 PK나 무기 든 하이브리드 상대로는 Parrying 80 방패가 근접 데미지를 기대값 30% 감소.

> "Players may parry melee attacks with shields, two-handed weapons, paired weapons (wrestling/dual wielding) and parry daggers."
> "Chance to parry a melee attack is (50% \* (Parrying Skill / 100))"
> "Successfully parrying an attack from another player or creature will reduce its damage by 75%"
> "Successfully parrying an attack from another player, while wielding a two-handed weapon, will reduce its damage by only 50% however"
> "You cannot parry spells in PVP"
> "Provides a (50% \* (Effective Parry Skill / 100)) reduction to Stamina losses that occur due to taking damage"

| Parrying | 근접을 막을 확률 | 막으면 | 맞을 때 잃는 스태미나 |
| --- | --- | --- | --- |
| 80 | 40% | -75%(양손 무기면 -50%) | -40% |
| 100 | 50% | 같음 | -50% |

- 레슬링 무기는 무기표에 **2H** 표기 → PvP 패링 감소가 -50%로 줄어드는지는 확인되지 않았다

PvP 근접 데미지 기대 감소 = 막을 확률 × 감소율.

| Parrying | 방패, paired 무기 | 양손 무기 |
| --- | --- | --- |
| 80 | `40% x 75% =` **30%** | `40% x 50% =` 20% |
| 100 | `50% x 75% =` **37.5%** | `50% x 50% =` 25% |

### <a id="03.A"></a>03.A 패리 메이지가 있는 이유

목적은 주문 방어가 아니라 **근접 방어와 방패 착용**.

> "Players with both 80 Magery and 80 Parrying or greater may cast spells and meditate with a shield (meditation rate will still be affected by the shield's meditation penalty)" -- Parrying
> "Armor rating provided from shields is (50% \* Shield Base AR) + (50% \* Shield Base AR \* (Parrying Skill / 100))" -- Parrying
> "Hits from a Macing-skill weapon against another player have a (100% \* (Damage / 50)) chance to cause the player to lose 5 Stamina" -- Mace Fighting
> "Dexterity Penalties have been removed from armor and shields and replaced with a Stamina Fatigue Penalty that increases the amount of stamina the player loses when taking damage" -- Armor &
> Weapons

- 메이지는 **Magery 80과 Parrying 80이 모두 있어야 방패를 든 채 시전.** 방패 AR: Parrying 0이면 Base AR의 절반, 100이면 전부
- PvP: 덱서의 근접 방어, 피격 스태미나 감소. 스태미나 0이면 걷기(Hamstring 원문 "reduced to 0 Stamina ... forcing them to walk")
- PvM: 역할이 더 많음. 크리처 주문 패링(`25% x (Parrying / 100)`, -75%), Taunt, Parry Codex
- Parry Codex에는 Mirror("reduces Spell Damage taken by 6% per rank") 같은 스탠스. 단 Codex 문서는 PvM 분류, XP도 크리처 처치로만 → **PvP 적용 여부 미기재**
- 위키 메이지 템플릿 페이지에 패리 메이지 없음. Parry Codex를 요구하는 메이지는 New Player 페이지의 Arcane Mage 하나

## <a id="04"></a>04 Resisting Spells

**Resist는 PvP에서도 주문 데미지 감소(80이면 10\~30%).** Curse, Poison 같은 비데미지 주문도 가끔 막음, 서클이 높을수록 확률 하락.

> "Spell damage taken is reduced by a minimum of (12.5% \* (Magic Resist Skill / 100)) (PvM/PvP)"
> "Spell damage taken is reduced by a maximum of (37.5% \* (Magic Resist Skill / 100)) (PvM/PvP)"
> "The chance to resist any hostile spell with a non-damaging effect such as Curse or Poison is ((40% - (Spell Circle \* 5%)) \* (Magic Resist Skill / 100))"

위키 표 발췌. 서클 칸 = 비데미지 주문 저항 확률.

| Resist | 데미지 감소 | 1서클 | 2서클 | 3서클 | 4서클 | 5서클 | 6서클 | 7서클 | 8서클 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 80 | 10\~30% | 28% | 24% | N/A | 16% | 12% | 8% | 4% | N/A |
| 100 | 12.5\~37.5% | 35% | 30% | N/A | 20% | 15% | 10% | 5% | N/A |

- 서클(위키 Magery 주문표): Weaken 1, **Poison과 Telekinesis 3**, Curse 4, Paralyze 5, **Energy Bolt와 Explosion 6**, Mana Vampire 7
- 위키 표는 3서클 N/A, 본문은 3서클 Poison을 예로 듦 → 불일치. 확인되지 않았다
- Discordance, Peacemaking, Provocation 80, 80, 80 바드: **Defensive Barding이 켜지면 100 행, Heat of Battle 중이면 printed 행**.
  2020 패치의 `/ 3` 공식이라면 켜져 있어도 80 행([Barding](barding.md#02.I) 02.I절)

## <a id="05"></a>05 Tracking

**Tracking: PK를 먼저 보고 회피.** Tracking 80이면 판정 성공 시 야외 84타일, 던전 42타일 안의 숨지 않은 대상 표시.

> "A downside of Bard Templates is clear lack to fight back Pks / Griefers. Through Defensive Barding they are tough to kill but lack the offensive to fight back." -- TemplatesBard
> "Consider squeezing 80-100 Tracking into a template to passively track hostile players (PK's) so you can avoid them." -- TemplatesBard
> "On a successful tracking attempt, players can see a list of non-hidden targets within (20 + (80 \* (Tracking Skill / 100))) tiles"
> "Inside dungeons, this tracking distance is halved (20 + (80 \* (Tracking Skill / 100))) / 2 tiles"
> "Increases Effective Barding skill by (10 \* (Tracking Skill / 100))"
> "When attacking any creature add Base Weapon Damage \* (25% \* (Tracking Skill / 100)) supplemental bonus damage per weapon hit."
> "When attacking any player, add Base Weapon Damage \* (10% \* (Tracking Skill / 100)) supplemental bonus damage per weapon hit"

| Tracking | 탐지 거리, 야외 | 탐지 거리, 던전 | Effective Barding | 무기 딜, PvM | 무기 딜, PvP |
| --- | --- | --- | --- | --- | --- |
| 80 | 84 | 42타일 | +8 | +20% | +8% |
| 100 | 100 | 50타일 | +10 | +25% | +10% |

- 바드의 Effective Barding 보너스, Hunting이 바드 스킬 쿨에 끼치는 영향: [Bard Necro](../templates/bard-necro.md#04.E) 04.E절
- Tracking은 주문 데미지 보조 스킬이기도 함. 위키 예시는 Tracking 100을 +10%로 계산([PvP](../game/pvp.md#05) 05절)
- Hamstring 요구조건 두 번째 줄 목록에도 포함([PvP](../game/pvp.md#03) 03절)
- Hunting 모드 코드: `escape/tracking` 모듈. lumberjack-enhanced와 tamer-mage-enhanced 루프가 사용
- `config__tracking_color`: 1(기본값) murderer players, 2 회색 criminal, 3 주황 enemy, 4 셋 모두
- 옛 `script/archive/mining.razor`와 `script/archive/lumberjack.razor`는 `track_only_red_players` 하나로 murderer players와 all hostile players 중 선택

### <a id="05.A"></a>05.A Hunting 모드

**딜과 바딩 보너스는 Hunting 없이도 적용.** Hunting은 PK 조기 발견에만 필요.

> "Players can activate and deactivate a "Hunting" mode from the Tracking window to automatically make Tracking skill checks at various intervals (still requiring the normal 5 second skill cooldown)
> against a specific type of player/creature"
> "Players will always receive their bonuses to Damage and Barding Skill from the Tracking skill even if they are not currently Hunting"
> "Tracking success chance is (100% \* (Tracking Skill / 100))"

- 판정 한 번의 성공률: Tracking 80이면 80%
- **Hunting 자동 판정도 5초 스킬 쿨 사용.** 서버 스킬 게이트는 하나뿐([Barding](barding.md#01.J) 01.J절) → 다른 스킬과 충돌 가능
- 판정 빈도: Hunt Frequency. "New When No Arrow", "New When No Target"은 화살표가 없을 때만 판정
- 주변에 Murderer가 없으면 화살표도 없음 → 계속 판정

::part[기록]

## <a id="06"></a>06 자주 틀렸던 것

| 틀린 생각 | 사실 |
| --- | --- |
| 패링으로 PK 주문 방어 | **불가.** "You cannot parry spells in PVP". 패리 메이지의 목적은 근접 방어와 방패 시전(03절) |
| 레슬링 무기 데미지 4\~13 | **13\~31, 평균 22.** 무기표의 DiceMax(4)와 MinDmg(13) 칸을 데미지로 잘못 읽은 값(02절) |

## <a id="07"></a>07 참고 링크

- [Wrestling](https://wiki.uooutlands.com/Wrestling), [Mace Fighting](https://wiki.uooutlands.com/Mace_Fighting) -- 명중 공식, 레슬링 무기
- [Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons) -- 무기표, 명중 보너스 상한
- [Arcane Staff](https://wiki.uooutlands.com/Arcane_Staff)
- [Alchemy](https://wiki.uooutlands.com/Alchemy) -- Sticky Potions, 포션 보너스
- [Meditation](https://wiki.uooutlands.com/Meditation)
- [Parrying](https://wiki.uooutlands.com/Parrying)
- [Resisting Spells](https://wiki.uooutlands.com/Resisting_Spells)
- [Tracking](https://wiki.uooutlands.com/Tracking)
- [TemplatesBard](https://wiki.uooutlands.com/TemplatesBard)
