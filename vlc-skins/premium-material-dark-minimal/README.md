# Premium Material Dark Minimal (VLC Skin)

A ready-to-use VLC Skin2 package with a dark, minimal, material-inspired layout.

## What you get

- Working Skin2 theme (`skin2/theme.xml`)
- Text-only source repository (bitmap assets are generated at build time)
- Color tokens (`colors.json`)
- Design reference (`skin-spec.md`)
- Packaging script (`build-vlt.sh`)

## Build

```bash
bash vlc-skins/premium-material-dark-minimal/build-vlt.sh
```

The build script generates required `skin2/*.bmp` files into a temp folder and packages everything into:

- `vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt`

## Install

- Linux: `~/.local/share/vlc/skins2/`
- Windows: `%APPDATA%/vlc/skins2/`

Select the new skin in VLC preferences and restart VLC.
