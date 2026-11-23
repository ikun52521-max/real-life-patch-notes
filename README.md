# Real-Life Patch Notes

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/ikun52521-max/real-life-patch-notes/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/ikun52521-max/real-life-patch-notes/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

An entry for the [make.fun](https://make.fun/?ref=hyfder3x) bounty
**Real-Life Patch Notes: The Comedy Changelog** — write the funniest
one-line patch note for a bug in real life or human biology, 160
characters max, in the terse register of a real release note.

The program writes a single original patch-note line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`):

> v2.7.1: fixed a bug where the bladder only reported low battery after the user had already left the house.

## Run it

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` is written;
otherwise it writes to `/output/entry.txt`. Python 3 only, standard
library only, no network. The output is deterministic: every run
writes the same 106-character line, byte for byte.

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty — https://make.fun/?ref=hyfder3x
