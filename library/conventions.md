# 저장소와 스크립트 규칙

파일을 어디에 두고 어떻게 이름 짓는가, 스크립트를 어떤 모양으로 쓰는가.
문법 자체 (되는 구문, 함정)는 [razor.md](razor.md), 머리 위 메시지는 [overheads.md](overheads.md).

## 목차

1. [저장소 구조](#1-저장소-구조)
    - 1.1 [폴더](#11-폴더)
    - 1.2 [script 분류와 파일명](#12-script-분류와-파일명)
    - 1.3 [파일 규칙](#13-파일-규칙)
    - 1.4 [config 는 사람별](#14-config-는-사람별)
2. [스크립트 모양](#2-스크립트-모양)
    - 2.1 [기준 파일](#21-기준-파일)
    - 2.2 [헤더](#22-헤더)
    - 2.3 [주석](#23-주석)
    - 2.4 [시작 4줄과 들여쓰기](#24-시작-4줄과-들여쓰기)
    - 2.5 [구조와 섹션 배너](#25-구조와-섹션-배너)
3. [변수](#3-변수)
    - 3.1 [접두](#31-접두)
    - 3.2 [실행 중 값과 영속 값](#32-실행-중-값과-영속-값)
    - 3.3 [serial 리터럴 금지](#33-serial-리터럴-금지)
    - 3.4 [varexist 는 선언 여부만 본다](#34-varexist-는-선언-여부만-본다)
4. [타이머](#4-타이머)
5. [그 외 관용구](#5-그-외-관용구)
6. [overhead](#6-overhead)
7. [PvP 겸용 스크립트](#7-pvp-겸용-스크립트)

---

## 1. 저장소 구조

### 1.1 폴더

| 폴더        | 무엇                                                                                                                     |
|-------------|--------------------------------------------------------------------------------------------------------------------------|
| `script/`   | Razor 스크립트. 모두가 공유한다                                                                                          |
| `config/`   | 사람마다 클라이언트 설정 원본 하나 (`config/<이름>/`). 링크 방식과 파일별 설명은 [config/README.md](../config/README.md) |
| `library/`  | 참고 문서. 무엇이 있는지는 [AGENTS.md](../AGENTS.md) 의 문서 지도                                                        |
| `language/` | README 번역본. 규칙은 [workflow.md](workflow.md) 5.4절                                                                   |
| `util/`     | `setup.sh` (게임을 저장소에 링크), `check.sh` (스크립트 블록 짝과 미선언 변수 검사)                                      |

웹/서버 프로젝트가 아니다. 빌드·린트·테스트 러너가 없고, 동작 검증은 인게임에서만 된다.

### 1.2 script 분류와 파일명

`script/` 는 **언제 돌리는 스크립트인지**로 나눈다. 파일명만 봐도 뭔지 알 수 있어야 한다.

| 폴더              | 언제                                           | 파일명 규칙                                    | 예                                                    |
|-------------------|------------------------------------------------|------------------------------------------------|-------------------------------------------------------|
| `script/combat/`  | 사냥 중 계속 돌리는 메인 루프                  | `<템플릿>[-<변형>]`                            | `bard-necro-enhanced`, `bard-mace`, `hally-mage`      |
| `script/hotkey/`  | 키에 물려 한 번 실행하는 매크로                | `<동작>[-<대상>]`, 무기 스왑은 `weapon-<무기>` | `weapon-katana`, `cancel-target`, `dress`, `moongate` |
| `script/train/`   | 스킬 트레이닝                                  | `<스킬>`                                       | `magery`, `carto`                                     |
| `script/gather/`  | 채집 루프                                      | `<채집>`                                       | `mining`, `lumberjack`                                |
| `script/loot/`    | 주워온 것 정리·분해                            | `<동사>-<대상>`                                | `recycle`, `pull-loot`, `bank-pouch`                  |
| `script/restock/` | 나가기 전 준비: 로드아웃, 리필                 | `<동사>-<대상>`                                | `loadout`, `refill-keg`, `refill-runebook`            |
| `script/shelf/`   | outlandsbutler.com 생성 Storage Shelf 로드아웃 | `<템플릿>`                                     | `bard-dexxer`, `sailing`                              |

전투 루프와 템플릿의 대응은 [script/README.md](../script/README.md) 의 전투 루프 표가 정본이다.

### 1.3 파일 규칙

- kebab-case, 소문자, 공백 없음. 폴더가 분류를 말하므로 파일명에 `combat-` 같은 접두는 붙이지 않는다.
- 같은 성격이 3개 이상 모이면 폴더를 나누고, 2개 이하면 기존 폴더에 둔다.
- `-temp`, `-old`, `-new`, `-backup` 파일을 만들지 않는다. 이력은 git 이 가진다.
- `shelf/` 는 outlandsbutler.com 생성물. 손으로 고치지 않고 사이트에서 다시 만든다. 내 셸프 serial 이 들어 있어 사실상 개인 파일이다.
- 외부 출처 스크립트 (Jaseowns, Demlar 등)는 헤더 크레딧을 유지하고, 상단 설정 변수 위주로만 고친다.
  이 문서의 규칙과 [overheads.md](overheads.md) 의 형식도 외부 출처 파일에는 적용하지 않는다.

### 1.4 config 는 사람별

- 스크립트는 모두가 공유하고 설정은 사람마다 분리된다. **다른 사람의 `config/` 는 건드리지 않는다.**
- `settings.json` 은 계정 비밀번호가 들어 있으므로 **절대 커밋하지 않는다.**
- `config/` 아래 파일은 게임을 끈 상태에서만 고친다. 이유는 [workflow.md](workflow.md) 4.3절.

## 2. 스크립트 모양

### 2.1 기준 파일

`script/combat/bard-throwing.razor` 와 `script/restock/loadout.razor`. 새 코드는 이 규칙을 따르고,
아직 옮기지 못한 파일을 고칠 때는 그 파일 스타일을 유지한다.

### 2.2 헤더

직접 만든 스크립트는 첫 줄에 한 줄 설명, 둘째 줄에 전제조건.

```
# Bard Necro main loop: sustain, bard control, necro rotation.
# Needs: organizer 1 (loot bag), cooldown "skill", hotkey "Clear Scavenger Cache", global__my_loot_chest set
```

### 2.3 주석

- 스크립트 안 주석은 영어이고, 줄 맨 앞의 `#` 로 쓴다. `//` 는 쓰지 않는다.
- **주석에 `;` 를 쓰지 않는다.** Razor 는 주석을 걷어내기 전에 `;` 를 구문 구분자로 보기 때문에,
  주석 안의 세미콜론도 그 뒤를 명령으로 파싱해서 그 줄에서 에러가 난다. 마침표로 문장을 끊는다.

### 2.4 시작 4줄과 들여쓰기

```
clearall
clearsysmsg
cleardragdrop
clearignore
```

들여쓰기는 스페이스 4칸, 줄끝은 CRLF (Razor 가 그렇게 다시 쓴다). 탭은 쓰지 않는다.
편집기 설정은 `.editorconfig` 가 정본이다.

### 2.5 구조와 섹션 배너

`SETUP`(변수, 타이머) → 준비 (악기 선택, 핫바 확인) → `while not dead` 메인 루프 하나 → `endwhile`.

```
# ####################################################################################
# # SECTION NAME
# ####################################################################################
```

## 3. 변수

### 3.1 접두

접두로 무엇인지 드러낸다. 단어는 snake_case, 접두는 **더블 언더스코어**로 끊는다.

| 접두         | 무엇                                                                                 | 수명    |
|--------------|--------------------------------------------------------------------------------------|---------|
| `config__`   | 손으로 조정하는 설정. 파일 맨 위에 모아 둔다                                         | 실행 중 |
| `wait__`     | 얼마나 쉬는지, 타겟 커서를 얼마나 기다리는지                                         | 실행 중 |
| `cooldown__` | `timer__` 나 `cooldown` 과 비교하는 임계값                                           | 실행 중 |
| `var__`      | 이 스크립트가 들고 있는 상태                                                         | 실행 중 |
| `alias__`    | `find` / `findtype` 의 `as` 바인딩 결과                                              | 실행 중 |
| `label__`    | `getlabel` 결과                                                                      | 실행 중 |
| `timer__`    | `createtimer` / `settimer` 대상                                                      | 실행 중 |
| `list__`     | `createlist` / `pushlist` 대상. `foreach x in list__y` 의 루프 변수 `x` 는 접두 없이 | 실행 중 |
| `global__`   | **프로필에 저장되고 스크립트 사이에서 공유되는 값**                                  | 영속    |

`alias__` 는 묶은 블록 밖에서 읽지 못한다 ([razor.md](razor.md) 3절).

### 3.2 실행 중 값과 영속 값

- 실행 중만 쓰는 값은 전부 `@setvar!`. 영속은 `global__` 뿐이고 `setvar` 를 쓴다.
- **`global__` 이름을 바꾸면 프로필의 기존 항목과 연결이 끊긴다.** 이름이 곧 키라서, 바꾸면 전부 다시 타겟해야 하고 프로필에 옛 항목이 고아로 남는다.
  같은 이름을 쓰는 파일이 여러 개면 한 커밋에서 같이 바꾼다.

### 3.3 serial 리터럴 금지

**serial 리터럴 (`0x45147618` 같은 값)을 스크립트에 쓰지 않는다.** `script/` 는 공유 파일이라 남의 컨테이너 번호가
pull 한 사람 모두의 게임에 들어간다. 개인 값은 프로필에 저장하고 스크립트에는 이름만 남긴다.

```
if not varexist global__my_loot_chest
    overhead "[ loot chest, pick ]" 55
    setvar global__my_loot_chest
endif
```

`setvar 이름` 은 타겟을 요구하고 그 serial 을 프로필 script variable 로 저장한다.

### 3.4 varexist 는 선언 여부만 본다

잘못 타겟한 값이 들어 있어도 참이라 영영 안 고쳐진다. 그 물건 앞에 서 있는 것이
보장되는 스크립트에서는 `find` 로 실제 유효성까지 확인하고, 아니면 다시 요구한다.

```
if not varexist global__my_loot_chest or not find global__my_loot_chest ground -1 -1 3
    unsetvar global__my_loot_chest
    overhead "[ loot chest, pick ]" 55
    setvar global__my_loot_chest
endif
```

`find` 는 클라이언트가 지금 인식하는 것만 찾으므로, 집에 있는 상자를 던전에서 검사하면 멀쩡한 값을 지운다. **대상 앞에 서 있는 것이 확실한 곳에만** 붙인다.

## 4. 타이머

- `if not timerexists "x_timer"` → `createtimer` → `settimer`. 이름은 `_timer` 접미.
- 시간 제어는 타이머 기본. `cooldown` 명령은 기존 파일이 이미 그 스타일일 때만.
- 서버가 알려주는 쿨 (바드 스킬, 매저리 프록)은 자체 타이머로 흉내 내지 않고 `cooldown "이름"` 을 읽는다. 이유는 [overheads.md](overheads.md) 6.2절.

## 5. 그 외 관용구

- 시스템 메시지 띄우면 안 되는 명령은 `@` 접두.
- 검색은 `if findtype "name" backpack as alias__x` 로 alias 에 담아 재사용. 반복 검색은 `ignore` / `clearignore`.
- 라벨 분기는 `getlabel` → `if "문자열" in label`.
- 검프·핫바는 `gumpexists` / `ingump` 확인 후 `gumpresponse`.
- 디버그 출력은 `{{var}}` 보간. 확인 끝나면 지운다.

## 6. overhead

전부 `[ 대상, 상태 ]` 소문자. 시전 알림만 `[ 대상 ]`. 단어, hue, 어느 경로로 띄울지는 [overheads.md](overheads.md) 가 정본이다.
새 단어를 만들기 전에 그 문서의 어휘와 글로서리를 본다.

## 7. PvP 겸용 스크립트

- `if pvp` 분기를 먼저 두고, PvE 로직을 그대로 옮기지 않는다.
- 구조화 PvP · 팩션에서 막히는 명령은 [razor.md](razor.md) 7절.
