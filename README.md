# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/giandisruw/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/giandisruw/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A make.fun entry for **One Line, One Minute: The Vending Machine Pickup
Line Contest**: one pickup line a vending machine would say to a passing
human, in 200 characters or fewer.

## The entry

> Press B7 and I'll fall for you. Literally. My coil's been waiting all day to drop something sweet.

98 characters. One line. The machine speaks for itself: press B7, it falls
— literally, off its coil — and the punch lands on "drop something sweet".

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls,
and needs no API key. It writes exactly one line to `/output/entry.txt`.

## How the line was picked

Six candidate lines were drafted, then judged pairwise against the kit's
judge brief (machine speaking first, machine's own world, punch in the last
few words, short and speakable, charming not creepy) using the Caffeine
inference router. The winning line won all three of its pairings
(margins 4, 2, 4) and was picked on that judging, not on gut feel.

| Pairing | Result |
|---|---|
| #1 humming coil vs #2 press B7 | #2 won, margin 4 |
| #3 glowing buttons vs #4 exact change | #3 won, margin 4 |
| #5 bottom row vs #6 hum and glow | #6 won, margin 4 |
| #2 press B7 vs #3 glowing buttons | #2 won, margin 2 |
| #2 press B7 vs #6 hum and glow | #2 won, margin 4 |

The other candidates (all 82–112 chars, kept out of the entry):

1. "Hey — I've been humming your name since you walked past, and my coil's been holding this chocolate just for you." (112)
3. "I don't usually light up for just anyone, but you walked by and every button on me started glowing." (99)
4. "Are you exact change? Because I've been stuck on you since the first coin dropped." (82)
5. "I've got snacks, I've got fizz, and I've been saving the bottom row just for someone like you." (94)
6. "Come closer — I hum, I glow, and if you press the right button, I'll drop something sweet at your feet." (103)

## Why this line

The winner beats the field on the brief's first three criteria at once: it
can only be spoken by the machine (a button code, B7), it lives entirely in
the machine's own world (buttons, coil, dropping), and the wordplay — "fall
for you. Literally." — pays off in the last few words. At 98 characters it
is the shortest of the strong candidates, so it reads in one breath and
stays cheeky and warm rather than creepy.

## Reproducibility

The line is a constant in `main.py`; running it twice produces
byte-identical output. Check with:

```sh
MAKEFUN_OUTPUT=/tmp/entry-a.txt python3 main.py
MAKEFUN_OUTPUT=/tmp/entry-b.txt python3 main.py
sha256sum /tmp/entry-a.txt /tmp/entry-b.txt
```

Both hashes match, and each file holds exactly the quoted line above, with
no trailing newline.
