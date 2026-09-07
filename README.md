# Four Centres of Excellence

A cinematic, single-file web presentation for the BPUT Annual Academic Council —
Centurion University's four Centres of Excellence (Future Nexus, VEDIC, I5.0-4C Lab, PATHS)
and a Build·Operate·Scale·Transfer proposal.

The markup, styles, script and diagrams live in **`index.html`**; image files are
served directly from **`assets/`**. No build step is required for deployment.

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

Images are referenced directly from `assets/`. Replacing a file with another file
of the same name takes effect on the next Vercel deployment without regenerating
`index.html`. If an asset is renamed or added, update the asset URL block near the
end of the stylesheet in `index.html`.

## Editing content

Each slide is a `<section class="slide" data-title="…" data-section="…">`. Copy is
plain HTML inside `.slide__inner`. The three hand-authored SVG diagrams (VEDIC
Hub-and-Spoke, PATHS Learning Loop, Build·Operate·Scale·Transfer pipeline) are
inline and theme-aware via `currentColor` plus `--ember` / `--pulse` / `--gold`.
