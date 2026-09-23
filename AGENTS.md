# AGENTS.md

## 이 저장소

- Ultima Online Outlands용 Razor 스크립트 (`script/`), 클라이언트 설정 사본 (`config/`), 참고 자료 (`library/`).
- 웹/서버 프로젝트가 아니다. 빌드·린트·테스트 러너 없음. 동작 검증은 인게임에서만 가능하다.
- 근거 우선순위: 사용자 요청 > 이 문서 > 같은 폴더의 기존 스크립트 > 공식 위키.
- 문서와 답변은 한국어, 스크립트 안 주석은 영어.

## 참고 사이트

| 용도 | 링크 |
|---|---|
| Outlands Razor 문법 (확장 명령 포함, 1순위) | <https://wiki.uooutlands.com/Razor_Scripting> |
| 게임 메커니즘·아이템·몹 | <https://wiki.uooutlands.com/> |
| Razor CE 기본 문법 (Outlands가 포크한 원본) | <https://www.razorce.com/guide/> |
| 스크립트 라이브러리 (Jaseowns 등 공개 스크립트) | <https://outlands.uorazorscripts.com/> |
| Storage Shelf 로드아웃 스크립트 생성 | <https://www.outlandsbutler.com/> |
| 공식 포럼 | <https://forums.uooutlands.com/> |

문법이 애매하면 추측하지 말고 위키를 읽는다. Outlands Razor는 Razor CE에 없는 명령이 많다.

## 구조와 이름 규칙

`script/` 는 **언제 돌리는 스크립트인지**로 나눈다. 파일명만 봐도 뭔지 알 수 있어야 한다.

| 폴더 | 언제 | 파일명 규칙 | 예 |
|---|---|---|---|
| `script/combat/` | 사냥 중 계속 돌리는 메인 루프 | `<템플릿>[-<변형>]` | `bard-necro`, `bard-necro-eval`, `hally-mage` |
| `script/hotkey/` | 키에 물려 한 번 실행하는 매크로 | `<동작>[-<대상>]`, 무기 스왑은 `weapon-<무기>` | `weapon-katana`, `cancel-target`, `dress`, `moongate` |
| `script/train/` | 스킬 트레이닝 | `<스킬>` | `magery`, `carto` |
| `script/gather/` | 채집 루프 | `<채집>` | `mining`, `lumberjack` |
| `script/loot/` | 주워온 것 정리·분해 | `<동사>-<대상>` | `recycle`, `pull-loot`, `bank-pouch` |
| `script/restock/` | 나가기 전 준비: 로드아웃, 리필 | `<동사>-<대상>` | `loadout`, `refill-keg`, `refill-runebook` |
| `script/shelf/` | outlandsbutler.com 생성 Storage Shelf 로드아웃 | `<템플릿>` | `bard-dexxer`, `sailing` |

- kebab-case, 소문자, 공백 없음. 폴더가 분류를 말하므로 파일명에 `combat-` 같은 접두는 붙이지 않는다.
- 같은 성격이 3개 이상 모이면 폴더를 나누고, 2개 이하면 기존 폴더에 둔다.
- `-temp`, `-old`, `-new`, `-backup` 파일을 만들지 않는다. 이력은 git이 가진다.
- `shelf/` 는 outlandsbutler.com 생성물. 손으로 고치지 않고 사이트에서 다시 만든다. 내 셸프 serial 이 들어 있어 사실상 개인 파일이다.
- 외부 출처 스크립트(Jaseowns, Demlar 등)는 헤더 크레딧을 유지하고, 상단 설정 변수 위주로만 고친다.

`config/<이름>/` 는 그 사람의 클라이언트 설정 원본이다 (`util/setup.sh` 가 게임 폴더를 여기로 링크). 링크 방식과 파일별 설명은 `config/README.md`. 스크립트는 모두가 공유하고 설정은 사람마다 분리된다. 다른 사람의 `config/` 는 건드리지 않는다.
`settings.json` 은 계정 비밀번호가 들어 있으므로 절대 커밋하지 않는다.

`library/`:

| 파일 | 내용 |
|---|---|
| `templates.md` | 템플릿 ↔ 전투 스크립트 ↔ 핫키 ↔ shelf ↔ 프로필 매핑. 새 템플릿 만들면 한 줄 추가 |
| `hotkeys.md` | 키 배치와 주문 데미지 메모 |
| `item-list.razor` | 아이템 이름·graphic id·hue 목록. `findtype` 인자 찍을 때 참조 |
| `vendor-prices.md` | 상점 가격표 |
| `bard-necro-summon-guide.md` | Bard Necro 소환 조합·Tome 투자 가이드 |

## Razor 스크립트 컨벤션

기준 파일은 `script/combat/bard-necro-eval.razor`. 새 코드는 이 규칙을 따르고, 기존 파일을 고칠 때는 그 파일 스타일을 유지한다.

**헤더** — 직접 만든 스크립트는 첫 줄에 한 줄 설명, 둘째 줄에 전제조건.

```
# Bard Necro main loop: sustain, bard control, necro rotation.
# Needs: organizer 1 (loot bag), cooldown "Skill", hotkey "Clear Scavenger Cache", var_my_loot_chest set
```

**주석에 `;` 를 쓰지 않는다.** Razor 는 주석을 걷어내기 전에 `;` 를 구문 구분자로 보기 때문에,
주석 안의 세미콜론도 그 뒤를 명령으로 파싱해서 그 줄에서 에러가 난다. 마침표로 문장을 끊는다.

**시작 4줄** — `clearall` / `clearsysmsg` / `cleardragdrop` / `clearignore`

**들여쓰기** — 탭 (`.editorconfig` 에 있음).

**구조** — `SETUP`(변수, 타이머) → 준비(악기 선택, 핫바 확인) → `while not dead` 메인 루프 하나 → `endwhile`. 섹션 배너:

```
# ####################################################################################
# # SECTION NAME
# ####################################################################################
```

**변수**
- 이름은 `var_` 접두, snake_case.
- 스크립트 안 값은 `@setvar! var_x` (실행 중만 유지).
- 컨테이너 serial처럼 캐릭터별로 고정되는 값만 `setvar` (영속). 처음 쓰는 곳에서 `if not varexist` 로 감싸고, 없으면 `overhead` 로 세팅을 요구한다.
  - **serial 리터럴(`0x45147618` 같은 값)을 스크립트에 쓰지 않는다.** `script/` 는 공유 파일이라 남의 컨테이너 번호가 pull 한 사람 모두의 게임에 들어간다. 개인 값은 아래 패턴으로 프로필에 저장하고, 스크립트에는 변수 이름만 남긴다.
    ```
    if not varexist var_my_loot_chest
    	overhead "Target your loot chest" 55
    	setvar var_my_loot_chest
    endif
    ```
    `setvar 이름` 은 타겟을 요구하고 그 serial 을 프로필 script variable 로 저장한다 (`setvar!` 는 실행 중에만 유지). `restock/`, `loot/`, `gather/` 일부에 아직 리터럴이 남아 있으니 그 파일을 손볼 때 이 패턴으로 바꾼다.

**타이머**
- `if not timerexists "x_timer"` → `createtimer` → `settimer`. 이름은 `_timer` 접미.
- 시간 제어는 타이머 기본. `cooldown` 명령은 기존 파일이 이미 그 스타일일 때만.

**그 외**
- 시스템 메시지 띄우면 안 되는 명령은 `@` 접두.
- 검색은 `if findtype "name" backpack as found_x` 로 alias에 담아 재사용. 반복 검색은 `ignore` / `clearignore`.
- 라벨 분기는 `getlabel` → `if "문자열" in label`.
- 검프·핫바는 `gumpexists` / `ingump` 확인 후 `gumpresponse`.
- 디버그 출력은 `{{var}}` 보간. 확인 끝나면 지운다.

**`overhead` 색상**

| 색 | 용도 |
|---|---|
| 32 | 상태, 정보 |
| 33 | 경고 |
| 34 | 에러, 못 찾음 |
| 44 | 네크로 캐스팅 알림 |
| 83 | 매저리 캐스팅 알림 |
| 55 | 선택 프롬프트, 라벨 출력 |

## Outlands 확장 문법

Razor CE에 없거나 확장된 것. 존재 여부만 적어두니 인자 형식은 위키에서 확인.

- 검색: `findtype` `dclicktype` `findtypelist` `targettype` `lifttype` 에 `source` `hue` `quantity` `range` 인자
- alias: `ground`
- 표현식: `find` `findlayer` `targetexists` `followers` `hue` `name` `paralyzed` `invul` `warmode` `noto` `dead` `maxweight` `diffweight` `diffhits` `diffmana` `diffstam` `counttype` `gumpexists` `ingump` `varexist` `bandaging` `cooldown` `pvp`
- 명령: `setvar` `unsetvar` `ignore` `unignore` `clearignore` `warmode` `getlabel` `rename` `skill` `setskill` `waitforgump` `gumpresponse` `gumpclose` `cooldown`
- 연산자: `as` `in`
- 리스트: `createlist` `clearlist` `removelist` `pushlist` `poplist` `listexists` `list` `inlist` `atlist` `foreach`
- 타이머: `createtimer` `removetimer` `settimer` `timer` `timerexists`
- 모든 루프에 `index` 내장. `overhead` / `sysmessage` 에 `{{var}}` 보간.

## PvP 제약

- 구조화 PvP 또는 Faction 상태에서는 `settimer` `removetimer` `getlabel` `rename` `cooldown` `wait` 등이 제한되고, 플레이어 serial은 `0x0`, `find` 계열은 자기 아이템만 잡는다.
- PvP 겸용 스크립트는 `if pvp` 분기를 먼저 두고, PvE 로직을 그대로 옮기지 않는다.

## 작업 방식

- 수정 전에 대상 스크립트를 끝까지 읽는다. 메인 루프 하나에 타이머·타겟 캐시·후속 캐스팅이 얽혀 있어 한 분기만 고치면 다른 분기가 깨진다.
- 요청 범위만 구현한다. 저장소에 근거 없는 패턴은 추가하지 않는다.
- `.razor` 를 고친 뒤에는 `util/check.sh <파일>` 로 `if/endif`, `while/endwhile`, `for/endfor` 짝을 확인한다.
- 변경 보고에는 반드시 넣는다:
  - 추가·변경된 변수와 타이머
  - 인게임 확인 절차: 어떤 상황에서 어떤 `overhead` 가 떠야 하고, 어떤 상황이면 실패인지
- Razor는 스크립트 본문을 메모리에 캐시한다. 파일을 고친 뒤에는 Razor의 Scripts 탭을 다시 열거나 우클릭 → Reload all scripts 를 해야 반영된다. 프로필 xml 은 종료 시 덮어쓰므로 게임을 끈 상태에서만 수정한다. 검증 절차에 이 두 가지를 명시한다.
- 새 템플릿 스크립트를 만들면 `library/templates.md` 에 한 줄 추가한다.

## 커밋

- 제목 한 줄, 영어, 마침표 없음. 본문·트레일러·`Co-Authored-By` 는 넣지 않는다.
- Conventional Commits 접두(`feat:`, `fix:`)를 쓰지 않는다. 동사로 시작하는 평서문.
  - 좋음: `Regroup scripts by activity`, `Add eval rotation to bard-necro`, `Fix stuck target loop in bard-mace`
  - 나쁨: `feat: regroup`, `update`, `스크립트 수정`
- 한 커밋에 한 가지 변경. 스크립트 수정과 문서 수정이 독립적이면 나눈다.
- 사용자가 커밋하라고 할 때만 커밋한다. push 는 별도 요청이 있을 때만.
