#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST="$ROOT/dist"
PKG="$DIST/premium-material-dark-minimal.vlt"
TMPDIR="$(mktemp -d)"

mkdir -p "$DIST"
rm -f "$PKG"

mkdir -p "$TMPDIR/skin2"
python "$ROOT/scripts/generate_skin_bitmaps.py" "$TMPDIR/skin2"
cp "$ROOT/skin2/theme.xml" "$TMPDIR/skin2/theme.xml"
cp "$ROOT/skin2/README-build.md" "$TMPDIR/skin2/README-build.md"
cp -R "$ROOT/assets" "$TMPDIR/assets"
cp "$ROOT/colors.json" "$TMPDIR/colors.json"
cp "$ROOT/skin-spec.md" "$TMPDIR/skin-spec.md"
cp "$ROOT/README.md" "$TMPDIR/README.md"

(
  cd "$TMPDIR"
  zip -rq "$PKG" skin2 assets colors.json skin-spec.md README.md
)

python - <<PY
import shutil
shutil.rmtree(r'''$TMPDIR''', ignore_errors=True)
PY

(
  cd "$ROOT"
  zip -rq "$PKG" skin2 assets colors.json skin-spec.md README.md
)

echo "Built: $PKG"
