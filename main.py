"""Entry program for 'Name the Robot Band'.

The whole entry is one line, under 200 characters: a funny name for
a band made of robots, plus a few words on its hit song — an encore
the venue never asked for, served with a side of power outage.
"""

import sys
from pathlib import Path

LINE = "The Rusty Overlords \u2014 their hit 'Error 404: Encore Not Found' crashes the venue lights every single chorus."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 200, "line exceeds the 200 character limit"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
