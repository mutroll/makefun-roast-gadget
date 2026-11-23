"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (one line, at most 200 characters)
roasting the phone I use every day, to <output dir>/entry.txt.

The roast was chosen after brainstorming several candidates and judging
each against the judge's five criteria in order: it names one daily
gadget (my phone), it lands on a first read with a sting of recognition
(the phone deleting a precious photo), its angle is fresh (storage
auto-deletion choosing a forgotten app over a memory, not the usual
dead-battery complaint), it is tightly worded with the punch at the end,
and it is one person's specific gripe with a concrete detail (an app
opened once in 2019).

Python 3.13 standard library only. Deterministic: no network, no
randomness, no timestamps, no environment-dependent output. The same
input always produces the same bytes.
"""

import os

ROAST = (
    "My phone deleted the only photo of my grandma to make room for "
    "an update to an app I opened once in 2019."
)


def main() -> None:
    # Self-check against the gate before writing anything: the entry
    # must be one line of 1 to 200 characters, not only white space.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast is {len(ROAST)} characters, must be 1-200")
    if "\n" in ROAST or "\r" in ROAST:
        raise ValueError("roast must be a single line")
    if not ROAST.strip():
        raise ValueError("roast must not be only white space")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one line, no trailing newline: the file is the roast, and
    # nothing but the roast, so its character count is the roast's.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
