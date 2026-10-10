# UOO 문서

Ultima Online Outlands Razor 스크립트의 작성과 수정 기준.
시작은 [Workflow](working/workflow.md). 문서 작성 기준은 [Writing](working/writing.md).

언제나 지킬 규칙과 커밋 규칙: [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md). 나머지 규칙: 아래 문서.

## 묶음

| 묶음 | 폴더 | 내용 |
| --- | --- | --- |
| How we work | `working/` | 작업 순서, 문서 쓰는 법 |
| Scripting | `scripting/` | 스크립트 규칙, Razor 문법, 모듈 조립, 머리 위 알림 |
| Game reference | `game/` | 게임 규칙과 자료. PvP, 핫키, 아이템 번호 |
| Templates | `templates/` | 템플릿별 판단과 설계 |
| Open questions | `questions/` | 아직 확인 못 한 것 |

## 문서

문서별 정본은 이 표 한 곳. 같은 내용은 다시 쓰지 않고 이 표의 문서로 링크.

| 문서 | 정본인 내용 |
| --- | --- |
| [Workflow](working/workflow.md) | 근거의 우선순위와 참고 사이트, 스크립트 수정 순서, 변경 보고, 게임 반영과 확인 |
| [Writing](working/writing.md) | 문서 작성. 새 문서, frontmatter, 짜임, 문장, Markdown, 언어와 번역본, 흐름도, 끝낼 때 확인 |
| [Conventions](scripting/conventions.md) | 폴더와 파일 이름, 스크립트 모양과 배너, 변수 접두, serial, 타이머 관용구, 편집기 하이라이팅 |
| [Razor](scripting/razor.md) | Outlands Razor 확장 문법, 확인된 함정, 되는 구문의 선례, 명령문 비용, PvP 명령 제약 |
| [Modules](scripting/modules.md) | 모듈 폴더, 레시피와 모듈 형식, 조립 규칙, base와 블록 사이 신호, 옮긴 기록 |
| [Overheads](scripting/overheads.md) | 알림의 세 경로, `[ 대상, 상태 ]` 형식, 어휘, hue, 쿨다운 바, 프로필 오버헤드 표 |
| [PvP](game/pvp.md) | 템플릿과 무관한 PvP 규칙과 숫자 |
| [Hotkeys](game/hotkeys.md) | 키 배치, 주문 데미지 메모 |
| [Item list](game/item-list.md) | 아이템 이름, graphic id, hue |
| [Bard Necro](templates/bard-necro.md) | Bard Necro 메커니즘, 소환수, 전투 루프 설계, PvP 판단, 인게임 확인 |
| [Lumberjack PvP](templates/lumberjack-pvp.md) | 벌목과 PvP 템플릿의 스킬, 스탯, 도끼 선택, 마나 예산, 교전 분기, 구현 요구사항 |
| [Open items](questions/open-items.md) | 사용자에게 물을 것. 뜨지 않는 바, 규칙과 어긋난 줄, 출처 없는 숫자, 인게임 확인 목록 |

저장소 안내(GitHub):

- 스크립트 폴더와 전투 루프: [script/README.md](https://github.com/minu-ha/uoo/blob/master/script/README.md)
- 게임을 저장소에 연결하는 법: [config/README.md](https://github.com/minu-ha/uoo/blob/master/config/README.md)

## 읽는 법

저장소 루트에서 `pnpm install` 한 번 → `pnpm docs:dev` → [localhost:4321](http://localhost:4321).
