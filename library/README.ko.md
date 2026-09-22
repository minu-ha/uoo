# uoo

[English](../README.md) · **한국어**

**[Ultima Online Outlands](https://uooutlands.com/)** 용 Razor 스크립트와 클라이언트 설정.

![Outlands](https://img.shields.io/badge/UO-Outlands-8b1a1a) ![Razor](https://img.shields.io/badge/Razor-Outlands%20fork-2b6cb0) ![License](https://img.shields.io/badge/license-MIT-green)

사냥 루프, 핫키 매크로, 스킬 트레이너, 집 정리 스크립트. Outlands 클라이언트에 딸려오는 Razor 빌드와
그 확장 문법 기준이라 일반 Razor CE 나 UOSteam 에서는 그대로 돌아가지 않습니다.
문법 참고: [Outlands 위키 Razor Scripting](https://wiki.uooutlands.com/Razor_Scripting).

## 쓰는 법

- **스크립트 하나만 필요하면** `.razor` 파일을 Razor `Scripts` 폴더에 복사하면 끝입니다.
- **저장소에서 바로 돌리고, 내 설정도 git 으로 관리하고, 수정도 올리고 싶으면** clone 하고
  `util/setup.sh` 를 한 번 실행합니다. 무엇을 하는지는 [config/README.ko.md](../config/README.ko.md).

## 어디에 뭐가

| | |
|---|---|
| [`script/`](../script/README.md) | 스크립트. 하는 일별로 묶음 |
| [`config/`](../config/README.ko.md) | Razor · ClassicUO 설정, 사람마다 폴더 하나. 게임을 저장소에 연결하는 방법 |
| `library/` | 참고 자료: 아이템 graphic ID, 키 배치, 가이드, 템플릿 ↔ 스크립트 매핑 |
| `util/` | `setup.sh` 는 게임을 저장소에 링크, `check.sh` 는 스크립트 블록 짝 검사 |

## 크레딧

- [Jaseowns](https://outlands.uorazorscripts.com/) — 채광, 벌목, recycle, 스킬 트레이너는 그의 스크립트이거나 그것을 바탕으로 함
- Demlar — 드레스 스크립트 아이디어
- raveX — 스틸 트레이너
- [outlandsbutler.com](https://www.outlandsbutler.com/) — `shelf/` 로드아웃 스크립트 생성

나머지는 [MIT](../LICENSE). 제3자 스크립트는 원저자의 조건을 따릅니다. UO Outlands 와 무관합니다.
