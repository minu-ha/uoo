# UOO 문서

Ultima Online Outlands에서 돌리는 Razor 스크립트를 만들고 고칠 때 보는 문서다.
처음이면 [Workflow](working/workflow.md)부터 읽는다. 문서를 고치거나 새로 쓰는 법은 [Writing](working/writing.md)에 있다.

에이전트가 언제나 지킬 규칙과 커밋 규칙은 [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md)에 있다. 나머지 규칙은 모두 아래 문서에 있다.

## 묶음

| 묶음 | 폴더 | 담는 것 |
| --- | --- | --- |
| How we work | `working/` | 일하는 순서와 문서 쓰는 법 |
| Scripting | `scripting/` | 스크립트 규칙, Razor 문법, 모듈 조립, 머리 위 알림 |
| Game reference | `game/` | 게임 규칙과 자료. PvP, 핫키, 아이템 번호 |
| Templates | `templates/` | 캐릭터 템플릿마다 내린 판단과 설계 |
| Open questions | `questions/` | 아직 확인하지 못한 것 |

## 문서

어느 문서가 무엇의 정본인지는 이 표 한 곳에 둔다. 같은 내용은 다른 문서에 다시 쓰지 않고 이 표의 문서로 링크한다.

| 문서 | 정본인 내용 |
| --- | --- |
| [Workflow](working/workflow.md) | 근거의 우선순위와 참고 사이트, 스크립트 고치는 순서, 변경 보고, 게임에 반영하고 확인하는 법 |
| [Writing](working/writing.md) | 문서 쓰는 법. 새 문서, frontmatter, 짜임, 문장, Markdown, 글의 언어와 번역본, 흐름도, 끝낼 때 확인 |
| [Conventions](scripting/conventions.md) | 폴더와 파일 이름, 스크립트 모양과 배너, 변수 접두, serial, 타이머 관용구, 편집기 하이라이팅 |
| [Razor](scripting/razor.md) | Outlands Razor 확장 문법, 확인된 함정, 되는 구문의 선례, 명령문 비용, PvP 명령 제약 |
| [Modules](scripting/modules.md) | 모듈 폴더, 레시피와 모듈의 형식, 조립 규칙, base와 블록이 주고받는 신호, 옮긴 기록 |
| [Overheads](scripting/overheads.md) | 알림의 세 경로, `[ 대상, 상태 ]` 형식, 어휘, hue, 쿨다운 바, 프로필 오버헤드 표 |
| [PvP](game/pvp.md) | 템플릿과 상관없는 PvP 규칙과 숫자 |
| [Hotkeys](game/hotkeys.md) | 키 배치와 주문 데미지 메모 |
| [Item list](game/item-list.md) | 아이템 이름, graphic id, hue |
| [Bard Necro](templates/bard-necro.md) | Bard Necro의 메커니즘, 소환수, 전투 루프 설계, PvP 판단, 인게임 확인 |
| [Lumberjack PvP](templates/lumberjack-pvp.md) | 벌목과 PvP 템플릿의 스킬, 스탯, 도끼 선택, 마나 예산, 교전 분기와 구현 요구사항 |
| [Open items](questions/open-items.md) | 사용자에게 물을 것. 뜨지 않는 바, 규칙과 어긋난 줄, 출처 없는 숫자, 인게임 확인 목록 |

저장소 안의 다른 안내는 GitHub에서 본다.
스크립트 폴더와 전투 루프는 [script/README.md](https://github.com/minu-ha/uoo/blob/master/script/README.md)에,
게임을 저장소에 연결하는 법은 [config/README.md](https://github.com/minu-ha/uoo/blob/master/config/README.md)에 있다.

## 읽는 법

저장소 루트에서 `pnpm install`을 한 번 하고, `pnpm docs:dev`로 [localhost:4321](http://localhost:4321)에 띄운다.
