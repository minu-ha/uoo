---
name: Overheads
label: 머리 위 메시지와 쿨다운 바
group: Scripting
order: 40
---

게임 화면에 뜨는 알림 전부의 정본이다. 어느 경로로 띄우는가, 어떤 단어와 색을 쓰는가, 지금 무엇이 걸려 있는가.
같은 사건은 쿨다운 바 하나와 오버헤드 한 줄이 짝이고, 둘은 **같은 단어**를 쓴다. 바가 뜨면 어느 오버헤드의 짝인지 바로 안다.
스크립트 모양은 [conventions.md](conventions.md), 명령 문법은 [razor.md](razor.md)에 있다.

- 설정 파일은 게임을 끈 상태에서만 고친다 ([workflow.md](../working/workflow.md#04.C) 04.C절).
- 외부 출처 스크립트 (`loot/bank-pouch` `train/barding` `train/carto` `train/magery` `train/steal` `archive/mining`
  `archive/lumberjack` `shelf/*`)는 이 형식을 따르지 않고 그대로 둔다.

## <a id="00"></a>00 한눈에

| 절 | 무엇을 답하나 |
| --- | --- |
| [01](#01) | 알림을 어느 경로로 띄우나. 프로필, 쿨다운 바, 스크립트 중 누가 맡고 누구 머리 위에 뜨나 |
| [02](#02) | 한 줄을 어떤 형식으로 쓰나 |
| [03](#03) | 상태 자리에 어떤 낱말을 쓰나 |
| [04](#04) | 대상 자리에 어떤 낱말을 쓰나 |
| [05](#05) | 어떤 색을 쓰나 |
| [06](#06) | 쿨다운 바는 어떻게 정의하고 스크립트는 어떻게 읽나. 지금 바 목록 |
| [07](#07) | 프로필이 지금 무엇을 띄우나 |
| [08](#08) | 스크립트가 띄우는 줄은 어디서 보나 |
| [09](#09) | 문장을 아직 못 잡아 알림이 없는 사건은 무엇인가 |
| [10](#10) | 확인하지 못한 것 |
| [11](#11) | 출처 |

이 문서에 걸린 질문은 [open-items.md](../questions/open-items.md)에 모았다.

::part[규칙]

## <a id="01"></a>01 세 경로

### <a id="01.A"></a>01.A 어디에 무엇이

| 경로 | 파일 | 무엇 |
| --- | --- | --- |
| 쿨다운 바 | `config/<이름>/classicuo/<캐릭>/cooldowns.xml` | 메시지로 시작하는 타이머 바 (06.A). 스크립트가 `cooldown "이름"`으로 읽는다 |
| 프로필 오버헤드 | `config/<이름>/razor/profiles/<프로필>.xml`의 `<overheadmessages>` | 시스템 메시지를 머리 위 한 줄로 바꿔 띄운다 |
| 스크립트 | `script/**/*.razor`의 `overhead "..."` | 스크립트가 직접 띄우는 줄 |

### <a id="01.B"></a>01.B 경로 고르기

**그 사실을 누가 아느냐**로 정한다. 서버 문장인지를 먼저 묻는다. 상대에 관한 사건이라도 서버가 문장으로 알려 주면 프로필이 띄운다 (아래 둘째 항목).

```mermaid
flowchart TD
  server{"서버가 문장 하나로<br>알려 주는 사건인가"} -- 예 --> profile("프로필 오버헤드<br>내 머리 위") -- 지속되면 --> bar("쿨다운 바<br>같은 단어로 짝")
  server -- 아니요 --> who{"여러 명 중 누구인지가<br>곧 정보인가"}
  who -- 예 --> them("스크립트 overhead<br>serial로 그 대상 머리 위")
  who -- 아니요 --> me("스크립트 overhead<br>내 머리 위")
```

| 사실을 아는 쪽 | 경로 | 예 |
| --- | --- | --- |
| **서버**가 문장 하나로 알려 주는 사건 | 프로필 오버헤드. 지속시간이 있으면 쿨다운 바를 짝으로 둔다 | `[ hams, target ]` `[ para, on ]` |
| **스크립트**만 아는 상태 (무엇을 골랐는지, 재고, 무엇을 시전하는지) | 스크립트 `overhead` | `[ inst, out ]` `[ blood oath ]` |
| 여러 명 중 **누구인지**가 곧 정보인 것 | 스크립트 `overhead "…" 1288 <serial>`로 그 대상 머리 위에 (01.C) | `[ target, set ]` `[ explo, on ]` |

- **한 사건은 한 경로로만 띄운다.** 프로필이 이미 잡는 문장을 스크립트가 다시 띄우지 않는다.
  그래서 스크립트의 `[ heal pot, on ]`과 `[ drain ]` `[ curse ]` 시전 알림을 뺐다 (07절 `You drink a healing potion`, `You mana drain your target.`).
- 서버 문장으로 오는 사건 (`[ hams, target ]` 등)을 스크립트로 옮겨 상대 머리 위에 띄우지 않는다.
  - 저장소에 `injournal` 선례가 없고, 매 패스 저널을 확인하는 비용이 든다 (거짓 `if` 하나가 10\~20ms, [razor.md](razor.md#06) 06절).
  - 스크립트가 꺼져 있으면 안 뜬다. 프로필 오버헤드는 항상 뜬다.
  - 햄스트링이 들어간 상대가 `lasttarget`이라는 보장이 없다.
  - 구조화 PvP에서는 플레이어 serial이 `0x0`이라 상대 머리 위에 띄울 수 없다 ([razor.md](razor.md#07) 07절). 이 알림은 대부분 PvP용이다.
  - UO 화면은 내 캐릭터가 한가운데라 내 머리 위는 자리가 고정돼 가장 읽기 쉽다.

### <a id="01.C"></a>01.C 누구 머리 위에

- 스크립트 `overhead`는 셋째 인자에 serial을 주면 그 대상 머리 위에 뜬다.
- 상대에 관한 줄 (`[ target, set ]`, 커서에 쥔 Explosion의 `[ explo, on ]`)은 상대 위에 hue 1288로, 소환수에 붙인 이름 `[ name, leech ]`는 그 소환수 위에 hue 209로 띄운다.
- 나머지는 내 위에 띄운다. 프로필 오버헤드는 항상 내 위다.

## <a id="02"></a>02 형식

`[ 대상, 상태 ]`. 프로필이 서버 문장을 찾는 방식 (검색, 순서, 기다림)은 07절에 있다.

| 규칙 | 내용 |
| --- | --- |
| 형태 | `[ 대상, 상태 ]`. 전부 소문자, 대괄호 안쪽 공백 한 칸, 쉼표 뒤 공백 한 칸. 느낌표, 마침표, 대문자 강조는 쓰지 않는다. 심각도는 hue가 말한다 |
| 대상 | 04절 글로서리 단어. 없으면 온전한 단어. 줄임말은 **말로 할 때도 줄이는 것만** (`hams` `teleki` `inst` `explo` `eb` …). `magic arrow` `fireball` `lightning`은 안 줄인다 |
| 상태 | 03절 어휘. 드문 상태는 한 단어 |
| 시전 알림 | `[ blood oath ]`처럼 **대상만**. hue 219 / 284가 "지금 나간다"를 말하므로 상태가 필요 없다 |
| 값 | 서버 문장의 n번째 단어는 `{n}`으로 그대로 넣는다 (**1부터**, 공백 기준). "You must wait another 4 minutes"의 `{5}`가 4다. 검색어로 잘라 낸 부분이 아니라 전체 서버 문장의 단어 위치다. 구두점도 그대로 들어온다. 스크립트 변수는 `{{var}}`로 넣는다 (`[ inst, {{label__picked_instrument}} ]`) |
| 폭 | 대괄호 포함 **18자 목표, 22자 상한.** 넘으면 대상을 줄인다 (`No Longer Paralyzed` → `[ para, off ]`) |
| 구분 | 서버 문장은 절대 `[`로 시작하지 않는다. 대괄호가 곧 "커스텀" 표시다 |
| 쿨다운 바 이름 | 짝 오버헤드와 같은 단어를 **대괄호 없이** 쓴다 (`music` `heal pot` `hams, me`). 쉼표를 붙이는 경우는 6.1 |

`{n}`의 치환 방향은 Razor CE 원본의
[OverheadManager.DisplayOverheadMessage](https://github.com/markdwags/Razor/blob/master/Razor/Core/OverheadManager.cs)에서도 확인했다.
원문 전체를 공백으로 나눈 다음 첫 단어를 `{1}`에 넣는다. Outlands의 새 문장도 실제 단어 위치를 확인해서 매핑한다.

## <a id="03"></a>03 상태 어휘

| 뜻 | 단어 | 예 |
| --- | --- | --- |
| 상대가 나에게 | `me` | `[ hams, me ]` `[ teleki, me ]` `[ disarm, me ]` |
| 내가 상대에게 걸림 | `target` | `[ hams, target ]` `[ teleki, target ]` `[ bleed, target ]` |
| 내가 주변 여럿에게 걸림 (광역) | `area` | `[ disco, area ]` `[ peace, area ]` |
| 내 시도 실패 | `miss` | `[ hams, miss ]` `[ disco, miss ]` `[ lock, miss ]` |
| 잘못된 것 | `wrong` | `[ inst, wrong ]` `[ steal, wrong ]` |
| 쿨 끝, 할 수 있음 | `ready` | `[ str, ready ]` `[ hide, ready ]` `[ fireball, ready ]` |
| 켜짐, 진행 중 | `on` | `[ para, on ]` `[ guard, on ]` `[ bank safe, on ]` |
| 풀림, 아직 안 됨 | `off` | `[ para, off ]` `[ stealth, off ]` `[ guard, off ]` |
| 다 떨어짐, 없음 | `out` | `[ pouch, out ]` `[ inst, out ]` `[ range, out ]` |
| 들어오는 중 | `coming` | `[ heal, coming ]` `[ world, coming ]` |
| 골라라 (프롬프트) | `pick` | `[ inst, pick ]` `[ shelf, pick ]` |
| 저장됨 | `set` | `[ target, set ]` `[ var, set ]` `[ chest, set ]` |
| 끝남 | `done` | `[ lock, done ]` `[ loadout, done ]` |
| 시전이 끊김 | `disturbed` / `cut` | `[ cast, disturbed ]` (서버가 끊음, 프로필) / `[ curse, cut ]` (힐하려고 내가 끊음) |
| 수량, 초 | 숫자 | `[ stealth, 3 ]` `[ mush, {5} ]` `[ planted, 2s ]` `[ murder, +1 ]` |
| 이름, 라벨 | 이름 그대로 | `[ name, leech ]` (소환수에 붙인 이름, 그 소환수 머리 위) `[ stance, sunder ]` `[ head, {{label__head}} ]` |
| 드문 상태 | 한 단어 | `full` `over` `free` `blocked` `near` `slow` `clear` `deadly` `lethal` `refund` `charged` `extended` `moved` `worn` `back` `take` `skip` `dropped` `saving` `upgrade` `max` `absorbed` `crim` `restock` `resupply` |

상태 자리의 `target`은 방향 (내가 상대에게)에만 쓴다. "찍어라"는 `pick`이다.

## <a id="04"></a>04 글로서리

대상 단어.

| 뜻 | 단어 | 뜻 | 단어 | 뜻 | 단어 |
| --- | --- | --- | --- | --- | --- |
| hamstring | `hams` | telekinesis | `teleki` | paralyze | `para` |
| instrument | `inst` | explosion | `explo` | energy bolt | `eb` |
| discordance / provocation | `disco` / `provo` | peacemaking | `peace` | barding song | `song` |
| greater heal | `gheal` | mana drain / vampire | `drain` | meditation | `medi` |
| magic mushroom | `mush` | criminal | `crim` | veterinary | `vet` |
| herbal poultice | `herb` | herding | `herd` | invisibility | `invis` |
| chain lightning | `chain` | meteor swarm | `meteor` | teleport | `tp` |
| str / agi / resist 포션 | `str` `agi` `resist` | heal / cure 포션 | `heal pot` `cure pot` | refresh 포션 | `refresh` |
| explosion 포션 | `explo pot` | 달라붙은 폭발 포션 (나 또는 상대에게) | `bomb` | trapped pouch | `pouch` |
| smoke bomb | `smoke` | reagent satchel | `reg satchel` | alchemists satchel | `alch satchel` |
| identification wand | `id wand` | necromancy book | `necro book` | reactive armor | `reactive` |
| magic reflection | `reflect` | stamina | `stam` | script variable | `var` |
| 그 외 | 온전한 단어 |   |   |   |   |

`heal` `cure`는 주문 이름이라 포션은 `heal pot` `cure pot`으로 쓴다. 힘·민·레지 주문은 쓰지 않으니 포션도 `str` `agi` `resist` 그대로다.

## <a id="05"></a>05 hue 팔레트

색은 **뜻** 열이 정한다. 상태 단어 열은 그 뜻에 흔히 붙는 단어라서 같은 `on`이라도 나에게 걸린 `[ poison, on ]`은 234,
정보인 `[ medi, on ]`은 290이다. 색은 [Razor 색표](https://outlands.uorazorscripts.com/hues)에서 골랐고, 뜻이 다르면 색 계열도 다르게 했다.
따뜻한 색은 전투, 차가운 색은 정보, 초록은 준비와 해제다.

2026-10-07 사용자 요청으로 채도와 밝기를 한 단계 낮췄다. 색 값은 클라이언트 `hues.mul`에서 각 hue 색표의 맨 위 색 (index 31)을 읽었다.
옛 표의 값과 이 방식이 맞는 것도 확인했다. UO hue 표는 100 단위 띠마다 같은 색이 더 탁해지므로, 같은 색 계열을 +200 띠로 옮겨 채도 0.50\~0.67, 밝기 0.87\~0.90으로 맞췄다.

| 옛 hue | 새 hue | 옛 hue | 새 hue |
| --- | --- | --- | --- |
| 33 `#ee0031` | 234 `#de4a6a` | 9 `#6a31ee` | 209 `#734ade` |
| 43 `#ee6200` | 244 `#de834a` | 118 `#c510de` | 219 `#cd4ade` |
| 53 `#eeee00` | 254 `#dede4a` | 83 `#00eebd` | 284 `#4adebd` |
| 90 `#62e6f6` | 290 `#73d5e6` | 55 `#f6f662` | 255 `#e6e673` |
| 68 `#18ee00` | 269 `#5ade4a` | 123 `#de10b4` | 224 `#de4abd` |
| 65 `#9cf662` | 265 `#a4e673` | 705 `#9c9cbd` | 1288 `#ff0008` |

상대 머리 위 표시만은 반대로 갔다. 회보라 705가 잘 안 보인다는 사용자 보고로 선명한 빨강 1288로 바꿨다.
1288은 외부 출처 벌목·채광 스크립트가 이미 오버헤드에 쓰는 hue다. 내 머리 위 234와는 뜨는 자리와 채도가 달라 섞이지 않는다.

쿨다운 바의 hue (`cooldowns.xml`)는 이 팔레트와 따로이며 이번에 바꾸지 않았다.

| hue | 색 | 뜻 | 상태 단어 | 예 |
| --- | --- | --- | --- | --- |
| 234 | 진홍 `#de4a6a` | **나에게 걸린 것**, 지금 손써야 하는 것 | `me`, 나쁜 효과의 `on`, 바닥이 보이는 카운터 | `[ hams, me ]` `[ teleki, me ]` `[ poison, on ]` `[ throws, 0 ]` |
| 244 | 주황 `#de834a` | **내 공격·스킬이 먹힘** | `target` `area` | `[ disco, target ]` `[ fireball, target ]` `[ bleed, target ]` |
| 254 | 노랑 `#dede4a` | 경고. 실패, 막힘, 재고 없음, 버프 빠짐. 스크립트를 멈추게 하는 `out`도 여기에 든다 | `miss` `wrong` `out` `disturbed` `cut` `over` `blocked`, 버프의 `off` | `[ hams, miss ]` `[ heal pot, out ]` `[ reflect, off ]` `[ wait, 4m ]` |
| 290 | 하늘 `#73d5e6` | 정보, 카운터, 진행, 끝남. 스크립트에서는 `config__chatty`로 끈다 | `on` 숫자 `refund` `set` `done` | `[ unholy, 6/10 ]` `[ mana, refund ]` `[ lock, done ]` `[ var, set ]` |
| 269 | 초록 `#5ade4a` | 준비됨, 내 것 성공 | `ready` | `[ str, ready ]` `[ house, clear ]` `[ siphon, on ]` |
| 265 | 연두 `#a4e673` | 나쁜 것이 풀림 | 나쁜 효과의 `off` | `[ para, off ]` `[ poison, off ]` `[ hams, off ]` |
| 209 | 남보라 `#734ade` | 아군, 파티, 내 소환수 | `coming` 붙인 이름 | `[ heal, coming ]` `[ party, on ]` `[ name, leech ]` (소환수 머리 위) |
| 219 | 보라 `#cd4ade` | 네크로 주문이나 무기 능력 시전 (대상만) | — | `[ blood oath ]` `[ pummel ]` |
| 284 | 청록 `#4adebd` | 매저리 시전 (대상만). 지금 쓰는 줄은 없다. Drain / Curse는 프로필이 `[ drain, target ]` `[ curse, target ]`으로 띄운다 | — | `[ eb ]` |
| 255 | 연노랑 `#e6e673` | 프롬프트 | `pick` | `[ inst, pick ]` `[ shelf, pick ]` |
| 224 | 자홍 `#de4abd` | 월드 이벤트 | — | `[ world, saving ]` `[ boss, {7} ]` |
| 1288 | 빨강 `#ff0008` | **상대 머리 위 표시**. 스크립트가 `overhead "…" 1288 <serial>`로 그 대상 위에 띄운다 | `set` `on` | `[ target, set ]` `[ explo, on ]` |

::part[쿨다운 바]

## <a id="06"></a>06 쿨다운 바

### <a id="06.A"></a>06.A 규칙

짝 하나를 따라가면 이렇다. 같은 서버 문장이 `cooldowns.xml`에서는 바가 되고 프로필에서는 머리 위 한 줄이 된다. 둘은 같은 단어를 쓰고, 스크립트는 바를 그 이름 그대로 읽는다.

```mermaid
flowchart TD
  sentence("서버 문장<br>nomeehej has applied telekinesis to you.")
  sentence -- cooldowns.xml --> bar("쿨다운 바<br>teleki, me 30초") --> read("스크립트가 읽는다<br>cooldown teleki, me")
  sentence -- 프로필 --> line("머리 위 한 줄<br>[ teleki, me ] hue 234")
```

- 이름은 짝 오버헤드의 대상 단어를 소문자로 대괄호 없이 쓴다. 쉼표 뒤에는 방향 (`me` `target`)이나 상태 (`immune` `on`)만 붙인다
  (`hams, me` `teleki, target` `hams, immune` `frost, on`). 그 밖에는 쉼표 없이 대상만 쓴다 (`music` `heal pot`).
- 스크립트가 읽는 이름은 `cooldown "이름"`과 **정확히 일치**해야 한다. 바 이름을 바꿀 때는 `grep -rn 'cooldown "' script/`부터 한다.
- 트리거는 시스템 메시지 (`SysMessage`)나 머리 위 메시지 (`OverheadMessage`. 시전할 때 외치는 주문어, 스탠스 문구 등)다.
  스크립트가 `cooldown "corpse skin" 1000`처럼 직접 세우기도 한다.
- `cooldownbartype`이 `Regular`가 아닌 항목에는 트리거가 없다. `WeaponSwing` (`swing 1`\~`swing 4`, `weapon swing`),
  `Walk` (`walk`), `Bandage` (`bandage`), `PvP` (`pvp`), `Criminal` (`crim`)이다.
  `Criminal`과 `PvP`는 **클라이언트가 서버 타이머로 직접 채우는 특수 바**라 트리거를 달지 않는다 (Bapeths XML이 근거이고 인게임 확인은 10절).
  Heat of Battle은 `pvp` 바가 그 자리다.
- 항목 순서는 **바가 자주 뜨는 순서**다. 바드 바 다섯 개가 맨 앞이고 그 뒤가 매저리 프록 바다. 순서와 트리거 문장의 근거는
  [bard-necro.md](../templates/bard-necro.md#02.I) 02.I절.

### <a id="06.B"></a>06.B cooldown은 서버 값이 아니다

`cooldown "이름"`은 `cooldowns.xml`에 **직접 정의한 메시지 트리거 타이머**다. 서버 쿨이 아니라 **내가 설정한 값**을 알려 준다.
숫자가 이상하면 서버가 아니라 이 파일을 의심한다.

그래도 스크립트는 자체 `timer__` 대신 이것을 읽는다. 게임이 예고 없이 쿨을 초기화해도
(Lyric Aspect의 "Your barding skill cooldowns reset.") 리셋 문장에 트리거를 걸어 두면 바가 같이 0이 되기 때문이다.
예전에 `music`에 송 트리거가 섞여 서로 덮어쓰던 사고와 그 수정은 [bard-necro.md](../templates/bard-necro.md#02.I) 02.I절.

### <a id="06.C"></a>06.C 바 목록

`config/indian/classicuo/nomeehej/cooldowns.xml`의 항목을 파일 순서 그대로 적었다. 정본은 이 파일이다.
같은 `config/indian/`의 다른 캐릭터 다섯은 아직 이 규칙 전의 옛 22개 항목 (`mushroom` `CorpseSkin` `Heal Potion` …)을 쓴다.

`skill` `music` `disco` `peace/provo` `song` `magic arrow` `harm` `fireball` `lightning`
`mush` `heal pot` `steal` `hide` `stealth` `void mana` `void health` `swing 1` `swing 2`
`swing 3` `swing 4`
`medi` `pain spike` `necrosis` `hams, target` `hams, me` `hams, immune` `disarm, target` `noble sacrifice`
`holy light` `aspect` `poison strike` `corpse skin` `curse` `chain` `meteor` `mass curse`
`boarding` `sea combat` `repair` `spyglass` `cannons` `drain` `herd` `rope` `control points`
`teleki, target` `teleki, me` `para` `detonate` `reflect` `fish` `sp keg` `defensive` `sunder`
`cleave`
`wild swing` `shield bash` `warding` `testudo` `mirror` `bulwark` `arcane` `fowling` `incendiary`
`longshot` `maiming` `walk` `explo pot` `bandage` `pvp` `crim` `divine fury` `shrine`
`bomb, target`
`bomb, me` `siphon` `contested` `eject` `corpse creek` `vip` `flashpoint` `caravan` `idoc`
`dock` `smoke` `backstab` `reveal` `taunt` `fortify rations` `negate time` `rune` `summon`
`frost`
`frost, on` `weapon swing` `consecrate weapon` `pedestal` `bank note` `panacea` `shoot` `spam`
`crew heal` `quest` `omni pot` `ability`

| 바 | 메모 |
| --- | --- |
| `magic arrow` … `lightning`, `chain` `meteor` | 매저리 프록 15초. 발동 문장에 시작하고 "cast a wizardry … spell again"에 리셋한다. 앞의 넷은 [bard-necro.md](../templates/bard-necro.md#03.A) 03.A절 |
| `pain spike` `necrosis` `noble sacrifice` `holy light` `poison strike` `curse` `mass curse` `spyglass` `divine fury` `consecrate weapon` `spam` `crew heal` `quest` | 트리거가 없고 세우는 스크립트도 없다 |
| `corpse skin` `ability` | 트리거 없음. 스크립트가 직접 세운다 (archive의 backstab-mugging은 `cooldown "corpse skin" 1000`, bard-mace와 bard-throwing은 `cooldown "ability" cooldown__ability`) |
| `drain` | 트리거는 머리 위 메시지 "MV ON" 하나다. 지금 이 메시지를 띄우는 스크립트는 없다 |
| `teleki, target` `teleki, me` | 자기 TK뿐 아니라 적 TK 수신에도 둘 다 켜질 수 있다는 사용자 보고가 있다. 서로 독립적인 성공 증거가 아니므로 target 바만으로 내 공격 TK 적용을 확정하지 않는다 ([pvp.md](../game/pvp.md#04.D) 04.D절) |
| `reflect` | 설정상 "Magic reflect removed."면 30초 (몹), "Magic reflect removed (PvP)"면 60초 (플레이어) 바를 세운다. 실제 서버 제한과 시작 시점의 검증 범위는 [pvp.md](../game/pvp.md#05.A) 05.A절을 따른다. 자기 주문으로 없애면 "You remove your magic reflect spell."이 한 줄 더 오지만 트리거가 아니다 |
| `walk` | `Walk` 타입, 0.3초, 트리거 없음. 스크립트는 걷는 중이라는 신호로 읽고 시전을 미룬다 ([bard-necro.md](../templates/bard-necro.md#05.A) 05.A절의 행동 창 가드) |
| `pvp` `crim` | 특수 바 타입. 트리거 없음 (06.A) |
| `bomb, me` | 5초. "An explosion potion has stuck to you"로 시작한다 |
| `siphon` | 3600초. "Spell siphon active."로 시작하고 만료 문장에 리셋한다 |

::part[목록]

## <a id="07"></a>07 프로필 오버헤드 표

Razor 프로필 `summoner.xml`과 `default.xml`의 `<overheadmessages>`다. 정본은 프로필 xml이고, 항목을 바꾸면 이 표도 같이 고친다.
두 파일은 내용이 같다. 다만 `default.xml`에는 던지기 8줄 (`now planted`, `moving throws`, `wing your target`)이 없고 붕대 1줄이 더 있다.
2026-10-07부터 `default.xml`에는 벌목 3줄 (`Lumberjacking skillgain:`, `Your skill in Lumberjacking has increased`,
`You do not see any harvestable resources nearby`)도 없다.

프로필은 서버 문장을 아래 규칙으로 찾는다. "순서" 규칙 때문에 항목의 순서에도 뜻이 있다.

| 규칙 | 내용 |
| --- | --- |
| 검색 | 부분 문자열로 찾고 **대소문자를 가리지 않는다** (인게임 확인됨 2026-09-27, `Trapped pouches`가 "trapped pouches"에 걸렸다). 정규식이나 와일드카드는 없다 |
| 순서 | 한 문장에 항목 여러 개가 걸리면 **파일에서 앞의 것 하나만** 뜬다 (인게임 확인됨 2026-09-27, `[ wait, 4m 53s ]`가 `[ wait, 4s ]`를 눌렀다). 구체적인 검색어를 범용 검색어보다 **앞에** 둔다 |
| 기다림 | 기다리라는 문장은 `[ wait, … ]`로 띄운다. "wait another N" 꼴은 숫자 자리가 고정이라 `4m 17s` / `2m` / `59s`가 된다. 포션 대기 ("wait N" 꼴)는 분과 초가 섞인 형태와 초만 있는 형태를 가르지 못해 `1m 59s`를 만들 수 없다. 버프창이 이미 보여 주므로 **빈 메시지로 삼킨다** |

아래가 항목 전부이고 순서는 `summoner.xml`의 파일 순서다. `default.xml`에만 있는 붕대 줄은 그 파일에서의 자리에 넣었다.

| 서버 문장 (검색어) | 메시지 (hue) | 메모 |
| --- | --- | --- |
| : Attempting to heal you. | `[ heal, coming ] (209)` |   |
| You do not have a full suit of armor | `[ armor, out ] (254)` |   |
| Now tracking | `[ track, {3} {4} {5} ] (290)` |   |
| spaces to target | `[ track, {3} {4} {5} ] (290)` |   |
| You search the home and find no one hiding within. | `[ house, clear ] (269)` |   |
| script variable updated | `[ var, set ] (290)` |   |
| Your attack hamstrings your target | `[ hams, target ] (244)` |   |
| There's not enough wood here to harvest. | `[ wood, out ] (254)` |   |
| Harvest double yield/loot triggered | `[ harvest, double ] (269)` | default·summoner 공통. 추가 수확 발동 성공 |
| You chop some | `[ lumber, {4} ] (269)` | default·summoner 공통. 네 번째 단어를 표시한다. 일반 목재는 `logs`, 특수 목재는 `dullwood`·`shadowwood` 등 재질 이름이다. 수확 성공 색은 공통으로 68 |
| You hack at the tree for a while, but fail to produce any useable wood. | `[ lumber, miss ] (254)` | default·summoner 공통. 채집은 시도했으나 목재를 얻지 못함. 자원 고갈 안내와 구분 |
| Lumberjacking skillgain: | `[ lumber, {3} ] (290)` | default·summoner 공통. 세 번째 단어는 스킬 상승 확률이다. 실제 스킬 상승을 뜻하지 않음 |
| Your skill in Lumberjacking has increased | `[ lumber, gain ] (290)` | default·summoner 공통. 실제 스킬 상승 |
| You have recently traveled | `[ harvest, wait ] (254)` | default·summoner 공통. 여행 뒤 채집 거절 안내다. 대기 표시이며 별도 타이머를 시작하지 않는다 |
| You do not see any harvestable resources nearby | `[ harvest, out ] (254)` | default·summoner 공통. 주변 채집 자원 없음. 다음 채집 장소로 이동할 안내 |
| harvesting is not allowed | `[ harvest, blocked ] (254)` | default·summoner 공통. 채집 불가 안내 |
| you notice | `[ thief, me ] (234)` |   |
| you have already used the maximum | `[ field, out ] (254)` |   |
| You finish applying the bandages. | `[ bandage, done ] (290)` | `default.xml`에만 있다 |
| You have been poisoned! | `[ poison, on ] (234)` |   |
| You have been cured of all poisons. | `[ poison, off ] (265)` |   |
| You have been cured of all poisons! | `[ poison, off ] (265)` |   |
| You are already at full health. | `[ hits, full ] (290)` |   |
| You increase your damage resistance to creature-casted spells | `[ resist, on ] (290)` |   |
| You cannot move! | `[ para, on ] (234)` |   |
| You can move! | `[ para, off ] (265)` |   |
| before you may use another strength potion | 빈 메시지 | 버프창이 지속시간을 보여 주므로 띄우지 않는다. 지우면 뒤의 범용 `minutes `가 잡아 `[ wait, minutem secondss ]`가 뜨니 앞에서 **삼키려고** 남긴다 |
| before you may use another agility potion | 빈 메시지 | 위와 같다 |
| you are already at full stamina. | `[ stam, full ] (290)` |   |
| You are not poisoned. | `[ poison, off ] (265)` |   |
| You may now use a strength potion. | `[ str, ready ] (269)` |   |
| You may now use an agility potion. | `[ agi, ready ] (269)` |   |
| Looting this corpse will be a criminal act! | `[ loot, crim ] (254)` |   |
| Looting this monster corpse will be a criminal act! | `[ loot, crim ] (254)` |   |
| You carve materials from the corpse. | `[ carve, done ] (290)` | Forensic Evaluation 칼질 성공 (skinning-enhanced) |
| worth carving or investigating | `[ corpse, out ] (254)` | Smart Harvest가 깎을 시체를 못 찾음 |
| Criminal actions are not permitted | `[ crim, blocked ] (254)` | Sanctuary Dungeon의 소유권 없는 시체 칼질 거절. skinning-enhanced가 5분 동안 회색 시체만 깎는다 |
| That corpse has already been carved. | `[ corpse, carved ] (290)` | 이미 깎은 시체를 다시 찍음 (skinning-enhanced) |
| You have committed a criminal act! | `[ crim, on ] (234)` | 플레이어 시체 칼질 등. 뒤에 붙는 행동 이름은 무시한다 |
| You are now a criminal. | `[ crim, on ] (234)` |   |
| You have been reported for a murder! | `[ murder, +1 ] (234)` |   |
| You summon an ancient | `[ ancient, on ] (269)` |   |
| Your spellbook generates mana for your spell. | `[ mana, refund ] (290)` |   |
| You fail to ignite the campfire. | `[ camp, miss ] (254)` |   |
| Your campfire is now secure. | `[ camp, on ] (269)` |   |
| You feel it would take a few moments to secure your camp. | `[ camp, coming ] (290)` |   |
| You enter a meditative trance. | `[ medi, on ] (290)` |   |
| Your concentration is disturbed, thus ruining thy spell. | `[ cast, disturbed ] (254)` |   |
| Being perfectly rested, you shove something invisible out of the way. | `[ hidden, near ] (254)` |   |
| You may now attempt to | `[ hams, ready ] (269)` |   |
| You refrain from making hamstring attempts. | `[ hams mode, off ] (290)` |   |
| You will now attempt to hamstring your opponents. | `[ hams mode, on ] (290)` |   |
| You fail to hamstring your opponent. | `[ hams, miss ] (254)` |   |
| Their attack hamstrings you! | `[ hams, me ] (234)` |   |
| You are no longer hamstrung | `[ hams, off ] (265)` |   |
| You will now attempt to disarm your opponents. | `[ disarm mode, on ] (290)` |   |
| You refrain from making disarm attempts. | `[ disarm mode, off ] (290)` |   |
| Your strike disarms your target! | `[ disarm, target ] (244)` |   |
| You fail to disarm your opponent. | `[ disarm, miss ] (254)` |   |
| Their attack disarms you! | `[ disarm, me ] (234)` |   |
| Where do you wish to traverse to? | `[ rope, pick ] (255)` |   |
| That location is blocked. | `[ spot, blocked ] (254)` |   |
| Target cannot be seen. | `[ range, out ] (254)` |   |
| You are now under the protection of the town guards. | `[ guard, on ] (290)` |   |
| You have left the protection of the town guards. | `[ guard, off ] (254)` |   |
| Someone tried to steal from you. | `[ thief, me ] (234)` |   |
| You have been revealed! | `[ reveal, me ] (234)` |   |
| You have been banned from this house. | `[ ban, me ] (254)` |   |
| You have been ejected from this house! | `[ eject, me ] (254)` |   |
| You have been added to the party. | `[ party, on ] (209)` |   |
| You have been removed from the party. | `[ party, off ] (209)` |   |
| You feel ready to continue stealthing | `[ stealth, ready ] (269)` |   |
| You feel comfortable enough to begin stealthing | `[ stealth, ready ] (269)` |   |
| You have 5 stealth steps remaining | `[ stealth, 5 ] (290)` |   |
| You have successfully cleared it of traps | `[ trap, done ] (290)` |   |
| You successfully pick the lock | `[ lock, done ] (290)` |   |
| You fail to make any progress on the lock | `[ lock, miss ] (254)` |   |
| You fail to make any progress towards removing traps | `[ trap, miss ] (254)` |   |
| You finish using veterinary supplies | `[ vet, done ] (290)` |   |
| You begin using veterinary supplies | `[ vet, on ] (290)` |   |
| What do you wish to focus your follower's aggression towards? | `[ herd, pick ] (255)` |   |
| you extend the life of your creature | `[ summon, extended ] (290)` |   |
| you are now under the effect of herbal poultice | `[ herb, on ] (290)` |   |
| Your herbal poultice has lost its effectiveness. | `[ herb, off ] (254)` |   |
| That spell is already currently in effect. | `[ buff, on ] (290)` |   |
| already at full repair | `[ repair, done ] (290)` |   |
| You may now use another magic mushroom | `[ mush, ready ] (269)` |   |
| before you may consume another magic mushroom | `[ mush, {5} ] (290)` |   |
| One of more of your ship crewmembers | `[ crew, ready ] (269)` |   |
| Criminal healing will now be allowed | `[ crim heal, on ] (290)` |   |
| Criminal healing will now be prevented | `[ crim heal, off ] (290)` |   |
| Criminal looting will now be allowed | `[ crim loot, on ] (290)` |   |
| Criminal looting will now be prevented | `[ crim loot, off ] (290)` |   |
| Your lightning spell hinders your target | `[ lightning, target ] (244)` | 라이트닝 프록 |
| Your attack cripples your target, lowering their defense | `[ cripple, target ] (244)` |   |
| You smash through | `[ smash, target ] (244)` |   |
| susceptible to special | `[ bleed, target ] (244)` |   |
| armslore skillgain | `[ swing ] (290)` |   |
| attack causes your target to bleed | `[ bleed, target ] (244)` |   |
| minutes before / minute before | `[ wait, {5}m ] (254)` | "…wait another 2 minutes before…"처럼 초가 없는 형태. 초가 있는 형태보다 앞에 둔다 |
| minutes / minute (뒤 공백) | `[ wait, {5}m {7}s ] (254)` | "You must wait another 4 minutes 17 seconds …" |
| must wait another | `[ wait, {5}s ] (254)` |   |
| 0 Trapped pouches remain | `[ pouch, out ] (254)` |   |
| No trapped pouches found | `[ pouch, out ] (254)` |   |
| restricted from performing aggressive | `[ restrict, {14} ] (234)` |   |
| world will save | `[ world, coming ] (224)` |   |
| world is saving | `[ world, saving ] (224)` |   |
| save complete | `[ world, done ] (224)` |   |
| aspect and other bonuses return | `[ aspect, on ] (269)` |   |
| free cure potion | `[ cure pot, free ] (290)` |   |
| too fatiqued | `[ weight, over ] (254)` |   |
| too fatigued | `[ weight, over ] (254)` |   |
| are overloaded | `[ weight, over ] (254)` |   |
| contested boss has spawned | `[ boss, {7} ] (224)` |   |
| control points earned for current beacon | `[ beacon, +{2} {12} ] (290)` |   |
| kill points earned | `[ kill, +{2} {9} ] (290)` |   |
| DF A Dungeon Flashpoint will begin in 15 minutes. | `[ flashpoint, coming ] (224)` |   |
| cured the target of all poisons | `[ cure, target ] (269)` |   |
| cast a wizardry magic arrow spell again | `[ magic arrow, ready ] (269)` | 검색어를 준비 문장으로 좁혔다. "activated"는 아래 줄 |
| cast a wizardry harm spell again | `[ harm, ready ] (269)` |   |
| cast a wizardry fireball spell again | `[ fireball, ready ] (269)` |   |
| cast a wizardry lightning spell again | `[ lightning, ready ] (269)` |   |
| cast a wizardry chain lightning spell again | `[ chain, ready ] (269)` |   |
| cast a wizardry meteor swarm spell again | `[ meteor, ready ] (269)` |   |
| magic arrow / harm / fireball / chain lightning / meteor swarm activated | `[ 주문, target ] (244)` | 프록이 터졌다. 15초 바가 시작된다 (06.C) |
| upgraded to Deadly | `[ poison, deadly ] (244)` |   |
| upgraded to Lethal | `[ poison, lethal ] (244)` |   |
| Triggered (Epic) | `[ aspect, on ] (269)` |   |
| enough experience to upgrade | `[ aspect, upgrade ] (290)` |   |
| Society Job Progress | `[ society, {4} ] (290)` |   |
| You have completed a society job | `[ society, done ] (290)` |   |
| aspect experience | `[ {4}, {7} ] (290)` |   |
| resist a bleed | `[ bleed, off ] (265)` |   |
| resist a disease effect | `[ disease, off ] (265)` |   |
| been struck by an ancient blight | `[ disease, on ] (234)` |   |
| may now review results | `[ boss, done ] (290)` |   |
| struck by an evil omen | `[ omen, target ] (244)` |   |
| enough unholy | `[ unholy, out ] (254)` |   |
| unholy symbols remaining | `[ unholy, {4} ] (290)` |   |
| max unholy | `[ unholy, max ] (269)` | 원문은 "Max unholy symbols earned (10/10)". `{5}`는 괄호째 뜨므로 쓰지 않는다 |
| consume a magic mushroom | `[ mush, on ] (290)` | 원문은 "You consume a magic mushroom and restore some mana." 범용 `You consume`보다 앞에 둔다. 뒤에 두면 `[ essence, +a ]`가 뜬다 |
| mana from your mana well | `[ eldritch, +{3} ] (290)` | 원문은 "You draw 11 mana from your mana well." Eldritch 아스펙트 |
| You consume | `[ essence, +{3} ] (290)` |   |
| generates mana | `[ mana, refund ] (290)` |   |
| progress on the lock | `[ lock, {8} ] (290)` |   |
| clearing it of traps | `[ trap, {10} ] (290)` |   |
| thrown at that player within 30 | `[ teleki, target ] (244)` | 자기·수신 TK와 혼동 가능. 공격 대상 성공 인증이 아님 ([pvp.md](../game/pvp.md#04.D) 04.D절) |
| has applied telekinesis to you | `[ teleki, me ] (234)` | 원문은 "nomeehej has applied telekinesis to you." 건 사람 이름은 저널에 남는다 |
| An explosion potion has stuck to you | `[ bomb, me ] (234)` | 5초 표시의 바 `bomb, me`와 짝. 실제 점화부터의 퓨즈 측정과는 구분 ([open-items.md](../questions/open-items.md#08.C) 08.C절) |
| Your explosion potion sticks to your target | `[ bomb, target ] (244)` |   |
| free hand to drink | `[ hands, full ] (254)` |   |
| You drink a healing potion | `[ heal pot, on ] (290)` | 스크립트의 같은 줄은 뺐다 |
| You drink a cure potion | `[ cure pot, on ] (290)` | 스크립트의 같은 줄은 뺐다. 리프레시는 서버가 문장을 보내지 않아 없다. 힘·민 포션은 "Your strength has changed by 20"뿐인데 Weaken을 맞아도 같은 문장이라 잡지 않는다 |
| You will now automatically | `[ scroll mode, on ] (290)` |   |
| You may only cast that spell on a player once every 30 seconds. | `[ limit, 30s ] (254)` |   |
| Your boarding party fails to board the ship | `[ boarding, miss ] (254)` |   |
| That ship is too far away to board. | `[ range, out ] (254)` |   |
| Your shot hinders your target! | `[ hinder, target ] (244)` |   |
| You deactivate your stance. | `[ stance, off ] (254)` |   |
| You smash the unprotected | `[ smash, target ] (244)` |   |
| fallen to corruption | `[ shrine, on ] (224)` |   |
| You begin to move quietly | `[ stealth, on ] (290)` |   |
| You have 4 stealth | `[ stealth, 4 ] (254)` |   |
| You have 3 stealth | `[ stealth, 3 ] (254)` |   |
| You have 2 stealth | `[ stealth, 2 ] (254)` |   |
| You have 1 stealth | `[ stealth, 1 ] (234)` |   |
| You have 0 stealth | `[ stealth, 0 ] (234)` |   |
| You must hide first | `[ hide, off ] (254)` |   |
| Those cannons are out of ammunition | `[ cannon, out ] (254)` |   |
| You fail to steal | `[ steal, miss ] (254)` |   |
| You fail in your stealing attempt | `[ steal, miss ] (254)` |   |
| You steal | `[ steal, done ] (290)` |   |
| You successfully steal | `[ steal, done ] (290)` |   |
| You have already stolen from this creature | `[ steal, wrong ] (254)` |   |
| You may now taunt again. | `[ taunt, ready ] (269)` |   |
| Potion codex Panaccea upgrade is now ready. | `[ panacea, ready ] (269)` |   |
| Your ability to hide is no longer impeded | `[ hide, ready ] (269)` |   |
| Weapon ability ready | `[ ability, ready ] (269)` |   |
| your rapid | `[ move, slow ] (254)` |   |
| your movements attract | `[ move, slow ] (254)` |   |
| your quick movements draw the attention | `[ move, slow ] (254)` |   |
| iron flesh charges remaining | `[ iron flesh, {1} ] (290)` |   |
| You detonate a ground trap | `[ detonate, done ] (290)` |   |
| You may now detonate another trap | `[ detonate, ready ] (269)` |   |
| You increase your \[EventScore | `[ event, +{6} ] (290)` |   |
| You are now under the effect of a Song | `[ song, on ] (290)` |   |
| You fail to discord | `[ disco, miss ] (254)` |   |
| fail to pacify any nearby creatures | `[ peace, area miss ] (254)` |   |
| fail to pacify your opponent | `[ peace, miss ] (254)` |   |
| disrupting your opponent | `[ disco, target ] (244)` |   |
| briefly discording | `[ disco, area ] (244)` | 자기를 찍으면 8타일 광역, 각 5초 |
| pacifying your target | `[ peace, target ] (244)` |   |
| briefly pacifying | `[ peace, area ] (244)` | 자기를 찍으면 8타일 광역, 각 2초 |
| play successfully, provoking | `[ provo, target ] (244)` | 프로보는 광역이 없다. 자기를 찍으면 송이다 |
| fail to incite anger | `[ provo, miss ] (254)` |   |
| Song of Discordance / Peacemaking / Provocation effect ends | `[ disco song / peace song / provo song, off ] (254)` | 15분 송이 끝났다. 범용 `You play successfully`는 뺐다 |
| additional energy | `[ spell, charged ] (244)` |   |
| What instrument shall you play | `[ inst, out ] (254)` |   |
| now planted | `[ planted, on ] (290)` |   |
| 5 moving throws | `[ throws, 5 ] (290)` |   |
| 4 moving throws | `[ throws, 4 ] (290)` |   |
| 3 moving throws | `[ throws, 3 ] (290)` |   |
| 2 moving throws | `[ throws, 2 ] (290)` |   |
| 1 moving throws | `[ throws, 1 ] (234)` |   |
| 0 moving throws | `[ throws, 0 ] (234)` |   |
| wing your target | `[ wing, target ] (244)` |   |
| Magic reflect removed | `[ reflect, off ] (254)` | 바 `reflect`와 짝 (06.C) |
| Spell siphon active. | `[ siphon, on ] (269)` | 5분마다 첫 주문 피격에 켜지는 60분 PvM 버프. 바 `siphon`과 짝 |
| Your spell siphon bonus has expired | `[ siphon, off ] (254)` |   |
| You absorb their spell. | `[ spell, absorbed ] (269)` | Resist의 `25% x Resist/100` 확률, 피해 -75% |
| You mana drain your target. / You curse your target. | `[ drain, target ]` / `[ curse, target ] (244)` | 스크립트의 `[ drain ]` `[ curse ]` 시전 알림은 뺐다 |
| Your reactive armor spell has been nullified. | `[ reactive, off ] (254)` | 25를 흡수하고 빠진다. 다음에 서 있을 때 다시 건다 |
| You generate mana for your spell. | `[ mana, refund ] (290)` | 기존 `generates mana`는 이 문장을 못 잡았다 |
| recovered from energy bolt kill | `[ eb, refund ] (290)` | 회수량은 티어마다 달라 숫자는 띄우지 않는다 ([bard-necro.md](../templates/bard-necro.md#03.A) 03.A절) |
| That is too far away. | `[ range, out ] (254)` |   |

## <a id="08"></a>08 스크립트 오버헤드

규칙은 01\~05절 그대로다. 색은 05절 표에서 뜻으로 고르고, 누구 머리 위에 띄울지는 01.C절을 따른다.

지금 스크립트가 띄우는 줄은 `grep -rn 'overhead "\[' script/`로 본다. 목록이나 요약표를 여기에 옮겨 적지 않는다 (옮겨 둔 표는 hue 번호를 바꿀 때 따라오지 않아 틀렸다).

::part[기록]

## <a id="09"></a>09 구멍

서버 문장을 저널에서 잡아야 붙일 수 있는 것이다. 잡히면 바와 오버헤드를 짝으로 넣고 이 줄을 지운다.

| 상황 | 필요한 것 | 붙일 곳 |
| --- | --- | --- |
| 디스암당함 | 문장 "Their attack disarms you!"는 있다. **재장착까지 몇 초**인지가 필요하다 | 바 `disarm, me` |
| Mana Drain / Vampire 맞음 | 문장 | `[ drain, me ]` (레지 -10 / -20, 2분) |
| Curse / Weaken / Clumsy 맞음 | 문장 | `[ curse, me ]` 등 |
| Cure 포션 마심 | 문장 "You drink a cure potion"은 있고 바만 없다 | 바 `cure pot` |
| Refresh 포션 마심 | 서버가 문장을 안 보낸다. 지금으로는 방법이 없다 | 바 `refresh` |
| `sp keg` | 무엇의 줄임인지 모른다 (트리거는 머리 위 메시지 "spkeg") | 이름 |

## <a id="10"></a>10 확인 안 된 것

- PvP에서 `paralyzed`가 "You are frozen and cannot move." 상태를 잡는지, 파우치가 나가는지
- `message=""`인 항목이 정말 아무것도 안 띄우는지, Razor가 종료할 때 그 항목을 지우지 않는지 (힘·민 포션 대기). 빈 줄이 뜨거나 항목이 사라지면 다른 방법을 찾는다
- `hams, me` 두 문장 중 실제로 오는 쪽 ("You have been hamstrung" / "Their attack hamstrings you!")
- `heal pot` 트리거 "You drink a healing potion"이 실제 문장인지. 스크립트의 `cooldown "heal pot"`과 겹쳐도 같은 시각에 다시 시작할 뿐이다
- 범죄자가 될 때 `crim` 바가 트리거 없이 저절로 뜨는지 (특수 바 타입)
- Heat of Battle이 켜질 때 `pvp` 바가 트리거 없이 저절로 뜨는지 (같은 특수 바 타입)

## <a id="11"></a>11 참고 링크

- [Hamstring](https://wiki.uooutlands.com/Hamstring) -- 3초 스태미나 0, 재적용 불가 30초, 시전자 쿨 30\~53초
- [Magery](https://wiki.uooutlands.com/Magery) -- Telekinesis 끈끈이 PvP 30초, Paralyze PvP 10초, Teleport PvP 쿨 15초
- [Alchemy](https://wiki.uooutlands.com/Alchemy) -- Sticky Potions
- [Bapeths Total Cooldown XML](https://outlands.uorazorscripts.com/script/2138a7dc-785e-4d49-a465-e7c922d533ac) -- 커뮤니티 트리거 문장, Criminal / PvP 바에 트리거가 없는 근거
- [overheadmessages 스니펫](https://outlands.uorazorscripts.com/script/8b4e1a67-5eb7-4933-8a07-a1ad1c797cc2)
