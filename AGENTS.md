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
| `script/combat/` | 사냥 중 계속 돌리는 메인 루프 | `<템플릿>[-<변형>]` | `bard-necro-enhanced`, `bard-mace`, `hally-mage` |
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
| `overheads.md` | 쿨다운 바 · 오버헤드 알림. 이름 규칙(Out / On Me), 컨벤션, 아직 문장을 못 잡은 구멍 목록 |
| `item-list.razor` | 아이템 이름·graphic id·hue 목록. `findtype` 인자 찍을 때 참조 |
| `vendor-prices.md` | 상점 가격표 |
| `bard-necro-summon-guide.md` | Bard Necro 소환 조합·Tome 투자 가이드 |
| `bard-necro-combat-design.md` | `bard-necro-enhanced` 전투 루프 설계. 우선순위 사다리, 마나 예산, Grimoire·Codex 배분 |
| `bard-mechanics.md` | **바드 메커니즘 레퍼런스.** 쿨다운·송·바딩 브레이크·코덱스 원문. 바드 숫자는 여기서 인용한다 |

## Razor 스크립트 컨벤션

기준 파일은 `script/combat/bard-throwing.razor` 와 `script/restock/loadout.razor`. 새 코드는 이 규칙을 따르고,
아직 옮기지 못한 파일을 고칠 때는 그 파일 스타일을 유지한다.

**헤더** — 직접 만든 스크립트는 첫 줄에 한 줄 설명, 둘째 줄에 전제조건.

```
# Bard Necro main loop: sustain, bard control, necro rotation.
# Needs: organizer 1 (loot bag), cooldown "skill", hotkey "Clear Scavenger Cache", var_my_loot_chest set
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

**변수 이름** — 접두로 무엇인지 드러낸다. 단어는 snake_case, 접두는 **더블 언더스코어**로 끊는다.

| 접두 | 무엇 | 수명 |
|---|---|---|
| `config__` | 손으로 조정하는 설정. 파일 맨 위에 모아 둔다 | 실행 중 |
| `wait__` | 얼마나 쉬는지, 타겟 커서를 얼마나 기다리는지 | 실행 중 |
| `cooldown__` | `timer__` 나 `cooldown` 과 비교하는 임계값 | 실행 중 |
| `var__` | 이 스크립트가 들고 있는 상태 | 실행 중 |
| `alias__` | `find` / `findtype` 의 `as` 바인딩 결과 | 실행 중 |
| `label__` | `getlabel` 결과 | 실행 중 |
| `timer__` | `createtimer` / `settimer` 대상 | 실행 중 |
| `global__` | **프로필에 저장되고 스크립트 사이에서 공유되는 값** | 영속 |

- 실행 중만 쓰는 값은 전부 `@setvar!`. 영속은 `global__` 뿐이고 `setvar` 를 쓴다.
- **`global__` 이름을 바꾸면 프로필의 기존 항목과 연결이 끊긴다.** 이름이 곧 키라서, 바꾸면 전부 다시 타겟해야 하고 프로필에 옛 항목이 고아로 남는다. 같은 이름을 쓰는 파일이 여러 개면 한 커밋에서 같이 바꾼다.

**serial 리터럴(`0x45147618` 같은 값)을 스크립트에 쓰지 않는다.** `script/` 는 공유 파일이라 남의 컨테이너 번호가
pull 한 사람 모두의 게임에 들어간다. 개인 값은 프로필에 저장하고 스크립트에는 이름만 남긴다.

```
if not varexist global__my_loot_chest
    overhead "[ loot chest, pick ]" 55
    setvar global__my_loot_chest
endif
```

`setvar 이름` 은 타겟을 요구하고 그 serial 을 프로필 script variable 로 저장한다.

**`varexist` 는 선언 여부만 본다.** 잘못 타겟한 값이 들어 있어도 참이라 영영 안 고쳐진다. 그 물건 앞에 서 있는 것이
보장되는 스크립트에서는 `find` 로 실제 유효성까지 확인하고, 아니면 다시 요구한다.

```
if not varexist global__my_loot_chest or not find global__my_loot_chest ground -1 -1 3
    unsetvar global__my_loot_chest
    overhead "[ loot chest, pick ]" 55
    setvar global__my_loot_chest
endif
```

`find` 는 클라이언트가 지금 인식하는 것만 찾으므로, 집에 있는 상자를 던전에서 검사하면 멀쩡한 값을 지운다.
**대상 앞에 서 있는 것이 확실한 곳에만** 붙인다.

**산술을 쓰지 않는다.** `@setvar! var__n var__n + 1` 같은 식은 저장소에 선례가 없고 Razor 가 받는지 확인되지 않았다.
개수가 필요하면 `counttype` 으로 실제 상태를 다시 읽는다.
**변수의 크기 비교도 안 된다.** `if var__a >= var__b` 는 조용히 거짓이다 (네크로 로테이션이 그래서 한 번도 안 나갔다). 변수는 `=` 만 쓰고,
세어야 하면 리스트에 밀어 넣고 `list 'name' >= n` 으로 비교한다. `mana >= config__x` 처럼 **내장 식이 왼쪽**에 오는 비교는 된다.

**타이머**
- `if not timerexists "x_timer"` → `createtimer` → `settimer`. 이름은 `_timer` 접미.
- 시간 제어는 타이머 기본. `cooldown` 명령은 기존 파일이 이미 그 스타일일 때만.

**그 외**
- 시스템 메시지 띄우면 안 되는 명령은 `@` 접두.
- 검색은 `if findtype "name" backpack as found_x` 로 alias에 담아 재사용. 반복 검색은 `ignore` / `clearignore`.
- **`rename` 의 이름 인자는 따옴표 리터럴만.** 변수로 넘기면 서버가 `That name is unacceptable.` 로 거부한다.
- **`as` alias 는 그것을 묶은 `if` / `while` 블록 안에서만 산다.** 밖에서 읽으면 `4294967295` (없는 serial) 가 된다. 블록 밖으로 가져가려면 안에서 `@setvar! var__x alias__x` 로 복사한다. 모빌도 `findtype` 으로 잡힌다 (바디 번호나 이름, 둘 다 `as` 가 묶인다). 바디 번호는 인게임 `>info` 로 읽는다.
- 라벨 분기는 `getlabel` → `if "문자열" in label`.
- 검프·핫바는 `gumpexists` / `ingump` 확인 후 `gumpresponse`.
- 디버그 출력은 `{{var}}` 보간. 확인 끝나면 지운다.

**`overhead` 형식** — 전부 `[ 대상, 상태 ]` 소문자. 시전 알림만 `[ 대상 ]`. 단어와 hue 는 `library/overheads.md` 의
글로서리와 팔레트를 따르고, 쿨다운 바 이름(`cooldown "heal pot"`)도 같은 단어를 쓴다. 새 단어를 만들기 전에 그 문서를 본다.

| 색 | 용도 | 예 |
|---|---|---|
| 90 | 상태, 정보. `config__chatty` 로 끈다 | `[ target, set ]` |
| 53 | 경고, 재고 없음, 시전 끊김 | `[ heal pot, out ]` `[ heal, disturbed ]` |
| 33 | 에러, 그것 없이는 못 도는 것 | `[ inst, out ]` |
| 43 | 내 공격이 먹힘 | `[ hams, target ]` |
| 68 | 준비됨 | `[ hide, ready ]` |
| 118 | 능력 · 네크로 시전 알림 | `[ blood oath ]` |
| 83 | 매저리 시전 알림 | `[ curse ]` |
| 55 | 선택 프롬프트, 라벨 출력 | `[ inst, pick ]` |
| 705 | 상대 머리 위 표시. `overhead "…" 705 <serial>` | `[ target, set ]` |

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
- Razor는 스크립트 본문을 메모리에 캐시한다. 파일을 고친 뒤에는 Razor의 Scripts 탭을 다시 열거나 우클릭 → Reload all scripts 를 해야 반영된다.
  - **`Reload all scripts` 는 핫키에 바인딩된 스크립트를 갱신하지 못한다.** 리로드는 기존 객체를 교체하지 않고
    **새 객체를 목록에 덧붙인다.** 프로필에는 바인딩이 객체가 아니라 이름(`Play Script: hotkey\bard-buff`)으로
    저장돼 있어서, 키를 누르면 같은 이름 중 **맨 앞의 옛 객체**가 잡힌다. 증상은 이렇게 나타난다.
    - Scripts 탭의 Play 버튼 → 새 본문이 돈다
    - 핫키 → 옛 본문이 돈다
    - Hotkeys 목록에 `Play Script: ... (not assigned)` 가 리로드할 때마다 한 줄씩 쌓인다 (메모리에만, 파일엔 안 남는다)
  - **핫키 동작까지 확인해야 하면 클라이언트를 껐다 켠다.** 리로드로는 절대 안 된다.
    반복 테스트 중에는 핫키에 물리지 말고 Scripts 탭 Play 로 돌리면 리로드만으로 충분하다.
  - **파일을 고쳤는데도 스크립트 에러가 같은 줄번호를 계속 가리키면 캐시를 의심한다.** 줄을 지웠으면 그 아래 줄번호가
    같이 움직여야 하는데 안 움직인다는 뜻이다. Reload all scripts 로 안 풀리면 클라이언트를 완전히 껐다 켠다.
  - 캐시가 옛 본문을 들고 있는 상태로 Razor를 끄면 그 본문을 파일에 다시 쓴다. 외부 에디터로 고친 내용이 되돌아갈 수 있으니
    종료 후 `git status` 로 확인한다. 검증 절차에 이 두 가지를 명시한다.
    - 리로드를 반복하면 **옛 본문을 든 객체가 계속 쌓이므로 이 위험이 같이 커진다.** 이것도 재시작이 답이다.
    - 외부 에디터로 스크립트를 고치는 프로필은 Razor 설정 `AutoSaveScript` 를 꺼 둔다.
  - Razor 편집기에 직접 붙여넣으면 기존 객체의 본문이 바뀌므로 핫키도 새 본문을 쓴다. 다만 그 순간부터
    **Razor가 그 파일의 주인**이 되니, 외부 에디터 편집과 섞지 않는다.
- **`config/` 아래 파일은 종료 시 클라이언트가 통째로 덮어쓴다.** Razor 프로필 xml 뿐 아니라
  ClassicUO 의 `cooldowns.xml`, `macros.xml` 등 전부 해당된다. **게임을 끈 상태에서만 수정한다.**
  켜둔 채로 고치면 종료할 때 조용히 사라진다. 실제로 한 번 날아갔다.
- 새 템플릿 스크립트를 만들면 `library/templates.md` 에 한 줄 추가한다.

## 커밋

- 제목 한 줄, 영어, 마침표 없음. 본문·트레일러·`Co-Authored-By` 는 넣지 않는다.
- Conventional Commits 접두(`feat:`, `fix:`)를 쓰지 않는다. 동사로 시작하는 평서문.
  - 좋음: `Regroup scripts by activity`, `Add eval rotation to bard-necro`, `Fix stuck target loop in bard-mace`
  - 나쁨: `feat: regroup`, `update`, `스크립트 수정`
- 한 커밋에 한 가지 변경. 스크립트 수정과 문서 수정이 독립적이면 나눈다.
- 사용자가 커밋하라고 할 때만 커밋한다. push 는 별도 요청이 있을 때만.
