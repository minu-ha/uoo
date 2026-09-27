# 핫키 배치

두 캐릭터(nomeehej 바드 네크로, xuezhonglian PK 메이지)가 **같은 자리에 같은 역할**을 둔다.
템플릿이 채우는 칸은 `1 2 3`, `F1`, `F4`, Alt 줄뿐이다.

## 규칙

| 층 | 뜻 | 줄별 |
|---|---|---|
| 무수정 | 손에 익어야 하는 것 | 이동 · 타겟/펫 · 핵심 콤보 · 도주 · 긴급 |
| Shift | 밖으로 던지는 것 | 윗줄 공격 주문 5, 아랫줄 플레이어 교전 3 |
| Ctrl | 나와 내 편에 좋은 것 | 숫자 포션 6, 윗줄 버프 4, 아랫줄 필드·유틸 4, `` ` `` 펫 힐 |
| Alt | 소환. 그것뿐 | `1` VS → `2`~`6`. 전투 밖에서 천천히 누른다 |

**Mac 키 이름.** Wine 이 `Cmd → Ctrl`, `Option → Alt` 로 넘긴다 (`prefix/user.reg` 의 `LeftCommandIsCtrl`, `LeftOptionIsAlt`).
아래 표의 **Ctrl 은 엄지로 누르는 Cmd**, Alt 는 Option 이다. `Ctrl+Space` 는 macOS 가 먹으므로 쓰지 않는다.
`Alt+`` ` ``` 도 안 된다 — Option+` 은 macOS 가 악센트 dead key 로 잡아서 Razor 에 안 들어오고, Razor 는 종료할 때 그 바인딩을 지워 버린다. Alt 줄은 `1` 부터 쓴다.

**어디에 거는가.** 주문 = ClassicUO `macros.xml` (Vengeful Spirit 도 여기, `[VengefulSpirit` Say 매크로). 나머지(타겟 · 펫 · 포션 · Pouch · 힐 · VS · 스킬 · 스크립트) = Razor 프로필 `<hotkeys>`.
**같은 키를 양쪽에 걸지 않는다** — 프로필이 `HotKeyStop=False` 라 Razor 키가 CUO 로도 넘어가서 두 번 나간다.
인게임 카운터·핫바에도 걸지 않는다. 파일에 없는 바인딩은 저장소가 못 지킨다.

## 펑션줄

| | Esc | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 무수정 | 스크립트 정지 | **전투 루프** | cancel-target | recycle | **PvP 루프** | 이름 표시 | 투명 | 하이드 | 명상 | — | share-loot | claim-loot | loadout |
| Shift | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Ctrl | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Alt | — | — | — | — | — | — | — | — | — | — | — | — | — |

## 숫자줄

| | `` ` `` | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 무수정 | **Smart Heal/Cure** | 시그니처 ① | 시그니처 ② | 시그니처 ③ | Explosion | Energy Bolt | Paralyze |
| Shift | — | — | — | — | — | — | — |
| Ctrl | **Greater Heal** (커서 → 펫·동료) | 힐 포션 | 큐어 포션 | 리프 포션 | 힘 포션 | 민 포션 | 레지 포션 |
| Alt | — | **Vengeful Spirit** | Fire El → Lich | Earth El → Mummy | Daemon → Vampire | Water El → Rag Witch | Summon Creature |

`Alt+0` = dress. 소환 줄에 붙어 있지만 소환은 아니고, 자주 안 누르는 자리라 거기 둔 것. `F4` 는 PK 를 만났을 때: PvE 루프가 멈추고 `bard-necro-pvp` 가 돈다, `F1` 로 복귀.

## 윗줄

| | Tab | Q | W | E | R | T | Y | U |
|---|---|---|---|---|---|---|---|---|
| 무수정 | — | 셋 라타 | ↑ | **라타 발사** | 텔레포트 | Telekinesis | Flamestrike | — |
| Shift | — | Harm | Magic Arrow | Lightning | Fireball | Mind Blast | — | — |
| Ctrl | — | Reactive Armor | Magic Reflection | Protection | Bless | — | — | — |
| Alt | — | — | — | — | — | — | — | — |

## 홈줄

| | A | S | D | F | G | H | J |
|---|---|---|---|---|---|---|---|
| 무수정 | ← | ↓ | → | 로프 | 폭발물약 | **Chain Lightning** | — |
| Shift | — | — | — | — | — | — | — |
| Ctrl | — | — | — | — | — | — | — |
| Alt | — | — | — | — | — | — | — |

## 아랫줄

| | Z | X | C | V | B | N |
|---|---|---|---|---|---|---|
| 무수정 | All Follow Me | All Guard Me | **All Kill** | **근접 몬스터 타겟** | moongate | home |
| Shift | — | 이전 플레이어 | 다음 플레이어 | Attack Last Target | — | — |
| Ctrl | Wall of Stone | Mass Dispel | Invisibility | Reveal | — | — |
| Alt | — | — | — | — | — | — |

## 마우스·기타

| | Space | 휠 위 | 휠 아래 | 사이드 위 (`-5`) | 사이드 아래 (`-4`) |
|---|---|---|---|---|---|
| 무수정 | 자기 타겟 | — | **Interrupt** | 타겟 취소 | **Pouch** (마비 해제) |
| Shift | — | 다음 아군 플레이어 | 이전 아군 플레이어 | — | — |
| Ctrl | — | — | — | — | — |
| Alt | — | — | — | — | — |

## 템플릿이 채우는 칸

| | 1 2 3 | F1 | F4 | Alt 줄 |
|---|---|---|---|---|
| Bard Necro (nomeehej, 프로필 `bard mace`) | Disco / Peace / Provo | bard-necro-enhanced | bard-necro-pvp | 소환 5 + VS |
| PK 메이지 (xuezhonglian, 프로필 `default`) | Curse / Weaken / Clumsy | hally-mage | — | Earth El · Water El 만 (Alt+3 5) |

## 손에 잡히는 흐름

- **PvP**: `F4` → PvE 루프 정지 + PvP 루프. 타겟은 `Q` / `Shift+X C` / `C` 로 잡은 라타 하나. `F1` 로 복귀.
- **PvE 수동**: `V` (라타 = 근접 몹) → `1 E` `2 E` → `4 E` `5 E`. 펫은 `C V` — All Kill 커서를 V 가 채운다.
- **PvP**: `Shift+C` (다음 플레이어 = 라타) → `6 E` → `4 E` `5 E`.
- **폭탄**: `T` `E` (상대가 30초 끈끈이) → `G` `E`. Telekinesis 가 먼저다.
- **긴급**: `` ` `` 힐 (새끼), 사이드 아래 Pouch (엄지), `Ctrl+1` 힐 포션 (엄지 + 약지). 손가락이 안 움직인다.
- **펫**: `Ctrl+`` ` ``` → 펫 클릭 (Greater Heal). `Ctrl+R` Bless 는 팔로워 데미지·공속 +5%.
- **소환**: `Alt+1` (VS) → `Alt+2` → `Alt+2` (Lich 둘). 근접 플레이어 타겟은 서버가 막아 놨다 — 플레이어는 순환만 된다.

## 아직 확인 안 된 것

- 인게임 카운터·핫바에 남아 있던 포션 · T · Y 바인딩 해제.
- 메이지의 `1 2 3` = Curse / Weaken / Clumsy 와 `F1` = hally-mage 는 임시 배정. 실제 템플릿에 맞춰 바꾼다.
- 사이드 위/아래는 코드 `-5` / `-4` 로 배정했다. 눌러 보고 반대면 두 줄을 맞바꾼다.

## Razor 내장 이름 (`L:번호`)

프로필의 `L:번호` 는 `Assistant/Language/Razor_lang.enu` 에서 찾는다. 지금 쓰는 것:

| 번호 | 이름 | 번호 | 이름 |
|---|---|---|---|
| 1058 | Last Target | 2013 | Target Closest Non-Friendly Monster |
| 1059 | Target Self | 2022 / 2024 / 2026 | All Follow Me / All Guard Me / All Kill |
| 1060 | Set Last Target | 2054 / 2057 | Next / Previous Non-Friendly Player Target |
| 1332 | Cancel Current Target | 2052 / 2055 | Next / Previous Friendly Player Target |
| 1391 | > Smart Heal/Cure Self | 2101 | > Stop Current Script |
| 1395 | Attack Last Target | 2124 | Vengeful Spirit — **쓰지 않는다.** 프로필에 넣어도 Razor 가 종료할 때 지운다. VS 는 CUO 매크로 `[VengefulSpirit` 로 건다 |
| 1028 ~ 1034 | Drink Heal / Cure / Refresh / Magic Resist / Explosion / Strength / Agility | 2527 | Pouch |
| 1994 | > Interrupt | 1044060 + 스킬번호 | 스킬 사용 (Disco 1044075, Peace 1044069, Provo 1044082) |

## 주문 데미지 메모

위키 PvM, Magery 100 기준. 자세한 건 [Magery](https://wiki.uooutlands.com/Magery).

| 주문 | 피해 | 비고 |
|---|---|---|
| Fireball | 14~18 | 0.5초 딜레이 |
| Lightning | 16~20 | 0.25초 딜레이 |
| Mind Blast | 20~32 | 상대 AR 만큼 증가 |
| Energy Bolt | 32~44 | |
| Explosion | 34~46 | 2.5초 딜레이 |
| Chain Lightning | 30~42, 2타일 | 리플렉트 벗김. 플레이어 맞으면 30초 쿨 |
| Flamestrike | 72~96 | PvP 는 연속 시전마다 10% 피즐 누적 |
| Earthquake | 15~25, 8타일 | PvP 는 현재 HP 50% |

옛 메모 (PvP 체감치):

- 함 : 2.25~3.375 데미지
- 매직에로우 : 5.625~7.875 피해
- 라이트닝 : 15.75~20.25 피해
- 텔레키네 : 폭탄부착용
- 커스 : 저주 힘민지 11
- 익스플로전 : 31.5~40.5 피해
- 에너지볼트 : 31.5~40.5 피해
- 패러렐라이즈 : 10초 마비
- 피블마인드 : 지능 11 감소 (2분)
- 위큰 : 힘 11 감소 (2분)
- 클럼시 : 민첩 11 감소 (2분)
