#!/usr/bin/env python3
"""Reconstruct the exact StructDepth paper-alignment patch stored in patch_parts/."""

from pathlib import Path
import base64
import gzip
import hashlib

EXPECTED_PATCH_SHA256 = "df125ef3acf7b429785df18a84e075b95f844ced3852afce243b9068abc648af"

root = Path(__file__).resolve().parent
parts = sorted((root / "patch_parts").glob("StructDepth_patch.diff.gz.b64.part*"))

if len(parts) != 8:
    raise SystemExit(f"Expected 8 patch parts, found {len(parts)}")

payload = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
gz_bytes = base64.b64decode(payload, validate=True)
patch_bytes = gzip.decompress(gz_bytes)
sha256 = hashlib.sha256(patch_bytes).hexdigest()

if sha256 != EXPECTED_PATCH_SHA256:
    raise SystemExit(
        "Patch integrity check failed:\n"
        f"  expected {EXPECTED_PATCH_SHA256}\n"
        f"  got      {sha256}"
    )

out = root / "StructDepth_patch_from_uploaded.diff"
out.write_bytes(patch_bytes)
print(f"Wrote: {out}")
print(f"SHA256: {sha256}")
print("Apply from the root of the ORIGINAL uploaded StructDepth source with:")
print(f"  patch --batch -p5 < {out}")
