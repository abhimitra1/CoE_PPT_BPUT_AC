#!/usr/bin/env python3
"""Refresh the asset URL block in index.html.

Images stay as normal files under assets/ so replacing a deployed file takes
effect without rebuilding Base64 data. Run this only when adding, removing, or
renaming an asset; changing an image's contents requires no rebuild.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
HTML = ROOT / "index.html"

ASSETS = {
    "cover": "assets/lab_photos/XR-Lab-Development and Testing Lab.png",
    "div01": "assets/lab_photos/XR-Lab-Thinkers Area.png",
    "lab-xr": "assets/lab_photos/XR-Lab-Development and Testing Area.jpeg",
    "lab-id": "assets/lab_photos/Industrial Design Lab.png",
    "xr-zone": "assets/lab_photos/XR Lab-Experience Zone.jpeg",
    "xr-headset": "assets/lab_photos/XR-Lab-Experience Zone.jpeg",
    "fn-logo": "assets/logo-light.png",
    "fn-logo-dark": "assets/logo-dark.png",
    "naac": "assets/NAAC A+ Logo.png",
    "cutm": "assets/Centurion University_Logo_Dark.jpeg",
    "vedic-bput": "assets/vedic_logos/bput_logo.png",
    "vedic-ds": "assets/vedic_logos/ds_logo.png",
    "vedic-gtet": "assets/vedic_logos/gtet_logo.png",
    "vedic-pmec": "assets/vedic_logos/pmec_logo.png",
    "lg-unity": "assets/logo-unity.svg",
    "lg-unreal": "assets/logo-unreal.svg",
    "lg-ethereum": "assets/logo-ethereum.svg",
    "lg-solidity": "assets/logo-solidity.svg",
    "lg-hyper": "assets/logo-hyperledger.svg",
    "lg-maya": "assets/logo-maya.png",
    "lg-3dx": "assets/logo-3dx.png",
}

missing = [path for path in ASSETS.values() if not (ROOT / path).is_file()]
if missing:
    raise SystemExit("Missing assets:\n  " + "\n  ".join(missing))

lines = [f'  --img-{name}:url("{path}");' for name, path in ASSETS.items()]
block = "/*__ASSETS_START__*/\n:root{\n" + "\n".join(lines) + "\n}\n/*__ASSETS_END__*/"

html = HTML.read_text(encoding="utf-8")
updated, count = re.subn(
    r"/\*__ASSETS_START__\*/.*?/\*__ASSETS_END__\*/",
    lambda _: block,
    html,
    flags=re.S,
)
if count != 1:
    raise SystemExit("Expected exactly one asset marker block in index.html.")

HTML.write_text(updated, encoding="utf-8")
print(f"Linked {len(ASSETS)} files from assets/ (no Base64 embedding).")
