# AGENTS.md

Ultima Online Outlands용 Razor 스크립트 (`script/`), 클라이언트 설정 사본 (`config/`), 설계 문서 (`document/`).
규칙과 정책은 전부 `document/`에 있고, 이 파일은 **언제 무엇을 읽는지**만 가리킨다. 작업을 시작하면 [document/working/workflow.md](document/working/workflow.md)부터 읽는다.
설계 문서는 [for humanity](https://for-humanity.fyi)로 읽는 Markdown이다. 사람은 `pnpm docs:dev`로 띄워 브라우저로 읽고, 홈은 [document/README.md](document/README.md)다.

## 목차

1. [항상 지키는 것](#1-항상-지키는-것)
   - [커밋](#커밋)
2. [언제 무엇을 읽나](#2-언제-무엇을-읽나)
3. [문서 지도](#3-문서-지도)

---

## 1. 항상 지키는 것

한 줄씩만 적는다. 이유와 자세한 규칙은 링크한 곳에 있다.

- 문서와 답변은 한국어, 스크립트 안 주석은 영어 → [workflow.md](document/working/workflow.md#05.A) 05.A절
- `.razor`를 고치기 전에 대상 파일을 끝까지 읽고 확인된 함정 표를 본다 → [razor.md](document/scripting/razor.md#03) 03절
- `config/` 아래는 게임을 끈 상태에서만 고친다 → [workflow.md](document/working/workflow.md#04.C) 04.C절
- 다른 사람의 `config/`는 건드리지 않고, `settings.json`은 절대 커밋하지 않는다 → [conventions.md](document/scripting/conventions.md#01.D) 01.D절
- 스크립트에 serial 리터럴을 쓰지 않는다 → [conventions.md](document/scripting/conventions.md#03.C) 03.C절
- 생성된 루프 (`script/combat/*`, `script/gather/*`)는 직접 고치지 않는다. `module/`·`recipe/`를 고치고 `pnpm build` (`node util/build-scripts.mjs`)로 만든다 → [modules.md](document/scripting/modules.md#07) 07절
- 커밋은 아래 [커밋](#커밋) 규칙을 따른다

### 커밋

커밋 규칙의 정본은 여기다. 좋은 제목과 나쁜 제목의 예는 [workflow.md](document/working/workflow.md#06) 06절에 있다.

- 커밋은 사용자가 하라고 할 때만, push는 따로 요청이 있을 때만 한다.
- 한 커밋에 한 가지 변경. 스크립트 수정과 문서 수정이 서로 독립이면 나눈다.
- 제목은 영어 한 줄, 동사 원형으로 시작하고 마침표를 찍지 않는다. `feat:` `fix:` 같은 Conventional Commits 접두는 쓰지 않는다.
- 본문과 트레일러 (`Co-Authored-By` 등)는 넣지 않는다.
- 요청 범위의 파일만 넣는다. `config/`의 게임 설정 변경과 `settings.json`은 따로 요청이 없으면 넣지 않는다.
- 커밋 전에 `pnpm check`와 `git diff --check`를 돌린다. `util/`을 고쳤으면 `pnpm test`도 돌린다.
- 예: `Port the loop builder to Node`, `Keep every summon name two letters away from the creature words`

## 2. 언제 무엇을 읽나

| 할 일                                   | 읽을 것                                                                                                                          |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 무엇이든 시작할 때                      | [workflow.md](document/working/workflow.md)                                                                                             |
| `.razor`를 고치거나 새로 쓸 때          | [conventions.md](document/scripting/conventions.md), [razor.md](document/scripting/razor.md), 알림을 띄우면 [overheads.md](document/scripting/overheads.md) |
| 모듈·레시피를 고치거나 루프를 조립할 때 | [modules.md](document/scripting/modules.md)                                                                                               |
| 파일을 새로 만들거나 이름을 지을 때     | [conventions.md](document/scripting/conventions.md#01) 01절                                                                               |
| 고친 것을 게임에서 확인할 때            | [workflow.md](document/working/workflow.md#04) 04절                                                                                     |
| `config/`를 고칠 때                     | [workflow.md](document/working/workflow.md#04.C) 04.C절, [config/README.md](config/README.md)                                           |
| 오버헤드나 쿨다운 바를 더하거나 바꿀 때 | [overheads.md](document/scripting/overheads.md)                                                                                           |
| 바드·네크로·소환수 숫자가 필요할 때     | [bard-necro.md](document/templates/bard-necro.md)                                                                       |
| PvP 규칙이 필요할 때                    | [pvp.md](document/game/pvp.md)                                                                                                       |
| 벌목·PvP 템플릿과 교전을 볼 때          | [lumberjack-pvp.md](document/templates/lumberjack-pvp.md)                                                               |
| 키 배치를 볼 때                         | [hotkeys.md](document/game/hotkeys.md)                                                                                               |
| `findtype` 인자 (graphic id, hue)       | [item-list.md](document/game/item-list.md)                                                                                           |
| 문서를 고치거나 새로 만들 때            | [writing.md](document/working/writing.md)                                                                                               |
| 사용자에게 물을 것이 남았을 때          | [open-items.md](document/questions/open-items.md)                                                                                         |
| 커밋할 때                               | 이 파일의 [커밋](#커밋), 제목의 예는 [workflow.md](document/working/workflow.md#06) 06절                                                |

## 3. 문서 지도

| 파일                                                                         | 무엇의 정본                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [document/README.md](document/README.md)                                   | 문서 사이트의 홈: 묶음별 문서 표, 사이트를 띄우는 법                                        |
| [document/for-humanity.config.mjs](document/for-humanity.config.mjs)       | 사이트 이름, 사이드바 묶음 순서, 상태 문구 (`인게임 확인됨`, `확인되지 않았다`)             |
| [document/working/writing.md](document/working/writing.md)                                 | 설계 문서를 쓰는 법: 새 문서, frontmatter, 짜임, 번호와 가름, 본문, 흐름도, 끝낼 때 확인    |
| [document/working/workflow.md](document/working/workflow.md)                               | 근거 우선순위와 참고 사이트, 작업 순서, 변경 보고, 게임 반영·검증, 글의 언어와 번역본, 커밋 |
| [document/scripting/modules.md](document/scripting/modules.md)                                 | 모듈 폴더, 레시피와 모듈 형식, 조립 규칙, base와 블록끼리의 신호, 옮긴 기록                 |
| [document/scripting/conventions.md](document/scripting/conventions.md)                         | 폴더와 파일 이름, 스크립트 모양과 배너, 변수 접두, serial, 타이머 관용구, 편집기 하이라이팅 |
| [document/scripting/razor.md](document/scripting/razor.md)                                     | Outlands Razor 확장 문법, 확인된 함정, 되는 구문의 선례, 명령문 비용, PvP 명령 제약         |
| [document/scripting/overheads.md](document/scripting/overheads.md)                             | 알림 세 경로, `[ 대상, 상태 ]` 형식, 어휘, hue, 쿨다운 바, 프로필 오버헤드 표               |
| [document/game/pvp.md](document/game/pvp.md)                                         | 템플릿과 무관한 PvP 규칙과 숫자                                                             |
| [document/templates/bard-necro.md](document/templates/bard-necro.md)         | Bard Necro의 메커니즘, 소환수, 전투 루프 설계, PvP 판단, 인게임 확인                        |
| [document/templates/lumberjack-pvp.md](document/templates/lumberjack-pvp.md) | 벌목·PvP 템플릿의 스킬·스탯·도끼 선택, 마나 예산, 교전 분기와 구현 요구사항                 |
| [document/game/hotkeys.md](document/game/hotkeys.md)                                 | 키 배치와 주문 데미지 메모                                                                  |
| [document/questions/open-items.md](document/questions/open-items.md)                           | 사용자에게 물을 것으로 남긴 것: 뜨지 않는 바, 규칙과 어긋난 줄, 출처 없는 숫자, 규칙 해석   |
| [document/game/item-list.md](document/game/item-list.md)                             | 아이템 이름·graphic id·hue                                                                  |
| [script/README.md](script/README.md)                                         | 스크립트 폴더 구성, 전투 루프 ↔ 템플릿                                                      |
| [config/README.md](config/README.md)                                         | 게임을 저장소에 링크하는 방법, 설정 파일별 설명                                             |
| [language/](language/)                                                       | README 번역본                                                                               |
