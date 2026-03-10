#!/usr/bin/env python3
from pathlib import Path
import struct


def write_bmp(path: Path, w: int, h: int, pixfunc):
    row_pad = (4 - (w * 3) % 4) % 4
    row_size = w * 3 + row_pad
    pixel_data_size = row_size * h
    file_size = 54 + pixel_data_size

    with path.open('wb') as f:
        f.write(b'BM')
        f.write(struct.pack('<IHHI', file_size, 0, 0, 54))
        f.write(struct.pack('<IIIHHIIIIII', 40, w, h, 1, 24, 0, pixel_data_size, 2835, 2835, 0, 0))

        for y in range(h - 1, -1, -1):
            row = bytearray()
            for x in range(w):
                r, g, b = pixfunc(x, y)
                row += bytes((b, g, r))
            row += b'\x00' * row_pad
            f.write(row)


def fill(rgb):
    return lambda _x, _y: rgb


def generate(target: Path):
    target.mkdir(parents=True, exist_ok=True)

    write_bmp(target / 'bg.bmp', 1200, 720, fill((15, 17, 21)))
    write_bmp(target / 'topbar.bmp', 1200, 72, fill((21, 25, 35)))
    write_bmp(target / 'bottombar.bmp', 1152, 76, fill((27, 33, 48)))
    write_bmp(target / 'stage.bmp', 1152, 528, fill((10, 12, 16)))

    bw, bh = 44, 44
    cols = 7
    w, h = bw * cols, bh * 3
    base = [(27, 33, 48), (38, 45, 63), (18, 23, 33)]
    accent = (94, 129, 244)

    def button_sheet(x, y):
        c = x // bw
        s = y // bh
        color = base[s]
        if c == 1:
            color = accent if s == 0 else (124, 155, 255) if s == 1 else (74, 104, 204)
        if c == 6:
            color = (130, 40, 45) if s == 0 else (170, 55, 60) if s == 1 else (100, 25, 30)
        return color

    write_bmp(target / 'buttons.bmp', w, h, button_sheet)
    write_bmp(target / 'knob.bmp', 14, 14, fill((233, 237, 245)))
    write_bmp(target / 'seek_track.bmp', 650, 6, fill((42, 49, 66)))
    write_bmp(target / 'vol_track.bmp', 90, 6, fill((42, 49, 66)))


if __name__ == '__main__':
    import sys

    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('skin2')
    generate(out)
    print(f'Generated BMP assets in: {out}')
