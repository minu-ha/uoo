---
name: Bard Archer
label: Bard Archer 핸드북
group: Templates
order: 30
---

Bard Archer 템플릿의 판단과 숫자. 바딩, 회복, 버프는 루프, 사격은 손.
바드 메커니즘(쿨, 송, Ensemble, Virtuoso)은 [Bard Necro](bard-necro.md) 02절, 방어구와 마나 재생, 붕대, AR은 [PvP](../game/pvp.md) 05.D절과 09절.
**숫자는 추측 금지.** 인용과 확인 표시: [Workflow](../working/workflow.md#01.C) 01.C절.

- 캐릭터 `nomeehej`, Razor 프로필 `bard`
- 사냥: `script/combat/bard-archer-enhanced.razor`(F1). PK: `script/combat/pvp.razor`(F4)
- 2026-10-21 설계. bard-necro-enhanced와 summoner 프로필은 그대로 둠

## <a id="00"></a>00 한눈에

| 절 | 내용 |
| --- | --- |
| [01](#01) | 스킬, 스탯, 코덱스, 갑옷과 마나 |
| [02](#02) | 아처리. 무기와 사격 간격, 자세, 피니셔, 무기 능력, PvP에서 빠지는 것 |
| [03](#03) | 부활 |
| [04](#04) | `bard-archer-enhanced`의 설계와 `bard` 프로필 |
| [05](#05) | 출처 |

이 문서에 걸린 질문과 인게임 확인은 [Open items](../questions/open-items.md#16) 16절.

::part[캐릭터]

## <a id="01"></a>01 캐릭터

### <a id="01.A"></a>01.A 스킬과 스탯

| 스킬 | 값 |
| --- | --- |
| Provocation, Peacemaking, Discordance | 80 |
| Musicianship | 0. Bard Codex `Self Taught` T2가 대체([Bard Necro](bard-necro.md#02.Q) 02.Q절) |
| Anatomy, Healing | 80 |
| Magery | 80 |
| Tactics, Archery | 80 |
| Resisting Spells | 80 |

- 합 720. 스탯 STR 100, DEX 80, INT 45. 교전 중 Greater Strength, Greater Agility 포션 → STR 120, DEX 100
- 무기: Rampart Crossbow. 2H, Speed 20(02.A절)
- **공격은 손.** `Z`(가장 가까운 몹)나 `Q`(Set Last Target Harmful)로 고르고 `V`(Attack Last Target)
- 루프가 맡는 것: 바딩, 회복, 자기 버프, 코덱스 자세와 피니셔 전환, 무기 능력 요청(04절)
- **warmode는 Tab으로 직접.** 켜면 손으로 바딩하는 구간 → 루프의 바딩, 노래, 버프, 음식 정지(04.A절). `Z`, `V`는 warmode를 안 바꿈
- 바딩, 시전과 사격은 서로 안 막음. 사용자 확인 2026-10-21

### <a id="01.B"></a>01.B 코덱스

Bard Codex 20점. 효과 원문과 티어별 값은 [Bard Necro](bard-necro.md#02.Q) 02.Q절.

| 업그레이드 | 점수 | 이 템플릿에서 |
| --- | --- | --- |
| Ensemble | 5 | Discord와 Peace나 Provo가 함께 걸린 대상에 +40% |
| Perfect Pitch | 5 | 바딩 성공률 +30% of normal |
| Virtuoso | 5 | 성공한 바딩 뒤 15초, 바딩한 대상에 피해와 저항 +20%(세 스킬 80) |
| Self Taught | 3 | Musicianship 80 대체 |
| Refrain | 1 | Barding Break 4% 무시 |
| Revolution Song | 1 | 프로보한 몹의 피해 +40% |

- bard-necro의 배분([Bard Necro](bard-necro.md#03.F) 03.F절)과 다른 이유: 거기는 소환수가 딜의 63%. 여기는 딜 전부가 본체 → 본체 몫인 Ensemble, Virtuoso를 T3
- Refrain 1과 Reverb 1은 둘 다 4% 수준, 차이 미미
- Sing Your Own Praises 제외: 테이머와 다니면 그쪽 펫이 받는 내 송 효과가 줄어듦
- Virtuoso는 15초마다 다시 성공해야 유지 → 루프가 Discordance로 갱신(04.C절)

Archery Codex: 자세 다섯 모두 7랭크, 피니셔 둘 5티어, 능력 셋. 고르는 기준은 02절.

Healer's Codex 20점: Immunize 5, Triage 5, Self Treatment 5, Specialist 5.

> "Patients for the next 15 seconds have a 100% chance for new poisons to apply at 1 level lower, and for new Bleed and Disease effects to be applied at 40% reduced damage
> (cannot stack)" -- Immunize T3, Healer's Codex 화면
> "Patient receives a (3% / 9% / 15%) bonus to damage resistance while in the process of being healed with bonus doubled if patient is below 33% health (cannot stack)" -- Triage
> "Reduces time needed to bandage self by (0.75 / 2.25 / 3.75) seconds (will not apply to veterinary supplies)" -- Self Treatment
> "Increases patient healing amounts and chance to cure or resurrect by (8% / 24% / 40%) of normal" -- Specialist

- 요구: Healing, Anatomy 각 80
- Immunize가 Combat Medic보다 나음: 고렙 던전일수록 상태 이상이 많음. 사용자 판단 2026-10-21
- Self Treatment: 자기 붕대 DEX 100에서 10초 → 6.25초, DEX 80에서 11.3초 → 7.6초([PvP](../game/pvp.md#09.C) 09.C절의 식)
- Specialist: 부활 확률 1.4배(03절)
- **몹 상대로만.** "will only apply for the patient against creatures"([Healing](https://wiki.uooutlands.com/Healing)) → PvP에서 Triage, Immunize 효과 없음

### <a id="01.C"></a>01.C 갑옷과 마나

재생 식과 갑옷별 간격은 [PvP](../game/pvp.md#05.D) 05.D절, AR 표는 [PvP](../game/pvp.md#09.E) 09.E절. 아래는 음식 버프 +25%를 넣은 값.

- Meditation 0, INT 45 → 최대 마나 45
- 유지 버프: Reactive Armor 4, Magic Reflection 14, Protection 6. RA와 Reflect는 쓰여 없어질 때까지, Protection은 2분
- Protection: "Increases caster's Armor Rating by (15 \* (Magery / 100)) for 2 minutes" → Magery 80이면 AR +12([Template:SpellCircles](https://wiki.uooutlands.com/Template:SpellCircles))

마나로 AR을 사는 값. 120초 기준, 체인 한 벌에서 출발.

| 사는 것 | AR | 120초에 드는 마나 | 마나 1당 AR |
| --- | --- | --- | --- |
| Protection | +12 | 6. 시전 비용 | 2.0 |
| 체인 → 플레이트, 머리, 목, 장갑만 | +3(NPC 표) | 1.6 | 1.9 |
| 체인 → 플레이트 한 벌 | +8.2(Butler bronze) | 5 | 1.6 |
| 체인 → 플레이트, 가슴, 다리, 팔 | +4(NPC 표) | 3.4 | 1.2 |

- Butler 화면의 bronze 한 벌 AR: 체인 71.8, 플레이트 80. 2026-10-21 사용자 화면
- **고른 조합: 체인 + Protection.** AR 83.8 > 플레이트 한 벌 80, 재생은 120초에 30. Protection 6을 빼면 24 → Reflect 한 번(14)과 RA 두 번(8)
- 섞을 수 있으면 머리, 목, 장갑만 플레이트. 가슴, 다리, 팔은 마나 대비 AR이 가장 비쌈
- bronze, GM 보정은 갑옷 AR에만 붙고 Protection에는 안 붙음 → 실제로는 플레이트 작은 부위가 Protection보다 조금 나을 수 있음
- **Bless는 루프에서 뺌.** 포션과 안 겹쳐 남는 것은 최대 마나 +8.8뿐([PvP](../game/pvp.md#09.D) 09.D절). 2분마다 9마나. 부활 직전에 손으로(03절)
- 시전 문턱: RA 24, Reflect 34, Protection 26. Greater Heal 11과 Telekinesis나 Teleport 9의 20을 남김. skinning-enhanced와 같은 방식
- **Lyric Aspect 방어구.** bard-necro는 Lyric 방어구로 Effective Barding 170, 벗으면 136([Bard Necro](bard-necro.md#02.M) 02.M절).
  체인으로 바꾸며 Lyric을 유지하는지 확인되지 않았다 → 송 메시지가 `8.5%`면 170, `6.8%`면 136

::part[메커니즘]

## <a id="02"></a>02 아처리

### <a id="02.A"></a>02.A 무기와 사격 간격

- Rampart Crossbow: [Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons) 무기표의 "(2H) Heavy Crossbow, Rampart Crossbow, Great Bow" 줄. 스윙당 3.75초, 피해 17\~45, 평균 31
- 사거리: 석궁과 Great Bow 8칸, 활 10칸([Archery](https://wiki.uooutlands.com/Archery))
- 간격 식: [PvP](../game/pvp.md#09.B) 09.B절. 스태미나 100에서 3.75초. 맞아서 스태미나가 줄면 느려짐

> "Increases Swing Speed by (5% \* (Anatomy Skill / 100))" -- Archery
> "Ranged weapons (excluding Ocean Weapons) have a flat .5 second stationary delay requiring players, regardless of their Dexterity, to stay in place before firing." -- Armor & Weapons

- Anatomy 80 → 공격 속도 +4% → 3.61초. **15초에 4.2발**
- DEX 100(포션) → 스태미나 최대 100. 간격 식의 상한
- PvM은 쏘기 전 0.5초 서 있어야 함

### <a id="02.B"></a>02.B 자세

| 자세 | 랭크당 | 7랭크 | 판단 |
| --- | --- | --- | --- |
| Arcane | 정확도와 피해 3% | +21%, +21% | **기본.** 조건 없이 매 발 |
| Fowling | 피해 2%, 쏜 뒤 5초 피해 저항 4% | +14%, 저항 +28% | **다쳤을 때.** 잃은 HP 45 초과에서 켜고 30 미만에서 끔 |
| Incendiary | 피해의 10%를 2칸 안 무작위 적에게 | 70% | **여러 마리일 때.** 판정은 04.B절 |
| Longshot | 사거리 (랭크 / 2) 올림, 피해 3% | +4칸, +21% | 안 씀. 8칸으로 충분 |
| Maiming | Hinder 지속 10%, Overpowered Hinder 피해 10% | +70%, +70% | 안 씀. 아래 |

- 출처: [Archery](https://wiki.uooutlands.com/Archery)의 Codex Stances
- Fowling 기준: 2026-10-21 사용자 선택. 회복 뒤에도 큰 손실이 남으면 방어 전환, 충분히 회복한 뒤 해제. 인게임 효과는 확인되지 않았다
- Incendiary: 프로보로 붙어 싸우는 짝이 대상 옆에 있으면 Arcane의 21%보다 큼. 대상 옆에 적이 없으면 손해

Hinder와 Maiming.

> "Increases Damage by 100% and Hinders target (prevents all movement, casting, melee attacks) for 4-8 seconds." -- Archery
> "Hinder effect duration scales based on weapon speed (slower archery weapons have longer effect duration)" -- Archery
> "any new Hinder effects attempting to be applied will instead result in a damage bonus" -- Archery, Hinder가 끝난 뒤의 면역 동안

- 특수 공격은 공격당 기본 10%. Arms Lore 없음 → 3.61초 간격, 모두 명중 가정 시 평균 36초에 한 번
- 시전 봉쇄 비율: Hinder 최대 8초 → 최대 22%. Maiming(+70%) 13.6초 → 최대 38%
- Peace가 걸린 몹은 이미 못 움직이고 못 침. 프로보 짝을 묶으면 서로 못 싸움
- Peace 중에도 주문을 쓰는 몹이 있음. 사용자 관찰 2026-10-21 → 시전 몹이 많은 던전용으로 설정만 열어 둠(`archery_stance_main` 5)

### <a id="02.C"></a>02.C 피니셔

> "Weapon Finisher Threshold: 25% \* (Finisher Tier / 5)" -- Weapon and Parry Codex
> "(10%) + (10% \* (Anatomy Skill/100))" -- Weapon and Parry Codex, 피니셔 확률
> "Players can only trigger a single Finisher on each mob (i.e. an infinite cooldown)." -- Weapon and Parry Codex

- 5티어 → 대상 HP 25% 이하에서, 확률 18%. 무기 속도 보정이 더 붙음, 식은 위키에 없음
- Ricochet: 대상 350%, 대상 6칸 안 다른 적 최대 둘에 350%씩. Pincushion: 대상에 100% 여섯 번 = 600%

| 상황 | 피니셔 | 이유 |
| --- | --- | --- |
| 한 마리 | Pincushion | 대상에 600% > 350% |
| 여러 마리 | Ricochet | 대상 350%와 다른 적에 최대 700% |

- 보스는 일정 시간마다 다시 터짐. 위키의 두 문장(`120 - (12 × 티어)`초, 60초)이 5티어에서는 같은 60초

### <a id="02.D"></a>02.D 무기 능력

> "For next 15 seconds damage increased by 35% and can fire while moving" -- Skirmish
> "For next 15 seconds damage increased by 50%, but must be stationary for 3 seconds to fire" -- Full Draw
> "If not currently stealthed, immediately makes 3 hits, each inflicting 75% weapon damage (scaled by weapon speed)" -- Repeater
> "All Weapon Abilities for the player share the same weapon ability cooldown." -- Weapon and Parry Codex

- 세 능력이 게이지 하나. Arms Lore 없으면 60초
- 15초에 4.2발(02.A절) 기준

| 능력 | 15초 동안 더하는 피해 |
| --- | --- |
| Full Draw | 4.2발 × 50% = 208%. 모두 명중하고 15초 내내 서 있을 때 |
| Repeater | 3 × 75% = **225%**. 즉시 |
| Skirmish | 4.2발 × 35% = 147% |

- **Repeater.** 대상이 중간에 죽거나 한 발 움직여도 손해 없음. 스태미나가 줄어 발 수가 줄면 차이가 더 벌어짐
- Full Draw는 사격 직후에 켜면 5발(250%)이지만 루프는 손으로 쏘는 박자에 못 맞춤
- Repeater의 무기 속도 보정 식은 위키에 없음 → 일반 사격 한 발과 비교 필요
- 일반 석궁(Speed 28, 1H)이었다면 15초에 5.8발 → Full Draw 291%가 나음

### <a id="02.E"></a>02.E PvP에서 빠지는 것

- 코덱스, Mastery Chain, Aspect는 PvP에서 꺼짐. 사용자 확인 2026-10-21 → 자세, 피니셔 판단은 PvM 전용
- 아처리 특수 공격(Hinder)은 몹에만, 보조 무기 스킬 보너스는 PvM 25%, PvP 10%([Archery](https://wiki.uooutlands.com/Archery))
- PvP의 정지 대기는 DEX로 줄어듦: DEX 25 이하 1.0초, 100 이상 0.5초

> "A player with 63 Dex must remain stationary for 0.75 seconds." -- Archery

- Healer's Codex도 몹 상대로만(01.B절)
- PK를 만나면 F4 `combat/pvp`. 이 루프는 구조적 PvP에서 멈춤([Modules](../scripting/modules.md#06) 06절)

## <a id="03"></a>03 부활

**손으로.** 루프에 없음. 붕대 먼저, 마나가 차면 스크롤.

| 방법 | 성공 | 시간 | 비용 |
| --- | --- | --- | --- |
| 붕대 | 시도당 33.6% | DEX 100에서 시도당 5초, 평균 약 15초 | 붕대 |
| Resurrection 스크롤 | 늘 성공 | 시전 5초 | 50마나, Bless 9, 스크롤 |

- 붕대: Healing 80의 24%([PvP](../game/pvp.md#09.C) 09.C절) × Specialist 1.4 = 33.6%. 11번(56초) 연속 실패할 확률 1.1%
- 스크롤: Magery 80은 8서클 최소치, 스크롤이 실효 Magery +20 → 100 → 늘 성공

> "Min Required to Cast - 80 Magery" / "100% Success to Cast - 100 Magery" -- Magery, 8서클
> "Casting a spell from a scroll increases a player's Effective Magery skill by 20" -- Magery

- INT 45 → 최대 마나 45 < 50 → Bless(+8.8) 뒤에만 가능
- 45에서 Bless 9 → 36. 50까지 14 → 체인에 음식이면 4초에 1, 56초. 음식 없이 70초
- → 붕대를 시작하고 그사이 Bless. 56초 동안 붕대가 못 살리면 스크롤. 스크롤은 보험

::part[루프]

## <a id="04"></a>04 bard-archer-enhanced

정본은 레시피 [recipe/bard-archer-enhanced-recipe.razor](https://github.com/minu-ha/uoo/blob/master/recipe/bard-archer-enhanced-recipe.razor). 블록 동작은 각 모듈 파일 머리 주석.

### <a id="04.A"></a>04.A 블록과 순서

| 자리 | 블록 | 값과 출처 |
| --- | --- | --- |
| base | | `warmode_is_manual` 1, `recover_in_warmode` 1, `settle_first` 1(bard-necro). `heal_skill_min` 10(skinning) |
| 다쳤거나 독, 마비 | `recovery/cure`, `heal`, `bandage`, `light-heal` | 잃은 HP 기준 `heal_hits` 35, `emergency_hits` 45. 회복 정책은 아래 |
| 공용 | `fight/target`, `magery/reagents` | `acquire_range` 18, `target_range` 10, `target_grace` 500(bard-necro) |
| 5초마다 | `bard/instrument`, `recovery/refresh`, `buff/food`, `buff/potions`, `pack/gold-drop` | `refresh_stam` 60(skinning). 포션 기준선 STR 120, DEX 100은 기본값 |
| 늘 | `bard/provo`, `fight/archery-codex` | 자세와 피니셔 전환(04.B절) |
| 교전 중 | `bard/disco`, `bard/peace`, `fight/weapon-ability` | `keep_virtuoso` 1. Archery 코덱스, Repeater, 사거리 8 |
| 이동 중 | `bard/song` | |
| 늘 | `buff/spells` | RA 24, Reflect 34, Protection 26, 독이면 버프 안 함 |

- 교전 = 고른 적이 10칸 안. 바딩 사거리. 사격 사거리 8칸은 손으로 맞춤
- **바딩 우선순위: Provo, Disco, Peace.** Provo로 짝을 붙인 뒤 현재 대상에 Discordance, Peacemaking. bard-necro와 같은 순서. 코덱스 전환은 Provo와 Disco 사이
- 스킬별 쿨과 공유 쿨: [Bard Necro](bard-necro.md#02.E) 02.E절
- **평소 회복은 붕대.** 잃은 HP 35 이상이면 힐 포션, 그 패스에 포션을 안 마셨고 손실 45 이상이면 Greater Heal. 붕대 종료를 기다리지 않음
- 일반 Heal은 붕대 대체용으로 유지. 이 템플릿의 기본 설정에서는 붕대가 없고 감는 중도 아닐 때만 사용, 붕대 중첩 시전 없음
- `buff/spells`는 교전 중에도. 사격과 시전이 서로 안 막음(01.A절), 패스 끝에 둬서 바딩이 먼저
- warmode(수동 구간): 바딩, 노래, 버프, 음식 정지. 회복 시전, 포션, 붕대, 코덱스 전환, 무기 능력은 계속

### <a id="04.B"></a>04.B 여러 마리 판정

- Razor는 적을 스스로 못 찾음(`module/bard/provo.razor` 머리 주석) → 고른 적(`Z`, `Q`)을 목록에 모음
- 2초마다 목록에서 살아 있고 10칸 안인 적을 셈. **둘 이상이면 Incendiary와 Ricochet**, 아니면 Arcane과 Pincushion
- 하나로 줄어도 6초 유지 → 짝 하나가 잠깐 멀어질 때 자세가 깜빡이지 않음
- 대상 옆 2칸 판정은 불가. 몹끼리 거리를 재는 식이 없음. 프로보 짝은 붙어 싸우므로 짝 중 하나를 쏘면 Incendiary가 다른 쪽에 감
- 다쳤을 때(Fowling)가 가장 먼저. 피니셔는 다쳤을 때도 마릿수로
- 전환은 코덱스 라벨로 지금 자세와 피니셔를 읽은 뒤에만. 명령이 켜고 끄는 토글이라 같은 것을 또 말하면 꺼짐
- 라벨에 자세 이름이 없거나 둘 이상이면 자세 전환을, 피니셔 이름이 없거나 둘이면 피니셔 전환을 그 Play 동안 멈춤(`[ archery stance, off ]`, `[ archery finisher, off ]`).
  라벨이 지금 것 하나만 보이는지는 확인되지 않았다
- 라벨은 2초 확인마다가 아니라 원하는 것과 기억한 것이 다를 때만, 3초에 한 번까지 읽음. 손으로 바꾼 것은 30초마다 기억을 지워 다시 읽음
- 명령: `[ArcheryAmmunition1`\~`5`(위키 순서 Arcane, Fowling, Incendiary, Longshot, Maiming), `[ArcheryFinisher1`(Ricochet), `[ArcheryFinisher2`(Pincushion). [Commands](https://wiki.uooutlands.com/Commands)
- 자세가 바뀌면 서버가 머리 위에 `Fowling ammunition` 같은 문장을 띄움 → 스크립트는 같은 알림을 다시 안 띄움([Overheads](../scripting/overheads.md#01.B) 01.B절)

### <a id="04.C"></a>04.C Virtuoso 유지

- `bard/disco`의 `keep_virtuoso` 1: Virtuoso가 빠지면 이미 Discord 걸린 대상에게도 다시 Discordance
- 근거: Discord 걸린 대상에게 다시 성공해도 Virtuoso가 다시 생기고, 송으로는 안 생김([Bard Necro](bard-necro.md#02.Q) 02.Q절)
- 한 마리를 오래 잡으면 약 15초마다 Discordance. Music 5초를 쓰지만 Peace는 약 51초에 한 번([Bard Necro](bard-necro.md#01.D) 01.D절)이라 겹침이 적음

### <a id="04.D"></a>04.D bard 프로필

- `summoner`를 복사한 `bard`. nomeehej의 에이전트, 정리 목록, 컨테이너 변수를 그대로 가져옴
- 다른 점: 아랫줄은 basic식(`Z` 가장 가까운 몹, `V` Attack Last Target, `X`, `C` 플레이어), F1 = `combat\bard-archer-enhanced`, Alt 소환 줄 없음
- 같은 점: `1 2 3` Disco, Peace, Provo, `Shift+Z` 다음 몹, Q와 E, Ctrl 버프 줄, F4 pvp
- 키 배치의 정본: [Hotkeys](../game/hotkeys.md) 01.E절, 03절

::part[기록]

## <a id="05"></a>05 출처

- [Archery](https://wiki.uooutlands.com/Archery): 자세, 피니셔, 능력, Hinder, 사거리, PvP 차이
- [Weapon and Parry Codex](https://wiki.uooutlands.com/Weapon_and_Parry_Codex): 피니셔 문턱과 확률, 능력 게이지
- [Commands](https://wiki.uooutlands.com/Commands): `[ArcheryAmmunition`, `[ArcheryFinisher`, `[WeaponAbility`
- [Armor & Weapons](https://wiki.uooutlands.com/Armor_%26_Weapons): 무기표, 정지 대기, AR, 마나 페널티, 스태미나 피로
- [Healing](https://wiki.uooutlands.com/Healing): Healer's Codex, 부활 확률
- [Magery](https://wiki.uooutlands.com/Magery), [Template:SpellCircles](https://wiki.uooutlands.com/Template:SpellCircles): 서클별 성공 기준, 스크롤, Protection, Bless
- [outlandsbutler.com](https://www.outlandsbutler.com/): 장비 AR과 마나 재생 계산. 2026-10-21 사용자 화면
