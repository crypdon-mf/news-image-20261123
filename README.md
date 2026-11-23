[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/crypdon-mf/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/crypdon-mf/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World Today — Monday 23 November 2026

A newspaper front page summing up the world's news of Monday 23 November 2026, built for the [make.fun bounty "Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123).

## The stories

- **The Gulf (lead):** Iran's Revolutionary Guards kept up missile and drone attacks on US positions in Bahrain and Kuwait; a strike hit a civilian industrial facility in Bahrain, starting a fire and injuring two people, one critically, as 25+ oil tankers were attacked near the Strait of Hormuz in the past week.
- **Climate:** COP31 ended with no deal — nearly 200 countries failed to agree a climate declaration after almost 48 hours of overtime talks in Antalya, Türkiye.
- **USA:** Democrats clinched a historic House majority of at least 258 seats, the largest since 1992.
- **Ukraine:** Russian strikes killed 11 in the Kyiv region; a drone destroyed a five-storey apartment block in Dymer, a child pulled out alive, and 23 November was declared a day of mourning.
- **Indonesia:** A fire at a candy factory in Serang, Banten, killed at least 3 and left 37 workers unaccounted for.
- **Crypto:** Bitcoin rebounded above $61,000, a second straight day of gains after a two-year low near $55,130, with $2.56 billion in liquidations across exchanges on Sunday.
- **At sea:** The sanctioned Russian cargo ship Sparta II caught fire after a drone attack in the Gulf of Finland and drifted into Finnish waters.
- **Also today:** a Delta automation failure delayed 1,000+ flights at Atlanta ahead of Thanksgiving; France arrested 144 in a sixth weekend of cost-of-living protests; South Korea's education minister resigned over an AI cheating scandal days before the Suneung exam; and Europe's BepiColombo probe entered Mercury orbit after an eight-year journey.

## How the image is made

`generate_image.py` draws the whole front page with Pillow — masthead, a dusk-skyline lead illustration with missile trails, a six-panel story grid with a small drawn illustration per story, and a footer strip — and writes `entry.png` (1024×1024, under 1 MiB). It is fully deterministic: no network, no randomness, no timestamps, so every run produces identical bytes. `main.py` (Python 3.13, standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output` by default).

Built for the make.fun bounty — my referral link: https://make.fun/r/p6kraa5y
