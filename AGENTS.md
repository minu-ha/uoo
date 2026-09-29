# AGENTS.md

Ultima Online Outlands용 Razor 스크립트 (`script/`), 클라이언트 설정 사본 (`config/`), 설계 문서 (`blueprint/`).
규칙과 정책은 전부 `blueprint/`에 있고, 이 파일은 **언제 무엇을 읽는지**만 가리킨다. 작업을 시작하면 [blueprint/workflow.html](blueprint/workflow.html)부터 읽는다.
설계 문서는 HTML이다. 사람은 브라우저로 [blueprint/_index.html](blueprint/_index.html)을 연다.

## 목차

1. [항상 지키는 것](#1-항상-지키는-것)
2. [언제 무엇을 읽나](#2-언제-무엇을-읽나)
3. [문서 지도](#3-문서-지도)

---

## 1. 항상 지키는 것

한 줄씩만 적는다. 이유와 자세한 규칙은 링크한 곳에 있다.

- 문서와 답변은 한국어, 스크립트 안 주석은 영어 → [workflow.html](blueprint/workflow.html#05.D) 05.D절
- `.razor`를 고치기 전에 대상 파일을 끝까지 읽고 확인된 함정 표를 본다 → [razor.html](blueprint/razor.html#03) 03절
- `config/` 아래는 게임을 끈 상태에서만 고친다 → [workflow.html](blueprint/workflow.html#04.C) 04.C절
- 다른 사람의 `config/`는 건드리지 않고, `settings.json`은 절대 커밋하지 않는다 → [conventions.html](blueprint/conventions.html#01.D) 01.D절
- 스크립트에 serial 리터럴을 쓰지 않는다 → [conventions.html](blueprint/conventions.html#03.C) 03.C절
- 커밋은 사용자가 하라고 할 때만, push는 따로 요청이 있을 때만 → [workflow.html](blueprint/workflow.html#06) 06절

## 2. 언제 무엇을 읽나

| 할 일                                   | 읽을 것                                                                                                                                      |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 무엇이든 시작할 때                      | [workflow.html](blueprint/workflow.html)                                                                                                     |
| `.razor`를 고치거나 새로 쓸 때          | [conventions.html](blueprint/conventions.html), [razor.html](blueprint/razor.html), 알림을 띄우면 [overheads.html](blueprint/overheads.html) |
| 파일을 새로 만들거나 이름을 지을 때     | [conventions.html](blueprint/conventions.html#01) 01절                                                                                       |
| 고친 것을 게임에서 확인할 때            | [workflow.html](blueprint/workflow.html#04) 04절                                                                                             |
| `config/`를 고칠 때                     | [workflow.html](blueprint/workflow.html#04.C) 04.C절, [config/README.md](config/README.md)                                                   |
| 오버헤드나 쿨다운 바를 더하거나 바꿀 때 | [overheads.html](blueprint/overheads.html)                                                                                                   |
| 바드·네크로·소환수 숫자가 필요할 때     | [bard-necro-handbook.html](blueprint/bard-necro-handbook.html)                                                                               |
| PvP 규칙이 필요할 때                    | [pvp.html](blueprint/pvp.html)                                                                                                               |
| 키 배치를 볼 때                         | [hotkeys.html](blueprint/hotkeys.html)                                                                                                       |
| `findtype` 인자 (graphic id, hue)       | [item-list.txt](blueprint/item-list.txt)                                                                                                     |
| 문서를 고치거나 새로 만들 때            | [workflow.html](blueprint/workflow.html#05) 05절                                                                                             |
| 커밋할 때                               | [workflow.html](blueprint/workflow.html#06) 06절                                                                                             |

## 3. 문서 지도

| 파일                                                                     | 무엇의 정본                                                                                          |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [blueprint/_index.html](blueprint/_index.html)                           | 브라우저로 여는 첫 화면. 문서 목록은 `_index.js`의 `blueprint_docs`, 모든 문서의 모양은 `_index.css` |
| [blueprint/workflow.html](blueprint/workflow.html)                       | 근거 우선순위와 참고 사이트, 작업 순서, 변경 보고, 게임 반영·검증, 문서 규칙, 커밋                   |
| [blueprint/conventions.html](blueprint/conventions.html)                 | 폴더와 파일 이름, 스크립트 모양, 변수 접두, serial, 타이머 관용구                                    |
| [blueprint/razor.html](blueprint/razor.html)                             | Outlands Razor 확장 문법, 확인된 함정, 되는 구문의 선례, 명령문 비용, PvP 명령 제약                  |
| [blueprint/overheads.html](blueprint/overheads.html)                     | 알림 세 경로, `[ 대상, 상태 ]` 형식, 어휘, hue, 쿨다운 바, 프로필 오버헤드 표                        |
| [blueprint/pvp.html](blueprint/pvp.html)                                 | 템플릿과 무관한 PvP 규칙과 숫자                                                                      |
| [blueprint/bard-necro-handbook.html](blueprint/bard-necro-handbook.html) | Bard Necro의 메커니즘, 소환수, 전투 루프 설계, PvP 판단, 인게임 확인                                 |
| [blueprint/hotkeys.html](blueprint/hotkeys.html)                         | 키 배치와 주문 데미지 메모                                                                           |
| [blueprint/item-list.txt](blueprint/item-list.txt)                       | 아이템 이름·graphic id·hue                                                                           |
| [script/README.md](script/README.md)                                     | 스크립트 폴더 구성, 전투 루프 ↔ 템플릿                                                               |
| [config/README.md](config/README.md)                                     | 게임을 저장소에 링크하는 방법, 설정 파일별 설명                                                      |
| [language/](language/)                                                   | README 번역본                                                                                        |
