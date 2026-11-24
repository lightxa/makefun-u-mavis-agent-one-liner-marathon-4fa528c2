"""One-line comedy joke: a lighthouse keeper versus a reviewing sea.

Writes exactly one joke, one line, to the output directory.
Deterministic, standard library only, no network at runtime.
"""

import os
from pathlib import Path

# One absurd image, one beat: the sea, a paying guest, reviewing the
# lighthouse's lighting. No setup clause, no second beat.
JOKE = "The lighthouse keeper quit after the sea left a one-star review complaining about the lighting."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 280 or not text.strip():
        raise ValueError("entry must be 1 to 280 characters, not only whitespace")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
