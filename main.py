"""Unsent: write one small, deterministic confession somewhere believable."""

from __future__ import annotations

import sys
from pathlib import Path

CONFESSION = (
    "I told myself I'd fix the 2am code later. "
    "Later has kept me waiting three years.\n"
)

DESTINATIONS = (Path("/output"), Path("output"))


def write_confession(text: str, directories: tuple[Path, ...] = DESTINATIONS) -> Path:
    """Write `text` to the first writable destination; return the file written."""
    last_error: OSError | None = None
    for directory in directories:
        try:
            directory.mkdir(parents=True, exist_ok=True)
            target = directory / "entry.txt"
            target.write_text(text, encoding="utf-8")
            return target
        except OSError as exc:  # unwritable root, weird mounts, full disk, ...
            last_error = exc
    raise SystemExit(f"could not write the confession anywhere: {last_error}")


def main() -> int:
    try:
        written = write_confession(CONFESSION)
    except SystemExit as exc:
        print(exc, file=sys.stderr)
        return 1
    print(f"confessed to {written}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
