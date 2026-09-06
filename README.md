# Three Centres of Excellence

A cinematic, single-file web presentation for the BPUT Annual Academic Council —
Centurion University's three Centres of Excellence (Future Nexus, VEDIC, PATHS)
and a Build·Operate·Scale·Transfer proposal.

Everything (markup, styles, script, diagrams) lives in **`index.html`**. No build
step, no dependencies except Google Fonts.

## Run

Open `index.html` in any modern browser, or serve the folder with a static server.
Slide URLs are `#1` … `#14`.

## Controls

| Key | Action |
| --- | --- |
| `←` `→` / `Space` | Previous / next slide |
| `Home` `End` | First / last slide |
| `O` | Slide overview grid |
| `T` | Light / dark theme (remembered) |
| `F` | Fullscreen |
| `P` | Export / print to PDF |
| `?` | Keyboard help |

Mouse wheel and touch-swipe also navigate on desktop. On phones the deck becomes a
vertical scroll-snap sequence.

## Export to PDF

Press `P` (or the export icon), then in the print dialog choose **Landscape** and
enable **Background graphics**. One slide per page. The PDF follows the current
theme — switch to light first for an ink-friendly file.

## Images

Photo slots use `source.unsplash.com` placeholders that resolve on the open web and
fall back to a designed gradient panel when offline or blocked. To use your own
photos, replace the `src="…"` on each `<img>` (cover backdrop, the PATHS triptych)
and drop images into the folder. Search the file for `SWAP:` / `photo__tag`.

## Editing content

Each slide is a `<section class="slide" data-title="…" data-section="…">`. Copy is
plain HTML inside `.slide__inner`. The three hand-authored SVG diagrams (VEDIC
Hub-and-Spoke, PATHS Learning Loop, Build·Operate·Scale·Transfer pipeline) are
inline and theme-aware via `currentColor` plus `--ember` / `--pulse` / `--gold`.
