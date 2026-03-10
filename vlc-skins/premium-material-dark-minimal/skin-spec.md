# Skin Specification — Premium Material Dark Minimal

## 1) Canvas

- Base resolution: `1200 x 720`
- Corner radius: `24px`
- Safe padding: `24px`

## 2) Color tokens

- Background: `#0F1115`
- Surface: `#151923`
- Surface elevated: `#1B2130`
- Text primary: `#E9EDF5`
- Text secondary: `#9AA4B5`
- Accent: `#5E81F4`
- Accent hover: `#7C9BFF`
- Divider: `#2A3142`

## 3) Zones

### A. Top app bar (`1200x72`)

- Left: VLC mark / skin title
- Center: track title (ellipsis)
- Right: window controls (`minimize`, `maximize`, `close`)

### B. Video stage (`1152x528`, centered)

- Rounded container with subtle shadow
- Dark fallback gradient for audio-only mode

### C. Bottom control bar (`1152x88`)

- Left cluster: previous, play/pause, next
- Center: seek bar + current time / duration
- Right cluster: volume, fullscreen, playlist

## 4) Sizing and spacing

- Primary icon button: `44x44`
- Play button (emphasized): `52x52`
- Button radius: `22px` and `26px` for play
- Horizontal gap between controls: `12px`
- Seek bar height: `6px`
- Thumb size: `14px`

## 5) Interaction states

- Default: surface elevated
- Hover: add `#FFFFFF` at 8% overlay
- Pressed: add `#000000` at 12% overlay
- Active toggle: fill with accent color

## 6) Motion guidance

- Hover transition: `120ms ease-out`
- Press transition: `80ms ease-in`
- Progress thumb movement: linear

## 7) Typography

- Family: `Inter` or system sans fallback
- Title: 16 semibold
- Secondary/meta: 12 medium
- Time labels: 12 medium, tabular if available

## 8) Accessibility

- Minimum contrast ratio: 4.5:1 for text
- Focus ring: 2px accent outer glow
- Hitbox min size: 40x40
