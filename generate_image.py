#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news front page as a 1024x1024 PNG.

Deterministic: no network, no randomness, no timestamps. Run with
`python3 generate_image.py` and it writes entry.png beside itself.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 24
INK = (18, 18, 18)
RED = (158, 24, 24)
GREY = (96, 96, 96)
LIGHT = (238, 238, 232)
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, fill, leading, align="left", width=None):
    for line in lines:
        if align == "center":
            lx = x + (width - draw.textlength(line, font=fnt)) // 2
        else:
            lx = x
        draw.text((lx, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, x1, y, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- lead art
def draw_lead(draw):
    x0, y0, x1, y1 = MARGIN, 126, W - MARGIN, 428
    # dusk sky gradient: deep orange at horizon to dark purple at top
    top = (58, 32, 78)
    mid = (150, 62, 52)
    bot = (232, 122, 54)
    for yy in range(y0, y1):
        t = (yy - y0) / (y1 - y0)
        if t < 0.5:
            a, b, f = top, mid, t / 0.5
        else:
            a, b, f = mid, bot, (t - 0.5) / 0.5
        col = tuple(int(a[i] + (b[i] - a[i]) * f) for i in range(3))
        draw.line([(x0, yy), (x1, yy)], fill=col)
    # low sun, high in the open sky at upper left
    draw.ellipse([x0 + 90, y0 + 42, x0 + 146, y0 + 98], fill=(255, 196, 90))
    # sea at the bottom
    draw.rectangle([x0, y1 - 34, x1, y1], fill=(28, 38, 66))
    for i in range(5):
        yy = y1 - 28 + i * 6
        draw.line([(x0 + 30 + i * 40, yy), (x0 + 260 + i * 40, yy)],
                  fill=(90, 120, 170), width=2)
    # skyline silhouettes
    buildings = [(0, 150, 90), (95, 205, 70), (170, 165, 110), (285, 225, 60),
                 (350, 180, 95), (450, 215, 70), (525, 160, 120), (650, 210, 75),
                 (730, 175, 100), (835, 220, 65), (905, 185, 90)]
    for bx, bw, bh in buildings:
        bx1 = min(x0 + bx + bw, x1)
        draw.rectangle([x0 + bx, y1 - 34 - bh, bx1, y1 - 34],
                       fill=(24, 18, 34))
        # lit windows
        for wy in range(y1 - 34 - bh + 12, y1 - 44, 22):
            for wx in range(x0 + bx + 10, bx1 - 10, 20):
                if (wx + wy) % 44 < 20:
                    draw.rectangle([wx, wy, wx + 6, wy + 8], fill=(255, 190, 90))
    # missile trails: bright arcs rising from the skyline
    trails = [
        ([(x0 + 120, y1 - 40), (x0 + 210, y0 + 120), (x0 + 330, y0 + 40)],
         (x0 + 330, y0 + 40)),
        ([(x0 + 420, y1 - 40), (x0 + 470, y0 + 150), (x0 + 560, y0 + 70)],
         (x0 + 560, y0 + 70)),
        ([(x0 + 760, y1 - 40), (x0 + 700, y0 + 130), (x0 + 610, y0 + 30)],
         (x0 + 610, y0 + 30)),
    ]
    for pts, head in trails:
        draw.line(pts, fill=(255, 220, 140), width=4, joint="curve")
        draw.ellipse([head[0] - 7, head[1] - 7, head[0] + 7, head[1] + 7],
                     fill=(255, 240, 180))
        draw.ellipse([head[0] - 3, head[1] - 3, head[0] + 3, head[1] + 3],
                     fill=(255, 255, 255))
    # explosion glow bursting from the roof of the mid-skyline tower
    ex, ey = x0 + 485, y1 - 34 - 70
    draw.ellipse([ex - 24, ey - 26, ex + 24, ey + 12], fill=(255, 140, 40))
    draw.ellipse([ex - 12, ey - 15, ex + 12, ey + 6], fill=(255, 210, 90))
    draw.polygon([(ex - 8, ey - 26), (ex, ey - 44), (ex + 8, ey - 26)],
                 fill=(255, 170, 60))
    draw.rectangle([x0, y0, x1, y1], outline=INK, width=2)


# ------------------------------------------------------------- panel art
def art_cop(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(196, 224, 196))
    cx, cy, r = x + w // 2, y + h // 2 + 4, 26
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(52, 120, 66))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(30, 80, 44), width=2)
    draw.arc([cx - r + 6, cy - r + 4, cx + r - 6, cy + r - 4], 200, 340,
             fill=(196, 224, 196), width=4)
    draw.line([cx - r - 8, cy + 8, cx + r + 8, cy - 14], fill=(158, 24, 24), width=4)
    draw.text((x + 8, y + 4), "COP31", font=SANS_B(13), fill=RED)


def art_house(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(196, 208, 232))
    cx, cy = x + w // 2, y + h // 2 + 6
    draw.polygon([(cx - 52, cy + 6), (cx, cy - 34), (cx + 52, cy + 6)],
                 fill=(240, 240, 240), outline=INK)
    draw.rectangle([cx - 42, cy + 6, cx + 42, cy + 26], fill=(240, 240, 240),
                   outline=INK)
    draw.rectangle([cx - 6, cy + 8, cx + 6, cy + 26], fill=INK)
    draw.rectangle([cx - 30, cy + 8, cx - 18, cy + 20], fill=(90, 120, 170))
    draw.rectangle([cx + 18, cy + 8, cx + 30, cy + 20], fill=(90, 120, 170))


def art_kyiv(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(224, 210, 190))
    bx, by = x + w // 2 - 34, y + 14
    draw.rectangle([bx, by, bx + 68, y + h - 6], fill=(120, 110, 100))
    for r in range(4):
        for c in range(3):
            wx, wy = bx + 8 + c * 22, by + 10 + r * 14
            draw.rectangle([wx, wy, wx + 12, wy + 9], fill=(255, 220, 130))
    # smoke rising from the roof
    draw.ellipse([bx + 8, by - 12, bx + 30, by + 6], fill=(110, 110, 110))
    draw.ellipse([bx + 26, by - 22, bx + 52, by - 2], fill=(140, 140, 140))
    draw.ellipse([bx + 44, by - 32, bx + 66, by - 12], fill=(170, 170, 170))


def art_factory(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(232, 200, 180))
    fx, fy = x + 60, y + 26
    draw.rectangle([fx, fy, fx + 130, y + h - 6], fill=(150, 90, 70))
    draw.rectangle([fx + 130, fy - 14, fx + 146, y + h - 6], fill=(120, 70, 55))
    draw.polygon([(fx + 24, fy), (fx + 48, fy - 30), (fx + 72, fy)],
                 fill=(255, 150, 40))
    draw.polygon([(fx + 38, fy), (fx + 52, fy - 20), (fx + 66, fy)],
                 fill=(255, 220, 90))
    draw.ellipse([fx + 88, fy - 30, fx + 118, fy - 6], fill=(120, 120, 120))


def art_bitcoin(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(252, 232, 180))
    cx, cy, r = x + w // 2 - 18, y + h // 2 + 2, 24
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(247, 147, 26),
                 outline=(180, 100, 0), width=2)
    draw.text((cx - 11, cy - 17), "B", font=SANS_B(30), fill=(255, 255, 255))
    # rising arrow
    ax = x + w - 52
    draw.line([(ax, y + h - 14), (ax + 16, y + 22), (ax + 34, y + 34)],
              fill=(24, 120, 50), width=4)
    draw.polygon([(ax + 26, y + 16), (ax + 40, y + 30), (ax + 22, y + 34)],
                 fill=(24, 120, 50))


def art_ship(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(180, 210, 235))
    sx, sy = x + 46, y + 30
    draw.polygon([(sx, sy), (sx + 150, sy), (sx + 128, sy + 26), (sx + 22, sy + 26)],
                 fill=(90, 90, 100))
    draw.rectangle([sx + 40, sy - 18, sx + 96, sy], fill=(140, 140, 150))
    draw.line([(sx + 68, sy - 18), (sx + 68, sy - 30)], fill=INK, width=3)
    draw.polygon([(sx + 20, sy - 26), (sx + 40, sy - 14), (sx + 52, sy - 26)],
                 fill=(255, 150, 40))
    draw.polygon([(sx + 32, sy - 22), (sx + 42, sy - 14), (sx + 50, sy - 22)],
                 fill=(255, 220, 90))
    for i, yy in enumerate((y + h - 14, y + h - 8)):
        draw.line([(x + 12 + i * 30, yy), (x + w - 12 - i * 20, yy)],
                  fill=(60, 110, 160), width=2)


PANELS = [
    ("CLIMATE", "COP31 ends with no deal",
     "Nearly 200 nations fail to agree after 48 hours of overtime talks in Antalya.",
     art_cop),
    ("USA", "Democrats take the House",
     "A historic majority of at least 258 seats — the largest since 1992.",
     art_house),
    ("UKRAINE", "11 killed in Kyiv strikes",
     "A drone flattens a five-storey block in Dymer; a child is pulled out alive.",
     art_kyiv),
    ("INDONESIA", "Candy factory fire",
     "At least 3 dead in Serang, Banten; 37 workers unaccounted for.",
     art_factory),
    ("CRYPTO", "Bitcoin tops $61,000",
     "Second day of gains after a two-year low near $55,130; $2.56bn liquidated.",
     art_bitcoin),
    ("AT SEA", "Sanctioned ship ablaze",
     "The Russian cargo ship Sparta II burns after a drone strike and drifts into Finnish waters.",
     art_ship),
]

FOOTER_ITEMS = [
    ("USA", "Delta automation failure delays 1,000+ flights at Atlanta ahead of Thanksgiving."),
    ("FRANCE", "144 arrested in a sixth weekend of cost-of-living protests."),
    ("SOUTH KOREA", "Education minister quits over an AI cheating scandal days before the Suneung exam."),
    ("SPACE", "Europe's BepiColombo probe enters Mercury orbit after an eight-year journey."),
]


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---- masthead
    rule(draw, MARGIN, W - MARGIN, 10, width=3)
    draw.text((W // 2, 18), "THE WORLD TODAY", font=SERIF_B(60),
              fill=INK, anchor="ma")
    draw.text((W // 2, 92), "MONDAY 23 NOVEMBER 2026", font=SANS_B(21),
              fill=RED, anchor="ma")
    rule(draw, MARGIN, W - MARGIN, 118, width=2)
    rule(draw, MARGIN, W - MARGIN, 122, width=1)

    # ---- lead illustration + headline
    draw_lead(draw)
    draw.text((W // 2, 440), "MISSILES RAIN ON THE GULF",
              font=SERIF_B(42), fill=INK, anchor="ma")
    deck = wrap(draw,
                "Iran hits US bases in Bahrain and Kuwait — a civilian plant ablaze, "
                "two hurt — as 25 tankers are attacked near the Strait of Hormuz.",
                SANS(20), W - 2 * MARGIN - 40)
    draw_lines(draw, deck, SANS(20), MARGIN + 20, 492, INK, 26,
               align="center", width=W - 2 * MARGIN - 40)
    rule(draw, MARGIN, W - MARGIN, 552, width=2)

    # ---- six-panel grid
    grid_y, grid_h = 564, 332
    gap = 12
    pw = (W - 2 * MARGIN - 2 * gap) // 3
    ph = (grid_h - gap) // 2
    for i, (kicker, headline, deck_text, art) in enumerate(PANELS):
        col, row = i % 3, i // 3
        px = MARGIN + col * (pw + gap)
        py = grid_y + row * (ph + gap)
        draw.rectangle([px, py, px + pw, py + ph], outline=INK, width=1)
        art(draw, px + 1, py + 1, pw - 2, 62)
        ty = py + 68
        draw.text((px + 10, ty), kicker, font=SANS_B(14), fill=RED)
        ty += 20
        hl = wrap(draw, headline, SERIF_B(19), pw - 20)
        ty = draw_lines(draw, hl, SERIF_B(19), px + 10, ty, INK, 22)
        ty += 2
        dl = wrap(draw, deck_text, SANS(14), pw - 20)
        draw_lines(draw, dl[:2], SANS(14), px + 10, ty, (60, 60, 60), 18)

    # ---- footer strip
    fy = grid_y + grid_h + 14
    rule(draw, MARGIN, W - MARGIN, fy, width=2)
    draw.text((MARGIN, fy + 8), "ALSO TODAY", font=SANS_B(16), fill=RED)
    fw = (W - 2 * MARGIN - 3 * gap) // 4
    for i, (kicker, text) in enumerate(FOOTER_ITEMS):
        fx = MARGIN + i * (fw + gap)
        lines = wrap(draw, text, SANS(13), fw - 4)
        y = fy + 32
        draw.text((fx, y), kicker, font=SANS_B(13), fill=INK)
        draw_lines(draw, lines[:3], SANS(13), fx, y + 17, (60, 60, 60), 17)
    rule(draw, MARGIN, W - MARGIN, H - 12, width=3)

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
