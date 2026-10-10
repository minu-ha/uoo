---
name: Writing
label: 문서 쓰는 법
group: Rules
order: 40
---

이 저장소의 설계 문서를 쓰고 고치는 법. 문서는 [for-humanity](https://for-humanity.fyi) Markdown이고, `pnpm docs:dev`로 사이트를 띄워 읽는다.
무엇이 무엇의 정본인지는 [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md) 3절 문서 지도에 있다.
Markdown 기능 자체 (frontmatter, Note·Details, 표, 흐름도)는 for-humanity의 [Writing](https://github.com/minu-ha/for-humanity/blob/main/templates/document/writing.md) 안내가 정본이다.

## <a id="00"></a>00 한눈에

| 절 | 무엇을 답하나 |
| --- | --- |
| [01](#01) | `blueprint/`에 무엇이 있고, 사이트는 어떻게 만드나 |
| [02](#02) | 새 문서는 어떻게 더하나 |
| [03](#03) | 새 문서는 어떤 틀에서 시작하나 |
| [04](#04) | 문서는 어떻게 짜나. 번호, 앵커, 가름 |
| [05](#05) | 본문에 무엇을 어떻게 쓰나 |
| [06](#06) | 같은 사실을 두 곳에 쓰면 왜 안 되나 |
| [07](#07) | 흐름도는 어떻게 그리나 |
| [08](#08) | 끝내기 전에 무엇을 확인하나 |

::part[파일]

## <a id="01"></a>01 파일

| 파일 | 하는 일 |
| --- | --- |
| `README.md` | 사이트의 홈 (`/`). frontmatter 없이 쓴다 |
| `for-humanity.config.mjs` | 사이트 이름, 묶음 순서 (`navigation`), 확인 알약 문구 (`status`) |
| `*.md` | 문서 한 장씩 |
| `dist/` | `pnpm docs:build`가 만든 사이트. git에 넣지 않는다 |

모양과 동작은 `for-humanity` 패키지가 정한다. 버전은 루트 `package.json`에 정확히 고정한다.

| 명령 | 하는 일 |
| --- | --- |
| `pnpm docs:dev` | 고치는 대로 다시 그리는 사이트를 [localhost:4321](http://localhost:4321)에 띄운다 |
| `pnpm docs:build` | `blueprint/dist/`에 사이트를 만든다. frontmatter, 깨진 `.md` 링크, 부품 문법을 검사한다 |
| `pnpm docs:preview` | 만든 사이트를 띄운다 |
| `node util/check-docs.mjs` | 만든 사이트의 끊긴 링크와 앵커, 번호 제목의 앵커를 검사한다 |

::part[쓰기]

## <a id="02"></a>02 새 문서

1. `blueprint/`에 kebab-case `.md`로 만든다. 템플릿 전용이면 `<템플릿>-handbook.md`다.
2. 03절의 빈 틀에서 시작한다.
3. frontmatter를 채운다.
   - `name`은 영어 이름이다. 문서의 제목과 사이드바 문서 목록이 이 이름을 쓴다.
   - `label`은 한글 이름이다. 사이드바에서 이름에 마우스를 올리면 뜨고, 홈의 문서 표에도 쓴다.
   - `group`은 사이드바 묶음이다. 지금은 `Rules`, `Reference`, `Templates`, `Records` 넷이다.
     새 묶음을 만들면 `for-humanity.config.mjs`의 `navigation`에 순서를 더한다.
   - `order`는 묶음 안의 순서다. 10 단위로 매겨 사이에 끼울 자리를 둔다.
4. 홈 [README.md](README.md)의 문서 표, [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md)의 문서 지도,
   루트 [README.md](https://github.com/minu-ha/uoo/blob/master/README.md)의 `blueprint/` 칸에 한 줄씩 더한다.
   루트 README를 고치면 번역본도 같이 고친다 ([workflow.md](workflow.md#05.A) 05.A절).

## <a id="03"></a>03 빈 틀

```markdown
---
name: {영어 이름}
label: {한글 이름}
group: {묶음}
order: {묶음 안 순서}
---

{이 문서가 답하는 것 한두 줄. 여기 없는 것은 어디 있는지 링크}

## <a id="00"></a>00 한눈에

{먼저 알 것과 남은 것}

::part[{가름}]

## <a id="01"></a>01 {절}

{본문}

### <a id="01.A"></a>01.A {소제목}

{본문}
```

- `#` 제목은 쓰지 않는다. `name`이 문서의 제목이 된다.
- 첫 `##` 앞의 글이 문서 머리다. 이 문서가 답하는 것 한두 줄과, 여기 없는 것은 어디 있는지 링크를 둔다.

## <a id="04"></a>04 짜임

- 목차는 쓰지 않는다. for-humanity가 `##`와 `###`로 On this page 목차를 만든다.
- 절은 두 자리로 `## <a id="01"></a>01 이름`, 소제목은 절 번호에 대문자를 붙여 `### <a id="01.A"></a>01.A 이름`처럼 쓴다.
  번호를 제목 글과 앵커에 같이 적는다.
- **앵커가 번호 링크를 지킨다.** for-humanity는 제목 글로 id를 만든다 (`01 이름` → `01-이름`). 제목 글을 고치면 그 id가 바뀐다.
  그래서 제목 안에 번호와 같은 `<a id>`를 두고, 다른 곳은 언제나 번호로 가리킨다 (`razor.md#03`).
  앵커를 제목 위에 따로 한 줄로 두면 빈 문단이 되어 앞 절 끝에 붙는다. 그래서 제목 줄 안에 둔다.
- `####` 이하에는 번호도 앵커도 달지 않는다. 목차에 들지 않는 작은 제목이다.
- `00`은 한눈에 자리다. "절 | 무엇을 답하나" 표로 문서를 처음 여는 사람이 길을 찾게 하고, 이 문서에 걸린 질문은 [open-items.md](open-items.md)로 보낸다.
- 절이 많으면 몇 절씩 가름으로 묶는다. 가름을 여는 첫 절의 제목 바로 위에 `::part[이름]` 한 줄을 둔다.
  사이트가 그 앞에 가름 머리를 달고, On this page 목차도 가름마다 끊는다.
- 00 한눈에는 가름 밖에 두고, 끝의 확인 안 된 것 · 자주 틀렸던 것 · 참고 링크는 `기록` 가름으로 묶는다.
- 글 안에서는 제목에 보이는 번호 그대로 "03절", "05.D절"로 가리킨다. 다른 문서는 상대 경로 링크에 절을 붙인다 (`[razor.md](razor.md#03) 03절`).
- 절을 넣거나 빼면 번호와 앵커를 같이 고치고, 그 번호를 가리킨 곳도 저장소 전체에서 찾아 고친다.
  AGENTS.md와 스크립트 주석 (`part 5`)도 절 번호를 쓴다: `git grep -n -e '05.H' -e 'part 5'`.

## <a id="05"></a>05 본문

- 본문은 GFM Markdown이다. 문단, 목록, 표, 코드, 인용 (`>`)을 쓴다. 원시 HTML은 제목 앵커와 아래 강조 예외에만 쓴다.
- 강조가 문장부호나 코드로 끝나고 바로 한글이 붙으면 CommonMark가 강조로 읽지 않는다 (`**(A OR B)**다`가 별표째 보인다).
  이럴 때는 `<strong>…</strong>`로 쓴다.
- 범위의 `~`는 `\~`로 쓴다. GFM은 한 문단 안의 `~` 둘을 취소선으로 읽는다 (`3~5초, 7~9초`).
- 코드 밖의 `*`, `_`, `[`, 영문자 앞의 `<`는 `\`로 막는다. 식별자와 값은 코드 (`var__fighting`)로 쓰면 막을 필요가 없다.
- 큰따옴표와 `--`는 사이트에서 둥근 따옴표와 대시로 보인다. 원문 그대로 보여야 하는 서버 문장은 코드로 쓴다.
- 코드 블록에는 코드, 의사 코드, 파일 트리만 쓴다. 칸을 맞춰야 하는 것은 표로 쓴다.
- Razor 코드 블록에는 언어를 달지 않는다 (` ``` `만). 사이트의 코드 강조 (Shiki)에 Razor 문법이 없어서 `razor`를 달아도 색 없이 그대로 나온다.
  예전 `_index.js`가 입히던 Razor 색은 지금 없다.
- 인용과 확인 표시는 [workflow.md](workflow.md#01.C) 01.C절에 적은 대로 쓴다. "인게임 확인됨"과 "확인되지 않았다"는 그 글자 그대로 쓰면 확인 알약으로 보인다.
  뒤에 날짜가 붙으면 날짜까지 알약이 되고 (`인게임 확인됨 2026-09-28`), 괄호로 감싸면 괄호 없이 보인다. 코드, 링크, 제목 안에서는 바뀌지 않는다.
  문구는 `for-humanity.config.mjs`의 `status`에 있다.
- `#e80030`처럼 색 값만 든 인라인 코드에는 색 칩이 붙는다.
- 다른 문서는 상대 경로 `.md`로 건다. `blueprint/` 밖의 파일 (AGENTS.md, `script/`, `util/` 등)은 GitHub 주소로 건다
  (`https://github.com/minu-ha/uoo/blob/master/<경로>`). for-humanity는 문서 폴더 밖을 가리키는 상대 링크를 사이트 주소로 바꾸지 못해 그 링크가 끊긴다.

## <a id="06"></a>06 한 사실은 한 곳에

- 같은 내용을 두 문서에 쓰지 않는다. 한 곳을 정본으로 두고 다른 곳은 절 번호로 링크한다.
  두 곳에 쓰면 한쪽만 고쳐지고, 어느 쪽이 맞는지 모르게 된다 (overheads.md의 옛 hue 표가 그렇게 틀렸다).
- 무엇이 무엇의 정본인지는 [AGENTS.md](https://github.com/minu-ha/uoo/blob/master/AGENTS.md) 3절 문서 지도 한 곳에 둔다. 문서를 새로 만들거나 정본을 옮기면 그 표를 고친다.
- 템플릿 문서 (bard-necro-handbook 같은)에는 **그 템플릿이 내린 판단**만 둔다. 서버 규칙이나 문법처럼 다른 템플릿에서도 쓰는 내용이 생기면
  공통 문서로 옮기고 링크를 남긴다.

## <a id="07"></a>07 흐름도

- 흐름도는 ` ```mermaid ` 코드 블록에 mermaid 원문을 쓴다. for-humanity가 빌드할 때 beautiful-mermaid 격자 렌더러로 SVG를 그린다.
  격자 렌더러라 mermaid 문법이 전부 되지는 않는다.
- 잘 되는 것: `flowchart TD` 사슬과 나무, `flowchart LR` 판단 사슬 (`예` 사슬을 윗줄로), `sequenceDiagram`.
- 라벨에 괄호를 넣지 않는다. 렌더러가 괄호에서 글을 잘라 낸다. 긴 라벨은 `<br>`로 줄을 나눈다.
- 선 라벨은 한 낱말로 쓴다 (`-- 예 -->`). 띄어 쓰면 격자가 빈칸을 선으로 채워 라벨이 둘로 갈린다.
- 되돌아가는 선과 라벨 달린 합류선은 엉킨다. 그림이 크거나 엉키면 여러 장으로 쪼갠다
  ([bard-necro-handbook.md](bard-necro-handbook.md#05.A) 05.A절).
- 폭은 140칸 안쪽으로 둔다. 넘치면 `LR`을 `TD`로 바꾸거나 둘로 나눈다.

::part[확인]

## <a id="08"></a>08 끝낼 때 확인

- 한 줄은 200자까지다 (`.editorconfig`의 `max_line_length`). 넘으면 코드 밖의 빈칸에서 줄을 바꾸고, 되도록 문장 끝에서 바꾼다.
  문단 안의 줄바꿈은 빈칸 하나로 보이므로 화면이 달라지지 않는다. 표의 줄과 코드 블록 안은 바꾸지 않는다.
- `pnpm docs:build`를 돌린다. frontmatter, 깨진 `.md` 링크, `::part`와 부품 문법이 틀리면 여기서 멈추거나 경고한다.
- 이어서 `node util/check-docs.mjs`를 돌린다. 만든 사이트의 끊긴 링크와 앵커, 앵커가 없거나 번호가 다른 번호 제목을 잡는다.
- `pnpm docs:dev`로 열어 본다. 밝게와 어둡게, 폭 1024와 390에서 가로로 밀리는 곳이 없는지, 흐름도가 그려지는지 본다.
