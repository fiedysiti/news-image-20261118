# news-image-20261118 — The World's News of 18 November 2026, in One Image

Entry for the [make.fun bounty `news-image-20261118`](https://make.fun/bounty/news-image-20261118)
($250 shared by the 50 best-ranked entries).

## The image

`entry.png` is a 1024×1024 newspaper front page — **THE WORLD TODAY**,
dated **Wednesday, 18 November 2026** — summing up the day's world news so
far in real rendered text (PIL + DejaVu fonts; no AI-generated imagery):

1. **APEC summit (lead)** — APEC opens in Shenzhen; Xi Jinping urges AI
   cooperation and free trade; the first-ever Trump–Xi–Putin summit follows
   on Thursday.
2. **Gulf** — Iran drones target Bahrain and Kuwait after the U.S. strike on
   a missile site on Qeshm Island.
3. **Ukraine** — Crimea Bridge partially collapses under a second-day
   attack; European markets slide.
4. **U.S. politics** — Democrats flip the Alaska Senate seat (Mary Peltola
   beats Dan Sullivan); Democratic majority widens to 56 seats.
5. **Health** — U.S. loses measles-free status after 26 years (5,400+
   cases in 2026).
6. **Health** — Ebola in DR Congo more than doubles: 11,000+ cases,
   5,400 deaths, per the UN.
7. **In brief** — Category 5 Cyclone Xavier hits the Northern Cook Islands;
   Russian military plane crash in Siberia kills 19; S&P 500 −1.0%.

## The program

`main.py` (Python 3.13, standard library only) deterministically copies the
repository-held `entry.png` to `/output/entry.png`. No network access; two
runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Stories were taken from same-day news reporting (18 Nov 2026), including
One Turn world news, Horizon world news and markets, FeedCast Daily Brief,
Daily Baku, and Nexus Europa. See `BUILD-LOG.md` in the build workspace for
the full source list.

## License

MIT — see `LICENSE`.
