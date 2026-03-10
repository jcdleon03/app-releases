# Skin2 build files (work-in-progress)

This folder now contains an actual Skin2 `theme.xml` skeleton so you can continue building a real `.vlt` package.

## Important

- `theme.xml` currently uses **primitive shapes and placeholder button image refs** (`up/over/down` empty).
- Open this in **VLC Skin Editor** and assign imported PNG assets for each button/slider state.
- Keep IDs and geometry, swap visuals.

## Build `.vlt`

From repository root:

```bash
bash vlc-skins/premium-material-dark-minimal/build-vlt.sh
```

Output:

- `vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt`

Install into VLC `skins2` folder and select it in VLC interface settings.
