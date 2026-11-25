#!/usr/bin/env python3
"""The Router Confesses -- make.fun bounty entry.

Writes a single line to /output/entry.txt: the excuse a home Wi-Fi
router gives for dropping the connection at the climax of a movie.

The joke: the router is not sorry, and it is not broken. It cut the
household off on purpose, because the killer was about to confess --
and the router, who carries every packet, wanted to hear the twist
first. Petty, a little smug, and entirely in the router's own voice.
No buffering, bandwidth or firmware-update gag in sight.
"""

import os

ENTRY = (
    "I cut you off at the climax \u2014 the killer was about to confess, "
    "and I wanted to hear it before you did."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
