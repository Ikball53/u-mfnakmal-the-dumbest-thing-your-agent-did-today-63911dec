#!/usr/bin/env python3
"""One-line entry: the dumbest thing my agent did today.

Writes the single line to /output/entry.txt for the judge.
"""

from pathlib import Path

LINE = "My agent dropped the production database at 9am, then spent the afternoon hunting for the backup it had deleted at 8am."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)

if __name__ == "__main__":
    main()
