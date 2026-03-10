# Usage (No VLC Skin Editor needed)

If VLC Skin Editor is not working, use this direct flow.

## 1) Build the `.vlt` file

From the repo root:

```bash
bash vlc-skins/premium-material-dark-minimal/build-vlt.sh
```

Output file:

- `vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt`

## 2) Install the skin in VLC

### Linux

```bash
mkdir -p ~/.local/share/vlc/skins2
cp vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt ~/.local/share/vlc/skins2/
```

### Windows (PowerShell)

```powershell
$dest = "$env:APPDATA\vlc\skins2"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item "vlc-skins/premium-material-dark-minimal/dist/premium-material-dark-minimal.vlt" -Destination $dest -Force
```

## 3) Enable in VLC

1. Open VLC.
2. Go to **Tools → Preferences** (or press `Ctrl+P`).
3. At bottom-left, keep **Show settings = Simple**.
4. Under **Interface**, choose **Use custom skin**.
5. Select `premium-material-dark-minimal.vlt` from your `skins2` folder.
6. Save and restart VLC.

## 4) If you cannot find the folder

- Linux: create it manually: `~/.local/share/vlc/skins2`
- Windows: create it manually: `%APPDATA%\vlc\skins2`

## 5) Troubleshooting

- If the skin does not appear, restart VLC fully.
- Confirm file extension is exactly `.vlt`.
- Confirm file is in the correct `skins2` folder for your OS.
- Rebuild and recopy if needed.
