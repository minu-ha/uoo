<div align="center">

<img src="../document/favicon.svg" width="96" height="96" alt="UO Outlands 로고를 본뜬 불타는 O">

# uoo

**Ultima Online Outlands용 Razor 스크립트**

사냥, 채집, 스킬 훈련, 집 정리. 루프는 공용 블록으로 조립하고, 이유는 문서로 남긴다.

[Outlands](https://uooutlands.com/) · [Razor Scripting](https://wiki.uooutlands.com/Razor_Scripting) · [문서](../document/README.md)

[![MIT](https://img.shields.io/badge/license-MIT-1111aa?style=flat-square)](../LICENSE)
![UO Outlands](https://img.shields.io/badge/UO-Outlands-8b1a1a?style=flat-square)
![Razor](https://img.shields.io/badge/Razor-Outlands%20fork-2b6cb0?style=flat-square)
![Node 22+](https://img.shields.io/badge/node-22%2B-444444?style=flat-square)
![Docs](https://img.shields.io/badge/docs-for%20humanity-444444?style=flat-square)

[Quick start](#quick-start) · [스크립트](../script/README.md) · [문서](../document/README.md) · [설정](config.ko.md) · [English](../README.md)

</div>

## A few loops. Every reason kept.

- **바로 돌린다.** Outlands 클라이언트에 딸린 Razor용 사냥 루프, 핫키 매크로, 스킬 트레이너, 집 정리 스크립트.
  그 Razor의 확장 문법을 쓰므로 일반 Razor CE나 UOSteam에서는 그대로 돌아가지 않습니다.
- **한 번만 쓴다.** 전투 루프와 채집 루프는 `recipe/`의 레시피가 `module/`의 공용 블록을 모아 조립합니다.
  블록 하나를 고치면 그 블록을 쓰는 모든 루프가 함께 고쳐집니다.
- **이유를 남긴다.** 메커니즘, 숫자, 인게임 확인은 문서에 두고, 확인된 것과 아직 확인되지 않은 것을 표시합니다.
- **설정도 git으로.** Razor와 ClassicUO 프로필은 `config/`에 두고, 스크립트 하나로 게임에 연결합니다.

## Quick start

- **스크립트 하나만 필요하면** `.razor` 파일을 Razor `Scripts` 폴더에 복사하면 끝입니다.
- **저장소에서 바로 돌리고, 내 설정도 git으로 관리하고, 수정도 올리고 싶으면** clone 하고 `util/setup.sh`를 한 번 실행합니다.
  무엇을 하는지는 [config.ko.md](config.ko.md).

### 빌드와 검사

루프나 문서를 고치려면 Node.js 22 이상과 pnpm이 필요합니다.

```sh
pnpm install
pnpm build       # module/과 recipe/로 script/combat, script/gather를 조립
pnpm check       # 블록 짝, 값을 넣지 않은 변수, 오래된 루프, 문서 링크
pnpm test        # PvP 시뮬레이터와 문서 검사의 테스트
pnpm docs:dev    # localhost:4321에서 문서 읽기
```

생성된 루프는 손으로 고치지 않습니다. `module/`과 `recipe/`를 고치고 `pnpm build`를 돌립니다.

## 어디에 뭐가

| 폴더                                   | 무엇                                                                                                                         |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [`script/`](../script/README.md)       | 스크립트. 하는 일별로 묶음                                                                                                   |
| `module/`, `recipe/`                   | 한 벌만 둔 루프 블록과, `util/build-scripts.mjs`가 `script/combat/`과 `script/gather/`의 모든 루프로 조립하는 레시피           |
| [`document/`](../document/README.md) | Markdown 설계 문서. [for humanity](https://for-humanity.fyi)로 읽고, 묶음마다 폴더 하나다. 작업 방식, 스크립트 규칙, 게임 자료, 템플릿, 확인할 것. 지도는 [문서 홈](../document/README.md) |
| [`config/`](config.ko.md)              | Razor와 ClassicUO 설정. 사람마다 폴더 하나를 쓴다. 게임을 저장소에 연결하는 방법도 있다                                                    |
| `util/`                                | `setup.sh`는 게임을 저장소에 링크, `build-scripts.mjs`는 루프 조립, `check.sh`는 스크립트 검사, `check-docs.mjs`는 문서 링크 검사, `pvp-sim.mjs`는 필드 결투 모델, `razor-syntax/`는 WebStorm과 VS Code용 `.razor` 하이라이팅 |
| `language/`                            | README 번역본 (이 파일)                                                                                                      |

## 크레딧

- [Jaseowns](https://outlands.uorazorscripts.com/) — 채광, 벌목, recycle, 스킬 트레이너는 그의 스크립트이거나 그것을 바탕으로 함
- Demlar — 드레스 스크립트 아이디어
- raveX — 스틸 트레이너
- [outlandsbutler.com](https://www.outlandsbutler.com/) — `shelf/` 로드아웃 스크립트 생성

## License

나머지는 [MIT](../LICENSE). 제3자 스크립트는 원저자의 조건을 따릅니다. UO Outlands와 무관합니다.
