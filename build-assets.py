#!/usr/bin/env python3
"""
Inline everything in assets/ into index.html as data: URIs, so the deck stays a
single portable file that works as a local file, on any host, inside a
claude.ai Artifact, and in PDF export.

Re-run this whenever you change a file in assets/. It only rewrites the block
between /*__ASSETS_START__*/ and /*__ASSETS_END__*/ inside <style id="asset-uris">.

    python3 build-assets.py
"""
import base64, io, re, sys, pathlib

ROOT = pathlib.Path(__file__).parent
A = ROOT / "assets"
HTML = ROOT / "index.html"

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required:  python3 -m pip install pillow")


def photo(name, src, width, quality=66, crop=None):
    im = Image.open(A / src).convert("RGB")
    if crop:  # (left, top, right, bottom) as fractions of w/h
        w, h = im.size
        im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return name, "image/jpeg", buf.getvalue()


def png(name, src, width):
    im = Image.open(A / src).convert("RGBA")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return name, "image/png", buf.getvalue()


def svg(name, src, recolor=None):
    txt = (A / src).read_text(encoding="utf-8")
    for a, b in (recolor or {}).items():
        txt = txt.replace(a, b)
    txt = re.sub(r"\s+", " ", txt).strip()
    return name, "image/svg+xml", txt.encode("utf-8")


ASSETS = [
    # cinematic backdrops (dark, sit under a gradient scrim)
    photo("cover",  "lab_photos/XR-Lab-Development and Testing Lab.jpeg", 1600, 70),
    photo("div01",  "lab_photos/XR-Lab-Thinkers Area.jpeg",              1400, 66),
    # lab cards
    photo("lab-xr", "lab_photos/XR-Lab-Development and Testing Area.jpeg", 1200, 66),
    photo("lab-id", "lab_photos/Industrial Design Lab.jpeg",              1200, 66),
    # extra XR spaces (available if you want more photos on other slides)
    photo("xr-zone",    "lab_photos/XR Lab-Experience Zone.jpeg",         1100, 64),
    photo("xr-headset", "lab_photos/XR-Lab-Experience Zone.jpeg",         1100, 64),
    # marks
    png("fn-logo",      "logo-light.png", 480),   # Future Nexus, white wordmark — for dark theme
    png("fn-logo-dark", "logo-dark.png",  480),   # Future Nexus, black wordmark — for light theme
    png("naac",    "NAAC A+ Logo.png", 260),
    # Keep the complete portrait mark. Cropping this asset removes the lower
    # university wordmark and makes the logo appear broken in the deck.
    photo("cutm",  "Centurion University_Logo_Dark.jpeg", 500, 88),
    png("vedic-bput", "vedic_logos/bput_logo.png", 260),
    png("vedic-ds",   "vedic_logos/ds_logo.png",   520),
    png("vedic-gtet", "vedic_logos/gtet_logo.png", 300),
    png("vedic-pmec", "vedic_logos/pmec_logo.png", 260),
    # partner logos — recoloured to ink so they read inside a white chip
    svg("lg-unity",    "logo-unity.svg",    {"#ffffff": "#0B1A30"}),
    svg("lg-unreal",   "logo-unreal.svg",   {"#ffffff": "#0B1A30"}),
    svg("lg-ethereum", "logo-ethereum.svg", {"#ffffff": "#0B1A30"}),
    svg("lg-solidity", "logo-solidity.svg", {"#ffffff": "#0B1A30"}),
    svg("lg-hyper",    "logo-hyperledger.svg"),
    png("lg-maya",     "logo-maya.png", 240),
    png("lg-3dx",      "logo-3dx.png",  240),
]

lines, total = [], 0
for name, mime, raw in ASSETS:
    b64 = base64.b64encode(raw).decode("ascii")
    total += len(b64)
    lines.append(f'  --img-{name}:url("data:{mime};base64,{b64}");')
    print(f"  {name:12} {mime:16} {len(raw)/1024:7.1f} KB raw -> {len(b64)/1024:7.1f} KB b64")

block = "/*__ASSETS_START__*/\n:root{\n" + "\n".join(lines) + "\n}\n/*__ASSETS_END__*/"

html = HTML.read_text(encoding="utf-8")
if "/*__ASSETS_START__*/" not in html:
    sys.exit("index.html has no <style id=\"asset-uris\"> block with the ASSETS markers.")
html = re.sub(r"/\*__ASSETS_START__\*/.*?/\*__ASSETS_END__\*/", lambda m: block, html, flags=re.S)
HTML.write_text(html, encoding="utf-8")

print(f"\n  inlined {len(ASSETS)} assets  ~{total/1024/1024:.2f} MB base64  ->  index.html")
