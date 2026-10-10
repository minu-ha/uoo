# AGENTS.md

Ultima Online Outlands용 Razor 스크립트 저장소다.
스크립트는 `script/`, 루프를 조립하는 블록과 레시피는 `module/`과 `recipe/`, 클라이언트 설정은 `config/`, 설계 문서는 `document/`에 있다.

이 파일에는 언제나 지킬 규칙과 커밋 규칙만 둔다. 나머지 규칙은 모두 `document/`에 있고, 3절 표에서 할 일에 맞는 문서를 찾는다.
작업을 시작하면 [Workflow](document/working/workflow.md)부터 읽는다. 사람은 `pnpm docs:dev`로 문서 사이트를 띄워 읽는다.

## 목차

1. [항상 지키는 것](#1-항상-지키는-것)
2. [커밋](#2-커밋)
3. [언제 무엇을 읽나](#3-언제-무엇을-읽나)

---

## 1. 항상 지키는 것

규칙마다 한 줄만 적는다. 이유와 자세한 내용은 링크한 절에 있다.

- 답변과 문서는 한국어로, 스크립트 안 주석은 영어로 쓴다. → [Writing](document/working/writing.md#07) 07절
- `.razor`를 고치기 전에 그 파일을 끝까지 읽고, 확인된 함정 표를 본다. → [Razor](document/scripting/razor.md#03) 03절
- 게임 숫자는 추측하지 않고, 출처나 인게임 확인 날짜를 적는다. → [Workflow](document/working/workflow.md#01.C) 01.C절
- `config/` 아래는 게임을 끈 상태에서만 고친다. → [Workflow](document/working/workflow.md#04.C) 04.C절
- 다른 사람의 `config/`는 건드리지 않는다. `settings.json`은 절대 커밋하지 않는다. → [Conventions](document/scripting/conventions.md#01.D) 01.D절
- 스크립트에 serial 숫자를 그대로 쓰지 않는다. → [Conventions](document/scripting/conventions.md#03.C) 03.C절
- 생성된 루프(`script/combat/*`, `script/gather/*`)는 직접 고치지 않는다. `module/`과 `recipe/`를 고치고 `pnpm build`로 다시 만든다. → [Modules](document/scripting/modules.md#07) 07절
- 같은 규칙이나 사실을 두 곳에 쓰지 않는다. 정본 한 곳에 쓰고 다른 곳은 링크한다. → [Writing](document/working/writing.md#08) 08절

## 2. 커밋

커밋 규칙은 여기에만 둔다.

- 사용자가 하라고 할 때만 커밋한다. push는 따로 요청이 있을 때만 한다.
- 커밋 제목은 영어 동사로 시작하고, 무엇을 바꿨는지 간단히 설명한다. 동사는 원형으로 쓰고 마침표는 찍지 않는다.
- AI 도움을 받은 커밋은 제목 끝에 ` | aa`를 붙인다. `aa`는 AI assistance를 받은 작업이라는 표시다.
- 제목 한 줄만 쓴다. 본문과 트레일러(`Co-Authored-By` 같은)는 넣지 않는다.
- `feat:`, `fix:` 같은 Conventional Commits 접두는 쓰지 않는다.
- 한 커밋에는 변경 하나만 담는다. 스크립트 수정과 문서 수정이 서로 독립이면 나눈다.
- 요청 범위의 파일만 넣는다. `config/`의 게임 설정 변경은 따로 요청이 없으면 넣지 않는다.
- 커밋 전에 `pnpm check`와 `git diff --check`를 돌린다. `util/`을 고쳤으면 `pnpm test`도 돌린다.

| 좋음                                       | 나쁨                                 | 왜                                    |
|--------------------------------------------|--------------------------------------|---------------------------------------|
| `Update favicon and add cursor face \| aa` | `Update favicon and add cursor face` | AI 도움을 받았는데 ` \| aa`가 없다    |
| `Regroup scripts by activity \| aa`        | `feat: regroup`                      | 접두를 쓰지 않는다                    |
| `Add eval rotation to bard-necro \| aa`    | `update`                             | 무엇을 바꿨는지 없다                  |
| `Fix stuck target loop in bard-mace \| aa` | `스크립트 수정`                      | 영어가 아니고, 대상과 동작이 없다     |
| `Port the loop builder to Node \| aa`      | `Ported the loop builder to Node.`   | 원형 동사로 쓰고 마침표를 찍지 않는다 |

## 3. 언제 무엇을 읽나

| 할 일                                        | 읽을 것                                                                                                                                              |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 무엇이든 시작할 때                           | [Workflow](document/working/workflow.md)                                                                                                             |
| `.razor`를 고치거나 새로 쓸 때               | [Conventions](document/scripting/conventions.md), [Razor](document/scripting/razor.md). 알림을 띄우면 [Overheads](document/scripting/overheads.md)도 |
| 모듈이나 레시피를 고치거나 루프를 조립할 때  | [Modules](document/scripting/modules.md)                                                                                                             |
| 파일을 새로 만들거나 이름을 지을 때          | [Conventions](document/scripting/conventions.md#01) 01절                                                                                             |
| 고친 것을 게임에서 확인할 때                 | [Workflow](document/working/workflow.md#04) 04절                                                                                                     |
| `config/`를 고칠 때                          | [Workflow](document/working/workflow.md#04.C) 04.C절, [config/README.md](config/README.md)                                                           |
| 오버헤드나 쿨다운 바를 더하거나 바꿀 때      | [Overheads](document/scripting/overheads.md)                                                                                                         |
| 바드, 네크로, 소환수 숫자가 필요할 때        | [Bard Necro](document/templates/bard-necro.md)                                                                                                       |
| PvP 규칙이 필요할 때                         | [PvP](document/game/pvp.md)                                                                                                                          |
| 벌목과 PvP 템플릿, 그 교전을 볼 때           | [Lumberjack PvP](document/templates/lumberjack-pvp.md)                                                                                               |
| 키 배치를 볼 때                              | [Hotkeys](document/game/hotkeys.md)                                                                                                                  |
| `findtype` 인자(graphic id, hue)가 필요할 때 | [Item list](document/game/item-list.md)                                                                                                              |
| 문서를 고치거나 새로 만들 때                 | [Writing](document/working/writing.md)                                                                                                               |
| 사용자에게 물을 것이 남았을 때               | [Open items](document/questions/open-items.md)                                                                                                       |
| 어느 문서가 무엇의 정본인지 볼 때            | [문서 홈](document/README.md)                                                                                                                        |
