#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST="$ROOT/dist"
PKG="$DIST/premium-material-dark-minimal.vlt"

mkdir -p "$DIST"
rm -f "$PKG"

(
  cd "$ROOT"
  zip -rq "$PKG" skin2 assets colors.json skin-spec.md README.md
)

echo "Built: $PKG"
