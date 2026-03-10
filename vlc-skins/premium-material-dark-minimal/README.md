# Premium Material Dark Minimal (VLC Skin)

A ready-to-use VLC Skin2 package with a dark, minimal, material-inspired layout.

## Fast answer: where is the `.vlt`?

After build, it is here:

- `vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt`

## Build
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

## No editor workflow

VLC Skin Editor is optional and not required for this package.

- Full install/use steps: `USAGE.md`
5. Copy generated file:
   - `vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt`

## Install

- Linux: `~/.local/share/vlc/skins2/`
- Windows: `%APPDATA%/vlc/skins2/`

Then pick the skin in VLC settings and restart VLC.

## Current status

- Layout, zones, and control wiring are prepared.
- Visual polish now mainly depends on adding your final bitmap states in Skin Editor.
