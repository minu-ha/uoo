---
name: Writing
label: 문서 쓰는 법
group: How we work
order: 20
---

설계 문서 작성 기준. 문서는 [for-humanity](https://for-humanity.fyi) Markdown, `pnpm docs:dev`로 읽음.
문서별 정본은 [문서 홈](../README.md)의 표. for-humanity 기능(frontmatter, Note, Details, 표, 흐름도)의 정본은 for-humanity [Writing](https://github.com/minu-ha/for-humanity/blob/main/templates/document/writing.md).

## <a id="00"></a>00 한눈에

| 절 | 내용 |
| --- | --- |
| [01](#01) | `document/` 구성과 사이트 명령 |
| [02](#02) | 새 문서 추가 순서 |
| [03](#03) | 빈 틀 |
| [04](#04) | 짜임. 번호, 앵커, 가름 |
| [05](#05) | 문장 |
| [06](#06) | Markdown 표기 |
| [07](#07) | 언어와 번역본 |
| [08](#08) | 한 사실은 한 곳에 |
| [09](#09) | 흐름도 |
| [10](#10) | 끝낼 때 확인 |

이 문서에 걸린 질문은 [Open items](../questions/open-items.md).

::part[파일]

## <a id="01"></a>01 파일

묶음 하나 = 폴더 하나. 폴더와 사이드바 묶음이 같음.

| 폴더 | 묶음 | 내용 |
| --- | --- | --- |
| `working/` | How we work | 작업 순서, 문서 쓰는 법 |
| `scripting/` | Scripting | 스크립트 규칙, Razor 문법, 모듈 조립, 머리 위 알림 |
| `game/` | Game reference | 게임 규칙과 자료. PvP, 핫키, 아이템 번호 |
| `templates/` | Templates | 템플릿별 판단과 설계 |
| `questions/` | Open questions | 아직 확인 못 한 것 |

| 폴더 밖 파일 | 역할 |
| --- | --- |
| `README.md` | 사이트 홈(`/`). 문서 표. frontmatter 없음 |
| `for-humanity.config.mjs` | 사이트 이름, 묶음 순서(`navigation`), 확인 알약 문구(`status`) |
| `favicon.svg` | 사이트 아이콘. `pnpm docs:build`가 결과물에 덮어씀 |

- `dist/`: `pnpm docs:build` 결과물. git 제외
- 모양과 동작: `for-humanity` 패키지. 버전은 루트 `package.json`에 정확히 고정

| 명령 | 역할 |
| --- | --- |
| `pnpm docs:dev` | [localhost:4321](http://localhost:4321) 개발 서버. 수정 시 다시 그림 |
| `pnpm docs:build` | `document/dist/`에 사이트 생성. frontmatter, 깨진 `.md` 링크, 부품 문법 검사 |
| `pnpm docs:preview` | 생성한 사이트 띄우기 |
| `node util/check-docs.mjs` | 끊긴 링크와 앵커, 번호 제목의 앵커 검사 |

::part[쓰기]

## <a id="02"></a>02 새 문서

1. 맞는 묶음 폴더에 kebab-case `.md` 생성. 템플릿 문서는 `templates/<템플릿>.md`
2. 03절 빈 틀에서 시작
3. frontmatter
   - `name`: 영어 이름. 문서 제목과 사이드바 목록
   - `label`: 한글 이름. 사이드바 툴팁
   - `group`: 폴더에 맞는 묶음(01절 표). 새 묶음이면 폴더 추가, `for-humanity.config.mjs`의 `navigation`에 순서 추가
   - `order`: 묶음 안 순서. 10 단위
4. 세 곳에 한 줄씩 추가
   - [문서 홈](../README.md) 문서 표
   - [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md) "언제 무엇을 읽나" 표. 읽을 일이 있는 문서만
   - 루트 [README.md](https://github.com/minu-ha/uoo/blob/master/README.md)의 `document/` 칸. 번역본도 함께(07절)

## <a id="03"></a>03 빈 틀

```markdown
---
name: {영어 이름}
label: {한글 이름}
group: {묶음}
order: {묶음 안 순서}
---

{이 문서의 범위 한두 줄. 여기 없는 것의 위치 링크}

## <a id="00"></a>00 한눈에

{절마다 내용을 적은 표}

::part[{가름}]

## <a id="01"></a>01 {절}

{본문}

### <a id="01.A"></a>01.A {소제목}

{본문}
```

- `#` 제목 없음. `name`이 문서 제목
- 첫 `##` 앞 = 문서 머리. 범위 한두 줄과 다른 문서 링크

## <a id="04"></a>04 짜임

- 목차 없음. for-humanity가 `##`, `###`로 On this page 목차 생성
- 절: 두 자리 번호, `## <a id="01"></a>01 이름`. 소제목: 절 번호 + 대문자, `### <a id="01.A"></a>01.A 이름`
- **앵커가 번호 링크를 지킴.** for-humanity는 제목 글로 id 생성(`01 이름` → `01-이름`) → 제목을 고치면 id도 바뀜.
  제목 안의 `<a id>` 덕분에 언제나 번호로 링크 가능(`razor.md#03`). 앵커를 제목 위 별도 줄에 두면 빈 문단이 되어 앞 절 끝에 붙음 → 제목 줄 안에 둠
- `####` 이하: 번호, 앵커 없음. 목차 밖 작은 제목
- `00` = 한눈에. "절 | 내용" 표. 이 문서에 걸린 질문은 [Open items](../questions/open-items.md)로
- 절이 많으면 가름으로 묶음. 가름 첫 절 제목 바로 위에 `::part[이름]` 한 줄 → 가름 머리와 목차 구분
- 00 한눈에는 가름 밖. 끝의 확인 안 된 것, 자주 틀렸던 것, 참고 링크는 `기록` 가름
- 글 안 참조: "03절", "05.D절". 다른 문서: 문서 이름 링크 + 절(`[Razor](../scripting/razor.md#03) 03절`)
- 절을 넣거나 빼면 번호와 앵커를 함께 수정. 그 번호를 가리키던 곳도 저장소 전체에서 수정.
  AGENTS.md와 스크립트 주석(`part 5`)도 절 번호 사용 → `git grep -n -e '05.H' -e 'part 5'`

## <a id="05"></a>05 문장

짧고 간결한 명사형. 한눈에 읽히는 글.

- **한 줄 한 사실.** 긴 문장은 나눔
- **명사형 종결.** "~한다", "~이다" 대신 명사나 명사형으로 끝냄(`수정`, `불가`, `필요`, `덮어씀`)
- **군더더기 없음.** 접속사, 수식어, 경위 생략. 이유는 필요할 때만 짧게
- **결론 먼저.** 규칙과 결정 먼저, 이유는 뒤. 경위는 기록 가름이나 날짜 붙은 한 줄
- **목록과 표 우선.** 나열은 목록, 비교는 표, 절차는 번호 목록. 목록 항목과 표 칸에는 마침표 없음
- **가운뎃점(`·`) 금지.** 쉼표로 나열(`회복, 실패, 재시도`). 제목, 표, 라벨도 같음
- **빗금(`/`)으로 낱말 연결 금지.** 쉼표나 "또는". 경로, 명령, 값은 그대로
- **화살표(`→`)**: 대응과 결과에만(`핫키 실행 → 재시작 필요`)
- **괄호 최소.** 짧은 보충만, 중첩 금지
- **용어 통일.** 아래 표 기준
- **고유 이름은 원문.** 스킬과 주문(Discordance, Greater Heal), Razor 명령(`findtype`), 파일, 변수. 그 밖은 한국어, 익숙한 영어 용어는 영어
- **숫자에 단위.** 초, ms, 칸, 포인트. 날짜는 `2026-10-11`
- **강조 최소.** 놓치면 안 되는 한 줄에만 굵게

| 말 | 뜻 |
| --- | --- |
| 루프 | 핫키 하나로 켜 두는 메인 스크립트(`script/combat/*`, `script/gather/*`) |
| 패스 | `while not dead` 한 바퀴 |
| 모듈, 블록 | `module/` 파일 하나. 루프 안에서는 그 파일에서 온 코드 묶음 = 블록 |
| 레시피 | 루프 하나의 모듈 구성과 설정을 적은 `recipe/` 파일 |
| 템플릿 | 캐릭터 스킬 구성(Bard Necro, Lumberjack PvP 등) |
| 교전 | `var__fighting` 1. 사거리 안에 고른 적 있음 |

| 고치기 전 | 고친 뒤 |
| --- | --- |
| `config/` 아래 파일은 게임을 끈 상태에서만 고친다. 클라이언트가 종료할 때 설정 파일을 통째로 덮어쓰기 때문이다. | `config/`는 게임 종료 상태에서만 수정. 종료 시 클라이언트가 통째로 덮어씀 |
| 핫키로 돌리면 클라이언트를 껐다 켠다. 리로드로는 절대 안 된다. | 핫키 실행 → 클라이언트 재시작. 리로드로는 반영 불가 |
| 회복·실패·재시도 분기 | 회복, 실패, 재시도 분기 |

## <a id="06"></a>06 Markdown

- 본문은 GFM. 문단, 목록, 표, 코드, 인용(`>`). 원시 HTML은 제목 앵커와 아래 강조 예외만
- 강조 뒤에 문장부호나 코드가 오고 바로 한글이 붙으면 CommonMark가 강조로 읽지 않음(`**(A OR B)**다`) → `<strong>…</strong>`
- 범위의 `~`는 `\~`. GFM이 한 문단 안의 `~` 둘을 취소선으로 읽음(`3~5초, 7~9초`)
- 코드 밖의 `*`, `_`, `[`, 영문자 앞 `<`는 `\`로 막음. 식별자와 값은 코드(`var__fighting`)로
- 큰따옴표와 `--`는 사이트에서 둥근 따옴표와 대시로 바뀜 → 원문 그대로 보일 서버 문장은 코드로
- 코드 블록: 코드, 의사 코드, 파일 트리만. 칸 맞춤은 표로
- Razor 코드 블록은 언어 표시 없이(` ``` `만). Shiki에 Razor 문법 없음
- 인용과 확인 표시: [Workflow](workflow.md#01.C) 01.C절. "인게임 확인됨"과 "확인되지 않았다"는 그대로 쓰면 확인 알약.
  날짜까지 알약(`인게임 확인됨 2026-09-28`), 괄호는 숨김. 코드, 링크, 제목 안은 그대로. 문구는 `for-humanity.config.mjs`의 `status`
- 색 값만 든 인라인 코드(`#e80030`)에 색 칩
- 다른 문서: 상대 경로 `.md` 링크. `document/` 밖 파일(AGENTS.md, `script/`, `util/` 등): GitHub 주소
  (`https://github.com/minu-ha/uoo/blob/master/<경로>`). for-humanity는 문서 폴더 밖 상대 링크를 변환하지 못함

## <a id="07"></a>07 언어와 번역본

- 문서와 답변: 한국어. 스크립트 주석: 영어
- README 원본: 영어. 번역본: `language/<무엇>.<언어>.md`
  - `language/README.ko.md` = 루트 README
  - `language/config.ko.md` = `config/README.md`
- 예외: `document/`. 홈 `document/README.md`도 한국어, 번역본 없음
- 원본 맨 위에 번역본 링크, 번역본 맨 위에 원본 링크. 원본 수정 시 번역본도 같은 커밋에서 수정

## <a id="08"></a>08 한 사실은 한 곳에

- 같은 내용은 한 곳에만. 다른 곳은 절 번호 링크. 두 곳에 쓰면 한쪽만 고쳐짐(overheads.md의 옛 hue 표가 그 예)
- 문서별 정본: [문서 홈](../README.md) 표 한 곳. 새 문서나 정본 이동 시 그 표 수정
- 규칙도 같음. 언제나 지킬 규칙과 커밋 규칙은 AGENTS.md에만, 나머지는 이 문서들에만. AGENTS.md는 한 줄 요약과 링크만
- 템플릿 문서: **그 템플릿의 판단만.** 다른 템플릿에도 쓰이는 내용(서버 규칙, 문법)은 공통 문서로 옮기고 링크

## <a id="09"></a>09 흐름도

- ` ```mermaid ` 코드 블록. 빌드 시 beautiful-mermaid 격자 렌더러가 SVG 생성. mermaid 문법 일부만 지원
- 잘 되는 것: `flowchart TD` 사슬과 나무, `flowchart LR` 판단 사슬(`예` 사슬을 윗줄로), `sequenceDiagram`
- 라벨에 괄호 금지. 렌더러가 괄호에서 글을 자름. 긴 라벨은 `<br>`
- 선 라벨은 한 낱말(`-- 예 -->`). 띄어 쓰면 라벨이 둘로 갈림
- 되돌아가는 선, 라벨 달린 합류선은 엉킴 → 여러 장으로 쪼갬([Bard Necro](../templates/bard-necro.md#05.A) 05.A절)
- 폭 140칸 이내. 넘치면 `LR` → `TD` 또는 둘로 나눔

::part[확인]

## <a id="10"></a>10 끝낼 때 확인

- 한 줄 200자 이내(`.editorconfig`의 `max_line_length`). 넘으면 코드 밖 빈칸, 되도록 문장 끝에서 줄바꿈. 표의 줄과 코드 블록 안은 예외
- 05절 기준 재확인. 가운뎃점은 `git grep -n '·' -- document`
- `pnpm check`: 사이트 생성(`pnpm docs:build`), 링크와 앵커와 번호 제목 검사(`node util/check-docs.mjs`)
- `pnpm docs:dev`로 확인. 밝은 테마와 어두운 테마, 폭 1024와 390에서 가로 밀림, 흐름도
