# 머리 위 메시지와 쿨다운 바

게임 화면에 뜨는 알림 전부의 정본. 어느 경로로 띄우는가, 어떤 단어와 색을 쓰는가, 지금 무엇이 걸려 있는가.
같은 사건은 쿨다운 바 하나 + 오버헤드 한 줄이 짝이고, 둘은 **같은 단어**를 쓴다. 바가 뜨면 어느 오버헤드 짝인지 바로 안다.

- 설정 파일은 게임을 끈 상태에서만 고친다 ([workflow.md](workflow.md) 4.3절).
- 외부 출처 스크립트 (`loot/recycle` `loot/bank-pouch` `train/barding` `train/carto` `train/magery` `train/steal` `gather/*`, `shelf/*`)는 이 형식을 따르지 않고 그대로 둔다.

## 목차

1. [세 경로](#1-세-경로)
    - 1.1 [어디에 무엇이](#11-어디에-무엇이)
    - 1.2 [경로 고르기](#12-경로-고르기)
    - 1.3 [누구 머리 위에](#13-누구-머리-위에)
2. [형식](#2-형식)
3. [상태 어휘](#3-상태-어휘)
4. [글로서리](#4-글로서리)
5. [hue 팔레트](#5-hue-팔레트)
6. [쿨다운 바](#6-쿨다운-바)
    - 6.1 [규칙](#61-규칙)
    - 6.2 [cooldown 은 서버 값이 아니다](#62-cooldown-은-서버-값이-아니다)
    - 6.3 [바 목록](#63-바-목록)
7. [프로필 오버헤드 표](#7-프로필-오버헤드-표)
8. [스크립트 오버헤드](#8-스크립트-오버헤드)
9. [구멍](#9-구멍)
10. [확인 안 된 것](#10-확인-안-된-것)
11. [출처](#11-출처)

---

## 1. 세 경로

### 1.1 어디에 무엇이

| 경로            | 파일                                                                | 무엇                                                                         |
|-----------------|---------------------------------------------------------------------|------------------------------------------------------------------------------|
| 쿨다운 바       | `config/<이름>/classicuo/<캐릭>/cooldowns.xml`                      | 시스템 메시지로 시작하는 타이머 바. 스크립트가 `cooldown "이름"` 으로 읽는다 |
| 프로필 오버헤드 | `config/<이름>/razor/profiles/<프로필>.xml` 의 `<overheadmessages>` | 시스템 메시지를 머리 위 한 줄로 바꿔 띄운다                                  |
| 스크립트        | `script/**/*.razor` 의 `overhead "..."`                             | 스크립트가 직접 띄우는 줄                                                    |

### 1.2 경로 고르기

**그 사실을 누가 아느냐**로 정한다.

| 사실을 아는 쪽                                                      | 경로                                                            | 예                                |
|---------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------|
| **서버**가 문장 하나로 알려주는 사건                                | 프로필 오버헤드. 지속시간이 있으면 쿨다운 바를 짝으로           | `[ hams, target ]` `[ para, on ]` |
| **스크립트**만 아는 상태 (무엇을 골랐는지, 재고, 무엇을 시전하는지) | 스크립트 `overhead`                                             | `[ inst, out ]` `[ blood oath ]`  |
| 여러 명 중 **누구인지**가 곧 정보인 것                              | 스크립트 `overhead "…" 705 <serial>` 로 그 대상 머리 위에 (1.3) | `[ target, set ]` `[ explo, on ]` |

- **한 사건은 한 경로로만 띄운다.** 프로필이 이미 잡는 문장을 스크립트가 다시 띄우지 않는다.
  그래서 스크립트의 `[ heal pot, on ]` 과 `[ drain ]` `[ curse ]` 시전 알림을 뺐다 (7절 `You drink a healing potion`, `You mana drain your target.`).
- 서버 문장으로 오는 사건 (`[ hams, target ]` 등)을 스크립트로 옮겨 상대 머리 위에 띄우지 않는다.
  - 저장소에 `injournal` 선례가 없고, 매 패스 저널을 확인하는 비용이 든다 (거짓 `if` 하나가 10~20ms, [razor.md](razor.md) 6절).
  - 스크립트가 꺼져 있으면 안 뜬다. 프로필 오버헤드는 항상 뜬다.
  - 햄스트링이 들어간 상대가 `lasttarget` 이라는 보장이 없다.
  - 구조화 PvP 에서는 플레이어 serial 이 `0x0` 이라 상대 머리 위에 띄울 수 없다 ([razor.md](razor.md) 7절). 이 알림들은 대부분 PvP 용이다.
  - UO 화면은 내 캐릭터가 중심이라 내 머리 위가 위치가 고정돼 있어 가장 읽기 쉽다.

### 1.3 누구 머리 위에

- 스크립트 `overhead` 는 셋째 인자에 serial 을 주면 그 대상 머리 위에 뜬다.
- 상대에 관한 줄 (`[ target, set ]`, 들고 있는 `[ explo, on ]`)은 상대 위에 hue 705 로, 소환수에 붙인 이름 `[ name, nomeehei ]` 은 그 소환수 위에 hue 9 로 띄운다.
- 나머지는 내 위. 프로필 오버헤드는 항상 내 위다.

## 2. 형식

`[ 대상, 상태 ]`.

| 규칙           | 내용                                                                                                                                                                                                                               |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 형태           | `[ 대상, 상태 ]`. 전부 소문자, 대괄호 안쪽 공백 한 칸, 쉼표 뒤 공백 한 칸. 느낌표 · 마침표 · 대문자 강조 없음. 심각도는 hue 가 말한다                                                                                              |
| 대상           | 4절 글로서리 단어. 없으면 온전한 단어. 줄임말은 **말로 할 때도 줄이는 것만** (`hams` `teleki` `inst` `explo` `eb` …). `magic arrow` `fireball` `lightning` 은 안 줄인다                                                            |
| 상태           | 3절 어휘. 드문 상태는 한 단어                                                                                                                                                                                                      |
| 시전 알림      | `[ blood oath ]` 처럼 **대상만**. hue 118 / 83 이 "지금 나간다" 를 말하므로 상태가 필요 없다                                                                                                                                       |
| 값             | 서버 문장의 n 번째 단어는 `{n}` 으로 그대로 넣는다 (**1부터**, 공백 기준): "You must wait another 4 minutes" 의 `{5}` 가 4. 스크립트 변수는 `{{var}}`: `[ inst, {{label__picked_instrument}} ]`                                    |
| 폭             | 대괄호 포함 **18자 목표, 22자 상한.** 넘으면 대상을 줄인다 (`No Longer Paralyzed` → `[ para, off ]`)                                                                                                                               |
| 구분           | 서버 문장은 절대 `[` 로 시작하지 않는다. 대괄호가 곧 "커스텀" 표시다                                                                                                                                                               |
| 검색           | 부분 문자열, **대소문자 안 가림** (인게임 확인: `Trapped pouches` 가 "trapped pouches" 에 걸렸다). 정규식·와일드카드 없음                                                                                                          |
| 기다림         | 기다리라는 문장은 `[ wait, … ]`. "wait another N" 꼴은 숫자 자리가 고정이라 `4m 17s` / `2m` / `59s`. 포션 대기("wait N" 꼴)는 혼합 형태와 초 형태를 못 갈라 `1m 59s` 를 못 만들고, 버프창이 이미 보여주므로 **빈 메시지로 삼킨다** |
| 순서           | 한 문장에 항목 여러 개가 걸리면 **파일에서 앞의 것 하나만** 뜬다 (인게임 확인, `[ wait, 4m 53s ]` 가 `[ wait, 4s ]` 를 눌렀다). 구체적인 검색어를 범용 검색어보다 **앞에** 둔다                                                    |
| 쿨다운 바 이름 | 같은 단어, **대괄호 없이**. 방향이 있을 때만 쉼표: `hams, me` / `teleki, target`. 그 외는 한 단어: `music` `heal pot`                                                                                                              |

## 3. 상태 어휘

| 뜻                 | 단어                | 예                                                                                                                                                 |
|--------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 상대가 나에게      | `me`                | `[ hams, me ]` `[ teleki, me ]` `[ disarm, me ]`                                                                                                   |
| 내가 상대에게 걸림 | `target`            | `[ hams, target ]` `[ teleki, target ]` `[ bleed, target ]`                                                                                        |
| 내 시도 실패       | `miss`              | `[ hams, miss ]` `[ disco, miss ]` `[ lock, miss ]`                                                                                                |
| 잘못된 것          | `wrong`             | `[ inst, wrong ]` `[ steal, wrong ]`                                                                                                               |
| 쿨 끝 · 할 수 있음 | `ready`             | `[ str, ready ]` `[ hide, ready ]` `[ fireball, ready ]`                                                                                           |
| 켜짐 · 진행 중     | `on`                | `[ para, on ]` `[ guard, on ]` `[ bank safe, on ]`                                                                                                 |
| 풀림 · 아직 안 됨  | `off`               | `[ para, off ]` `[ stealth, off ]` `[ guard, off ]`                                                                                                |
| 다 떨어짐 · 없음   | `out`               | `[ pouch, out ]` `[ inst, out ]` `[ range, out ]`                                                                                                  |
| 들어오는 중        | `coming`            | `[ heal, coming ]` `[ world, coming ]`                                                                                                             |
| 골라라 (프롬프트)  | `pick`              | `[ inst, pick ]` `[ shelf, pick ]`                                                                                                                 |
| 저장됨             | `set`               | `[ target, set ]` `[ var, set ]` `[ chest, set ]`                                                                                                  |
| 끝남               | `done`              | `[ lock, done ]` `[ loadout, done ]`                                                                                                               |
| 시전이 끊김        | `disturbed` / `cut` | `[ heal, disturbed ]` (서버가 끊음) / `[ curse, cut ]` (힐하려고 내가 끊음)                                                                        |
| 수량 · 초          | 숫자                | `[ stealth, 3 ]` `[ mush, {5} ]` `[ planted, 2s ]` `[ murder, +1 ]`                                                                                |
| 붙인 이름          | 이름 그대로         | `[ name, nomeehei ]` (소환수에 붙인 이름, 그 소환수 머리 위)                                                                                       |
| 드문 상태          | 한 단어             | `full` `over` `free` `blocked` `near` `slow` `clear` `deadly` `lethal` `refund` `charged` `extended` `moved` `worn` `back` `take` `skip` `dropped` |

`target` 은 방향에만 쓴다. "찍어라" 는 `pick`.

## 4. 글로서리

대상 단어.

| 뜻                        | 단어                 | 뜻                   | 단어                  | 뜻                 | 단어           |
|---------------------------|----------------------|----------------------|-----------------------|--------------------|----------------|
| hamstring                 | `hams`               | telekinesis          | `teleki`              | paralyze           | `para`         |
| instrument                | `inst`               | explosion            | `explo`               | energy bolt        | `eb`           |
| discordance / provocation | `disco` / `provo`    | peacemaking          | `peace`               | barding song       | `song`         |
| greater heal              | `gheal`              | mana drain / vampire | `drain`               | meditation         | `medi`         |
| magic mushroom            | `mush`               | criminal             | `crim`                | veterinary         | `vet`          |
| herbal poultice           | `herb`               | herding              | `herd`                | invisibility       | `invis`        |
| chain lightning           | `chain`              | meteor swarm         | `meteor`              | teleport           | `tp`           |
| str / agi / resist 포션   | `str` `agi` `resist` | heal / cure 포션     | `heal pot` `cure pot` | refresh 포션       | `refresh`      |
| explosion 포션            | `explo pot`          | 나에게 붙은 폭탄     | `bomb`                | trapped pouch      | `pouch`        |
| smoke bomb                | `smoke`              | reagent satchel      | `reg satchel`         | alchemists satchel | `alch satchel` |
| identification wand       | `id wand`            | necromancy book      | `necro book`          | reactive armor     | `reactive`     |
| 그 외                     | 온전한 단어          |                      |                       |                    |                |

`heal` `cure` 는 주문이라 포션은 `heal pot` `cure pot`. 힘·민·레지는 주문을 안 쓰니 `str` `agi` `resist` 그대로.

## 5. hue 팔레트

상태 단어가 색을 정한다. 색은 [Razor 색표](https://outlands.uorazorscripts.com/hues) 에서 골랐고, 뜻이 다르면 색 계열도 다르게 했다.
따뜻한 색은 전투, 차가운 색은 정보, 초록은 준비·해제.

| hue | 색               | 뜻                                                                                                   | 상태 단어                                                             | 예                                                                       |
|-----|------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------|
| 33  | 진홍 `#e80030`   | **나에게 걸린 것**, 그것 없이는 못 싸우는 것                                                         | `me`, 치명적 `out`                                                    | `[ hams, me ]` `[ teleki, me ]` `[ pouch, out ]` `[ inst, out ]`         |
| 43  | 주황 `#e86000`   | **내 공격·스킬이 먹힘**                                                                              | `target` `area`                                                       | `[ disco, target ]` `[ fireball, target ]` `[ bleed, target ]`           |
| 53  | 노랑 `#e8e800`   | 경고 — 실패 · 막힘 · 재고 없음 · 버프 빠짐                                                           | `miss` `wrong` `out` `disturbed` `cut` `over` `blocked`, 버프의 `off` | `[ hams, miss ]` `[ heal pot, out ]` `[ reflect, off ]` `[ wait, 4m ]`   |
| 90  | 하늘 `#60e0f0`   | 정보 · 카운터 · 진행. 스크립트에서는 `config__chatty` 로 끈다                                        | `on` 숫자 `refund` `set`                                              | `[ unholy, 6/10 ]` `[ mana, refund ]` `[ mush, on ]` `[ var, set ]`      |
| 68  | 초록 `#18e800`   | 준비됨 · 끝남 · 내 것 성공                                                                           | `ready` `done`                                                        | `[ str, ready ]` `[ lock, done ]` `[ siphon, on ]`                       |
| 65  | 연두 `#98f060`   | 나쁜 것이 풀림                                                                                       | 나쁜 효과의 `off`                                                     | `[ para, off ]` `[ poison, off ]` `[ hams, off ]`                        |
| 9   | 남보라 `#6830e8` | 아군 · 파티 · 내 소환수                                                                              | `coming` 붙인 이름                                                    | `[ heal, coming ]` `[ party, on ]` `[ name, nomeehei ]` (소환수 머리 위) |
| 118 | 보라 `#c010d8`   | 네크로 · 무기 능력 시전 (대상만)                                                                     | —                                                                     | `[ blood oath ]` `[ pummel ]`                                            |
| 83  | 청록 `#00e8b8`   | 매저리 시전 (대상만). 지금 쓰는 줄은 없다. Drain / Curse 는 프로필이 `[ drain, target ]` 으로 띄운다 | —                                                                     | `[ eb ]`                                                                 |
| 55  | 연노랑 `#f0f060` | 프롬프트                                                                                             | `pick`                                                                | `[ inst, pick ]` `[ shelf, pick ]`                                       |
| 123 | 자홍 `#d810b0`   | 월드 이벤트                                                                                          | —                                                                     | `[ world, saving ]` `[ boss, {7} ]`                                      |
| 705 | 회보라 `#9898b8` | **상대 머리 위 표시** — 스크립트가 `overhead "…" 705 <serial>` 로 그 몹 위에 띄운다                  | `set` `on`                                                            | `[ target, set ]` `[ explo, on ]`                                        |

## 6. 쿨다운 바

### 6.1 규칙

- 이름은 소문자 글로서리 단어. 방향이 있을 때만 `, me` / `, target` / `, immune` / `, on`.
- `cooldownbartype="Criminal"` 과 `"PvP"` 는 **클라이언트가 서버 타이머로 직접 채우는 특수 바**다. 트리거를 달지 않는다.
  Heat of Battle 은 `pvp` 바가 그 자리다.
- 자기한테 TK 를 걸면 `teleki, target` 과 `teleki, me` 가 둘 다 뜬다. 서버가 시전자 문장과 대상 문장을 둘 다 보내므로 맞는 동작이다.
- `reflect` 바는 "Magic reflect removed." 로 시작하는 30초, 서버의 재시전 잠금 그대로다. 자기 주문으로 없애면
  "You remove your magic reflect spell." 이 한 줄 더 오는데 그건 트리거가 아니다.
- 스크립트가 읽는 이름은 `cooldown "이름"` 과 **정확히 일치**해야 한다. 바 이름을 바꿀 때는 `grep -rn 'cooldown "' script/` 부터.
- 항목 순서는 **바가 자주 뜨는 순서**다. 바드 바 다섯 개가 맨 앞이고 그 뒤에 매저리 프록 바. 순서와 트리거 문장의 근거는
  [bard-necro-handbook.md](bard-necro-handbook.md) 2.9절.

### 6.2 cooldown 은 서버 값이 아니다

`cooldown "이름"` 은 `cooldowns.xml` 에 **직접 정의한 메시지 트리거 타이머**다. 서버 쿨이 아니라 **내가 설정한 값**을 알려준다.
숫자가 이상하면 서버가 아니라 이 파일을 의심한다.

그래도 스크립트는 자체 `timer__` 대신 이것을 읽는다. 게임이 예고 없이 쿨을 초기화하는 경우
(Lyric Aspect 의 "Your barding skill cooldowns reset.")에도 리셋 문장에 트리거를 걸어 두면 바가 같이 0 이 되기 때문이다.
예전에 `music` 에 송 트리거가 섞여 서로 덮어쓰던 사고와 그 수정은 [bard-necro-handbook.md](bard-necro-handbook.md) 2.9절.

### 6.3 바 목록

`config/indian/classicuo/nomeehej/cooldowns.xml` 의 항목, 파일 순서 그대로. 정본은 이 파일이다.

`skill` `music` `disco` `peace/provo` `song` `magic arrow` `harm` `fireball` `lightning` `mush` `heal pot` `steal` `hide` `stealth` `void mana` `void health` `swing 1` `swing 2` `swing 3` `swing 4`
`medi` `pain spike` `necrosis` `hams, target` `hams, me` `hams, immune` `disarm, target` `noble sacrifice` `holy light` `aspect` `poison strike` `corpse skin` `curse` `chain` `meteor` `mass curse`
`boarding` `sea combat` `repair` `spyglass` `cannons` `drain` `herd` `rope` `control points` `teleki, target` `teleki, me` `para` `detonate` `reflect` `fish` `sp keg` `defensive` `sunder` `cleave`
`wild swing` `shield bash` `warding` `testudo` `mirror` `bulwark` `arcane` `fowling` `incendiary` `longshot` `maiming` `walk` `explo pot` `bandage` `pvp` `crim` `divine fury` `shrine` `bomb, target`
`bomb, me` `siphon` `contested` `eject` `corpse creek` `vip` `flashpoint` `caravan` `idoc` `dock` `smoke` `backstab` `reveal` `taunt` `fortify rations` `negate time` `rune` `summon` `frost`
`frost, on` `weapon swing` `consecrate weapon` `pedestal` `bank note` `panacea` `shoot` `spam` `crew heal` `quest` `omni pot` `ability`

| 바                          | 메모                                                                            |
|-----------------------------|---------------------------------------------------------------------------------|
| `corpse skin`               | backstab-mugging 이 `cooldown "corpse skin"` 으로 직접 세운다                   |
| `bomb, me`                  | 5초. "An explosion potion has stuck to you"                                     |
| `siphon`                    | 3600초. "Spell siphon active." 로 시작하고 만료 문장에 리셋                     |
| `pvp` `crim`                | 특수 바 타입. 트리거 없음 (6.1)                                                 |
| `magic arrow` … `lightning` | 매저리 프록 15초. 문장은 [bard-necro-handbook.md](bard-necro-handbook.md) 3.1절 |

## 7. 프로필 오버헤드 표

서버 문장 (검색어) → 메시지 (hue). Razor 프로필 `bard mace.xml` 과 `default.xml` 이 같은 내용이고,
`default.xml` 에는 던지기 8줄 (`now planted`, `moving throws`, `wing your target`)이 없고 붕대 1줄이 더 있다.
정본은 프로필 xml 이다. 항목을 바꾸면 이 표도 같이 고친다. 표의 순서는 파일 순서이고, 2절 "순서" 규칙 때문에 의미가 있다.

| 서버 문장                                                                | 메시지 (hue)                                                                                                                                                               |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| : Attempting to heal you.                                                | `[ heal, coming ] (9)`                                                                                                                                                     |
| You do not have a full suit of armor                                     | `[ armor, out ] (53)`                                                                                                                                                      |
| Now tracking                                                             | `[ track, {3} {4} {5} ] (90)`                                                                                                                                              |
| spaces to target                                                         | `[ track, {3} {4} {5} ] (90)`                                                                                                                                              |
| You search the home and find no one hiding within.                       | `[ house, clear ] (68)`                                                                                                                                                    |
| script variable updated                                                  | `[ var, set ] (90)`                                                                                                                                                        |
| Your attack hamstrings your target                                       | `[ hams, target ] (43)`                                                                                                                                                    |
| There's not enough wood here to harvest.                                 | `[ wood, out ] (53)`                                                                                                                                                       |
| you notice                                                               | `[ thief, me ] (33)`                                                                                                                                                       |
| you have already used the maximum                                        | `[ field, out ] (53)`                                                                                                                                                      |
| You have been poisoned!                                                  | `[ poison, on ] (33)`                                                                                                                                                      |
| You have been cured of all poisons.                                      | `[ poison, off ] (65)`                                                                                                                                                     |
| You have been cured of all poisons!                                      | `[ poison, off ] (65)`                                                                                                                                                     |
| You are already at full health.                                          | `[ hits, full ] (90)`                                                                                                                                                      |
| You increase your damage resistance to creature-casted spells            | `[ resist, on ] (90)`                                                                                                                                                      |
| You cannot move!                                                         | `[ para, on ] (33)`                                                                                                                                                        |
| You can move!                                                            | `[ para, off ] (65)`                                                                                                                                                       |
| before you may use another strength potion                               | **빈 메시지** — 버프창이 지속시간을 보여주니 안 띄운다. 항목을 지우면 뒤의 범용 `minutes ` 가 잡아 `[ wait, minutem secondss ]` 가 되므로, 앞에서 **삼키는 용도**로 남긴다 |
| before you may use another agility potion                                | 빈 메시지, 위와 같음                                                                                                                                                       |
| you are already at full stamina.                                         | `[ stam, full ] (90)`                                                                                                                                                      |
| You are not poisoned.                                                    | `[ poison, off ] (90)`                                                                                                                                                     |
| You may now use a strength potion.                                       | `[ str, ready ] (68)`                                                                                                                                                      |
| You may now use an agility potion.                                       | `[ agi, ready ] (68)`                                                                                                                                                      |
| Looting this corpse will be a criminal act!                              | `[ loot, crim ] (53)`                                                                                                                                                      |
| Looting this monster corpse will be a criminal act!                      | `[ loot, crim ] (53)`                                                                                                                                                      |
| You are now a criminal.                                                  | `[ crim, on ] (33)`                                                                                                                                                        |
| You have been reported for a murder!                                     | `[ murder, +1 ] (33)`                                                                                                                                                      |
| You summon an ancient                                                    | `[ ancient, on ] (68)`                                                                                                                                                     |
| Your spellbook generates mana for your spell.                            | `[ mana, refund ] (90)`                                                                                                                                                    |
| You fail to ignite the campfire.                                         | `[ camp, miss ] (53)`                                                                                                                                                      |
| Your campfire is now secure.                                             | `[ camp, on ] (68)`                                                                                                                                                        |
| You feel it would take a few moments to secure your camp.                | `[ camp, coming ] (90)`                                                                                                                                                    |
| You enter a meditative trance.                                           | `[ medi, on ] (90)`                                                                                                                                                        |
| Your concentration is disturbed, thus ruining thy spell.                 | `[ cast, disturbed ] (53)`                                                                                                                                                 |
| Being perfectly rested, you shove something invisible out of the way.    | `[ hidden, near ] (53)`                                                                                                                                                    |
| You may now attempt to                                                   | `[ hams, ready ] (68)`                                                                                                                                                     |
| You refrain from making hamstring attempts.                              | `[ hams mode, off ] (90)`                                                                                                                                                  |
| You will now attempt to hamstring your opponents.                        | `[ hams mode, on ] (90)`                                                                                                                                                   |
| You fail to hamstring your opponent.                                     | `[ hams, miss ] (53)`                                                                                                                                                      |
| Their attack hamstrings you!                                             | `[ hams, me ] (33)`                                                                                                                                                        |
| You are no longer hamstrung                                              | `[ hams, off ] (65)`                                                                                                                                                       |
| You will now attempt to disarm your opponents.                           | `[ disarm mode, on ] (90)`                                                                                                                                                 |
| You refrain from making disarm attempts.                                 | `[ disarm mode, off ] (90)`                                                                                                                                                |
| Your strike disarms your target!                                         | `[ disarm, target ] (43)`                                                                                                                                                  |
| You fail to disarm your opponent.                                        | `[ disarm, miss ] (53)`                                                                                                                                                    |
| Their attack disarms you!                                                | `[ disarm, me ] (33)`                                                                                                                                                      |
| Where do you wish to traverse to?                                        | `[ rope, pick ] (55)`                                                                                                                                                      |
| That location is blocked.                                                | `[ spot, blocked ] (53)`                                                                                                                                                   |
| Target cannot be seen.                                                   | `[ range, out ] (53)`                                                                                                                                                      |
| You are now under the protection of the town guards.                     | `[ guard, on ] (90)`                                                                                                                                                       |
| You have left the protection of the town guards.                         | `[ guard, off ] (53)`                                                                                                                                                      |
| Someone tried to steal from you.                                         | `[ thief, me ] (33)`                                                                                                                                                       |
| You have been revealed!                                                  | `[ reveal, me ] (33)`                                                                                                                                                      |
| You have been banned from this house.                                    | `[ ban, me ] (53)`                                                                                                                                                         |
| You have been ejected from this house!                                   | `[ eject, me ] (53)`                                                                                                                                                       |
| You have been added to the party.                                        | `[ party, on ] (9)`                                                                                                                                                        |
| You have been removed from the party.                                    | `[ party, off ] (9)`                                                                                                                                                       |
| You feel ready to continue stealthing                                    | `[ stealth, ready ] (68)`                                                                                                                                                  |
| You feel comfortable enough to begin stealthing                          | `[ stealth, ready ] (68)`                                                                                                                                                  |
| You have 5 stealth steps remaining                                       | `[ stealth, 5 ] (90)`                                                                                                                                                      |
| You have successfully cleared it of traps                                | `[ trap, done ] (68)`                                                                                                                                                      |
| You successfully pick the lock                                           | `[ lock, done ] (68)`                                                                                                                                                      |
| You fail to make any progress on the lock                                | `[ lock, miss ] (53)`                                                                                                                                                      |
| You fail to make any progress towards removing traps                     | `[ trap, miss ] (53)`                                                                                                                                                      |
| You finish using veterinary supplies                                     | `[ vet, done ] (68)`                                                                                                                                                       |
| You begin using veterinary supplies                                      | `[ vet, on ] (90)`                                                                                                                                                         |
| What do you wish to focus your follower's aggression towards?            | `[ herd, pick ] (55)`                                                                                                                                                      |
| you extend the life of your creature                                     | `[ summon, extended ] (90)`                                                                                                                                                |
| you are now under the effect of herbal poultice                          | `[ herb, on ] (90)`                                                                                                                                                        |
| Your herbal poultice has lost its effectiveness.                         | `[ herb, off ] (53)`                                                                                                                                                       |
| That spell is already currently in effect.                               | `[ buff, on ] (90)`                                                                                                                                                        |
| already at full repair                                                   | `[ repair, done ] (90)`                                                                                                                                                    |
| You may now use another magic mushroom                                   | `[ mush, ready ] (68)`                                                                                                                                                     |
| before you may consume another magic mushroom                            | `[ mush, {5} ] (90)`                                                                                                                                                       |
| One of more of your ship crewmembers                                     | `[ crew, ready ] (68)`                                                                                                                                                     |
| Criminal healing will now be allowed                                     | `[ crim heal, on ] (90)`                                                                                                                                                   |
| Criminal healing will now be prevented                                   | `[ crim heal, off ] (90)`                                                                                                                                                  |
| Criminal looting will now be allowed                                     | `[ crim loot, on ] (90)`                                                                                                                                                   |
| Criminal looting will now be prevented                                   | `[ crim loot, off ] (90)`                                                                                                                                                  |
| Your lightning spell hinders your target                                 | `[ lightning, target ] (43)` — 라이트닝 프록                                                                                                                               |
| Your attack cripples your target, lowering their defense                 | `[ cripple, target ] (43)`                                                                                                                                                 |
| You smash through                                                        | `[ smash, target ] (43)`                                                                                                                                                   |
| susceptible to special                                                   | `[ bleed, target ] (43)`                                                                                                                                                   |
| armslore skillgain                                                       | `[ swing ] (90)`                                                                                                                                                           |
| attack causes your target to bleed                                       | `[ bleed, target ] (43)`                                                                                                                                                   |
| minutes before / minute before                                           | `[ wait, {5}m ] (53)` — "…wait another 2 minutes before…" 처럼 초가 없는 형태. 초가 있는 형태보다 앞에 둔다                                                                |
| minutes  / minute  (뒤 공백)                                             | `[ wait, {5}m {7}s ] (53)` — "You must wait another 4 minutes 17 seconds …"                                                                                                |
| must wait another                                                        | `[ wait, {5}s ] (53)`                                                                                                                                                      |
| 0 Trapped pouches remain                                                 | `[ pouch, out ] (33)`                                                                                                                                                      |
| No trapped pouches found                                                 | `[ pouch, out ] (33)`                                                                                                                                                      |
| restricted from performing aggressive                                    | `[ restrict, {14} ] (33)`                                                                                                                                                  |
| world will save                                                          | `[ world, coming ] (123)`                                                                                                                                                  |
| world is saving                                                          | `[ world, saving ] (123)`                                                                                                                                                  |
| save complete                                                            | `[ world, done ] (123)`                                                                                                                                                    |
| aspect and other bonuses return                                          | `[ aspect, on ] (68)`                                                                                                                                                      |
| free cure potion                                                         | `[ cure pot, free ] (90)`                                                                                                                                                  |
| too fatiqued                                                             | `[ weight, over ] (53)`                                                                                                                                                    |
| too fatigued                                                             | `[ weight, over ] (53)`                                                                                                                                                    |
| are overloaded                                                           | `[ weight, over ] (53)`                                                                                                                                                    |
| contested boss has spawned                                               | `[ boss, {7} ] (123)`                                                                                                                                                      |
| control points earned for current beacon                                 | `[ beacon, +{2} {12} ] (90)`                                                                                                                                               |
| kill points earned                                                       | `[ kill, +{2} {9} ] (90)`                                                                                                                                                  |
| DF A Dungeon Flashpoint will begin in 15 minutes.                        | `[ flashpoint, coming ] (123)`                                                                                                                                             |
| cured the target of all poisons                                          | `[ cure, target ] (68)`                                                                                                                                                    |
| cast a wizardry magic arrow spell again                                  | `[ magic arrow, ready ] (68)` — 검색어를 준비 문장으로 좁힘, "activated" 는 아래                                                                                           |
| cast a wizardry harm spell again                                         | `[ harm, ready ] (68)`                                                                                                                                                     |
| cast a wizardry fireball spell again                                     | `[ fireball, ready ] (68)`                                                                                                                                                 |
| cast a wizardry lightning spell again                                    | `[ lightning, ready ] (68)`                                                                                                                                                |
| cast a wizardry chain lightning spell again                              | `[ chain, ready ] (68)`                                                                                                                                                    |
| cast a wizardry meteor swarm spell again                                 | `[ meteor, ready ] (68)`                                                                                                                                                   |
| magic arrow / harm / fireball / chain lightning / meteor swarm activated | `[ 주문, target ] (43)` — 프록이 터졌다, 15초 바 시작                                                                                                                      |
| upgraded to Deadly                                                       | `[ poison, deadly ] (43)`                                                                                                                                                  |
| upgraded to Lethal                                                       | `[ poison, lethal ] (43)`                                                                                                                                                  |
| Triggered (Epic)                                                         | `[ aspect, on ] (68)`                                                                                                                                                      |
| enough experience to upgrade                                             | `[ aspect, upgrade ] (90)`                                                                                                                                                 |
| Society Job Progress                                                     | `[ society, {4} ] (90)`                                                                                                                                                    |
| You have completed a society job                                         | `[ society, done ] (68)`                                                                                                                                                   |
| aspect experience                                                        | `[ {4}, {7} ] (90)`                                                                                                                                                        |
| resist a bleed                                                           | `[ bleed, off ] (65)`                                                                                                                                                      |
| resist a disease effect                                                  | `[ disease, off ] (65)`                                                                                                                                                    |
| been struck by an ancient blight                                         | `[ disease, on ] (33)`                                                                                                                                                     |
| may now review results                                                   | `[ boss, done ] (90)`                                                                                                                                                      |
| struck by an evil omen                                                   | `[ omen, target ] (43)`                                                                                                                                                    |
| enough unholy                                                            | `[ unholy, out ] (53)`                                                                                                                                                     |
| unholy symbols remaining                                                 | `[ unholy, {4} ] (90)`                                                                                                                                                     |
| max unholy                                                               | `[ unholy, max ] (68)` — "Max unholy symbols earned (10/10)", 괄호가 그대로 뜨는 `{5}` 대신                                                                                |
| consume a magic mushroom                                                 | `[ mush, on ] (90)` — "You consume a magic mushroom and restore some mana." 범용 `You consume` 보다 앞, 안 그러면 `[ essence, +a ]` 가 뜬다                                |
| mana from your mana well                                                 | `[ eldritch, +{3} ] (90)` — "You draw 11 mana from your mana well." Eldritch 아스펙트                                                                                      |
| You consume                                                              | `[ essence, +{3} ] (90)`                                                                                                                                                   |
| generates mana                                                           | `[ mana, refund ] (90)`                                                                                                                                                    |
| progress on the lock                                                     | `[ lock, {8} ] (90)`                                                                                                                                                       |
| clearing it of traps                                                     | `[ trap, {10} ] (90)`                                                                                                                                                      |
| thrown at that player within 30                                          | `[ teleki, target ] (43)`                                                                                                                                                  |
| free hand to drink                                                       | `[ hands, full ] (53)`                                                                                                                                                     |
| You will now automatically                                               | `[ scroll mode, on ] (90)`                                                                                                                                                 |
| You may only cast that spell on a player once every 30 seconds.          | `[ limit, 30s ] (53)`                                                                                                                                                      |
| Your boarding party fails to board the ship                              | `[ boarding, miss ] (53)`                                                                                                                                                  |
| That ship is too far away to board.                                      | `[ range, out ] (53)`                                                                                                                                                      |
| Your shot hinders your target!                                           | `[ hinder, target ] (43)`                                                                                                                                                  |
| You deactivate your stance.                                              | `[ stance, off ] (53)`                                                                                                                                                     |
| You smash the unprotected                                                | `[ smash, target ] (43)`                                                                                                                                                   |
| fallen to corruption                                                     | `[ shrine, on ] (123)`                                                                                                                                                     |
| You begin to move quietly                                                | `[ stealth, on ] (90)`                                                                                                                                                     |
| You have 4 stealth                                                       | `[ stealth, 4 ] (53)`                                                                                                                                                      |
| You have 3 stealth                                                       | `[ stealth, 3 ] (53)`                                                                                                                                                      |
| You have 2 stealth                                                       | `[ stealth, 2 ] (53)`                                                                                                                                                      |
| You have 1 stealth                                                       | `[ stealth, 1 ] (33)`                                                                                                                                                      |
| You have 0 stealth                                                       | `[ stealth, 0 ] (33)`                                                                                                                                                      |
| You must hide first                                                      | `[ hide, off ] (53)`                                                                                                                                                       |
| Those cannons are out of ammunition                                      | `[ cannon, out ] (53)`                                                                                                                                                     |
| You fail to steal                                                        | `[ steal, miss ] (53)`                                                                                                                                                     |
| You fail in your stealing attempt                                        | `[ steal, miss ] (53)`                                                                                                                                                     |
| You steal                                                                | `[ steal, done ] (68)`                                                                                                                                                     |
| You successfully steal                                                   | `[ steal, done ] (68)`                                                                                                                                                     |
| You have already stolen from this creature                               | `[ steal, wrong ] (53)`                                                                                                                                                    |
| You may now taunt again.                                                 | `[ taunt, ready ] (68)`                                                                                                                                                    |
| Potion codex Panaccea upgrade is now ready.                              | `[ panacea, ready ] (68)`                                                                                                                                                  |
| Your ability to hide is no longer impeded                                | `[ hide, ready ] (68)`                                                                                                                                                     |
| Weapon ability ready                                                     | `[ ability, ready ] (68)`                                                                                                                                                  |
| your rapid                                                               | `[ move, slow ] (53)`                                                                                                                                                      |
| your movements attract                                                   | `[ move, slow ] (53)`                                                                                                                                                      |
| your quick movements draw the attention                                  | `[ move, slow ] (53)`                                                                                                                                                      |
| iron flesh charges remaining                                             | `[ iron flesh, {1} ] (90)`                                                                                                                                                 |
| You detonate a ground trap                                               | `[ detonate, done ] (43)`                                                                                                                                                  |
| You may now detonate another trap                                        | `[ detonate, ready ] (68)`                                                                                                                                                 |
| You increase your [EventScore                                            | `[ event, +{6} ] (90)`                                                                                                                                                     |
| You are now under the effect of a Song                                   | `[ song, on ] (90)`                                                                                                                                                        |
| You fail to discord                                                      | `[ disco, miss ] (53)`                                                                                                                                                     |
| fail to pacify your opponent                                             | `[ peace, miss ] (53)`                                                                                                                                                     |
| fail to pacify any nearby creatures                                      | `[ peace, area miss ] (53)` — 범용 `fail to pacify` 보다 앞                                                                                                                |
| disrupting your opponent                                                 | `[ disco, target ] (43)`                                                                                                                                                   |
| briefly discording                                                       | `[ disco, area ] (43)` — 자기 타겟 = 8타일 광역, 각 5초                                                                                                                    |
| pacifying your target                                                    | `[ peace, target ] (43)`                                                                                                                                                   |
| briefly pacifying                                                        | `[ peace, area ] (43)` — 자기 타겟 = 8타일 광역, 각 2초                                                                                                                    |
| play successfully, provoking                                             | `[ provo, target ] (43)` — 프로보는 광역이 없다. 자기 타겟은 송                                                                                                            |
| fail to incite anger                                                     | `[ provo, miss ] (53)`                                                                                                                                                     |
| Song of Discordance / Peacemaking / Provocation effect ends              | `[ disco song / peace song / provo song, off ] (53)` — 15분 송이 끝남. 범용 `You play successfully` 는 뺐다                                                                |
| additional energy                                                        | `[ spell, charged ] (43)`                                                                                                                                                  |
| What instrument shall you play                                           | `[ inst, out ] (33)`                                                                                                                                                       |
| now planted                                                              | `[ planted, on ] (90)`                                                                                                                                                     |
| 5 moving throws                                                          | `[ throws, 5 ] (90)`                                                                                                                                                       |
| 4 moving throws                                                          | `[ throws, 4 ] (90)`                                                                                                                                                       |
| 3 moving throws                                                          | `[ throws, 3 ] (90)`                                                                                                                                                       |
| 2 moving throws                                                          | `[ throws, 2 ] (90)`                                                                                                                                                       |
| 1 moving throws                                                          | `[ throws, 1 ] (33)`                                                                                                                                                       |
| 0 moving throws                                                          | `[ throws, 0 ] (33)`                                                                                                                                                       |
| wing your target                                                         | `[ wing, target ] (43)`                                                                                                                                                    |
| Magic reflect removed                                                    | `[ reflect, off ] (53)` — 바 `reflect` 는 "Magic reflect removed." 30초 (몹), "Magic reflect removed (PvP)" 60초 (플레이어)                                                |
| has applied telekinesis to you                                           | `[ teleki, me ] (33)` — "nomeehej has applied telekinesis to you." 건 사람 이름은 저널에                                                                                   |
| An explosion potion has stuck to you                                     | `[ bomb, me ] (33)` — 퓨즈 5초, 바 `bomb, me` 와 짝                                                                                                                        |
| Your explosion potion sticks to your target                              | `[ bomb, target ] (43)`                                                                                                                                                    |
| You finish applying the bandages.                                        | `[ bandage, done ] (68)` — `default.xml` 에만 있다                                                                                                                         |
| You drink a healing potion                                               | `[ heal pot, on ] (90)` — 스크립트의 같은 줄은 뺐다                                                                                                                        |
| You drink a cure potion                                                  | `[ cure pot, on ] (90)`. 리프레시는 서버가 아무 문장도 안 보내서 없고, 힘·민은 "Your strength has changed by 20" 뿐이라 안 잡는다 — Weaken 을 맞아도 같은 문장이다         |
| You mana drain your target. / You curse your target.                     | `[ drain, target ]` / `[ curse, target ] (43)` — 스크립트의 `[ drain ]` `[ curse ]` 시전 알림은 뺐다                                                                       |
| Your reactive armor spell has been nullified.                            | `[ reactive, off ] (53)` — 25 흡수하고 빠짐, 다음 정지 구간에 다시 건다                                                                                                    |
| You generate mana for your spell.                                        | `[ mana, refund ] (90)` — 기존 `generates mana` 는 이 문장을 못 잡았다                                                                                                     |
| recovered from energy bolt kill                                          | `[ eb, refund ] (90)` — 티어마다 5/10/15 라 숫자는 안 보인다                                                                                                               |
| That is too far away.                                                    | `[ range, out ] (53)`                                                                                                                                                      |
| Spell siphon active.                                                     | `[ siphon, on ] (68)` — 5분마다 첫 주문 피격에 켜지는 60분 PvM 버프. 바 `siphon` 과 짝                                                                                     |
| Your spell siphon bonus has expired                                      | `[ siphon, off ] (53)`                                                                                                                                                     |
| You absorb their spell.                                                  | `[ spell, absorbed ] (68)` — Resist 의 `25% x Resist/100` 확률, 피해 -75%                                                                                                  |

## 8. 스크립트 오버헤드

규칙은 1~5절 그대로다. 스크립트에서 자주 헷갈리는 것만 모았다.

| 상황                                 | 모양                                       | hue |
|--------------------------------------|--------------------------------------------|-----|
| 상태, 정보. `config__chatty` 로 끈다 | `[ bard necro, on ]` `[ moongate, set ]`   | 90  |
| 재고 없음. 루프는 계속 돈다          | `[ heal pot, out ]` `[ crook, out ]`       | 53  |
| 시전 끊김                            | `[ heal, disturbed ]` `[ curse, cut ]`     | 53  |
| 그것 없이는 루프가 못 도는 것        | `[ inst, out ]` `[ necro book, out ]`      | 33  |
| 프롬프트                             | `[ inst, pick ]` `[ loot chest, pick ]`    | 55  |
| 네크로 · 무기 능력 시전              | `[ blood oath ]` `[ pummel ]`              | 118 |
| 매저리 시전 (지금 쓰는 줄 없음)      | `[ eb ]`                                   | 83  |
| 상대 머리 위                         | `[ target, set ]` `[ explo, on ]` + serial | 705 |
| 소환수 머리 위                       | `[ name, {{summon_name}} ]` + serial       | 9   |

지금 스크립트가 띄우는 줄은 `grep -rn 'overhead "\[' script/` 로 본다. 목록을 여기에 옮겨 적지 않는다 (옮겨 둔 표가 hue 번호를 바꿀 때 안 따라와서 틀렸다).

## 9. 구멍

서버 문장을 저널에서 잡아야 붙일 수 있는 것. 잡히면 바 + 오버헤드 짝으로 넣고 이 줄을 지운다.

| 상황                         | 필요한 것                                                          | 붙일 곳                               |
|------------------------------|--------------------------------------------------------------------|---------------------------------------|
| 디스암 당함                  | 문장은 있음 "Their attack disarms you!" — **재장착까지 몇 초**인지 | 바 `disarm, me`                       |
| Mana Drain / Vampire 맞음    | 문장                                                               | `[ drain, me ]` (레지 -10 / -20, 2분) |
| Curse / Weaken / Clumsy 맞음 | 문장                                                               | `[ curse, me ]` 등                    |
| Cure 포션 마심               | 문장은 있음 "You drink a cure potion" — 바만 없다                  | 바 `cure pot`                         |
| Refresh 포션 마심            | 서버가 문장을 안 보낸다. 지금으로는 방법이 없다                    | 바 `refresh`                          |
| `sp keg`                     | 무엇의 줄임인지 모름 (오버헤드 "spkeg" 트리거)                     | 이름                                  |

## 10. 확인 안 된 것

- PvP 에서 `paralyzed` 가 "You are frozen and cannot move." 상태를 잡는지, 파우치가 나가는지
- `message=""` 인 항목이 정말 아무것도 안 띄우는지, Razor 가 종료 때 그 항목을 지우지 않는지 (힘·민 포션 대기). 빈 줄이 뜨거나 항목이 사라지면 다른 방법을 찾는다
- `hams, me` 두 문장 중 실제로 오는 쪽 ("You have been hamstrung" / "Their attack hamstrings you!")
- `heal pot` 트리거 "You drink a healing potion" 이 실제 문장인지. 스크립트의 `cooldown "heal pot"` 과 겹쳐도 같은 시각에 다시 시작할 뿐이다
- 범죄자가 될 때 `crim` 바가 트리거 없이 저절로 뜨는지 (특수 바 타입)
- Heat of Battle 이 켜질 때 `pvp` 바가 트리거 없이 저절로 뜨는지 (같은 특수 바 타입)

## 11. 출처

- [Hamstring](https://wiki.uooutlands.com/Hamstring) — 3초 스태미나 0, 재적용 불가 30초, 시전자 쿨 30~53초
- [Magery](https://wiki.uooutlands.com/Magery) — Telekinesis 끈끈이 PvP 30초, Paralyze PvP 10초, Teleport PvP 쿨 15초
- [Alchemy](https://wiki.uooutlands.com/Alchemy) — Sticky Potions
- [Bapeths Total Cooldown XML](https://outlands.uorazorscripts.com/script/2138a7dc-785e-4d49-a465-e7c922d533ac) — 커뮤니티 트리거 문장, Criminal / PvP 바에 트리거가 없는 근거
- [overheadmessages 스니펫](https://outlands.uorazorscripts.com/script/8b4e1a67-5eb7-4933-8a07-a1ad1c797cc2)
