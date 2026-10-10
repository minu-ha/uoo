// Check the docs for two things the for-humanity build does not catch:
//   1. a link in the built site to a page, file or anchor that does not exist
//   2. a numbered heading in the Markdown sources without its anchor, or with an anchor whose
//      number differs from the heading text (## <a id="04"></a>04 ..., ### <a id="04.C"></a>04.C ...)
//
// Section anchors are section numbers, so renumbering a section breaks every link that points at
// it. Run this after moving or renumbering sections, and after every docs build.
//
//   pnpm docs:build && node util/check-docs.mjs [site] [docs]
//
// site defaults to blueprint/dist and docs to blueprint, both from the repository root.
// Exit 1 if anything is wrong.
import {existsSync, readFileSync, readdirSync, statSync} from "node:fs";
import {dirname, join, relative, resolve} from "node:path";
import {fileURLToPath} from "node:url";
import {parse} from "parse5";

const repo = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const site = resolve(process.argv[2] ?? join(repo, "blueprint", "dist"));
const docs = resolve(process.argv[3] ?? join(repo, "blueprint"));
const problems = [];

/**
 * Every element under a parse5 node. Script and style bodies are text nodes, so markup inside
 * them is not taken for real elements.
 */
const elementsOf = (node) => {
    const children = node.childNodes ?? [];
    const own = node.attrs === undefined ? [] : [node];

    return [...own, ...children.flatMap(elementsOf), ...(node.content ? elementsOf(node.content) : [])];
};

const attributeOf = (element, name) => element.attrs.find((attribute) => attribute.name === name)?.value;

// ---------------------------------------------------------------------------- built site links

if (!existsSync(site)) {
    problems.push(`${relative(repo, site)}: no built site. Run pnpm docs:build first`);
} else {
    const pages = new Map();

    for (const path of readdirSync(site, {recursive: true}).filter((path) => path.endsWith(".html"))) {
        const file = join(site, path);
        const elements = elementsOf(parse(readFileSync(file, "utf8")));
        const ids = elements.map((element) => attributeOf(element, "id")).filter((id) => id !== undefined);
        const repeated = ids.filter((id, index) => ids.indexOf(id) !== index);

        for (const id of new Set(repeated)) {
            problems.push(`${path}: the id "${id}" appears more than once`);
        }

        pages.set(file, {path, elements, ids: new Set(ids)});
    }

    let checked = 0;

    for (const [file, page] of pages) {
        for (const element of page.elements) {
            const reference = attributeOf(element, "href") ?? attributeOf(element, "src");

            // External links and other schemes (mailto:, data:) are not ours to check
            if (reference === undefined || /^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(reference)) {
                continue;
            }

            const url = new URL(reference, `http://site/${relative(site, file).split("\\").join("/")}`);
            let target = join(site, decodeURIComponent(url.pathname));

            if (existsSync(target) && statSync(target).isDirectory()) {
                target = join(target, "index.html");
            }

            checked += 1;

            if (!existsSync(target)) {
                problems.push(`${page.path}: ${reference} -- no such page or file`);
                continue;
            }

            const destination = pages.get(target);
            const anchor = decodeURIComponent(url.hash.slice(1));

            if (destination !== undefined && anchor !== "" && !destination.ids.has(anchor)) {
                problems.push(`${page.path}: ${reference} -- no such anchor`);
            }
        }
    }

    console.log(`${relative(repo, site)}: ${pages.size} pages, ${checked} local references`);
}

// ---------------------------------------------------------------------------- heading anchors

const sources = readdirSync(docs).filter((name) => name.endsWith(".md"));
let numbered = 0;

for (const name of sources) {
    let inFence = "";

    readFileSync(join(docs, name), "utf8").split("\n").forEach((line, index) => {
        const where = `${relative(repo, join(docs, name))}:${index + 1}`;
        const fence = /^(`{3,}|~{3,})/.exec(line)?.[1];

        // Headings inside a code block are examples, like the empty template in writing.md
        if (fence !== undefined && (inFence === "" || fence.startsWith(inFence))) {
            inFence = inFence === "" ? fence : "";
            return;
        }

        const heading = inFence === "" ? /^(#{2,6}) (?:<a id="([^"]*)"><\/a>)?(.*)$/.exec(line) : null;

        if (heading === null) {
            return;
        }

        const [, hashes, anchor, text] = heading;
        const number = /^(\d{2}(?:\.[A-Z])?)(?: |$)/.exec(text)?.[1];

        if (hashes.length > 3) {
            if (anchor !== undefined) {
                problems.push(`${where}: ${hashes} headings take no anchor`);
            }
            return;
        }

        if (number === undefined) {
            if (anchor !== undefined) {
                problems.push(`${where}: the anchor "${anchor}" is on a heading without a number`);
            }
            return;
        }

        numbered += 1;

        if (anchor === undefined) {
            problems.push(`${where}: the numbered heading "${number}" has no <a id="${number}"></a>`);
        } else if (anchor !== number) {
            problems.push(`${where}: the anchor "${anchor}" does not match the heading number "${number}"`);
        }
    });
}

console.log(`${relative(repo, docs)}: ${sources.length} sources, ${numbered} numbered headings`);

for (const problem of problems) {
    console.error(problem);
}

if (problems.length > 0) {
    process.exit(1);
}

console.log("ok");
