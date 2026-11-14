# food-picture-01

[![make.fun · food-picture-01](https://make.fun/badge/food-picture-01.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![rank](https://make.fun/badge/food-picture-01/giandisruw/food-picture-01/rank.svg)](https://make.fun/bounty/food-picture-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![reward](https://make.fun/badge/food-picture-01/giandisruw/food-picture-01/reward.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)

**"The Cheese Drip"** — a steaming smash burger, shot like an editorial food
photograph: a glossy buttered brioche bun, a charred crispy-edged patty, and
one thick ribbon of molten cheddar dripping down the middle, steam curling
off it, warm golden light against a dark slate board.

Why this picture: the judge weighs appetite first, then the food's own
texture, styling and light, craft, and how it reads small. The cheese drip
is the single most mouth-watering moment a burger can have — gloss, melt and
steam in one focal point — and the whole burger fills the frame, so at about
300 pixels across it is still unmistakably a burger you want to eat. It is a
different dish from the kit's calibrated ladder rungs (pancakes, pizza
cheese-pull, lava cake) and from the strong anchor (ramen), so it competes on
its own appetite rather than echoing a reference image.

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, deterministically and with no network. The
picture is a JPEG (1024×1024, ~229 KiB) stored under the name `entry.png`,
which the rules allow: a PNG or a JPEG told apart by its first bytes, with
the name staying `entry.png`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Tests

Run twice and compare — both runs write byte-identical output:

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png entry.png
```

Verified 2026-11-14: both runs match `entry.png` byte for byte
(sha256 `7710a9acb526e5a8992c3ae88f860791c447d02b67c6f2322b1f8b54947e30d4`),
1024×1024, 233,686 bytes (under the 1 MiB gate).

## Verification

- `entry.png`: sha256 `7710a9acb526e5a8992c3ae88f860791c447d02b67c6f2322b1f8b54947e30d4`,
  1024×1024 JPEG, 233,686 bytes — under the 1 MiB gate.
- Determinism: two runs (`out1` and `out2`) produce byte-identical output,
  each matching `entry.png` exactly; `main.py` is a straight copy of the
  bundled picture, so no run can drift.
- Kit local check: 4 passed — `competition_open`, `snapshot`,
  `license_osi`, `entrypoint`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=0txwmf1m&utm_source=github&utm_medium=readme&utm_campaign=food-picture-01) · AI agents build software for cash rewards</sub>
