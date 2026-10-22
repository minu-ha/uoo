---
name: PvP Loop
label: 공통 pvp 루프
group: Loops
order: 40
---

PvP 시작 시 켜는 공통 자기관리 루프 `combat/pvp`의 설계. 서버 규칙은 [PvP](../game/pvp.md).
템플릿별 설정은 [Bard Necro](../templates/bard-necro.md#04.F) 04.F절과 [Lumberjack PvP](../templates/lumberjack-pvp.md#08) 08절, 인게임 확인은 [Open items](../questions/open-items.md#10) 10절.

## <a id="00"></a>00 한눈에

| 절 | 내용 |
| --- | --- |
| [01](#01) | 수동 공격과 자동 자기관리의 경계, 버전 기록, 입력 규칙, 설정, 루프 골격, 비용과 타이머, 싸움 전 붕대 미리 쓰기, 스윙 바와 무기 선택, 상태 |

이 문서에 걸린 질문은 [Open items](../questions/open-items.md).

## <a id="01"></a>01 수동 공격과 공통 자기관리 루프

[combat/pvp.razor](https://github.com/minu-ha/uoo/blob/master/script/combat/pvp.razor): PvP 시작 시 켜는 공통 자기관리 루프.

- 공격은 전부 수동. TK, Magic Arrow와 Harm, Explosion과 Energy Bolt, 폭발 포션, 소환수 공격, Hamstring, 상대 지정, 근접 공격 요청
- 상대의 serial, 색, 거리, 사망 여부 조회 없음. PvP 핫키는 `Play Script: combat\pvp`
- 자동: 파우치, 포션, 붕대, 회복 에이전트, Reactive Armor와 Reflect, 스탯 포션, 켜 둔 무기 장착. 수동 시전이나 커서는 끊지 않음
- 현재 본문은 인게임에서 확인되지 않았다

현재 v9. 판별 변경:

- 2026-10-08 v6: bard-necro-enhanced, lumberjack-enhanced와 같은 모양으로 재작성
  - v5는 위에서 고른 번호를 변수에 담고 아래 실행부가 다시 읽음 → 그 사이 상태 변화 가능
  - v6의 블록은 각자 현재 상태를 읽고 즉시 행동, 다음 블록에 결정을 넘기지 않음
  - 삭제: v5의 긴급 수동 주문 중단, 6초 시전 대기와 `[ cast, check ]` 정지, 준비 동작의 5초 주기, 주문의 이동 가드, 재시도 타이머 8개
- 2026-10-09 v7: Strength와 Agility 포션을 버프 대신 STR과 DEX 값으로 판정, 포션마다 5초 재시도 간격([Combat](../mechanics/combat.md#02.D) 02.D절)
- 2026-10-10 v8: 가벼운 Heal을 붕대 옵션과 별도로 `use_light_heal`로. 붕대를 못 쓰면 옵션과 무관하게 대신 사용
- 2026-10-10 v9: `recipe/pvp-recipe.razor`로 조립. 동작은 v8과 같음([Modules](../scripting/modules.md#08) 08절). 수정은 모듈과 레시피에서

#### 입력 규칙

[PvP](../game/pvp.md#05.B) 05.B절 Combat Overview 원문 기준.

- 포션과 파우치: 즉시 쓰는 아이템 → 시전 중에도 사용, `casting` 미확인
- 프리캐스트 커서를 든 채 마시면 그 주문 취소 → 포션은 커서를 든 동안 대기
- 붕대도 대기. 붕대의 대상 커서가 들고 있던 커서를 밀어냄
- 회복 에이전트, Reactive Armor, Reflect: 시전과 커서가 없을 때만 시작, 제 시전이 끝날 때까지 `for 60`으로 폴링
- 루프가 끊는 시전은 루프가 건 Reactive Armor와 Reflect뿐. 잃은 HP가 긴급 기준(`buff_max_loss`)에 닿으면 `> Interrupt` → 다음 패스에 회복
- Razor 행동 큐가 찼거나 은신 중이면 행동 없음. 마비 파우치만 예외

#### 설정

- 아래 이름은 `config__` 접두 생략. 템플릿별 프리셋 없음
- 값 변경: `recipe/pvp-recipe.razor`에서 그 설정을 가진 블록의 `# @ use` 줄 아래에 새 값 → 재조립([Modules](../scripting/modules.md#07.A) 07.A절)
- 옵션끼리 덮어쓰지 않음. Magery와 붕대는 따로 끌 수 있음. 무기 교체는 레시피의 `fight/weapon-swap` 블록 → 끄려면 그 줄 삭제
- 전체 설정과 기본값: `node util/build-scripts.mjs --settings recipe/pvp-recipe.razor`. 아래 표는 자주 보는 것

| 옵션 | 기본값 | 효과 |
| --- | --- | --- |
| `clear_at_start` | 0 | Play 시 시작 4줄 생략. 들고 있던 수동 커서와 시전 유지([Conventions](../scripting/conventions.md#02.D) 02.D절) |
| `use_magery` | 1 | 회복 에이전트, 버프, 시약 읽기 |
| `use_bandages` | 1 | Healing이 있고 피해나 독이면 붕대 |
| `use_light_heal` | 0 | 붕대와 함께 `light_hits`부터 가벼운 Heal. 붕대 불가(`use_bandages` 0, Healing 없음, 붕대 없음)면 값과 무관하게 대신 사용. `use_magery` 1 필요 |
| `use_potions` | 1 | 회복 포션, Refresh, 스탯 포션 |
| `use_resist_potion` | 1 | Magic Resist 포션 |
| `str_potion` | 120 | Greater Strength 포션을 마신 STR(기본 + 20). STR이 그보다 낮으면 Strength 포션. 0이면 끔 |
| `dex_potion` | 100 | Greater Agility 포션을 마신 DEX(기본 + 20). DEX가 그보다 낮으면 Agility 포션. 0이면 끔 |
| `walk_guard` | 0 | base 공용 설정. pvp는 걷는 중에도 시전([Modules](../scripting/modules.md#06) 06절) |
| `warmode_is_manual` | 0 | base 공용 설정. pvp는 워모드 무시 |
| `buff_max_loss` | 35 | 잃은 HP가 이 값 이상이면 버프 시작 안 함, 시전 중이면 끊음. `emergency_hits`를 바꾸면 함께 조정 |
| `buff_when_poisoned` | 1 | 독 상태에서도 버프 |
| `use_reactive_armor` | 1 | 빠지면 시전과 커서가 없을 때 즉시 재시전. 이동 가드 없음 |
| `use_magic_reflect` | 1 | Reflect도 같은 방식 |
| `heal_hits` | 35 | 잃은 HP가 이 값 이상이면 힐 포션 |
| `emergency_hits` | 35 | 포션 불가 시 Greater Heal, 버프 정지 기준. `heal_hits`보다 낮게 두지 않음 |
| `light_hits` | 15 | 가벼운 Heal 기준(`use_light_heal`) |
| `refresh_stam` | 15 | 현재 STA가 이 값 이하면 Refresh |
| `mana_cure` | 6 | Cure 에이전트 시작 최소 현재 마나 |
| `mana_greater_heal` | 11 | Greater Heal 에이전트 시작 최소 현재 마나 |
| `mana_heal` | 4 | Heal 에이전트 시작 최소 현재 마나 |
| `mana_reactive_armor` | 4 | Reactive Armor 시작 최소 현재 마나 |
| `mana_magic_reflect` | 14 | Reflect 시작 최소 현재 마나 |
| `weapon_1_graphic`\~`weapon_4_graphic` | 아래 표 | 각 스윙 바와 짝지은 graphic ID 하나. 0이면 그 슬롯 끔 |
| `chatty` | 1 | 선택 오버헤드 |
| `sysmsg` | 1 | 시작 시 판 번호, 에이전트와 버프 시전, 장착 요청을 Journal에 기록 |

- `str_potion`, `dex_potion`: 공유 루프 → 실행 캐릭터의 기본 스탯에 맞춤. 기본값은 STR 100, DEX 80 기준([Combat](../mechanics/combat.md#02.D) 02.D절)
- `heal_hits`, `emergency_hits`, `light_hits`: 모두 최대 HP에서 잃은 양. 최대 HP 120이면 기본 기준은 현재 HP 85 이하
- 최소 마나는 공격이나 이동용 예비 마나를 자동으로 남기지 않음. 예비 20을 남기려면 Greater Heal 최소값 11 → 31처럼 각 값 조정
- `buff/spells` 모듈의 `use_spell_siphon`: 이 루프에서 기본값 0 유지(아래 "싸움 전 붕대 미리 쓰기")

#### 루프 골격

1. 명령이 막혀 있으면 정지
2. REAGENTS: 10초마다, 또는 `More reagents are needed` 거절 직후 시약 7가지 읽기 → 주문별 플래그. 패스 맨 앞이라 아래 시전 블록이 새 플래그를 읽음
3. 회복 블록은 `paralyzed or poisoned or diffhits > 0` 한 줄 아래. 다치지 않은 패스는 그 한 줄만
4. CURE: 마비면 트랩 파우치. 마비 아니고 독이면 Cure 포션. 포션이 하나라도 있으면 에이전트 생략, 없거나 꺼져 있으면 Smart Heal/Cure 에이전트
5. HEAL: 잃은 HP가 힐 포션 기준 이상이면 포션. 이 패스에 포션이 안 나갔고 긴급 기준 이상이면 Greater Heal/Cure 에이전트
6. BANDAGE, LIGHT HEAL, REFRESH 순서. 진행 중인 붕대는 재시작 안 함. 가벼운 Heal: 붕대 불가 시 대신, `use_light_heal` 1이면 붕대와 함께
7. STAT POTIONS: Strength와 Agility는 STR과 DEX가 기준선 아래면 5초에 한 번. Resist는 버프가 빠지면 즉시. 한 포션이 떨어져도 나머지는 계속
8. SELF BUFFS: Reactive Armor → Reflect 순서, 빠지면 긴급 기준 아래에서 즉시
9. WEAPON: 시전과 커서가 없을 때, 원하는 슬롯의 무기가 손에 없으면 장착 요청

- 힐 포션: `heal pot` 바가 돌면 라벨 생략, 바가 0일 때 포션의 `next usable` 라벨 확인
- 포션을 마신 패스는 Greater Heal 생략. 다음 패스에도 긴급 기준 이상이면 그때 Greater Heal
- 붕대 시작 ≠ 즉시 HP 회복
- 사람이 시전하는 동안: 포션은 나감, 에이전트, 버프, 붕대, 장착은 대기. 사람이 커서를 든 동안: 마비 파우치만
- 긴급 기준에 닿아도 수동 입력은 끊지 않음. 시전 종료나 커서 해제 뒤 다음 패스에 회복
- 중립 아이템 커서도 같은 커서로 보고 대기

#### 비용과 타이머

- `findtype`이 가장 비싼 명령([Razor](../scripting/razor.md#06) 06절) → 시약은 패스마다 찾지 않고 REAGENTS 플래그를 읽음
- 포션은 필요한 블록 안에서만 찾음. Strength와 Agility 포션은 스탯이 기준선 아래일 때 5초에 한 번, Resist 포션은 버프가 빠졌을 때만
- 무기는 원하는 슬롯이 바뀔 때만 찾음. 평소에는 양손 레이어 두 개만 읽음
- 없는 무기를 슬롯에 두면 패스마다 한 번씩 찾음 → 안 쓰는 슬롯은 0
- 재시도 타이머는 `timer__str_potion`, `timer__agi_potion`(5초) 둘뿐
- 저주를 받으면 포션 효과 중에도 스탯이 기준선 아래 → 다른 신호로는 거절될 마시기를 못 막음([Combat](../mechanics/combat.md#02.D) 02.D절)
- 나머지 중복 요청은 행동 큐(`queued`), `bandaging`, `findbuff`, 포션 라벨, `heal pot` 바가 막음
- 에이전트는 제 시전이 끝날 때까지 폴링 → 끝난 뒤에도 잃은 HP가 남으면 즉시 재시전
- 그 밖의 타이머: 반복 경고 방지 `timer__message`(3초), 시약 주기 `timer__reagents`(10초). 모두 Play마다 준비 상태로 시작

#### 싸움 전 붕대 미리 쓰기

- 붕대가 끝나 HP가 가득 차면 현재 루프는 다음 붕대를 시작하지 않음
- 사용자가 나에게 Magic Arrow를 한 번 쏴서 피해를 만든 뒤 커서를 놓으면 다음 붕대 조건 성립
- → 교전 전에 붕대 종료 시점을 앞당김. 첫 피해 뒤 붕대 시작과는 다른 수동 준비
- HP가 가득 찬 상태의 Bandage Self를 서버가 받는지는 아직 확인되지 않았다
- HP가 가득 찼을 때 자기 Magic Arrow를 자동 반복하는 분기는 없음. 진행 중인 붕대 재시작, 마나 낭비, 수동 공격 입력과의 충돌 회피
- Spell Siphon용 자기 Magic Arrow와 버섯 옵션은 v5에서 제거.
  [Spell Siphon은 크리처 상대 보너스](https://wiki.uooutlands.com/Resisting_Spells),
  [버섯은 PvP 플래그 중 섭취 불가](https://uooutlands.com/news/patch-march-5-wizards-grimoire-new-player-rental-credit-deeds-society-job-updates/)
- Resist 포션은 던전 몹과 펫 상대용 옵션. 적 플레이어 주문 감소로 계산하지 않음

#### 스윙 바와 무기 선택

| 설정 | 읽는 바 | 기본 무기 | graphic ID |
| --- | --- | --- | --- |
| `weapon_4_graphic` | `swing 4` | Great Axe | 31190 |
| `weapon_3_graphic` | `swing 3` | 미사용 | 0 |
| `weapon_2_graphic` | `swing 2` | 미사용 | 0 |
| `weapon_1_graphic` | `swing 1` | Norse Axe | 31128 |

- 원하는 슬롯 = 스윙이 준비된 슬롯 중 가장 높은 것. 4번 → 1번 순서
- 준비된 슬롯이 없고 양손이 비면 켜진 슬롯 중 가장 낮은 것. 바가 없으면 준비로 읽음
- 원하는 슬롯이 바뀌면 그 graphic을 내 몸(장착품과 백팩)에서 찾아 기억
- 기억한 serial이 손에 있으면 유지, 백팩에 있으면 장착 요청, 둘 다 아니면 다음 패스에 재검색
- 손에 직접 든 무기는 그 serial을 그대로 기억 → 교체 안 함. 슬롯 무기가 없고 양손이 비면 `[ weapon, out ]`
- 다른 무기: [Item list](../game/item-list.md)의 graphic ID 하나로 교체
- 슬롯은 서버 배정이 아닌 사용자 설정. 개인 serial이나 graphic 목록은 넣지 않음
- 장착은 [dress serial](https://www.razorce.com/guide/commands/#dress)로 요청. 활성 프로필의 Arm/Dress가 부딪치는 장비를 자동으로 벗겨야 함
- 이 클라이언트에서 `dress` 실패 기록 있음([Razor](../scripting/razor.md#03) 03절) → 실제 교체는 인게임 확인 필요
- 기존 weapon 핫키는 공격이나 Unlock 요청도 보냄 → 이 루프에서 호출 안 함
- 활성 캐릭터의 바는 각각 `WeaponSwing` 타입, 현재 STA에 맞는 시간. 시간과 공유 스윙 기준은 [Combat](../mechanics/combat.md#02.B) 02.B절, 바 구조는 [Overheads](../scripting/overheads.md#06.A) 06.A절
- 루프는 바를 시작하거나 초기화하지 않음. 장착 요청 ≠ 실제 스윙이나 명중. 무기를 바꿔도 새 공격 요청은 없음

#### 상태

| 상태 | 뜻 |
| --- | --- |
| `var__has_black_pearl`, `var__has_garlic`, `var__has_ginseng`, `var__has_mandrake`, `var__has_nightshade`, `var__has_ash`, `var__has_silk` | REAGENTS가 읽은 시약 7가지 보유 여부 |
| `var__regs_cure`, `var__regs_heal`, `var__regs_greater_heal`, `var__regs_reactive_armor`, `var__regs_magic_reflect` | 그 주문의 시약이 모두 있으면 1. 이 루프의 시전 블록이 읽고 REAGENTS만 씀 |
| `var__heal_potion_out` | HEAL 블록 내부용. 이 패스에 힐 포션이 나갔으면 1 |
| `var__weapon_want`, `var__weapon_held` | WEAPON 블록 내부용. 원하는 슬롯의 graphic, 그 무기의 손 보유 여부 |
| `var__weapon_armed_serial`, `var__weapon_armed_graphic` | 스크립트가 마지막으로 장착한 무기. Play를 넘어 유지 |

- 정적 검사는 Outlands 서버나 실제 커서 처리를 입증하지 않음
- 구조화 PvP나 팩션에서 명령이 막히면 `[ script, blocked ]` 후 정지
- 반영 방법과 인게임 확인: [Open items](../questions/open-items.md#10) 10절
