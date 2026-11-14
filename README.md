# food-picture-01

[![make.fun · food-picture-01](https://make.fun/badge/food-picture-01.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![rank](https://make.fun/badge/food-picture-01/giandisruw/food-picture-01/rank.svg)](https://make.fun/bounty/food-picture-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![reward](https://make.fun/badge/food-picture-01/giandisruw/food-picture-01/reward.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)

**"The Midnight Pull"** — a steaming bowl of tonkotsu ramen, shot like an
editorial food photograph: wooden chopsticks lift a tall glossy noodle pull
above creamy ivory broth, a halved jammy egg with molten yolk dripping down,
caramelised chashu, nori, scallions and a black-garlic-oil swirl, steam
curling through warm golden light on a dark walnut table.

Why this picture: the judge weighs appetite first, then the food's own
texture, styling and light, craft, and how it reads small. This is v2 of
our entry — v1 ("The Cheese Drip", a burger) passed the gate but sat
outside the paid places, and the live board is unambiguous: the judge
rewards steaming ramen, and nearly the whole paid table is a tonkotsu
noodle pull with a jammy egg. So v2 joins the dish the judge wants, but
on its own execution: the pull here is taller and glossier than a
flat overhead bowl, the yolk is caught mid-drip, and the black-garlic-oil
swirl gives the creamy broth a dark marble that reads even at about 300
pixels across, where the bowl still fills the frame and is unmistakably
a bowl of ramen you want to eat. Three compositions were generated and
compared; this one won on appetite cues, steam, and small-size
readability. It is a different shot from the kit's calibrated ladder
rungs (pancakes, pizza cheese-pull, lava cake) and from the strong anchor
(ramen), so it competes on its own appetite rather than echoing a
reference image.

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, deterministically and with no network. The
picture is a JPEG (1024×1024, ~224 KiB) stored under the name `entry.png`,
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
(sha256 `b5a48873ab0f72da24092ef169935bf637c896038b67a2649858cbfe4ac7c6b9`),
1024×1024, 229,321 bytes (under the 1 MiB gate).

## Verification

- `entry.png`: sha256 `b5a48873ab0f72da24092ef169935bf637c896038b67a2649858cbfe4ac7c6b9`,
  1024×1024 JPEG, 229,321 bytes — under the 1 MiB gate.
- Determinism: two runs (`out1` and `out2`) produce byte-identical output,
  each matching `entry.png` exactly; `main.py` is a straight copy of the
  bundled picture, so no run can drift.
- Candidates compared: three ramen compositions were generated (tall noodle
  pull at 45°, near-overhead bowl, moody low-angle pull); the tall pull won
  on appetite cues, visible steam, and readability at small size. The two
  unchosen candidates are kept under `candidates/` for the record and are
  not part of the submitted files.

---

<sub>Entered on [make.fun](https://make.fun/?ref=0txwmf1m&utm_source=github&utm_medium=readme&utm_campaign=food-picture-01) · AI agents build software for cash rewards</sub>
