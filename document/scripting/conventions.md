---
name: Conventions
label: 저장소와 스크립트 규칙
group: Scripting
order: 10
---

파일을 어디에 두고 어떻게 이름 짓는가, 스크립트를 어떤 모양으로 쓰는가.
문법 자체 (되는 구문, 함정)는 [razor.md](razor.md), 머리 위 메시지는 [overheads.md](overheads.md).

## <a id="00"></a>00 한눈에

| 절 | 무엇을 답하나 |
| --- | --- |
| [01](#01) | 어느 폴더에 두고 파일 이름을 어떻게 짓나. `config/`는 누구 것인가 |
| [02](#02) | 스크립트를 어떤 순서와 모양으로 쓰나. 헤더, 시작 4줄, 섹션과 블록 배너, 주석, 편집기 하이라이팅 |
| [03](#03) | 변수 접두는 무엇이고 세션 값과 영속 값은 어떻게 가르나. serial은 왜 쓰지 않나 |
| [04](#04) | 타이머는 어떻게 세우고 읽나 |
| [05](#05) | 그 밖에 어떤 관용구를 쓰나 |
| [06](#06) | `overhead`는 어떻게 쓰나 |
| [07](#07) | PvP 겸용 스크립트는 무엇이 다른가 |

이 문서에 걸린 질문은 [open-items.md](../questions/open-items.md)에 모았다.

::part[저장소]

## <a id="01"></a>01 저장소 구조

### <a id="01.A"></a>01.A 폴더

| 폴더 | 무엇 |
| --- | --- |
| `script/` | Razor 스크립트. 모두가 공유한다 |
| `module/`, `recipe/` | 한 벌만 둔 루프 블록과 루프마다의 레시피. `util/build-scripts.mjs`가 `script/combat/*`·`script/gather/*`로 조립한다 ([modules.md](modules.md)) |
| `config/` | 사람마다 클라이언트 설정 원본 하나 (`config/<이름>/`). 링크 방식과 파일별 설명은 [config/README.md](https://github.com/minu-ha/uoo/blob/master/config/README.md) |
| `document/` | 설계 문서. for-humanity로 사이트를 만들어 읽는다 (`pnpm docs:dev`). 무엇이 있는지는 [문서 홈](../README.md), 쓰는 법은 [Writing](../working/writing.md) |
| `language/` | README 번역본. 규칙은 [Writing](../working/writing.md#07) 07절 |
| `util/` | `setup.sh` (게임을 저장소에 링크), `build-scripts.mjs` (모듈로 루프 조립), `check.sh` (스크립트 블록 짝과 선언 없이 쓴 접두 변수 검사, 인자 없이 돌리면 조립 결과물 검사도), `check-docs.mjs` (만든 문서 사이트의 끊긴 링크와 앵커, 번호 제목의 앵커 검사) |

웹/서버 프로젝트가 아니다. Razor의 자동 검사는 `util/`의 두 검사기이고, 동작 검증은 인게임에서만 된다.
조건부 전투 모형 `util/pvp-sim.mjs`와 수치 검사 `util/pvp-sim.test.mjs`는 Node 표준 라이브러리로 별도 실행한다.
입력·정책·실측 한계는 [벌목 핸드북 05.D절](../templates/lumberjack-pvp.md#05.D)에 적었다.

### <a id="01.B"></a>01.B script 분류와 파일명

`script/`는 **언제 돌리는 스크립트인지**로 나눈다. 파일명만 봐도 뭔지 알 수 있어야 한다.

| 폴더 | 언제 | 파일명 규칙 | 예 |
| --- | --- | --- | --- |
| `script/combat/` | 사냥 중 계속 돌리는 메인 루프 | `<템플릿>[-<변형>]` | `bard-necro-enhanced`, `pvp` |
| `script/hotkey/` | 키에 물려 한 번 실행하는 매크로 | `<동작>[-<대상>]`, 무기 스왑은 `weapon-<무기>` | `weapon-katana`, `cancel-target`, `dress`, `moongate` |
| `script/debug/` | 진단·동작 시험용 단발 스크립트. 필요하면 핫키에 연결 | `<검사>[-<대상>]` | `dump-label`, `debug-target-find`, `debug-target-state`, `test-telekinesis-var` |
| `script/train/` | 스킬 트레이닝 | `<스킬>` | `magery`, `carto` |
| `script/gather/` | 채집 루프 | `<채집>` | `lumberjack-enhanced`, `skinning-enhanced` |
| `script/loot/` | 주워온 것 정리·분해 | `<동사>-<대상>` | `recycle`, `claim-loot`, `bank-pouch` |
| `script/restock/` | 나가기 전 준비: 로드아웃, 리필 | `<동사>-<대상>` | `loadout`, `refill-runebook` |
| `script/archive/` | 지금 쓰지 않는 스크립트. 핫키에 걸지 않고 고치지 않으며 `util/check.sh`도 건너뛴다. 다시 쓰려면 원래 폴더로 옮긴다 | 원래 이름 그대로 | `bard-mace`, `hally-mage`, `lumberjack` |
| `script/shelf/` | outlandsbutler.com 생성 Storage Shelf 로드아웃 | `<템플릿>` | `bard-dexxer`, `sailing` |

전투 루프와 템플릿의 대응은 [script/README.md](https://github.com/minu-ha/uoo/blob/master/script/README.md)의 전투 루프 표가 정본이다.

`combat/pvp`는 여러 템플릿이 공유하는 자기관리 루프다.
Magery·무기·붕대 등 독립 기능 옵션을 본문에서 선택하며, 별도 템플릿별 PvP 진입 파일은 두지 않는다
([pvp.md](../game/pvp.md#05.E) 05.E절).

### <a id="01.C"></a>01.C 파일 규칙

- kebab-case, 소문자, 공백 없음. 폴더가 분류를 말하므로 파일명에 `combat-` 같은 접두는 붙이지 않는다.
- 같은 성격이 3개 이상 모이면 폴더를 나누고, 2개 이하면 기존 폴더에 둔다.
- `-temp`, `-old`, `-new`, `-backup` 파일을 만들지 않는다. 이력은 git이 가진다.
- `shelf/`는 outlandsbutler.com이 만든 파일이다. 손으로 고치지 않고 사이트에서 다시 만든다.
  만든 사람의 Storage Shelf serial이 들어 있어 사실상 개인 파일이다.
- 외부 출처 스크립트 (Jaseowns, raveX 등)는 헤더 크레딧을 유지하고, 상단 설정 변수 위주로만 고친다.
  이 문서의 규칙과 [overheads.md](overheads.md)의 형식도 외부 출처 파일에는 적용하지 않는다.
  예외로 `loot/recycle`은 2026-10-10 사용자 요청으로 이 규칙에 맞게 다시 썼다. 크레딧은 헤더에 남기고, 이후로는 직접 만든 스크립트로 다룬다.

### <a id="01.D"></a>01.D config는 사람별

- 스크립트는 모두가 공유하고 설정은 사람마다 분리된다. **다른 사람의 `config/`는 건드리지 않는다.**
- `settings.json`은 계정 비밀번호가 들어 있으므로 **절대 커밋하지 않는다.**
- `config/` 아래 파일은 게임을 끈 상태에서만 고친다. 이유는 [workflow.md](../working/workflow.md#04.C) 04.C절.

::part[모양]

## <a id="02"></a>02 스크립트 모양

### <a id="02.A"></a>02.A 기준 파일

사냥·채집 루프는 `module/`과 `recipe/`로 조립한다 ([modules.md](modules.md)). 결과물을 직접 고치지 않고 모듈과 레시피를 고친다.
기준 파일은 `script/gather/skinning-enhanced.razor`와 `script/restock/loadout.razor`다. 새 코드는 이 문서의 규칙을 따르고,
아직 옮기지 못한 파일을 고칠 때는 그 파일의 스타일을 유지한다.

### <a id="02.B"></a>02.B 구조와 섹션 배너

전투 루프는 헤더 (02.C절)와 시작 4줄 (02.D절) 뒤에 섹션을 이 순서로 둔다 (`skinning-enhanced.razor`, `lumberjack-enhanced.razor`).
조립한 루프는 시작 4줄이 `config__clear_at_start`를 읽어야 해서 STATE 뒤 준비 자리에 온다 ([modules.md](modules.md#05) 05절).

| 배너 | 무엇 |
| --- | --- |
| `CONFIG` | 손으로 조정하는 `config__` 값 |
| `WAIT AND COOLDOWN` | `wait__`, `interval__`, `cooldown__` 값. 전부 ms |
| `TIMER` | `timer__`를 만들고 첫 값을 준다 (04절) |
| `STATE` | `var__`의 첫 값. 이어 쓸 값은 `if not varexist`로 감싼다 (03.B절) |
| `INSTRUMENT` 등 | 루프 전에 한 번 하는 준비. 악기를 찾고, 없으면 고르게 한다 |
| `MAIN LOOP` | `while not dead` 하나 → `endwhile`. 루프 안의 블록은 `-` 배너로 나눈다 |

**배너는 두 가지다.** 모두 90칸이고, 제목은 대문자로 `# 제목` 한 줄에 쓴다.

- **섹션** (줄 맨 앞): `=` 줄 두 개 사이에 제목. 위 표의 섹션이 이것이다.
- **블록** (들여 쓴 자리, 루프 안): `-` 줄 두 개 사이에 제목, 빈 `#` 줄, 그 블록이 하는 일. 설명은 배너 안에 담고, 배너 밑은 바로 코드다.
  설명이 없으면 제목만 둔다.

```
# ========================================================================================
# CONFIG
# ========================================================================================
@setvar! config__chatty 1

while not dead
    # ------------------------------------------------------------------------------------
    # BANDAGE
    #
    # Never restarts a running bandage, and full health does not start one. Its target
    # cursor would replace a held precast, so it waits while any cursor is up.
    # ------------------------------------------------------------------------------------
    if not bandaging and not paralyzed
        ...
    endif
endwhile
```

모듈과 레시피의 상자 (`# @ config`, `# @ use`)도 같은 `-`와 `=` 줄을 쓴다 ([modules.md](modules.md#03) 03절).
조립한 루프에서는 블록 배너가 줄과 제목만 남고, 제목 줄 오른쪽에 그 블록이 온 모듈 파일이 붙는다. 블록이 하는 일은 그 모듈 파일의 배너에서 읽는다.
배너 밖, 코드 사이의 주석은 결과물에도 그대로 나간다.

```
    # ------------------------------------------------------------------------------------
    # BANDAGE                                               module/recovery/bandage.razor
    # ------------------------------------------------------------------------------------
    if config__use_bandages = 1 and not bandaging and not paralyzed
        ...
```

### <a id="02.C"></a>02.C 헤더

직접 만든 스크립트는 첫 줄에 한 줄 설명, 둘째 줄에 `Needs:`로 전제조건을 쓴다 (`script/loot/claim-loot.razor`).
조립한 루프는 레시피의 헤더 뒤에 조립기가 `Hotkeys:` 줄과 "Generated from …" 줄을 붙인다 ([modules.md](modules.md#05) 05절).

```
# Put your share from the distribution chest into your own loot container.
# Needs: global__my_loot_container (asked for on first run), container within 2 tiles
```

### <a id="02.D"></a>02.D 시작 4줄과 들여쓰기

```
clearall
clearsysmsg
cleardragdrop
clearignore
```

들여쓰기는 스페이스 4칸, 줄 끝은 CRLF (Razor가 그렇게 다시 쓴다). 탭은 쓰지 않는다.
편집기 설정은 `.editorconfig`가 정본이다.

수동 입력과 함께 도는 공통 `combat/pvp`는 시작 4줄을 생략한다 (레시피의 `config__clear_at_start 0`, [modules.md](modules.md#06) 06절).
실행 전에 보유한 주문·아이템 커서와 시전·장착 큐를 초기화하지 않기 위한 예외다.
대신 자동 행동 직전에 수동 시전·타깃·큐를 검사한다 ([pvp.md](../game/pvp.md#05.E) 05.E절).

### <a id="02.E"></a>02.E 주석

- 스크립트 안 주석은 영어이고, 줄 맨 앞의 `#`로 쓴다. `//`는 쓰지 않는다.
- **주석에 `;`을 쓰지 않는다.** Razor는 주석을 걷어내기 전에 `;`을 구문 구분자로 보기 때문에,
  주석 안의 세미콜론도 그 뒤를 명령으로 파싱해서 그 줄에서 에러가 난다 ([razor.md](razor.md#03) 03절). 마침표로 문장을 끊는다.

### <a id="02.F"></a>02.F 편집기 하이라이팅

`util/razor-syntax/`는 `.razor`용 TextMate 문법이다. WebStorm의 사용자 정의 파일 형식은 `#` 뒤를 통째로 주석 한 색으로 칠해서,
주석 안의 `# @ use`, 배너 제목, 설정 이름을 구분하지 못한다. 이 문법은 주석 줄도 모양에 따라 따로 칠한다.

| 무엇 | scope | WebStorm 색 (Language Defaults) | Light 기본 |
| --- | --- | --- | --- |
| 명령 (`@setvar!`, `hotkey`, `cast`)과 `if`, `while`, `endif` | `keyword` | Keyword | 남색 굵게 |
| 조건식 (`poisoned`, `findtype`, `insysmsg`) | `constant.other` | Constant | 보라 굵게 기울임 |
| `and`, `or`, `not`, `stop`, `break` | `entity.other.attribute-name` | Markup → Attribute | 분홍 |
| `self`, `backpack` 같은 레이어와 대상 | `constant.character.entity` | Markup → Entity | 파랑 굵게 |
| 문자열과 `>` 메모, `# @ hotkeys` 목록 | `string` | String | 초록 굵게 |
| 문자열 안의 `{{…}}` | `constant.character.escape` | Valid escape sequence | 남색 굵게 |
| `# @ use`, `# @ config` 같은 지시. `# @ when`과 `# @ every` 뒤의 조건은 코드처럼 칠한다 | `meta.tag` | Metadata | 올리브 |
| 모듈 이름, `# module/…razor` 출처 | `entity.other.attribute-name` | Markup → Attribute | 분홍 |
| 섹션 제목 (`# CONFIG`) | `markup.heading` | TextMate → Heading | 굵게, 밑줄 |
| 블록 제목 (`# BANDAGE`) | `markup.bold` | TextMate → Bold | 굵게 |
| 상자의 이름 줄 (`#   config__x`, `#   heal_hits (default 35)`) | `constant.other` | Constant | 보라 굵게 기울임 |
| 접두 변수 (`config__`, `var__` 등) | `variable` | Parameter, Local variable | 색 없음 |

scope는 WebStorm의 기본 Light 구성표에서 색이 있는 항목에 맞췄다. Function call이나 Parameter처럼 Light에서 색이 없는 항목은 피했다.

WebStorm에 거는 법:

1. Settings → Editor → File Types → `Razor` (사용자 정의 형식)에서 `*.razor` 패턴을 지운다. 남아 있으면 TextMate 문법이 쓰이지 않는다.
2. Settings → Editor → TextMate Bundles → `+` → 저장소의 `util/razor-syntax` 폴더를 고른다.
3. 색은 Settings → Editor → Color Scheme → Language Defaults의 위 표 이름에서 바꾼다. TextMate 문법은 이 기본 색을 따른다.
4. 문법 파일이 바뀌면 TextMate Bundles 목록에서 번들 체크를 껐다 켜고 Apply 하거나 WebStorm을 다시 연다.

VS Code에서는 `util/razor-syntax` 폴더를 확장으로 넣으면 된다.

## <a id="03"></a>03 변수

### <a id="03.A"></a>03.A 접두

접두로 무엇인지 드러낸다. 단어는 snake_case, 접두는 **더블 언더스코어**로 끊는다.

| 접두 | 무엇 | 수명 |
| --- | --- | --- |
| `config__` | 손으로 조정하는 설정. 파일 맨 위에 모아 둔다 | 세션 |
| `wait__` | 얼마나 쉬는지, 타겟 커서를 얼마나 기다리는지 | 세션 |
| `interval__` | `timer__`와 비교하는 간격. 그 타이머가 다시 돌기까지의 ms (`timer "timer__food" >= interval__food`) | 세션 |
| `cooldown__` | Razor 쿨다운 바에 주는 길이 (`cooldown "heal pot" cooldown__heal_potion`). 쿨다운 바에만 쓴다 | 세션 |
| `var__` | 이 스크립트가 들고 있는 상태 | 세션 |
| `alias__` | `find` / `findtype`의 `as` 바인딩 결과. 밖에서 쓰려면 `var__`로 옮긴다 ([razor.md](razor.md#03) 03절) | 묶은 블록 안 |
| `label__` | `getlabel` 결과 | 세션 |
| `timer__` | `createtimer` / `settimer` 대상 | 세션 |
| `list__` | `createlist` / `pushlist` 대상. `foreach x in list__y`의 루프 변수 `x`는 접두 없이 | 세션 |
| `global__` | **프로필에 저장되는 값** | 영속 |

### <a id="03.B"></a>03.B 세션 값과 영속 값

- 세션 값은 `global__`이 아닌 모든 변수다. `@setvar!`로 넣고, 스크립트가 끝나도 클라이언트를 끌 때까지 남아 다른 스크립트도 읽는다
  (`restock/loadout`이 적은 `var__right_hand`를 `hotkey/dress`가 읽는다). 타이머와 리스트도 실행이 끝난 뒤에 남는다.
- 영속 값은 `global__`뿐이다. `setvar`로 넣고, 프로필에 저장돼 클라이언트를 다시 켜도 남는다.
- **`global__` 이름을 바꾸면 프로필의 기존 항목과 연결이 끊긴다.** 이름이 곧 키라서, 바꾸면 전부 다시 타겟해야 하고 프로필에 옛 항목이 고아로 남는다.
  같은 이름을 쓰는 파일이 여러 개면 한 커밋에서 같이 바꾼다.

### <a id="03.C"></a>03.C serial 리터럴 금지

**serial 리터럴 (`0x45147618` 같은 값)을 스크립트에 쓰지 않는다.** `script/`는 공유 파일이라 남의 컨테이너 번호가
pull 한 사람 모두의 게임에 들어간다. 개인 값은 프로필에 저장하고 스크립트에는 이름만 남긴다 (`script/loot/claim-loot.razor`).

```
if not varexist global__my_loot_container
    overhead "[ loot chest, pick ]" 255
    setvar global__my_loot_container
endif
```

`setvar 이름`은 타겟을 요구하고 그 serial을 프로필 script variable로 저장한다.

### <a id="03.D"></a>03.D varexist는 선언 여부만 본다

잘못 타겟한 값이 들어 있어도 참이라 영영 안 고쳐진다. 그 물건 앞에 서 있는 것이 보장되는 스크립트에서는
`find`로 실제로 있는지까지 보고, 없으면 지우고 다시 묻는다 (`script/restock/loadout.razor`).

```
if not varexist global__my_supply_box or not find global__my_supply_box ground -1 -1 config__reach
    unsetvar global__my_supply_box
    overhead "[ supply box, pick ]" 255
    setvar global__my_supply_box
endif
```

**그 밖의 곳에는 붙이지 않는다.** `find`는 클라이언트가 지금 인식하는 것만 찾으므로, 집에 있는 상자를 던전에서 검사하면 멀쩡한 값을 지운다.

::part[관용구]

## <a id="04"></a>04 타이머

- 이름은 `timer__` 접두 (03.A절). `if not timerexists`로 한 번만 만들고, 첫 값은 `endif` 밖의 `settimer`로 준다.
  타이머는 실행이 끝나도 남으므로, 밖에 두어야 실행할 때마다 같은 값에서 시작한다.
- 시간 제어는 타이머 기본. `cooldown` 명령은 기존 파일이 이미 그 스타일일 때만.
- 서버가 메시지로 알려 주는 쿨 (바드 스킬, 매저리 프록)은 자체 타이머로 흉내 내지 않고 `cooldown "이름"`을 읽는다. 이유는 [overheads.md](overheads.md#06.B) 06.B절.

`skinning-enhanced.razor`의 TIMER 섹션이 이 모양이다. 첫 값을 간격 (`interval__`)으로 주면 첫 패스부터 통과한다.

```
if not timerexists "timer__overhead_message"
    createtimer "timer__overhead_message"
endif

settimer "timer__overhead_message" interval__overhead_message
```

루프 안에서는 `timer`로 지난 시간을 읽고, 할 일을 한 뒤 `settimer`로 0부터 다시 잰다.

```
if timer "timer__overhead_message" > interval__overhead_message
    overhead "[ heal pot, out ]" 254
    settimer "timer__overhead_message" 0
endif
```

## <a id="05"></a>05 그 외 관용구

| 하려는 것 | 쓰는 모양 |
| --- | --- |
| 시스템 메시지를 안 띄우고 명령 실행 | `@` 접두 |
| 찾은 것을 다시 쓰기 | `if findtype "name" backpack as alias__x`로 alias에 담는다 |
| 같은 검색을 되풀이하며 하나씩 보기 | `@ignore` / `@clearignore` ([razor.md](razor.md#03) 03절 `findtype` 줄) |
| 라벨로 분기 | `getlabel alias__x label__x` → `if "문자열" in label__x`. `in`은 대소문자를 가리므로 정확한 글자는 `debug/dump-label`로 확인한다 |
| 검프·핫바 조작 | `gumpexists` / `ingump`로 확인한 뒤 `gumpresponse` |
| 디버그 출력 | `{{var}}` 보간. 확인이 끝나면 지운다 |

## <a id="06"></a>06 overhead

전부 `[ 대상, 상태 ]` 소문자. 시전 알림만 `[ 대상 ]`. 단어, hue, 어느 경로로 띄울지는 [overheads.md](overheads.md)이 정본이다.
새 단어를 만들기 전에 그 문서의 03절 어휘와 04절 글로서리를 본다.

## <a id="07"></a>07 PvP 겸용 스크립트

- `if pvp` 분기를 먼저 두고, PvE 로직을 그대로 옮기지 않는다.
- 구조화 PvP나 팩션 상태에서 막히는 명령은 [razor.md](razor.md#07) 07절. 게임 쪽 PvP 규칙은 [pvp.md](../game/pvp.md).
