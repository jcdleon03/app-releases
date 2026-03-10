# Premium Material Dark Minimal (VLC Skin)

This is a **real VLC Skin2 starter** for a premium material-inspired, dark, minimalistic look.

## Included

- Dark material token system (`colors.json`)
- Design blueprint (`skin-spec.md`)
- SVG icon set (`assets/`)
- Buildable Skin2 project skeleton (`skin2/theme.xml`)
- `.vlt` packaging script (`build-vlt.sh`)

## Quick start

1. Open `skin2/theme.xml` in VLC Skin Editor.
2. Import your button/slider PNG states and assign them to each control (`up`, `over`, `down`).
3. Keep existing control IDs/layout or tune spacing as desired.
4. Build package:

```bash
bash vlc-skins/premium-material-dark-minimal/build-vlt.sh
```

5. Copy generated file:
   - `vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt`

## Install

- Linux: `~/.local/share/vlc/skins2/`
- Windows: `%APPDATA%/vlc/skins2/`

Then pick the skin in VLC settings and restart VLC.

## Current status

- Layout, zones, and control wiring are prepared.
- Visual polish now mainly depends on adding your final bitmap states in Skin Editor.
