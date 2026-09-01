# CLAUDE.md

Guidance for Claude Code sessions working in this repository.

## Project overview

"Optyka dla Artystów Technicznych" — a Polish-language static HTML book about
what a lens does to an image, and why. Not a photography course and not an
optics textbook: the reader is a CG artist who wants to understand **why the
picture looks the way it does** — how many elements, what glass, anamorphic,
halation, defocus, aberrations, distortion — and then reproduce or match it in
a render and a comp. Live at
https://bartoszskrzypiec.github.io/optyka-book/.

42 numbered chapters in nine parts build linearly; ~30 lettered appendices go
deeper (derivations, worked numbers, renderer/comp specifics); one
`matematyka/` primer covers the maths the chapters lean on.

This is a living project, not a one-shot publication. Don't build generated
structures (auto-built indexes, templating) that would need rebuilding on
every content change. `dev/scaffold.py` creates *missing* pages once and never
touches existing ones — it is a scaffolder, not a build step.

## The reader, and what follows from it

A technical artist: uses Nuke, Maya/Houdini and a production renderer, reads
a node graph without help, and has forgotten most of school physics. Not
a physicist, not an optical engineer, and **not** necessarily a photographer.

1. **Register is second person — "ty".** "Zobaczysz", "policzysz",
   "przymkniesz przysłonę". Same as `raytracing-book`, `lookdev-book` and
   `pipeline-book`. This deliberately differs from `atmosfera_chmury_book`,
   which uses "my" because its reader is anyone who looks up.
2. **Formulas are allowed in the main text**, in `.formula` blocks, and every
   formula defines its symbols — in the `.sub` span or in the prose beside it.
   `dev/scaffold.py sprawdz` warns about a `.formula` with no `.sub`.
   Full derivations still belong in appendices marked [WZORY].
3. **Intuition first, formula second.** A chapter never opens with an
   equation. The order is always: what you see → why it happens → the number
   that pins it down.
4. **Every effect must be traced to a cause.** This is the whole premise of
   the book: a Nuke plugin gives you a slider labelled "halation"; this book
   tells you it is light reflecting off the back of the film base and
   re-exposing the emulsion from behind. If a chapter can only describe an
   effect, it isn't finished.
5. **Numbers are metric and Polish-formatted.** Decimal comma, including in
   JavaScript readouts (`.toFixed(1).replace('.', ',')` — the sibling books do
   the same, and `bindSliders()` in `assets/sky3d.js` already defaults to it).
6. **Zero raster images.** No .png/.jpg anywhere. Everything is inline SVG,
   Canvas2D or a three.js widget — inherited from every sibling book, and it
   keeps the repo greppable and diffable. This applies to Część VIII too:
   film frames get **described and reconstructed as diagrams**, never pasted.

## Colour semantics

Same hex values as the sibling books (one visual family), different meanings —
consistent across every visualisation so the reader stops needing legends:

| Token | Means, in this book |
|---|---|
| `--amber` `#e8a33d` | **światło** — a ray, its path, a highlight, a flare |
| `--cyan` `#4fc3c0` | **szkło** — a lens element, a glass surface, a coating |
| `--violet` `#9c82d8` | **wada** — aberration, distortion, anything optics gets wrong. Also the "go deeper" affordance |
| `--raster` `#6e93be` | **matryca i taśma** — pixels, emulsion, grain, halation |

Practical consequence: on every diagram the ray is amber, the glass is cyan,
and what the optics breaks is violet. Inline SVG hardcodes these hexes; CSS
`var()` does not reach SVG presentation attributes.

## No build system

Pure static HTML/CSS/JS. No npm, no package.json, no bundler, no test suite,
no linter. To "run" it, open a file, or serve the root with any static server.
Deployed via GitHub Pages from `main` / root (`.nojekyll` is committed).

One caveat: the 3D widgets are ES modules, so pages carrying one need a real
server — `file://` blocks the import. Every other page opens straight off
disk. When the import is blocked (or three.js fails, or WebGL is missing), the
widget shows its `.viz3d__fallback` with a line naming the cause.

## The shared toolkit — copied in, not written here

`assets/` holds copies from
[learning-materials](https://github.com/bartoszskrzypiec/learning-materials).
Read that repo's `docs/INTEGRATION.md` before changing any of them, and check
its `CHANGELOG.md` before re-copying an update.

```
assets/style.css          — this book's own theme (tokens, layout, blocks)
assets/widgets.css        — component layer for viz.js          [toolkit]
assets/viz3d.css          — component layer for sky3d.js        [toolkit]
assets/interactive.js     — formula modals + .vec[data-tip]     [toolkit]
assets/viz.js             — WebGL2 shaderball + Canvas2D plots  [toolkit]
assets/i18n.js            — hard dependency of viz.js; no-ops on
                            a monolingual page, do not delete   [toolkit]
assets/sky3d.js           — three.js scene engine               [toolkit]
assets/sky3d-fallback.js  — classic script, must load BEFORE the
                            module; catches "module never ran"  [toolkit]
assets/vendor/            — three.js, vendored, never from a CDN
```

`assets/style.css` defines this book's tokens and then aliases them onto the
toolkit's contract (`--text-muted`, `--accent`, `--bg-elevated`, `--radius`,
`--viz-a/b/grid/bg`) in `:root`. **Alias, never rename what the toolkit
reads** — otherwise the next re-copy silently breaks.

`assets/sky3d.js` imports `./vendor/three.module.js` by bare relative path
with no import map, so `vendor/` must stay next to it. Refresh three.js per
`assets/vendor/VERSION`; do not add a package.json.

Polish fallback messages for 3D widgets live in `window.SKY3D_MESSAGES`,
emitted into every page head by `dev/scaffold.py` — the module's own defaults
are English.

## Which tool for which visualisation

The order to try them in, cheapest first:

1. **Static inline SVG** — most diagrams. Ray paths, element cross-sections,
   geometry.
2. **SVG + slider** (see `patterns/svg-slider-widget.md` in learning-materials)
   — a 2D relationship that changes with a parameter: MTF curves, the f-stop
   ladder driving circle of confusion, the Airy disc, blade count → starburst,
   a barrel/pincushion grid, LoCA vs TCA, cos⁴θ.
3. **Canvas2D `.sim`** — something that has to *happen over time* or needs
   per-pixel work: a bokeh-shape renderer, a halation kernel, grain.
4. **`viz.js`** — a lit sphere with real BRDF/Fresnel maths. Its
   `thinFilmRGB()` is exactly the maths of an anti-reflective coating, so
   "why is that ghost green" comes free.
5. **`sky3d.js`** — only where the point is genuinely three-dimensional and
   a flat projection would lie: the element stack with a ray running through
   it, the exit pupil seen from a corner (cat's eye), frustum and sensor
   format, the depth-of-field volume, an anamorphic cylinder.

**Budget: at most ~14 3D widgets in the whole book.** `atmosfera_chmury_book`
held 11 across 54 pages. 3D that only adds a spin is worse than a clean 2D
diagram.

## Structure

```
index.html                              — spis treści, root only
rozdzialy/rozdzial-NN-slug.html         — 42 chapters, NN zero-padded 01–42
dodatki/dodatek-x-slug.html             — ~30 appendices, x = a–z then aa–…
matematyka/podstawy-matematyczne.html   — "Zanim zaczniesz" primer; the one
                                          content page outside rozdzialy/
                                          dodatki, so any repo-wide script
                                          must glob it explicitly
dev/spis.json                           — the book's structure, single source
dev/scaffold.py                         — szkielet | sprawdz
dev/wstaw.py, dev/dopisz.py             — insert content into a page
dev/slowa.py                            — word/visualisation counter
```

The nine parts, in dependency order — **nothing appears before there is
something to explain it with**: Fresnel before ghosting, diffraction before
starbursts, the pupil before bokeh, and aberrations before lens designs
(because a design is an answer to an aberration).

I Światło zanim dotknie szkła · II Kadr i głębia · III Wady, czyli charakter ·
IV Konstrukcje · V Światło, które zbłądziło · VI Matryca, taśma i czas ·
VII To wszystko w CG · VIII Optyka jako język operatorski · IX Czytanie kadru

## Content authoring rules

Inherited from `raytracing-book`, where these conventions come from:

- **Never rename or reletter appendices** without asking. Prose
  cross-references ("Dodatek J", "Dodatek R") are scattered by *name* across
  other files.
- **Every appendix's `.viewport-readout` carries an `EXT OF` line** naming the
  chapter(s) it extends. That line is the source of truth for cross-linking —
  don't infer relationships from titles. The reverse mapping is what fills
  each chapter's `.deeper` block, and `sprawdz` enforces both directions.
- **File names and in-text numbering are decoupled.** Renaming a file must
  never change "Rozdział 12" inside content.
- Navigation is hand-maintained per page. The `topnav` links and the bottom
  `.site-nav.chapter-nav` are duplicates of the same targets — keep them
  identical; `sprawdz` counts them.
- Chapter page order is fixed: `topnav` → `.viewport-readout` → `.eyebrow` →
  `h1` → `.subtitle` → TL;DR (exactly 3 bullets) → `.section` × 2–6 →
  "Z praktyki" → "Słowniczek" → "Co dalej" → "Idź głębiej" → `.site-nav` →
  `.modal-overlay` if used.
- Target per chapter: **2000–3500 words and 5–8 visualisations**, measured
  with `python dev/slowa.py`.

## Część VIII — the one part where a reader can catch you in two seconds

Equipment claims about specific films (which camera, which lenses, which
format) **must be checked against sources while writing**, never recalled from
the model's memory. Everywhere else in the book an error is a physics error
that takes effort to spot; here it is a fact anyone can look up. If a claim
can't be sourced in the session, write the chapter without it — the optical
argument never depends on a particular title.

The same restraint applies to the argument itself: this part reads optical
decisions as dramatic decisions. It is not criticism of films and not a list
of favourite cinematographers.

## Sibling projects — link, don't repeat

This book stands on its own, but where a sibling already derives something in
depth, link to it instead of repeating:

- [raytracing-book](https://bartoszskrzypiec.github.io/raytracing-book/) —
  ray/geometry maths, BRDF, dispersion, spectral rendering.
- [lookdev-book](https://bartoszskrzypiec.github.io/lookdev-book/) — colour
  maths, ACES, transfer functions, log encodings.
- [pipeline-book](https://bartoszskrzypiec.github.io/pipeline-book/) — OCIO
  config architecture, the engineering side of colour.
- [pxrsurface-guide](https://bartoszskrzypiec.github.io/pxrsurface-guide/) —
  renderer material parameters.
- [atmosfera_chmury_book](https://bartoszskrzypiec.github.io/atmosfera_chmury_book/)
  — scattering, the physics of the sky, and the source of `sky3d.js`.

Cross-book links must be **absolute URLs** — these are separate repos and
sites, so a relative path would not resolve.

## Verification

Before every commit:

1. `python dev/scaffold.py sprawdz` — must pass clean.
2. `node --check` on any JS you touched.
3. Serve the root and open the page: no console errors, no horizontal
   overflow at 360 px, no SVG labels outside their `viewBox`.
4. A page with a 3D widget is tested **both** over http and over `file://` —
   they take different failure paths — plus once with WebGL disabled.

Note when checking widgets by screenshot: a widget that renders on demand
photographs **blank** in a headless browser, because the drawing buffer is
cleared after compositing. That is an artifact of the capture, not a broken
widget — read the pixels back with `readPixels`, or give the widget a
spinning camera, before concluding anything from an empty stage.

## Git workflow

Commit and push after each logical unit without asking. Commit messages are
ASCII-only (no Polish diacritics) to sidestep console encoding issues; page
*content* always uses full, correct Polish diacritics. Never force-push or
rewrite history without asking.
