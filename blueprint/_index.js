/*
 * blueprint 문서가 함께 쓰는 스크립트. 문서에는 글만 두고 목차와 부품은 이 파일이 붙인다.
 * <head> 에서 바로 돌아 그리기 전에 테마를 정하고, 나머지는 문서를 다 읽은 뒤에 한다.
 * 1. 테마를 밝게 · 어둡게 고정한다(기본은 시스템 설정)
 * 2. 목차를 만든다 — 문서 목록, 이 문서의 절(h2)과 소제목(h3)
 * 3. 목차가 지금 읽는 절과 소제목을 표시하고, 그 절의 소제목만 펼친다
 * 4. 제목부터 첫 절 앞까지를 머리로 묶고, 제목 앞 절 번호를 번호 글자로 가른다
 * 5. 표를 가로로 밀리는 상자로 감싼다
 * 6. "인게임 확인됨" · "확인되지 않았다" 를 상태 알약으로 바꾸고, <code>#rrggbb</code> 앞에 색 칩을 붙인다
 * 7. _index.html 의 문서 카드를 그린다
 * 8. mermaid 원문(pre.mermaid)을 흐름도로 바꾼다 — CDN 에서 받아 오므로 오프라인이면 원문이 남는다
 * 모양과 동작은 sk-ax-gas-pp 의 .ignore/blueprint/blueprint.js 에서 가져왔다.
 */

const theme_storage_key = 'bp-theme'
const theme_labels = { system: '테마 · 시스템', light: '테마 · 밝게', dark: '테마 · 어둡게' }
const theme_order = ['system', 'light', 'dark']
const mermaid_url = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs'

// 문서 목록 — 새 문서를 만들면 여기에 한 줄을 더한다. group 은 _index.html 카드의 묶음이다
const blueprint_docs = [
  { file: '_index.html', label: '한눈에' },
  { file: 'workflow.html', label: '작업 방식', group: '규칙' },
  { file: 'conventions.html', label: '저장소와 스크립트 규칙', group: '규칙' },
  { file: 'razor.html', label: 'Outlands Razor 문법', group: '문법 · 규정' },
  { file: 'pvp.html', label: 'PvP 규칙', group: '문법 · 규정' },
  { file: 'overheads.html', label: '머리 위 메시지와 쿨다운 바', group: '사양' },
  { file: 'hotkeys.html', label: '핫키 배치', group: '사양' },
  { file: 'bard-necro-handbook.html', label: 'Bard Necro 핸드북', group: '템플릿' },
  { file: 'item-list.txt', label: '아이템 목록', group: '자료' },
]

// 흐름도는 테마 색을 SVG 에 구워 넣으므로 테마가 바뀌면 다시 그린다. 흐름도가 있는 문서에서만 채워진다
let redrawFlows = () => {}

/**
 * 저장된 테마를 읽는다. 사생활 보호 창에서는 접근이 막히므로 실패해도 시스템 설정으로 돈다
 */
const readStoredTheme = () => {
  try {
    const stored = window.localStorage.getItem(theme_storage_key)

    return theme_order.includes(stored) ? stored : 'system'
  } catch {
    return 'system'
  }
}

const applyTheme = (theme) => {
  if (theme === 'system') {
    document.documentElement.removeAttribute('data-theme')
  } else {
    document.documentElement.setAttribute('data-theme', theme)
  }

  const button = document.querySelector('.bp_index__theme')

  if (button) {
    button.textContent = theme_labels[theme]
    button.setAttribute('aria-label', `${theme_labels[theme]}. 눌러서 바꾸기`)
  }

  redrawFlows()
}

const makeElement = (tag, className, text) => {
  const element = document.createElement(tag)

  element.className = className

  if (text !== undefined) {
    element.textContent = text
  }

  return element
}

const currentFile = () => decodeURIComponent(window.location.pathname.split('/').at(-1)) || '_index.html'

/**
 * 제목 첫머리의 절 번호(1. / 1.1)를 떼어 번호 글자로 감싼다. 번호와 번호를 뺀 제목을 돌려준다
 */
const splitNumber = (heading) => {
  const first = heading.firstChild
  const match = first?.nodeType === Node.TEXT_NODE ? first.textContent.match(/^\s*(\d+(?:\.\d+)*)\.?\s+/) : null

  if (!match) {
    return { number: '', title: heading.textContent.trim() }
  }

  first.textContent = first.textContent.slice(match[0].length)

  const title = heading.textContent.trim()

  heading.prepend(makeElement('span', 'bp_index__num', match[1]))

  return { number: match[1], title }
}

/**
 * 제목부터 첫 절(h2) 앞까지를 머리로 묶고, 그 위에 문서 자리를 한 줄 단다. _index.html 은 카드 앞에서 끊는다
 */
const wrapHead = (doc) => {
  const title = doc.querySelector('h1')

  if (!title) {
    return
  }

  const entry = blueprint_docs.find((item) => item.file === currentFile())
  const head = makeElement('header', 'bp_index__head')
  const eyebrow = makeElement('div', 'bp_index__eyebrow')

  for (const text of ['Blueprint', entry?.group ?? 'UOO', currentFile()]) {
    eyebrow.append(makeElement('span', '', text))
  }

  title.before(head)
  head.append(eyebrow)

  let node = title

  while (node && node.tagName !== 'H2' && !node.classList.contains('bp_index__cards')) {
    const next = node.nextElementSibling

    head.append(node)
    node = next
  }
}

/**
 * 목차를 만든다. 절마다 목차 줄과 소제목 목록을 짝지어 돌려주어, 읽는 자리 표시가 같은 짝을 쓴다
 */
const buildNav = (doc) => {
  const nav = makeElement('nav', 'bp_index__nav')
  const brand = makeElement('a', 'bp_index__brand', 'UO Outlands · Razor')
  const docs = makeElement('ul', 'bp_index__docs')
  const toc = makeElement('ul', 'bp_index__toc')
  const theme = makeElement('button', 'bp_index__theme')
  const sections = []

  nav.setAttribute('aria-label', '목차')
  brand.href = '_index.html'
  theme.type = 'button'

  for (const item of blueprint_docs) {
    const link = makeElement('a', 'bp_index__docsLink', item.label)
    const row = document.createElement('li')

    link.href = item.file

    if (item.file === currentFile()) {
      link.classList.add('bp_index__docsLink--current')
      link.setAttribute('aria-current', 'page')
    }

    row.append(link)
    docs.append(row)
  }

  for (const heading of doc.querySelectorAll('h2[id], h3[id]')) {
    const { number, title } = splitNumber(heading)
    const link = makeElement('a', heading.tagName === 'H2' ? 'bp_index__tocLink' : 'bp_index__tocSubLink')
    const row = document.createElement('li')

    link.href = `#${heading.id}`
    link.append(makeElement('span', 'bp_index__tocNum', number || '·'), title)
    row.append(link)

    if (heading.tagName === 'H2') {
      sections.push({ heading, link, list: null, subs: [] })
      toc.append(row)
      continue
    }

    const section = sections.at(-1)

    if (!section) {
      continue
    }

    if (!section.list) {
      section.list = makeElement('ul', 'bp_index__tocSub')
      section.link.after(section.list)
    }

    section.subs.push({ heading, link })
    section.list.append(row)
  }

  nav.append(brand, makeElement('div', 'bp_index__docsLabel', '문서'), docs)
  nav.append(makeElement('div', 'bp_index__navTitle', doc.querySelector('h1')?.textContent.trim() ?? ''))

  if (sections.length > 0) {
    nav.append(toc)
  }

  nav.append(theme)
  document.body.prepend(nav)
  theme.addEventListener('click', () => {
    current_theme = theme_order[(theme_order.indexOf(current_theme) + 1) % theme_order.length]
    applyTheme(current_theme)

    try {
      window.localStorage.setItem(theme_storage_key, current_theme)
    } catch {
      // 저장이 막혀도 이번 방문에는 적용된 채로 둔다
    }
  })

  return sections
}

/**
 * 화면 위쪽을 지난 마지막 절과 그 안의 소제목을 켠다. 소제목은 절 경계를 넘지 않아도 바뀌므로 스크롤마다(한 프레임에 한 번) 다시 잰다
 */
const startSectionSpy = (sections) => {
  if (sections.length === 0) {
    return
  }

  let frame = 0

  const markActive = () => {
    frame = 0

    const current = sections.filter((section) => section.heading.getBoundingClientRect().top < 120).at(-1) ?? sections[0]
    const sub = current.subs.filter((item) => item.heading.getBoundingClientRect().top < 100).at(-1)

    for (const section of sections) {
      const isCurrent = section === current

      section.link.classList.toggle('bp_index__tocLink--active', isCurrent)
      section.list?.classList.toggle('bp_index__tocSub--open', isCurrent)

      for (const item of section.subs) {
        item.link.classList.toggle('bp_index__tocSubLink--active', item === sub)
      }
    }
  }

  window.addEventListener(
    'scroll',
    () => {
      frame ||= window.requestAnimationFrame(markActive)
    },
    { passive: true },
  )

  markActive()
}

const wrapTables = (doc) => {
  for (const table of doc.querySelectorAll('table')) {
    const box = makeElement('div', 'bp_index__table')

    table.before(box)
    box.append(table)
  }
}

/**
 * 확인 표시 두 가지를 알약으로 바꾼다. 괄호로 감싼 "(인게임 확인됨 날짜)" 는 괄호째 알약이 된다.
 * 코드 · 링크 · 제목 안의 글은 건드리지 않는다
 */
const markVerification = (doc) => {
  const pattern = /\((인게임 확인됨(?: \d{4}-\d{2}-\d{2})?)\)|(인게임 확인됨(?: \d{4}-\d{2}-\d{2})?)|(확인되지 않았다)/g
  const walker = document.createTreeWalker(doc, NodeFilter.SHOW_TEXT, {
    acceptNode: (node) =>
      node.parentElement.closest('code, pre, a, h1, h2, h3, h4, h5') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT,
  })
  const nodes = []

  while (walker.nextNode()) {
    if (/인게임 확인됨|확인되지 않았다/.test(walker.currentNode.textContent)) {
      nodes.push(walker.currentNode)
    }
  }

  for (const node of nodes) {
    const text = node.textContent
    const fragment = document.createDocumentFragment()
    let last = 0

    for (const match of text.matchAll(pattern)) {
      const verified = match[3] === undefined

      fragment.append(text.slice(last, match.index))
      fragment.append(
        makeElement('span', `bp_index__pill bp_index__pill--${verified ? 'verified' : 'unverified'}`, match[1] ?? match[2] ?? match[3]),
      )
      last = match.index + match[0].length
    }

    fragment.append(text.slice(last))
    node.replaceWith(fragment)
  }
}

const markColors = (doc) => {
  for (const code of doc.querySelectorAll('code')) {
    const value = code.textContent.trim()

    if (/^#[0-9a-f]{3,8}$/i.test(value)) {
      code.classList.add('bp_index__color')
      code.style.setProperty('--app-color-chip', value)
    }
  }
}

const buildCards = () => {
  const box = document.querySelector('.bp_index__cards')

  if (!box) {
    return
  }

  for (const item of blueprint_docs.filter((entry) => entry.group)) {
    const card = makeElement('a', 'bp_index__card')

    card.href = item.file
    card.append(
      makeElement('span', 'bp_index__cardGroup', item.group),
      makeElement('span', 'bp_index__cardTitle', item.label),
      makeElement('span', 'bp_index__cardFile', item.file),
    )
    box.append(card)
  }
}

/**
 * mermaid 원문을 SVG 로 바꾼다. 색은 지금 테마의 토큰에서 읽는다. 렌더러가 못 오면 원문을 그대로 둔다.
 * 라벨은 SVG 글자로 그린다. HTML 라벨은 <p> 라서 문서 본문의 p 여백을 받아 상자 밖으로 잘린다.
 * 글자 폭을 재고 상자를 만드므로 웹 글꼴이 온 뒤에 그린다
 */
const drawFlows = async (doc) => {
  const sources = [...doc.querySelectorAll('pre.mermaid')]

  if (sources.length === 0) {
    return
  }

  let mermaid

  try {
    mermaid = (await import(mermaid_url)).default
  } catch {
    return
  }

  const flows = sources.map((pre) => ({ pre, source: pre.textContent, canvas: null }))
  let drawing = 0

  // 처음 그릴 때 원문 자리에 상자를 놓는다. 크게 보기는 제 크기로 키우고 흐름의 시작인 가운데로 민다
  const placeBox = (flow) => {
    const box = makeElement('div', 'bp_index__flow')
    const zoom = makeElement('button', 'bp_index__flowZoom', '크게 보기')

    flow.canvas = makeElement('div', 'bp_index__flowCanvas')
    zoom.type = 'button'
    zoom.setAttribute('aria-pressed', 'false')
    zoom.addEventListener('click', () => {
      const zoomed = flow.canvas.classList.toggle('bp_index__flowCanvas--zoomed')

      zoom.textContent = zoomed ? '맞춰 보기' : '크게 보기'
      zoom.setAttribute('aria-pressed', String(zoomed))
      flow.canvas.scrollLeft = zoomed ? (flow.canvas.scrollWidth - flow.canvas.clientWidth) / 2 : 0
    })
    box.append(zoom, flow.canvas)
    flow.pre.replaceWith(box)
  }

  const draw = async () => {
    const styles = getComputedStyle(document.documentElement)
    const token = (name) => styles.getPropertyValue(name).trim()
    const round = ++drawing

    mermaid.initialize({
      startOnLoad: false,
      theme: 'base',
      htmlLabels: false,
      flowchart: { htmlLabels: false, useMaxWidth: false },
      fontFamily: token('--app-font-sans'),
      themeVariables: {
        fontFamily: token('--app-font-sans'),
        fontSize: '13px',
        background: token('--app-color-surface'),
        primaryColor: token('--app-color-accent-soft'),
        primaryBorderColor: token('--app-color-accent'),
        primaryTextColor: token('--app-color-text-strong'),
        lineColor: token('--app-color-text-muted'),
        textColor: token('--app-color-text'),
        edgeLabelBackground: token('--app-color-surface'),
      },
    })

    for (const [index, flow] of flows.entries()) {
      try {
        const { svg } = await mermaid.render(`bp_index__flow${index}_${round}`, flow.source)

        if (round !== drawing) {
          return
        }

        if (!flow.canvas) {
          placeBox(flow)
        }

        flow.canvas.innerHTML = svg
      } catch {
        // 원문이 틀리면 그 흐름도만 원문으로 남긴다
      }
    }
  }

  redrawFlows = () => {
    draw()
  }
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', redrawFlows)
  await document.fonts.ready
  await draw()
}

// 저장이 막힌 창에서도 누를 때마다 돌도록 지금 테마를 여기서 들고 있는다
let current_theme = readStoredTheme()

applyTheme(current_theme)

document.addEventListener('DOMContentLoaded', () => {
  const doc = document.querySelector('.bp_index__doc')

  if (!doc) {
    return
  }

  wrapHead(doc)

  const sections = buildNav(doc)

  applyTheme(current_theme)
  wrapTables(doc)
  markVerification(doc)
  markColors(doc)
  buildCards()
  startSectionSpy(sections)
  drawFlows(doc)
})
