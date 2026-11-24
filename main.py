#!/usr/bin/env python3
"""Write one warm line about a small good thing to /output/entry.txt."""

from pathlib import Path

LINE = (
    "At dawn my neighbour left a lemon on my doorstep with a note: "
    "'for your tea \u2014 the tree has finally forgiven me.'"
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry line must be 1-200 characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
