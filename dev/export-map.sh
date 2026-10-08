#!/usr/bin/env bash
# Export dev/malapa_map.drawio to docs/img/malapa_map.webp (transparent background).
# Usage, from anywhere:  ./dev/export-map.sh
# Needs draw.io Desktop (https://www.drawio.com) and uv.
# On a headless Linux machine, set DRAWIO, e.g.  DRAWIO="xvfb-run -a drawio --no-sandbox"
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
src="$repo/dev/malapa_map.drawio"
out="$repo/docs/img/malapa_map.webp"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

if [[ -n "${DRAWIO:-}" ]]; then
  read -ra drawio_cmd <<< "$DRAWIO"
elif command -v drawio >/dev/null 2>&1; then
  drawio_cmd=(drawio)                                          # Linux desktop
else
  drawio_cmd=("/Applications/draw.io.app/Contents/MacOS/draw.io")  # macOS
fi

"${drawio_cmd[@]}" --export --format png --transparent --border 0 -o "$tmp/map.png" "$src"

uv run --no-project --with pillow python -I - "$tmp/map.png" "$out" <<'PY'
import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
Image.open(src).convert("RGBA").save(out, "WEBP", quality=90, method=6)
print(f"wrote {out}")
PY
