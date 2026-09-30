# blueprint

이 저장소의 설계 문서다. 읽는 사람은 브라우저로 [_index.html](_index.html)을 열고, 이 파일은 문서를 **쓰는** 사람이 본다.
무엇이 무엇의 정본인지는 [AGENTS.md](../AGENTS.md) 3절 문서 지도에 있다.

## 파일

| 파일          | 하는 일                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------|
| `_index.html` | 첫 화면. 문서 카드는 `_index.js`가 그린다                                                                    |
| `_index.css`  | 모든 문서의 모양, 글꼴, 테마                                                                                 |
| `_index.js`   | 문서 목록 `blueprint_docs`, 사이드바, 번호 글자, 가름 머리, 표 상자, 확인 알약, 색 칩, Razor 코드 색, 흐름도 |
| `favicon.svg` | 탭 아이콘                                                                                                    |
| `*.html`      | 문서 한 장씩. 글만 쓴다                                                                                      |
| `README.md`   | 이 파일                                                                                                      |

모양과 동작은 sk-ax-gas-pp의 `.ignore/blueprint/`에서 가져왔다. 한쪽의 모양이나 동작을 바꾸면 다른 쪽도 맞춘다.

## 새 문서

1. `blueprint/`에 kebab-case `.html`로 만든다. 템플릿 전용이면 `<템플릿>-handbook.html`이다.
2. 아래 빈 틀에서 시작한다.
3. `_index.js`의 `blueprint_docs`에 한 줄을 더한다.
   - `name`은 영어 이름이다. 문서의 `<h1>`, 사이드바 문서 목록, 첫 화면 카드 제목이 이 이름을 함께 쓴다.
   - 문서 목록은 `name`의 abc 순이고 첫 글자가 줄 앞 표지라, 다른 문서와 첫 글자가 겹치지 않게 짓는다.
   - `label`은 한글 이름이다. 카드의 둘째 줄이 되고, 사이드바에서는 이름에 마우스를 올리면 뜬다.
   - `group`은 첫 화면 카드와 문서 머리 윗줄에 보이는 묶음이다.
4. [AGENTS.md](../AGENTS.md)의 문서 지도와 루트 [README.md](../README.md)의 `blueprint/` 칸에 한 줄씩 더한다.
   루트 README를 고치면 번역본도 같이 고친다 ([workflow.html](workflow.html#05.A) 05.A절).

## 빈 틀

```html
<!doctype html>
<html lang="ko">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BLUEPRINT - UOO</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="_index.css">
<script src="_index.js"></script>

<body class="bp_index__root">
<main class="bp_index__doc">
<h1>{영어 이름, blueprint_docs의 name}</h1>
<p>{이 문서가 답하는 것 한두 줄. 여기 없는 것은 어디 있는지 링크}</p>

<h2 id="00">00 한눈에</h2>
<p>{먼저 알 것과 남은 것}</p>

<h2 id="01" data-part="{가름}">01 {절}</h2>
<p>{본문}</p>

<h3 id="01.A">01.A {소제목}</h3>
<p>{본문}</p>
</main>
```

- `<head>`는 모든 문서가 같다. 글꼴은 `_index.css`가 불러오므로 글꼴 링크를 따로 두지 않는다. `<body>`와 `<main>`의 class도 모든 문서가 같다.
- doctype이 빠지면 quirks 모드로 그려져 표 줄 높이가 달라진다.
- `<title>`은 모든 문서가 `BLUEPRINT - UOO` 하나다. 문서 이름은 사이드바 문서 목록이 보여 준다.

## 짜임

- 맨 위에는 `<h1>` 제목, 이 문서가 답하는 것 한두 줄, 여기 없는 것은 어디 있는지 링크를 둔다. 제목은 `blueprint_docs`의 `name`과 같게 쓴다 (`<h1>Overheads</h1>`).
- 목차는 쓰지 않는다. `_index.js`가 `id`가 있는 `<h2>`와 `<h3>`로 만든다.
- 절은 두 자리로 `<h2 id="01">01 이름</h2>`, 소제목은 절 번호에 대문자를 붙여 `<h3 id="01.A">01.A 이름</h3>`처럼 번호를 제목과 `id`에 같이 적는다.
  `<h4>`와 `<h5>`에는 번호도 `id`도 달지 않는다. 목차에 들지 않는 작은 제목이다.
- `00`은 한눈에 자리다. "절 | 무엇을 답하나" 표로 문서를 처음 여는 사람이 길을 찾게 하고, 이 문서에 걸린 질문은 [open-items.html](open-items.html)로 보낸다.
- 절이 많으면 몇 절씩 가름으로 묶는다. 가름을 여는 첫 절의 `<h2>`에 `data-part="이름"`을 단다 (`<h2 id="05" data-part="문서 · 커밋">`).
  `_index.js`가 그 앞에 가름 머리를 달고, 사이드바 목차도 가름마다 목록을 끊는다.
- 00 한눈에는 가름 밖에 두고, 끝의 확인 안 된 것 · 자주 틀렸던 것 · 참고 링크는 `기록` 가름으로 묶는다.
- 글 안에서는 제목에 보이는 번호 그대로 "03절", "05.D절"로 가리킨다. 다른 문서는 상대 경로 링크에 절을 붙인다 (`<a href="razor.html#03">razor.html</a> 03절`).
- 절을 넣거나 빼면 번호와 `id`를 같이 고치고, 그 번호를 가리킨 곳도 저장소 전체에서 찾아 고친다.
  AGENTS.md와 스크립트 주석 (`part 5`)도 절 번호를 쓴다: `git grep -n -e '05.H' -e 'part 5'`.

## 본문

- 본문은 태그만 쓴다: `h1`–`h5` `p` `ul` `ol` `li` `table` `thead` `tbody` `tr` `th` `td` `pre` `code` `blockquote` `a` `strong` `em` `hr`.
  `class`와 `style`은 쓰지 않는다. 예외는 흐름도 원문 `<pre class="mermaid">`와 가름을 여는 `<h2>`의 `data-part`다.
- 글 속의 `<` `>` `&`는 `&lt;` `&gt;` `&amp;`로 쓴다. 그대로 쓰면 브라우저가 태그로 읽어 글이 조용히 사라진다.
- `<pre>`에는 코드, 의사 코드, 파일 트리만 쓴다. 파일 트리의 한글은 줄 끝 주석에만 둔다. 칸을 맞춰야 하는 것은 `<table>`로 쓴다.
  코드 글꼴 JetBrains Mono에는 한글이 없어서 한글이 섞인 열은 어긋난다.
- Razor로 보이는 `<pre><code>`에는 `_index.js`가 색을 입힌다 (주석, 문자열, 키워드, 명령, 접두 변수). 그러니 예시는 실제로 도는 Razor 줄로 쓴다.
- 인용과 확인 표시는 [workflow.html](workflow.html#01.C) 01.C절에 적은 대로 쓴다. "인게임 확인됨"과 "확인되지 않았다"는 그 글자 그대로 쓰면 알약으로 보인다.
  코드, 링크, 제목 안에서는 바뀌지 않는다.
- `<code>#e80030</code>`처럼 색 값만 든 코드에는 색 칩이 붙는다.

## 한 사실은 한 곳에

- 같은 내용을 두 문서에 쓰지 않는다. 한 곳을 정본으로 두고 다른 곳은 절 번호로 링크한다.
  두 곳에 쓰면 한쪽만 고쳐지고, 어느 쪽이 맞는지 모르게 된다 (overheads.html의 옛 hue 표가 그렇게 틀렸다).
- 무엇이 무엇의 정본인지는 [AGENTS.md](../AGENTS.md) 3절 문서 지도 한 곳에 둔다. 문서를 새로 만들거나 정본을 옮기면 그 표를 고친다.
- 템플릿 문서 (bard-necro-handbook 같은)에는 **그 템플릿이 내린 판단**만 둔다. 서버 규칙이나 문법처럼 다른 템플릿에서도 쓰는 내용이 생기면
  공통 문서로 옮기고 링크를 남긴다.

## 흐름도

- 흐름도는 `<pre class="mermaid">` 안에 mermaid 원문을 쓴다. `_index.js`가 beautiful-mermaid 격자 렌더러로 SVG를 그린다.
  렌더러를 CDN에서 받아 오므로 오프라인이면 원문이 그대로 보인다. 격자 렌더러라 mermaid 문법이 전부 되지는 않는다.
- 잘 되는 것: `flowchart TD` 사슬과 나무, `flowchart LR` 판단 사슬 (`예` 사슬을 윗줄로), `sequenceDiagram`.
- 라벨에 괄호를 넣지 않는다. 렌더러가 괄호에서 글을 잘라 낸다. 긴 라벨은 `&lt;br&gt;`로 줄을 나눈다.
- 선 라벨은 한 낱말로 쓴다 (`-- 예 -->`). 띄어 쓰면 격자가 빈칸을 선으로 채워 라벨이 둘로 갈린다.
- 되돌아가는 선과 라벨 달린 합류선은 엉킨다. 그림이 크거나 엉키면 여러 장으로 쪼갠다
  ([bard-necro-handbook.html](bard-necro-handbook.html#05.A) 05.A절).
- 폭은 140칸 안쪽으로 둔다. 넘치면 `LR`을 `TD`로 바꾸거나 둘로 나눈다.

## 끝낼 때 확인

- 한 줄은 200자까지다 (`.editorconfig`의 `max_line_length`). 넘으면 태그와 `<code>` 밖의 빈칸에서 줄을 바꾸고, 되도록 문장 끝에서 바꾼다.
  `<pre>` 안은 바꾸지 않는다. 그 밖에서는 줄바꿈이 빈칸 하나로 보이므로 화면이 달라지지 않는다.
- `util/check-blueprint.sh`를 돌린다. 첫 줄 doctype, 끊긴 링크, 목록에 없는 문서, 이스케이프를 빠뜨린 꺾쇠, 제목 번호와 `id`가 어긋난 곳,
  `data-part`의 자리, 첫 글자가 겹치는 `name`, `name`과 다른 `<h1>`을 잡는다.
- 브라우저로 열어 본다. 밝게와 어둡게, 폭 1024와 390에서 가로로 밀리는 곳이 없는지, 흐름도가 그려지는지 본다.
