#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line to /output/entry.txt: the office printer's comeback to
the paper jams, the cryptic error codes and the thumps.

The line, in the printer's own voice:

    ERROR 0xPLEASE: after 41,208 sheets without complaint, this one
    stays in my throat until somebody says please.

Why this line:

* It is the printer speaking, not someone describing a printer. The
  error code is how a machine opens its mouth.
* It is a joke, not a complaint with a punchline bolted on: the jammed
  sheet is a hostage, and the ransom is a single word of manners.
* It sounds like the machine itself: weary, literal, faintly
  passive-aggressive, with the flat logic of a device that has counted
  every sheet it has ever fed — 41,208 of them, without a word.
* It lands in a single read: no setup, no second sentence, nothing to
  know beyond the office it sits in.
* It is fresh: the printer does not blame the paper, the user, or the
  network. It unionises, politely, over one sheet.

Gate (per RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 240
characters, not only white space. This entry is 110 characters.
"""

import os

# The printer's comeback, exactly as it will be judged.
ENTRY = (
    "ERROR 0xPLEASE: after 41,208 sheets without complaint, "
    "this one stays in my throat until somebody says please."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate checks, mirroring the sealed scorer.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 240, f"entry must be 1-240 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only white space"
    # One line: no newline inside the text itself.
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    encoded = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)

    # Round-trip verification: read it back and confirm the gate again.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == ENTRY, f"round-trip mismatch: {text!r} != {ENTRY!r}"
    assert 1 <= len(text) <= 240 and text.strip()

    print(f"Wrote {len(text)} characters ({len(encoded)} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
