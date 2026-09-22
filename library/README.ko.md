# uoo

[English](../README.md) · **한국어**

**[Ultima Online Outlands](https://uooutlands.com/)** 용 Razor 스크립트와 클라이언트 설정.

![Outlands](https://img.shields.io/badge/UO-Outlands-8b1a1a) ![Razor](https://img.shields.io/badge/Razor-Outlands%20fork-2b6cb0) ![License](https://img.shields.io/badge/license-MIT-green)

Outlands 클라이언트에 딸려오는 Razor 빌드와 그 확장 문법(`findtype … as`, `getlabel`, `in`, 타이머,
`gumpexists`, `followers`) 기준입니다. 일반 Razor CE나 UOSteam 에서는 돌아가지 않습니다.
문법 참고: [Outlands 위키 Razor Scripting](https://wiki.uooutlands.com/Razor_Scripting).

## 구조

```
script/            모두가 공유
  combat/          사냥 중 계속 돌리는 메인 루프, 템플릿당 하나
  hotkey/          키에 물리는 한 방 매크로: 무기 스왑, 드레스, 타겟 취소, 바드 버프
  home/            집·은행 작업: 로드아웃, 케그·룬북 리필, 루팅 정리, 셸프 로드아웃
  field/           사냥터에서 전투 외 작업: recycle, moongate
  skill/           스킬 트레이닝
  gather/          채광, 벌목
config/<이름>/     사람마다 폴더 하나
  razor/           Razor 프로필: 핫키, 에이전트, 쿨다운 바, script variable
  classicuo/       캐릭터마다 폴더 하나: 매크로, 스킬 그룹, 옵션
library/           참고 자료: 아이템 graphic ID, 키 배치, 가이드, 템플릿 ↔ 스크립트 매핑
util/
  setup.sh         게임 폴더를 이 저장소로 링크 (macOS / Sikarugir)
  check.sh         if/endif, while/endwhile, for/endfor 짝 검사
```

폴더는 *언제* 돌리는지, 파일명은 *무엇을* 하는지 말합니다. 전투 루프는 템플릿 이름(`bard-necro`,
`hally-mage`), 변형은 접미사(`-eval`, `-no-potion`), 나머지는 `동사-대상`(`refill-keg`, `pull-loot`).

## 전투 루프

| 스크립트 | 템플릿 |
|---|---|
| `bard-necro`, `bard-necro-eval` | Discord / Peace / Provo + Necromancy + Spirit Speak. `-eval` 은 Eval Int 딜 로테이션 추가 |
| `bard-mace` | 메이스 바드 덱서 |
| `bard-mage`, `bard-mage-summon` | 바드 메이지, 소환 없는 것과 있는 것 |
| `bard-archer`, `bard-archer-no-potion` | 바드 아처 |
| `hally-mage` | 무기 스왑 메이지: 할버드 / 카타나 / 바이킹 소드 |
| `dexxer-basic` | 최소 덱서 유지 루프: 밴디지, 포션, 힐링 |
| `backstab-mugging` | 스텔스 백스탭 도적 |
| `sea-cleaner` | 항해용 스텔스 덱서 |

모든 루프는 같은 골격입니다. 준비(변수, 타이머) → 악기 / 핫바 확인 → 생존·제어·딜을 처리하는
`while not dead` 루프 하나.

## 스크립트 쓰는 방법

몇 개만 쓰고 싶으면 `.razor` 파일을 Razor `Scripts` 폴더에 복사하면 끝입니다. 여기서 그만 읽어도 됩니다.

저장소에서 바로 돌리고, 내 설정도 git 으로 관리하고, 수정도 올리고 싶으면 clone 하고 `util/setup.sh`
를 한 번 실행합니다. 아래는 전부 그 얘기입니다.

## Setup

### 무엇을 하나

게임 설치 폴더 안의 세 폴더가 내 clone 을 가리키는 링크로 바뀝니다. 그 뒤로 클라이언트는 저장소를
직접 읽고 씁니다. 복사도 동기화도 없습니다.

```
Ultima Online Outlands/ClassicUO/
  settings.json                          링크 안 함: 로그인 정보
  Data/Plugins/Assistant/                Razor
    Scripts/     =>  uoo/script/                          공유
    Profiles/    =>  uoo/config/<이름>/razor/profiles/    내 것, Razor 프로필마다 .xml 하나
  Data/Profiles/<계정>/Outlands/
    CharA/       =>  uoo/config/<이름>/classicuo/CharA/   내 것, 캐릭터마다 폴더 하나
```

다른 사람의 수정은 내가 `git pull` 할 때만 내 PC 에 오고, 내 수정은 내가 `git push` 할 때만 갑니다.

### 실행

```sh
util/setup.sh                    # <이름> = git 이메일 첫 토큰: jane.doe@example.com -> config/jane/
util/setup.sh <이름>             # 직접 정해도 됨
util/setup.sh [<이름>] /path/to/ClassicUO/Data/Plugins/Assistant/Razor.exe   # Razor.exe 가 ~/Applications 밖일 때
util/setup.sh --undo             # 실제 폴더로 되돌리기
```

macOS(Sikarugir) 에서는 래퍼 안의 `Razor.exe` 를 찾아, Razor 프로필과 캐릭터 폴더를 `config/<이름>/`
으로 옮기고 그 자리에 링크를 남깁니다.

- **묻는 건 하나.** `config/<이름>/` 에 이미 파일이 있으면(두 번째 PC, 이름 바꾼 폴더, 또는 남의 이름)
  게임을 그쪽으로 연결하기 전에 물어봅니다.
- **지우지 않습니다.** 빈 폴더와, 저장소가 이미 가진 파일만 든 `Scripts` 폴더는 치웁니다. 그 외는
  원래 자리 옆에 `Scripts-bak`, `Profiles-bak`, `<캐릭>-bak` 으로 남습니다. 확인 후 지우세요.
- **언제든 다시 실행.** 이미 링크된 폴더는 건너뛰고, 새 캐릭터는 링크합니다.
- **`--undo`** 는 실제 폴더를 다시 만들고 링크가 가리키던 내용을 복사해 넣습니다. 저장소 파일은
  전부 그대로입니다.
- **이름 바꾸기:** `git mv config/<옛> config/<새>` 뒤에 `util/setup.sh <새>`. 한 번 묻고 다시 잇습니다.

Windows 는 관리자 PowerShell 에서 디렉터리 정션으로:

```powershell
$ASSIST = "C:\Program Files (x86)\Ultima Online Outlands\ClassicUO\Data\Plugins\Assistant"
Rename-Item "$ASSIST\Scripts" Scripts-bak
cmd /c mklink /J "$ASSIST\Scripts" "C:\src\uoo\script"
# $ASSIST\Profiles 와 ClassicUO\Data\Profiles\<계정>\<서버>\<캐릭> 도 같은 식으로
```

### 평소에

- **게임 → 저장소.** Razor 는 종료할 때 프로필 xml 을 쓰고, ClassicUO 는 로그아웃할 때 캐릭터 파일을
  쓰고, Razor 편집기에서 저장한 스크립트는 즉시 바뀝니다. `git status` 로 보고 남길 것만 커밋하세요.
- **저장소 → 게임.** Razor 는 스크립트 본문을 캐시합니다. 스크립트를 고쳤거나 pull 했으면 Scripts 탭을
  클릭하거나(우클릭 → *Reload all scripts*) 다음에 실행하세요. 프로필 xml 은 시작할 때 읽고 종료할 때
  덮어쓰니 **게임을 끈 상태에서** 고치거나 pull 하세요.
- **캐릭터.** Razor 프로필은 캐릭터 단위가 아닙니다. Profile 탭에서 캐릭터마다 골라 두면 `chars.lst`
  에 기억됩니다. ClassicUO 설정은 원래 캐릭터별입니다.
- **다중 클라, 두 번째 PC.** 클라를 여러 개 켜도 같은 설치·같은 링크라 달라지는 게 없습니다. 다른
  PC 에서는 같은 명령을 같은 이름으로 실행하고 `y`.

## 공유

push 는 collaborator 만 할 수 있습니다. 나머지는 clone 이나 fork 를 해서, 원하면 자기 사본에
`setup.sh` 를 돌리고, 고친 게 있으면 pull request 를 보냅니다. `setup.sh` 는 실행한 PC 만 건드립니다.

`script/` 는 공유, `config/<이름>/` 은 사람별이라 겹치지 않고, 남이 핫키나 organizer 를 어떻게 짰는지
읽어볼 수는 있습니다.

**개인 값은 스크립트에 넣지 않습니다.** 공유 스크립트에 적은 컨테이너 serial 은 pull 한 모두에게
*남의* 컨테이너가 됩니다. 프로필에 두세요:

```
if not varexist var_my_loot_chest
	overhead "Target your loot chest" 55
	setvar var_my_loot_chest
endif
```

`setvar` 는 타겟을 한 번 요구하고 그 serial 을 내 프로필에 저장합니다. 스크립트에는 이름만 남습니다.
`home/`, `gather/` 의 오래된 스크립트 몇 개에 아직 serial 이 박혀 있고, 바꿔가는 중입니다.

`config/<이름>/` 에 들어가는 것:

| 파일 | 내용 | 추적 |
|---|---|---|
| `razor/profiles/<프로필>.xml` | 핫키, 에이전트(organizer / restock / dress 목록, 컨테이너 serial), 필터, 쿨다운 바, script variable, 창 배치 | 함 |
| `razor/profiles/chars.lst` | 캐릭터마다 마지막에 쓴 프로필 | 함 |
| `classicuo/<캐릭>/macros.xml`, `skillsgroups.xml`, `infobar.xml` | 클라 매크로, 스킬 그룹, 인포바 | 함 |
| `classicuo/<캐릭>/profile.json` | 클라 옵션과 창 위치, 세션마다 바뀜 | 함, 노이즈 있음 |
| `classicuo/<캐릭>/gumps.xml`, `*.bak1..3`, `*.backup1..3` | 열린 창 상태, 자동 백업 | ignore |
| `ClassicUO/settings.json` | 해상도, fps, **username / password** | ignore, 링크 안 함 |

## 도구

```sh
util/check.sh                       # 모든 스크립트
util/check.sh script/combat/bard-necro.razor
```

Razor 에는 린터가 없고, 빠진 `endif` 가 스크립트가 조용히 이상해지는 가장 흔한 원인입니다.
`check.sh` 는 짝이 안 맞는 블록을 줄 번호와 함께 알려줍니다. bash 와 awk 만 씁니다.

## Library

- `item-list.razor` — `findtype` 용 아이템 이름, graphic ID, hue
- `hotkeys.md` — 키 배치와 주문 데미지 메모
- `templates.md` — 템플릿마다 어느 루프, 핫키, 셸프 로드아웃, 프로필을 쓰는지
- `bard-necro-summon-guide.md` — 소환 조합과 Summoner's Tome 투자 순서
- `vendor-prices.md` — 상점 가격표

## 크레딧

- [Jaseowns](https://outlands.uorazorscripts.com/) — 채광, 벌목, recycle, 스킬 트레이너는 그의 스크립트이거나 그것을 바탕으로 함
- Demlar — 드레스 스크립트 아이디어
- raveX — 스틸 트레이너
- [outlandsbutler.com](https://www.outlandsbutler.com/) — `shelf-*` 로드아웃 스크립트 생성

나머지는 [MIT](../LICENSE). 제3자 스크립트는 원저자의 조건을 따릅니다. UO Outlands 와 무관합니다.
