# Overview

Ultima Online Outlands에서 돌리는 Razor 스크립트를 만들고 고칠 때 펴 보는 문서들이다.
처음이면 [Workflow](working/workflow.md)부터 읽는다.

어떤 일에 어떤 문서를 읽는지는 [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md) 2절, 문서마다 무엇의 정본인지는 3절이 정한다.
문서를 고치거나 새로 쓰는 법은 [Writing](working/writing.md)에 있다.

## 문서

| 묶음 | 문서 | 내용 |
| --- | --- | --- |
| How we work | [Workflow](working/workflow.md) | 작업 방식 |
| How we work | [Writing](working/writing.md) | 문서 쓰는 법 |
| Scripting | [Conventions](scripting/conventions.md) | 저장소와 스크립트 규칙 |
| Scripting | [Razor](scripting/razor.md) | Outlands Razor 문법 |
| Scripting | [Modules](scripting/modules.md) | 모듈과 조립 |
| Scripting | [Overheads](scripting/overheads.md) | 머리 위 메시지와 쿨다운 바 |
| Game reference | [PvP](game/pvp.md) | PvP 규칙 |
| Game reference | [Hotkeys](game/hotkeys.md) | 핫키 배치 |
| Game reference | [Item list](game/item-list.md) | 아이템 목록 |
| Templates | [Bard Necro](templates/bard-necro.md) | Bard Necro 핸드북 |
| Templates | [Lumberjack PvP](templates/lumberjack-pvp.md) | 벌목과 PvP 핸드북 |
| Open questions | [Open items](questions/open-items.md) | 확인할 것 |

## 읽는 법

저장소 루트에서 `pnpm install` 한 번, 그 뒤 `pnpm docs:dev`로 [localhost:4321](http://localhost:4321)에 띄운다.
