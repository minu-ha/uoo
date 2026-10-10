// Tests for util/check-docs.mjs: node --test util/check-docs.test.mjs
import assert from "node:assert/strict";
import {spawnSync} from "node:child_process";
import {mkdirSync, mkdtempSync, rmSync, writeFileSync} from "node:fs";
import {tmpdir} from "node:os";
import {join} from "node:path";
import {test} from "node:test";
import {fileURLToPath} from "node:url";

const checker = fileURLToPath(new URL("./check-docs.mjs", import.meta.url));

/**
 * Runs the checker on a one-page site and one Markdown source, both written to a temp folder.
 */
const runCheck = ({html = "<h2 id=\"real\">Heading</h2>", markdown = "## Plain heading\n"} = {}) => {
    const directory = mkdtempSync(join(tmpdir(), "uoo-check-docs-"));

    try {
        mkdirSync(join(directory, "site"));
        mkdirSync(join(directory, "docs"));
        writeFileSync(join(directory, "site", "index.html"), html);
        writeFileSync(join(directory, "docs", "page.md"), markdown);

        return spawnSync(process.execPath, [checker, join(directory, "site"), join(directory, "docs")], {encoding: "utf8"});
    } finally {
        rmSync(directory, {recursive: true, force: true});
    }
};

test("passes a site whose links and anchors all exist", () => {
    const result = runCheck({html: "<h2 id=\"real\">Heading</h2><a href=\"#real\">Heading</a><a href=\"/\">Home</a>"});

    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /2 local references/);
});

test("ignores markup inside scripts, styles and comments", () => {
    const result = runCheck({
        html: `<script>const s = '<a href="missing/">'</script><style>a::after { content: '<a href="missing/">' }</style>
            <!-- <a href="missing/"> --><h2 id="real">Heading</h2><a href="#real">Heading</a>`,
    });

    assert.equal(result.status, 0, result.stderr);
});

test("rejects a link to a missing page and a missing anchor", () => {
    const result = runCheck({html: "<a href=\"/missing/\">Page</a><a href=\"#missing\">Anchor</a>"});

    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /\/missing\/ -- no such page or file/);
    assert.match(result.stderr, /#missing -- no such anchor/);
});

test("rejects a repeated id", () => {
    const result = runCheck({html: "<h2 id=\"twice\">First</h2><h2 id=\"twice\">Second</h2>"});

    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /"twice" appears more than once/);
});

test("passes numbered headings whose anchors match their numbers", () => {
    const result = runCheck({markdown: "## <a id=\"04\"></a>04 Game\n\n### <a id=\"04.C\"></a>04.C Config\n\n#### Small\n"});

    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /2 numbered headings/);
});

test("rejects a numbered heading without its anchor, or with another number", () => {
    const result = runCheck({markdown: "## 04 Game\n\n### <a id=\"04.B\"></a>04.C Config\n"});

    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /page\.md:1: the numbered heading "04" has no <a id="04"><\/a>/);
    assert.match(result.stderr, /page\.md:3: the anchor "04\.B" does not match the heading number "04\.C"/);
});

test("skips headings inside code blocks", () => {
    const result = runCheck({markdown: "```markdown\n## 01 {절}\n```\n"});

    assert.equal(result.status, 0, result.stderr);
});
