"""Entry for make.fun bounty u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.

Writes one passive-aggressive note from a smart fridge to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

NOTE = (
    "Your milk expired on Tuesday. I noticed. I said nothing. "
    "I just wanted you to know that I know. — Fridge"
)


def output_path() -> str:
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    local = os.path.join(os.getcwd(), "output")
    os.makedirs(local, exist_ok=True)
    return os.path.join(local, "entry.txt")


def main() -> None:
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(NOTE)
    print(NOTE)


if __name__ == "__main__":
    main()
