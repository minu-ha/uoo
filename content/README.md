<div align="center">

<img src="asset/favicon.svg" width="96" height="96" alt="픽셀 금색 고리">

# uoo

**Ultima Online Outlands용 Razor 스크립트**

사냥, 채집, 스킬 훈련, 집 정리. 공용 블록으로 조립한 루프와 선택의 근거를 담은 문서.

[Outlands](https://uooutlands.com/) | [Razor Scripting](https://wiki.uooutlands.com/Razor_Scripting) | [GitHub](https://github.com/minu-ha/uoo)

[![MIT](https://img.shields.io/badge/license-MIT-1111aa?style=flat-square)](https://github.com/minu-ha/uoo/blob/master/LICENSE)
![UO Outlands](https://img.shields.io/badge/UO-Outlands-8b1a1a?style=flat-square)
![Razor](https://img.shields.io/badge/Razor-Outlands%20fork-2b6cb0?style=flat-square)
![Node 22.12.0+](https://img.shields.io/badge/node-22.12.0%2B-444444?style=flat-square)
[![Docs](https://img.shields.io/badge/docs-for%20humanity-444444?style=flat-square)](https://for-humanity.fyi)

[시작하기](#시작하기) | [스크립트](https://github.com/minu-ha/uoo/blob/master/script/README.md) | [문서](#문서) | [설정](https://github.com/minu-ha/uoo/blob/master/language/config.ko.md)

</div>

## 사냥부터 집 정리까지

- **바로 실행.** Outlands 클라이언트에 포함된 Razor용 사냥 루프, 핫키 매크로, 스킬 트레이너, 집 정리 스크립트
- **공용 블록.** `module/`의 블록과 `recipe/`의 레시피로 전투와 채집 루프 조립. 블록 하나의 수정이 사용하는 모든 루프에 반영
- **근거 보관.** 게임 메커니즘, 숫자, 인게임 확인 기록. 확인된 것과 아직 확인되지 않은 것 구분
- **설정 관리.** Razor와 ClassicUO 프로필을 저장소에 보관하고 게임에 연결

Outlands Razor의 확장 문법 사용. 일반 Razor CE와 UOSteam에서는 수정 필요.

## 시작하기

- 스크립트 하나만 사용: [스크립트 목록](https://github.com/minu-ha/uoo/blob/master/script/README.md)에서 `.razor` 파일을 골라 Razor의 `Scripts` 폴더에 복사
- 게임에 저장소 연결: [설정 안내](https://github.com/minu-ha/uoo/blob/master/language/config.ko.md)
- 루프 수정: [Workflow](public/working/workflow.md)부터 읽고 [Modules](public/scripting/modules.md)에서 모듈과 레시피 확인
- 문서 작성: [Writing](public/working/writing.md)

로컬에서 문서를 읽거나 수정할 때:

```sh
pnpm install
pnpm docs:dev
```

Node.js 22.12.0 이상과 pnpm 필요. 실행 후 [localhost:4323/uoo/](http://localhost:4323/uoo/)에서 확인.

## 문서

문서별 정본은 아래 표. 언제나 지킬 규칙과 커밋 규칙은 [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md).

| 문서 | 정본인 내용 |
| --- | --- |
| [Workflow](public/working/workflow.md) | 근거의 우선순위와 참고 사이트, 스크립트 수정 순서, 변경 보고, 게임 반영과 확인 |
| [Writing](public/working/writing.md) | 문서 작성. 새 문서, frontmatter, 짜임, 문장, Markdown, 언어와 번역본, 흐름도, 끝낼 때 확인 |
| [Conventions](public/scripting/conventions.md) | 폴더와 파일 이름, 스크립트 모양과 배너, 변수 접두, serial, 타이머 관용구, 편집기 하이라이팅 |
| [Razor](public/scripting/razor.md) | Outlands Razor 확장 문법, 확인된 함정, 되는 구문의 선례, 명령문 비용, PvP 명령 제약 |
| [Modules](public/scripting/modules.md) | 모듈 폴더, 레시피와 모듈 형식, 조립 규칙, base와 블록 사이 신호, 옮긴 기록 |
| [Overheads](public/scripting/overheads.md) | 알림의 세 경로, `[ 대상, 상태 ]` 형식, 어휘, hue, 쿨다운 바, 프로필 오버헤드 표 |
| [PvP](public/game/pvp.md) | 템플릿과 무관한 PvP 규칙과 숫자 |
| [Hotkeys](public/game/hotkeys.md) | 키 배치, 주문 데미지 메모 |
| [Item list](public/game/item-list.md) | 아이템 이름, graphic id, hue |
| [Bard Necro](public/templates/bard-necro.md) | Bard Necro 메커니즘, 소환수, 전투 루프 설계, PvP 판단, 인게임 확인 |
| [Lumberjack PvP](public/templates/lumberjack-pvp.md) | 벌목과 PvP 템플릿의 스킬, 스탯, 도끼 선택, 마나 예산, 교전 분기, 구현 요구사항 |
| [Bard Archer](public/templates/bard-archer.md) | Bard Archer의 스킬과 코덱스, 갑옷과 마나, 아처리 자세와 피니셔와 무기 능력, 부활, 전투 루프 설계 |
| [Open items](public/questions/open-items.md) | 사용자에게 물을 것. 뜨지 않는 바, 규칙과 어긋난 줄, 출처 없는 숫자, 인게임 확인 목록 |

## 크레딧과 라이선스

[Jaseowns](https://outlands.uorazorscripts.com/), Demlar, raveX, [outlandsbutler.com](https://www.outlandsbutler.com/).
스크립트별 출처는 [저장소 README](https://github.com/minu-ha/uoo#credits).

제3자 스크립트는 원저자의 조건 적용. 그 밖의 코드는 [MIT](https://github.com/minu-ha/uoo/blob/master/LICENSE).
UO Outlands와 무관한 개인 프로젝트.
