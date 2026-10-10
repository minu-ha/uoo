# AGENTS.md

Ultima Online Outlands용 Razor 스크립트 (`script/`), 클라이언트 설정 사본 (`config/`), 설계 문서 (`blueprint/`).
규칙과 정책은 전부 `blueprint/`에 있고, 이 파일은 **언제 무엇을 읽는지**만 가리킨다. 작업을 시작하면 [blueprint/workflow.md](blueprint/workflow.md)부터 읽는다.
설계 문서는 [for humanity](https://for-humanity.fyi)로 읽는 Markdown이다. 사람은 `pnpm docs:dev`로 띄워 브라우저로 읽고, 홈은 [blueprint/README.md](blueprint/README.md)다.

## 목차

1. [항상 지키는 것](#1-항상-지키는-것)
2. [언제 무엇을 읽나](#2-언제-무엇을-읽나)
3. [문서 지도](#3-문서-지도)

---

## 1. 항상 지키는 것

한 줄씩만 적는다. 이유와 자세한 규칙은 링크한 곳에 있다.

- 문서와 답변은 한국어, 스크립트 안 주석은 영어 → [workflow.md](blueprint/workflow.md#05.A) 05.A절
- `.razor`를 고치기 전에 대상 파일을 끝까지 읽고 확인된 함정 표를 본다 → [razor.md](blueprint/razor.md#03) 03절
- `config/` 아래는 게임을 끈 상태에서만 고친다 → [workflow.md](blueprint/workflow.md#04.C) 04.C절
- 다른 사람의 `config/`는 건드리지 않고, `settings.json`은 절대 커밋하지 않는다 → [conventions.md](blueprint/conventions.md#01.D) 01.D절
- 스크립트에 serial 리터럴을 쓰지 않는다 → [conventions.md](blueprint/conventions.md#03.C) 03.C절
- 생성된 루프 (`script/combat/*`, `script/gather/*`)는 직접 고치지 않는다. `module/`·`recipe/`를 고치고 `pnpm build` (`node util/build-scripts.mjs`)로 만든다 → [modules.md](blueprint/modules.md#07) 07절
- 커밋은 사용자가 하라고 할 때만, push는 따로 요청이 있을 때만 → [workflow.md](blueprint/workflow.md#06) 06절

## 2. 언제 무엇을 읽나

| 할 일                                   | 읽을 것                                                                                                                          |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 무엇이든 시작할 때                      | [workflow.md](blueprint/workflow.md)                                                                                             |
| `.razor`를 고치거나 새로 쓸 때          | [conventions.md](blueprint/conventions.md), [razor.md](blueprint/razor.md), 알림을 띄우면 [overheads.md](blueprint/overheads.md) |
| 모듈·레시피를 고치거나 루프를 조립할 때 | [modules.md](blueprint/modules.md)                                                                                               |
| 파일을 새로 만들거나 이름을 지을 때     | [conventions.md](blueprint/conventions.md#01) 01절                                                                               |
| 고친 것을 게임에서 확인할 때            | [workflow.md](blueprint/workflow.md#04) 04절                                                                                     |
| `config/`를 고칠 때                     | [workflow.md](blueprint/workflow.md#04.C) 04.C절, [config/README.md](config/README.md)                                           |
| 오버헤드나 쿨다운 바를 더하거나 바꿀 때 | [overheads.md](blueprint/overheads.md)                                                                                           |
| 바드·네크로·소환수 숫자가 필요할 때     | [bard-necro-handbook.md](blueprint/bard-necro-handbook.md)                                                                       |
| PvP 규칙이 필요할 때                    | [pvp.md](blueprint/pvp.md)                                                                                                       |
| 벌목·PvP 템플릿과 교전을 볼 때          | [lumberjack-pvp-handbook.md](blueprint/lumberjack-pvp-handbook.md)                                                               |
| 키 배치를 볼 때                         | [hotkeys.md](blueprint/hotkeys.md)                                                                                               |
| `findtype` 인자 (graphic id, hue)       | [item-list.md](blueprint/item-list.md)                                                                                           |
| 문서를 고치거나 새로 만들 때            | [writing.md](blueprint/writing.md)                                                                                               |
| 사용자에게 물을 것이 남았을 때          | [open-items.md](blueprint/open-items.md)                                                                                         |
| 커밋할 때                               | [workflow.md](blueprint/workflow.md#06) 06절                                                                                     |

## 3. 문서 지도

| 파일                                                                         | 무엇의 정본                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [blueprint/README.md](blueprint/README.md)                                   | 문서 사이트의 홈: 묶음별 문서 표, 사이트를 띄우는 법                                        |
| [blueprint/for-humanity.config.mjs](blueprint/for-humanity.config.mjs)       | 사이트 이름, 사이드바 묶음 순서, 상태 문구 (`인게임 확인됨`, `확인되지 않았다`)             |
| [blueprint/writing.md](blueprint/writing.md)                                 | 설계 문서를 쓰는 법: 새 문서, frontmatter, 짜임, 번호와 가름, 본문, 흐름도, 끝낼 때 확인    |
| [blueprint/workflow.md](blueprint/workflow.md)                               | 근거 우선순위와 참고 사이트, 작업 순서, 변경 보고, 게임 반영·검증, 글의 언어와 번역본, 커밋 |
| [blueprint/modules.md](blueprint/modules.md)                                 | 모듈 폴더, 레시피와 모듈 형식, 조립 규칙, base와 블록끼리의 신호, 옮긴 기록                 |
| [blueprint/conventions.md](blueprint/conventions.md)                         | 폴더와 파일 이름, 스크립트 모양과 배너, 변수 접두, serial, 타이머 관용구, 편집기 하이라이팅 |
| [blueprint/razor.md](blueprint/razor.md)                                     | Outlands Razor 확장 문법, 확인된 함정, 되는 구문의 선례, 명령문 비용, PvP 명령 제약         |
| [blueprint/overheads.md](blueprint/overheads.md)                             | 알림 세 경로, `[ 대상, 상태 ]` 형식, 어휘, hue, 쿨다운 바, 프로필 오버헤드 표               |
| [blueprint/pvp.md](blueprint/pvp.md)                                         | 템플릿과 무관한 PvP 규칙과 숫자                                                             |
| [blueprint/bard-necro-handbook.md](blueprint/bard-necro-handbook.md)         | Bard Necro의 메커니즘, 소환수, 전투 루프 설계, PvP 판단, 인게임 확인                        |
| [blueprint/lumberjack-pvp-handbook.md](blueprint/lumberjack-pvp-handbook.md) | 벌목·PvP 템플릿의 스킬·스탯·도끼 선택, 마나 예산, 교전 분기와 구현 요구사항                 |
| [blueprint/hotkeys.md](blueprint/hotkeys.md)                                 | 키 배치와 주문 데미지 메모                                                                  |
| [blueprint/open-items.md](blueprint/open-items.md)                           | 사용자에게 물을 것으로 남긴 것: 뜨지 않는 바, 규칙과 어긋난 줄, 출처 없는 숫자, 규칙 해석   |
| [blueprint/item-list.md](blueprint/item-list.md)                             | 아이템 이름·graphic id·hue                                                                  |
| [script/README.md](script/README.md)                                         | 스크립트 폴더 구성, 전투 루프 ↔ 템플릿                                                      |
| [config/README.md](config/README.md)                                         | 게임을 저장소에 링크하는 방법, 설정 파일별 설명                                             |
| [language/](language/)                                                       | README 번역본                                                                               |
