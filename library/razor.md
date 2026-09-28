# Outlands Razor 문법

이 저장소 스크립트가 쓰는 언어의 정본. 되는 구문, 안 되는 구문, 명령문 비용, PvP 에서 막히는 것.
문법이 애매하면 추측하지 말고 [위키 Razor Scripting](https://wiki.uooutlands.com/Razor_Scripting) 을 읽고, 알게 된 것을 여기에 더한다.

- 스크립트를 **어떻게 쓰는가** (헤더, 변수 접두, 타이머 관용구)는 [conventions.md](conventions.md).
- 고친 스크립트를 **게임에 반영하고 확인하는 법** (캐시, 리로드)은 [workflow.md](workflow.md) 4절.

## 목차

1. [이 포크](#1-이-포크)
2. [확장 문법](#2-확장-문법)
3. [확인된 함정](#3-확인된-함정)
4. [되는 구문과 선례](#4-되는-구문과-선례)
5. [안 되는 구문의 근거](#5-안-되는-구문의-근거)
6. [명령문 비용](#6-명령문-비용)
7. [PvP 제약](#7-pvp-제약)

---

## 1. 이 포크

Outlands 클라이언트에 딸린 Razor 는 [Razor CE](https://www.razorce.com/guide/) 의 포크이고 CE 에 없는 명령이 많다.
근거는 위키 Razor Scripting 이 1순위, CE 가이드는 기본 문법 확인용이다. 공개 스크립트는
[outlands.uorazorscripts.com](https://outlands.uorazorscripts.com/) 에 있다.

## 2. 확장 문법

Razor CE 에 없거나 확장된 것. 존재 여부만 적어 두니 인자 형식은 위키에서 확인한다.

| 분류   | 무엇                                                                                                                                                                                                                                       |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 검색   | `findtype` `dclicktype` `findtypelist` `targettype` `lifttype` 에 `source` `hue` `quantity` `range` 인자                                                                                                                                   |
| alias  | `ground`                                                                                                                                                                                                                                   |
| 표현식 | `find` `findlayer` `targetexists` `followers` `hue` `name` `paralyzed` `invul` `warmode` `noto` `dead` `maxweight` `diffweight` `diffhits` `diffmana` `diffstam` `counttype` `gumpexists` `ingump` `varexist` `bandaging` `cooldown` `pvp` |
| 명령   | `setvar` `unsetvar` `ignore` `unignore` `clearignore` `warmode` `getlabel` `rename` `skill` `setskill` `waitforgump` `gumpresponse` `gumpclose` `cooldown`                                                                                 |
| 연산자 | `as` `in`                                                                                                                                                                                                                                  |
| 리스트 | `createlist` `clearlist` `removelist` `pushlist` `poplist` `listexists` `list` `inlist` `atlist` `foreach`                                                                                                                                 |
| 타이머 | `createtimer` `removetimer` `settimer` `timer` `timerexists`                                                                                                                                                                               |
| 기타   | 모든 루프에 `index` 내장. `overhead` / `sysmsg` 에 `{{var}}` 보간                                                                                                                                                                          |

## 3. 확인된 함정

전부 인게임에서 실제로 깨졌거나 프로브로 잰 것 (2026-09-28). `.razor` 를 고치기 전에 이 표를 읽는다. 근거는 5절, 비용 숫자는 6절.

| 함정                                                      | 증상                                                                                                     | 대신                                                                                                                     |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 주석 안의 `;`                                             | 그 뒤를 명령으로 파싱해서 그 줄에서 에러                                                                 | 마침표로 문장을 끊는다                                                                                                   |
| 변수끼리, 변수와 숫자의 크기 비교 (`if var__a >= var__b`) | 조용히 거짓. 네크로가 한 번도 안 나갔다                                                                  | 변수는 `=` `!=` 만. 세려면 리스트에 넣고 `list 'x' >= n`. `mana >= config__x` 처럼 **내장 식이 왼쪽**이면 된다           |
| 산술 (`@setvar! var__n var__n + 1`)                       | 선례 없음, 안 받는다고 본다                                                                              | `counttype` 으로 다시 읽거나 리스트 길이                                                                                 |
| `as` alias 를 묶은 `if` / `while` 블록 밖에서 읽기        | `4294967295`, `noto` 가 `Mobile … not found`                                                             | 블록 안에서 `@setvar! var__x alias__x` 로 복사해 나온다                                                                  |
| 단어를 변수에 담기                                        | `4294967295` (따옴표 무관). `rename` 에 주면 `That name is unacceptable.`                                | `pushlist` 항목은 글자를 유지한다. `foreach x in list__y` 로 꺼내 문자열 인자에 준다. 그 밖의 문자열은 `getlabel` 결과뿐 |
| `for <변수>`                                              | `Invalid for loop syntax`                                                                                | 값별 리터럴 `for N` 사슬                                                                                                 |
| `not list 'x' >= var`                                     | 파싱 에러 (`syntax error in line N`, 실행 자체가 안 됨)                                                  | `not` 뒤에 `list` 비교식을 두지 않는다. 갈래 안에서 `=` 로 비교                                                          |
| `sysmessage`                                              | `Unknown command`                                                                                        | `sysmsg`                                                                                                                 |
| `findtypelist` 를 명령으로                                | `Unknown command`                                                                                        | 안 쓴다 (표현식일 것, 미확인)                                                                                            |
| `findtype` 한 번으로 여러 모빌 중 하나 고르기             | 부를 때마다 **같은 모빌**이 온다                                                                         | `while findtype … as` → 검사 → 아니면 `@ignore` → `endwhile` → `@clearignore`                                            |
| 숫자(serial)를 펫 이름으로                                | `That name is unacceptable.`                                                                             | 글자 이름만                                                                                                              |
| 매 패스 `findtype` 로 상태 세기                           | 한 줄 5~10ms, 거짓 `if` 10~20ms, `findtype` 20~40ms. 32번이면 패스당 1초                                 | 천천히 변하는 상태는 타이머로 몇 초에 한 번. `if`/`elseif` 사슬은 통째로 한 틱이라 길어도 싸다                           |
| 모빌을 이름으로 찾기                                      | 되긴 하지만 이름을 바꾼 뒤 Razor 캐시가 갱신되는지 모른다                                                | 바디 번호. 인게임 `>info` 로 읽는다. 내 소환수의 noto 는 2 (friend)                                                      |
| `varexist` 로 값의 유효성 확인                            | 선언 여부만 본다. 잘못 타겟한 값도 참이라 영영 안 고쳐진다                                               | 대상 앞에 서 있는 게 확실한 곳에서만 `find` 로 확인 ([conventions.md](conventions.md) 3.4절)                             |
| 미선언 변수                                               | 빈 값으로 읽혀 조건이 조용히 안 맞는다                                                                   | `util/check.sh` 가 접두 붙은 변수는 잡는다. 접두 없는 이름은 못 잡는다                                                   |
| `for 25` + `wait 100` 로 커서 폴링                        | 4서클 커서가 루프가 끝난 뒤에 떴다 (2026-09-29). 남은 커서가 `not targetexists` 를 단 블록을 전부 막는다 | `for 60`. 한 바퀴가 `wait` 값보다 한참 짧게 도는 것으로 보인다. 원인은 확인되지 않았다                                   |

## 4. 되는 구문과 선례

전부 저장소에 선례가 있다. 새 패턴을 쓰기 전에 여기서 먼저 찾는다.

| 구문                                                                                                 | 선례                                                                                                      |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `not inlist '이름' alias`                                                                            | `bard-necro-enhanced.razor` OPENER                                                                        |
| `list__magic_drained_targets` + `list__magic_cursed_targets` 2단 오프닝                              | `bard-necro-enhanced.razor` OPENER                                                                        |
| `createlist` / `removelist` / `clearlist` / `pushlist`                                               | 여러 파일                                                                                                 |
| `while findtype ... backpack as` + `@ignore`                                                         | `bard-necro-enhanced.razor` INSTRUMENT                                                                    |
| `not dead X and noto X != "hostile" ...`                                                             | `bard-necro-enhanced.razor` COMBAT TARGET CACHE                                                           |
| `findbuff "song of discordance"`                                                                     | `bard-mace.razor:494`                                                                                     |
| `useskill` -> `waitfortarget` -> `target backpack`                                                   | `bard-mace.razor:518`                                                                                     |
| `stop`                                                                                               | `bard-necro-enhanced.razor` INSTRUMENT                                                                    |
| `cooldown "magic arrow" = 0`                                                                         | `cooldowns.xml` 에 항목 존재                                                                              |
| `for 60` + `break` 로 커서 폴링                                                                      | `bard-necro-enhanced.razor` PROC CORE, 레퍼런스 `auto-mage.razor:1160`                                    |
| `hotkey 'Vampiric Embrace'` + `hotkey 'Target Self'`                                                 | 위키: 자신을 타겟하면 주변 시체를 자동 탐색. **인게임 확인됨**                                            |
| `hotkey 'Drink Heal'` 등 포션 핫키                                                                   | Razor 핫키 목록 Potions 항목. 이름 그대로                                                                 |
| `hotkey "> Interrupt"`                                                                               | 휠다운에 물려 쓰던 것. 시전 폴링 안에서 긴급 힐용                                                         |
| `findtype 24\|158\|… ground -1 -1 <range> as` -- 바디 번호로 모빌 찾기                               | `bard-necro-enhanced.razor` SUMMON NAMES, 구식 `bard-necro` PROVO FOLLOWER CACHE                          |
| `@rename <alias> <var>`                                                                              | `bard-necro-enhanced.razor` SUMMON NAMES. 위키 `rename`, CE 는 `CanRename` 인 펫에만 보낸다               |
| `find <var> ground -1 -1 <range> as` + `dead` 로 슬롯 비우기                                         | `bard-necro-enhanced.razor` SUMMON NAMES, 구식 `bard-necro` PROVO FOLLOWER CACHE                          |
| `pushlist '리스트' '단어'` + `foreach x in 리스트` + `index = <변수>` -- 단어를 문자열 인자로 넘기기 | `bard-necro-enhanced.razor` SUMMON NAMES. 2026-09-28 프로브: 항목이 글자 그대로 읽히고 `rename` 이 받는다 |
| `ingump "10/"` … `"1/"` 큰 수부터 내려오는 사슬로 숫자 읽기                                          | `bard-necro-enhanced.razor` 심볼 수. `ingump` 는 부분 문자열 매칭이라 큰 수부터 본다                      |

## 5. 안 되는 구문의 근거

3절 표의 줄마다 무엇이 어떻게 깨졌는지. 선례가 없는 것도 같이 적는다.

- **변수끼리, 또는 변수와 숫자의 크기 비교** (`var__symbols >= config__symbols_blood_oath`). 조건에서 변수는 `=` 만 된다.
  Bard Necro 의 네크로가 한 번도 안 나가던 원인. 수를 세려면 옛 스크립트처럼 **리스트에 항목을 밀어 넣고 `list 'name' >= n`** 으로 비교한다.
  `mana >= config__x` 처럼 **내장 식이 왼쪽**이면 된다. 내장 `index` 도 왼쪽이면 변수와 비교된다.
- **`as` alias 를 묶은 블록 밖에서 읽기.** `if findtype … as alias__x` / `endif` 뒤에서 `alias__x` 를 읽으면
  `4294967295` 가 되어 `noto` 가 `Mobile … not found` 를 낸다. 안에서 `@setvar! var__x alias__x` 로 복사해 나온다.
  `bard-necro-enhanced.razor` 의 alias 가 전부 블록 안에서만 쓰이는 이유다.
- **`findtypelist` 를 명령으로 쓰기.** `Unknown command`. 쓴다면 `findtype` 처럼 `if` 안의 표현식일 것이다 (미확인).
- **단어를 변수에 담기.** `@setvar! var__x nomeeheh` 는 따옴표가 있든 없든 `4294967295` 로 읽힌다 (2026-09-28 프로브.
  숫자 `5000` 은 `5000`, `0x622396` 은 10진수 `6431638`). 변수는 숫자와 serial 전용이다. 그래서 `rename <serial> <변수>` 는
  서버에 쓰레기 이름이 가서 `That name is unacceptable.` 이 된다. 단어는 리스트에 담아 `foreach` 로 꺼낸다. serial 쪽은 변수여도 된다.
- **숫자를 펫 이름으로.** serial 을 그대로 이름으로 주면 `That name is unacceptable.` (2026-09-28 프로브). 이름에 숫자는 안 된다.
- **`for <변수>`.** `Invalid for loop syntax` (2026-09-28 프로브). 횟수는 리터럴만. 변수 횟수가 필요하면 값별 `for N` 사슬.
- **`while not list 'x' >= var`.** `syntax error` 로 파싱 자체가 안 된다 (2026-09-28). `not` 뒤에 `list` 비교식을 두지 않는다.
- **`findtype` 은 매번 같은 모빌을 돌려준다.** Razor CE 의 무작위가 아니다. 한 번만 부르면 이미 처리한 모빌만 계속 나온다
  (2026-09-28, 둘째 소환수에 이름이 안 붙었다). `while findtype … as` → 검사 → `@ignore` → `endwhile` → `@clearignore` 로 한 번에 다 본다.
- 선례가 없어서 쓰지 않는 것:
  - 산술 `@setvar! var__n var__n + 1`
  - `while <스크립트 변수> <`
  - `menu <serial> <변수>` -- 인덱스는 반드시 리터럴
  - 조건 안의 괄호

## 6. 명령문 비용

2026-09-28 측정. Razor CE 원본은 스크립트 엔진이 **타이머 틱마다 명령문 하나**를 실행한다 (`ScriptManager.ScriptTimer` → `Interpreter.ExecuteScript` → `ExecuteNext` 1회, 기본 25ms). 거짓인 `if` 는 본문을 건너뛰는 것까지 한 틱, `elseif` 사슬은 한 틱 안에서
평가된다.
이 포크는 그보다 빠르지만 같은 모양이다. 프로브 (`probe-tick`, 지움)로 잰 값:

| 잰 것                             | 걸린 시간    | 한 개당             |
|-----------------------------------|--------------|---------------------|
| 대입 100줄                        | 0.5 ~ 1초    | 5 ~ 10ms            |
| 거짓 `if` 100개 (3줄 본문 건너뜀) | 1 ~ 2초      | 10 ~ 20ms           |
| `findtype … self` 50번            | 1 ~ 2초      | **20 ~ 40ms**       |
| 20갈래 `elseif` 사슬 10번         | 0.25 ~ 0.5초 | 사슬 하나 25 ~ 50ms |

**비용은 검색 종류가 아니라 "이 패스에서 밟는 줄 수"이고, 그중 `findtype` 이 가장 비싸다.**

원칙: **자주 안 변하는 상태는 타이머로 게이트하고, 흔한 경로가 밟는 줄을 줄인다.**
Bard Necro 루프에 적용한 결과 (시약 플래그를 매 패스 `findtype` 32번 → 30초에 7번)는 [bard-necro-handbook.md](bard-necro-handbook.md) 5.8절.

## 7. PvP 제약

구조화 PvP 또는 Faction 상태에서:

| 막히는 것                                                         | 영향                                                                      |
|-------------------------------------------------------------------|---------------------------------------------------------------------------|
| `settimer` `removetimer` `getlabel` `rename` `cooldown` `wait` 등 | 타이머·라벨·쿨다운에 기대는 로직이 안 돈다                                |
| 플레이어 serial 이 `0x0`                                          | 상대를 변수에 담을 수 없고, 상대 머리 위 `overhead … <serial>` 도 안 된다 |
| `find` 계열이 자기 아이템만 잡는다                                | 상대나 바닥 물건을 찾는 로직이 안 돈다                                    |

- PvP 겸용 스크립트를 쓰는 규칙은 [conventions.md](conventions.md) 7절. 게임 쪽 PvP 규칙과 숫자는 [pvp.md](pvp.md).
