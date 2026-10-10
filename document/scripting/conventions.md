---
name: Conventions
label: 저장소와 스크립트 규칙
group: Scripting
order: 10
---

파일을 어디에 두고 어떻게 이름 짓는지, 스크립트를 어떤 모양으로 쓰는지 적은 문서다.
문법 자체, 그러니까 되는 구문과 함정은 [Razor](razor.md)에, 머리 위 메시지는 [Overheads](overheads.md)에 있다.

## <a id="00"></a>00 한눈에

| 절 | 무엇을 답하나 |
| --- | --- |
| [01](#01) | 어느 폴더에 두고 파일 이름을 어떻게 짓나. `config/`는 누구 것인가 |
| [02](#02) | 스크립트를 어떤 순서와 모양으로 쓰나. 헤더, 시작 4줄, 섹션과 블록 배너, 주석, 편집기 하이라이팅 |
| [03](#03) | 변수 접두는 무엇이고, 세션 값과 영속 값은 어떻게 가르나. serial은 왜 쓰지 않나 |
| [04](#04) | 타이머는 어떻게 세우고 읽나 |
| [05](#05) | 그 밖에 어떤 관용구를 쓰나 |
| [06](#06) | `overhead`는 어떻게 쓰나 |
| [07](#07) | PvP 겸용 스크립트는 무엇이 다른가 |

이 문서에 걸린 질문은 [Open items](../questions/open-items.md)에 모았다.

::part[저장소]

## <a id="01"></a>01 저장소 구조

### <a id="01.A"></a>01.A 폴더

폴더의 규칙은 이 표가 정본이다. 루트 README의 폴더 표는 사람에게 보여 주는 요약이다.

| 폴더 | 무엇 |
| --- | --- |
| `script/` | Razor 스크립트. 모두가 함께 쓴다 |
| `module/`, `recipe/` | 한 벌만 둔 루프 블록과, 루프마다 하나씩 둔 레시피. `util/build-scripts.mjs`가 이 둘로 `script/combat/*`와 `script/gather/*`를 조립한다([Modules](modules.md)) |
| `config/` | 사람마다 클라이언트 설정 원본 하나(`config/<이름>/`). 링크 방식과 파일별 설명은 [config/README.md](https://github.com/minu-ha/uoo/blob/master/config/README.md)에 있다 |
| `document/` | 설계 문서. 묶음마다 폴더 하나(`working/`, `scripting/`, `game/`, `templates/`, `questions/`)를 둔다. for-humanity로 사이트를 만들어 읽는다(`pnpm docs:dev`). 문서 목록은 [문서 홈](../README.md)에, 쓰는 법은 [Writing](../working/writing.md)에 있다 |
| `language/` | README 번역본. 규칙은 [Writing](../working/writing.md#07) 07절에 있다 |
| `util/` | 저장소 도구. 아래 표를 본다 |

`util/`에는 이것들이 있다. Node 도구는 Node 22 표준 라이브러리만 쓴다. 문서 검사만 `parse5`를 쓴다.

| 파일 | 하는 일 |
| --- | --- |
| `setup.sh` | 게임을 저장소에 링크한다 |
| `build-scripts.mjs` | 모듈과 레시피로 루프를 조립한다(`pnpm build`). `--check`, `--settings`, `--new-module`도 있다 |
| `check.sh` | 스크립트의 블록 짝과, 값을 넣지 않고 쓴 접두 변수를 검사한다. 인자 없이 돌리면 끝에 조립 결과물 검사(`build-scripts.mjs --check`)도 돈다 |
| `check-docs.mjs` | 만든 문서 사이트에서 끊긴 링크와 앵커를 찾고, 번호 제목에 앵커가 맞게 달렸는지 본다. 테스트는 `check-docs.test.mjs` |
| `pvp-sim.mjs` | 조건부 전투 모형. 수치 검사는 `pvp-sim.test.mjs` |
| `razor-syntax/` | `.razor` 편집기 하이라이팅(02.F절) |

웹이나 서버 프로젝트가 아니다. 스크립트를 자동으로 검사하는 것은 `check.sh`와 그 안에서 도는 조립 검사뿐이고, 동작은 인게임에서만 확인할 수 있다.
`pnpm check`가 스크립트 검사와 문서 검사를 함께 돌리고, `pnpm test`가 `util/`의 테스트를 돌린다.
전투 모형의 입력, 정책, 실측 한계는 [Lumberjack PvP](../templates/lumberjack-pvp.md#05.D) 05.D절에 적었다.

### <a id="01.B"></a>01.B script 분류와 파일명

`script/`는 **언제 돌리는 스크립트인지**로 나눈다. 파일명만 보고도 무엇인지 알 수 있어야 한다.

| 폴더 | 언제 | 파일명 규칙 | 예 |
| --- | --- | --- | --- |
| `script/combat/` | 사냥하는 동안 계속 돌리는 메인 루프 | `<템플릿>[-<변형>]` | `bard-necro-enhanced`, `pvp` |
| `script/hotkey/` | 키에 물려 한 번 실행하는 매크로 | `<동작>[-<대상>]`. 무기 바꾸기는 `weapon-<무기>` | `weapon-katana`, `cancel-target`, `dress`, `moongate` |
| `script/debug/` | 진단과 동작 시험에 쓰는 단발 스크립트. 필요하면 핫키에 건다 | `<검사>[-<대상>]` | `dump-label`, `debug-target-find`, `debug-target-state`, `test-telekinesis-var` |
| `script/train/` | 스킬 훈련 | `<스킬>` | `magery`, `carto` |
| `script/gather/` | 채집 루프 | `<채집>` | `lumberjack-enhanced`, `skinning-enhanced` |
| `script/loot/` | 주워 온 것을 정리하거나 분해한다 | `<동사>-<대상>` | `recycle`, `claim-loot`, `bank-pouch` |
| `script/restock/` | 나가기 전 준비. 로드아웃과 리필 | `<동사>-<대상>` | `loadout`, `refill-runebook` |
| `script/archive/` | 지금 쓰지 않는 스크립트. 핫키에 걸지 않고, 고치지 않고, `util/check.sh`도 건너뛴다. 다시 쓰려면 원래 폴더로 옮긴다 | 원래 이름 그대로 | `bard-mace`, `hally-mage`, `lumberjack` |
| `script/shelf/` | outlandsbutler.com이 만든 Storage Shelf 로드아웃 | `<템플릿>` | `bard-dexxer`, `sailing` |

전투 루프와 템플릿의 대응은 [script/README.md](https://github.com/minu-ha/uoo/blob/master/script/README.md)의 전투 루프 표가 정본이다.

`combat/pvp`는 여러 템플릿이 함께 쓰는 자기관리 루프다. Magery, 무기, 붕대 같은 기능은 레시피의 설정으로 켜고 끈다.
템플릿마다 따로 PvP 진입 파일을 두지 않는다([PvP](../game/pvp.md#05.E) 05.E절).

### <a id="01.C"></a>01.C 파일 규칙

- 파일 이름은 kebab-case 소문자로 쓰고 공백을 넣지 않는다. 폴더가 분류를 말하므로 `combat-` 같은 접두는 붙이지 않는다.
- 같은 성격의 파일이 3개 이상 모이면 폴더를 나눈다. 2개 이하면 기존 폴더에 둔다.
- `-temp`, `-old`, `-new`, `-backup` 파일을 만들지 않는다. 이력은 git이 가진다.
- `shelf/`는 outlandsbutler.com이 만든 파일이다. 손으로 고치지 않고 사이트에서 다시 만든다.
  만든 사람의 Storage Shelf serial이 들어 있어서 사실상 개인 파일이다.
- 외부에서 가져온 스크립트(Jaseowns, raveX 같은)는 헤더의 크레딧을 지키고, 맨 위 설정 변수 위주로만 고친다.
  이 문서의 규칙과 [Overheads](overheads.md)의 형식은 외부 파일에 적용하지 않는다.
  `loot/recycle`은 예외다. 2026-10-10 사용자 요청으로 이 규칙에 맞게 다시 썼다. 크레딧은 헤더에 남겼고, 그 뒤로는 직접 만든 스크립트로 다룬다.

### <a id="01.D"></a>01.D config는 사람별

- 스크립트는 모두가 함께 쓰고, 설정은 사람마다 따로 둔다. **다른 사람의 `config/`는 건드리지 않는다.**
- `settings.json`에는 계정 비밀번호가 들어 있다. **절대 커밋하지 않는다.**
- `config/` 아래 파일은 게임을 끈 상태에서만 고친다. 이유는 [Workflow](../working/workflow.md#04.C) 04.C절에 있다.

::part[모양]

## <a id="02"></a>02 스크립트 모양

### <a id="02.A"></a>02.A 기준 파일

사냥 루프와 채집 루프는 `module/`과 `recipe/`로 조립한다([Modules](modules.md)). 결과물은 직접 고치지 않고, 모듈과 레시피를 고친다.
모양의 기준 파일은 `script/gather/skinning-enhanced.razor`와 `script/restock/loadout.razor`다.
새 코드는 이 문서의 규칙을 따른다. 아직 옮기지 못한 파일을 고칠 때는 그 파일의 스타일을 지킨다.

### <a id="02.B"></a>02.B 구조와 섹션 배너

루프는 헤더(02.C절)와 시작 4줄(02.D절) 뒤에 섹션을 아래 순서로 둔다(`skinning-enhanced.razor`, `lumberjack-enhanced.razor`).
조립한 루프에서는 시작 4줄이 `config__clear_at_start`를 읽어야 해서, STATE 뒤 준비 자리에 온다([Modules](modules.md#05) 05절).

| 배너 | 무엇 |
| --- | --- |
| `CONFIG` | 손으로 조정하는 `config__` 값 |
| `WAIT AND COOLDOWN` | `wait__`, `interval__`, `cooldown__` 값. 단위는 모두 ms다 |
| `TIMER` | `timer__`를 만들고 첫 값을 준다(04절) |
| `STATE` | `var__`의 첫 값. Play를 넘어 이어 쓸 값은 `if not varexist`로 감싼다(03.B절) |
| `INSTRUMENT` 같은 준비 | 루프 전에 한 번 하는 준비. 예를 들어 악기를 찾고, 없으면 고르게 한다. 조립한 루프에서는 모듈마다 출처 상자 밑에 온다 |
| `MAIN LOOP` | `while not dead`에서 `endwhile`까지 루프 하나. 루프 안의 블록은 `-` 배너로 나눈다 |

**배너는 두 가지다.** 둘 다 폭이 90칸이고, 제목은 대문자로 `# 제목` 한 줄에 쓴다.

- **섹션 배너**는 줄 맨 앞에 둔다. `=` 줄 두 개 사이에 제목을 쓴다. 위 표의 섹션이 이것이다.
- **블록 배너**는 루프 안, 들여 쓴 자리에 둔다. `-` 줄 두 개 사이에 제목, 빈 `#` 줄, 그 블록이 하는 일을 쓴다.
  설명은 배너 안에 담고, 배너 바로 밑부터 코드다. 설명이 없으면 제목만 둔다.

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

모듈과 레시피의 상자(`# @ config`, `# @ use`)도 같은 `-` 줄과 `=` 줄을 쓴다([Modules](modules.md#03) 03절).
조립한 루프에서는 블록 배너에 줄과 제목만 남고, 제목 줄 오른쪽에 그 블록이 온 모듈 파일이 붙는다. 블록이 하는 일은 그 모듈 파일의 배너에서 읽는다.
배너 밖, 코드 사이의 주석은 결과물에도 그대로 나간다.

```
    # ------------------------------------------------------------------------------------
    # BANDAGE                                               module/recovery/bandage.razor
    # ------------------------------------------------------------------------------------
    if config__use_bandages = 1 and not bandaging and not paralyzed
        ...
```

### <a id="02.C"></a>02.C 헤더

직접 만든 스크립트는 첫 줄에 한 줄 설명을, 둘째 줄에 `Needs:`로 전제조건을 쓴다(`script/loot/claim-loot.razor`).
조립한 루프는 레시피의 헤더 뒤에 조립기가 `Hotkeys:` 줄과 "Generated from …" 줄을 붙인다([Modules](modules.md#05) 05절).

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

들여쓰기는 스페이스 4칸이고, 줄 끝은 CRLF다. Razor가 파일을 CRLF로 다시 쓰기 때문이다. 탭은 쓰지 않는다.
편집기 설정은 `.editorconfig`가 정본이다.

공통 `combat/pvp`는 플레이어의 수동 입력과 함께 돌기 때문에 시작 4줄을 건너뛴다. 레시피에 `config__clear_at_start 0`을 둔다([Modules](modules.md#06) 06절).
Play할 때 플레이어가 들고 있던 주문 커서, 아이템 커서, 시전 큐, 장착 큐를 지우지 않으려는 예외다.
그 대신 자동 행동 바로 앞에서 수동 시전, 타깃, 큐를 검사한다([PvP](../game/pvp.md#05.E) 05.E절).

### <a id="02.E"></a>02.E 주석

- 스크립트 안 주석은 영어로 쓰고, 줄 맨 앞의 `#`로 시작한다. `//`는 쓰지 않는다.
- **주석에 `;`을 쓰지 않는다.** Razor는 주석을 걷어 내기 전에 `;`을 구문 구분자로 본다.
  그래서 주석 안의 세미콜론 뒤도 명령으로 읽어서 그 줄에서 오류가 난다([Razor](razor.md#03) 03절). 문장은 마침표로 끊는다.

### <a id="02.F"></a>02.F 편집기 하이라이팅

`util/razor-syntax/`는 `.razor`용 TextMate 문법이다.
WebStorm의 사용자 정의 파일 형식은 `#` 뒤를 통째로 주석 한 가지 색으로 칠한다. 그래서 주석 안의 `# @ use`, 배너 제목, 설정 이름을 구분하지 못한다.
이 문법은 주석 줄도 모양에 따라 따로 칠한다.

| 무엇 | scope | WebStorm 색(Language Defaults) | Light 기본 |
| --- | --- | --- | --- |
| 명령(`@setvar!`, `hotkey`, `cast`)과 `if`, `while`, `endif` | `keyword` | Keyword | 남색 굵게 |
| 조건식(`poisoned`, `findtype`, `insysmsg`) | `constant.other` | Constant | 보라 굵게 기울임 |
| `and`, `or`, `not`, `stop`, `break` | `entity.other.attribute-name` | Markup → Attribute | 분홍 |
| `self`, `backpack` 같은 레이어와 대상 | `constant.character.entity` | Markup → Entity | 파랑 굵게 |
| 문자열과 `>` 메모, `# @ hotkeys` 목록 | `string` | String | 초록 굵게 |
| 문자열 안의 `{{…}}` | `constant.character.escape` | Valid escape sequence | 남색 굵게 |
| `# @ use`, `# @ config` 같은 지시. `# @ when`과 `# @ every` 뒤의 조건은 코드처럼 칠한다 | `meta.tag` | Metadata | 올리브 |
| 모듈 이름, `# module/…razor` 출처 | `entity.other.attribute-name` | Markup → Attribute | 분홍 |
| 섹션 제목(`# CONFIG`) | `markup.heading` | TextMate → Heading | 굵게, 밑줄 |
| 블록 제목(`# BANDAGE`) | `markup.bold` | TextMate → Bold | 굵게 |
| 상자의 이름 줄(`#   config__x`, `#   heal_hits (default 35)`) | `constant.other` | Constant | 보라 굵게 기울임 |
| 접두 변수(`config__`, `var__` 같은) | `variable` | Parameter, Local variable | 색 없음 |

scope는 WebStorm 기본 Light 구성표에서 색이 있는 항목에 맞췄다. Function call이나 Parameter처럼 Light에서 색이 없는 항목은 피했다.

WebStorm에는 이렇게 건다.

1. Settings → Editor → File Types → `Razor`(사용자 정의 형식)에서 `*.razor` 패턴을 지운다. 패턴이 남아 있으면 TextMate 문법이 쓰이지 않는다.
2. Settings → Editor → TextMate Bundles → `+`를 누르고 저장소의 `util/razor-syntax` 폴더를 고른다.
3. 색은 Settings → Editor → Color Scheme → Language Defaults에서 위 표의 이름으로 바꾼다. TextMate 문법은 이 기본 색을 따른다.
4. 문법 파일이 바뀌면 TextMate Bundles 목록에서 번들 체크를 껐다 켜고 Apply를 누르거나, WebStorm을 다시 연다.

VS Code에서는 `util/razor-syntax` 폴더를 확장으로 넣으면 된다.

## <a id="03"></a>03 변수

### <a id="03.A"></a>03.A 접두

접두로 무엇인지 드러낸다. 단어는 snake_case로 쓰고, 접두와 이름 사이는 **더블 언더스코어**로 끊는다.

| 접두 | 무엇 | 수명 |
| --- | --- | --- |
| `config__` | 손으로 조정하는 설정. 파일 맨 위에 모아 둔다 | 세션 |
| `wait__` | 얼마나 쉬는지, 타겟 커서를 얼마나 기다리는지 | 세션 |
| `interval__` | `timer__`와 비교하는 간격. 그 타이머가 다시 돌기까지의 ms(`timer "timer__food" >= interval__food`) | 세션 |
| `cooldown__` | Razor 쿨다운 바에 주는 길이(`cooldown "heal pot" cooldown__heal_potion`). 쿨다운 바에만 쓴다 | 세션 |
| `var__` | 이 스크립트가 들고 있는 상태 | 세션 |
| `alias__` | `find`나 `findtype`의 `as`로 묶은 결과. 블록 밖에서 쓰려면 `var__`로 옮긴다([Razor](razor.md#03) 03절) | 묶은 블록 안 |
| `label__` | `getlabel` 결과 | 세션 |
| `timer__` | `createtimer`와 `settimer`의 대상 | 세션 |
| `list__` | `createlist`와 `pushlist`의 대상. `foreach x in list__y`의 루프 변수 `x`에는 접두를 붙이지 않는다 | 세션 |
| `global__` | **프로필에 저장되는 값** | 영속 |

### <a id="03.B"></a>03.B 세션 값과 영속 값

- 세션 값은 `global__`이 아닌 모든 변수다. `@setvar!`로 넣는다.
  스크립트가 끝나도 클라이언트를 끌 때까지 남아서 다른 스크립트도 읽는다. `restock/loadout`이 적은 `var__right_hand`를 `hotkey/dress`가 읽는 식이다.
  타이머와 리스트도 실행이 끝난 뒤에 남는다.
- 영속 값은 `global__`뿐이다. `setvar`로 넣고, 프로필에 저장되어 클라이언트를 다시 켜도 남는다.
- **`global__` 이름을 바꾸면 프로필의 기존 항목과 연결이 끊긴다.** 이름이 곧 키라서, 바꾸면 전부 다시 타겟해야 하고 프로필에는 옛 항목이 고아로 남는다.
  같은 이름을 쓰는 파일이 여러 개면 한 커밋에서 함께 바꾼다.

### <a id="03.C"></a>03.C serial 리터럴 금지

**`0x45147618` 같은 serial 리터럴을 스크립트에 쓰지 않는다.** `script/`는 함께 쓰는 파일이라, 남의 컨테이너 번호가 pull 한 사람 모두의 게임에 들어간다.
개인 값은 프로필에 저장하고, 스크립트에는 이름만 남긴다(`script/loot/claim-loot.razor`).

```
if not varexist global__my_loot_container
    overhead "[ loot chest, pick ]" 255
    setvar global__my_loot_container
endif
```

`setvar 이름`은 타겟 커서를 띄우고, 찍은 대상의 serial을 프로필 script variable로 저장한다.

### <a id="03.D"></a>03.D varexist는 선언 여부만 본다

`varexist`는 값이 맞는지 보지 않는다. 잘못 타겟한 값이 들어 있어도 참이라서 영영 고쳐지지 않는다.
그래서 그 물건 앞에 서 있는 것이 확실한 스크립트에서는 `find`로 실제로 있는지까지 보고, 없으면 지우고 다시 묻는다(`script/restock/loadout.razor`).

```
if not varexist global__my_supply_box or not find global__my_supply_box ground -1 -1 config__reach
    unsetvar global__my_supply_box
    overhead "[ supply box, pick ]" 255
    setvar global__my_supply_box
endif
```

**그 밖의 곳에는 이 검사를 붙이지 않는다.** `find`는 클라이언트가 지금 인식하는 것만 찾는다. 집에 있는 상자를 던전에서 검사하면 멀쩡한 값을 지운다.

::part[관용구]

## <a id="04"></a>04 타이머

- 이름에는 `timer__` 접두를 붙인다(03.A절). `if not timerexists`로 한 번만 만들고, 첫 값은 `endif` 밖의 `settimer`로 준다.
  타이머는 실행이 끝나도 남는다. 그래서 첫 값을 밖에 두어야 실행할 때마다 같은 값에서 시작한다.
- 시간은 타이머로 잰다. `cooldown` 명령은 기존 파일이 이미 그 스타일일 때만 쓴다.
- 바드 스킬이나 마법 프록처럼 서버가 메시지로 알려 주는 쿨은 자체 타이머로 흉내 내지 않는다. `cooldown "이름"`을 읽는다. 이유는 [Overheads](overheads.md#06.B) 06.B절에 있다.

`skinning-enhanced.razor`의 TIMER 섹션이 이 모양이다. 첫 값을 간격(`interval__`)으로 주면 첫 패스부터 통과한다.

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
| 시스템 메시지를 띄우지 않고 명령 실행 | `@` 접두 |
| 찾은 것을 다시 쓰기 | `if findtype "name" backpack as alias__x`로 alias에 담는다 |
| 같은 검색을 되풀이하며 하나씩 보기 | `@ignore`와 `@clearignore`([Razor](razor.md#03) 03절의 `findtype` 줄) |
| 라벨로 분기 | `getlabel alias__x label__x` 뒤에 `if "문자열" in label__x`. `in`은 대소문자를 가리므로 정확한 글자는 `debug/dump-label`로 확인한다 |
| 검프와 핫바 조작 | `gumpexists`나 `ingump`로 확인한 뒤 `gumpresponse` |
| 디버그 출력 | `{{var}}` 보간. 확인이 끝나면 지운다 |

## <a id="06"></a>06 overhead

머리 위 메시지는 모두 `[ 대상, 상태 ]` 모양의 소문자로 쓴다. 시전 알림만 `[ 대상 ]`이다.
낱말, hue, 어느 경로로 띄울지는 [Overheads](overheads.md)가 정본이다. 새 낱말을 만들기 전에 그 문서의 03절 어휘와 04절 글로서리를 본다.

## <a id="07"></a>07 PvP 겸용 스크립트

- `if pvp` 분기를 먼저 둔다. PvE 로직을 그대로 옮기지 않는다.
- 구조화 PvP나 팩션 상태에서 막히는 명령은 [Razor](razor.md#07) 07절에 있다. 게임 쪽 PvP 규칙은 [PvP](../game/pvp.md)에 있다.
