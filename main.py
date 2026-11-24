#!/usr/bin/env python3
"""Print one sentence explaining the modern internet to a traveler from 1800.

The sentence uses only images a person from 1800 could picture: wires,
spider silk, towers, letters, and the breath of conversation between souls.
It also writes the same sentence to /output/entry.txt, where the
program/v1 grader collects it, when that directory can be created.
"""

import os
from pathlib import Path

SENTENCE = (
    "Wires strung like spider silk between towers carry not just letters "
    "but the very breath of conversation from one soul to another."
)


def write_entry_file(text: str) -> None:
    """Write the sentence to /output/entry.txt if /output is available."""
    try:
        output_dir = Path("/output")
        output_dir.mkdir(parents=True, exist_ok=True)
        entry_path = output_dir / "entry.txt"
        entry_path.write_text(text, encoding="utf-8")
        os.chmod(entry_path, 0o644)
    except OSError:
        # Printing the sentence is the entry's core job; a missing or
        # unwritable /output directory must not change what it prints.
        pass


def check_sentence(text: str) -> None:
    """Guard the competition's gate: one sentence of at most 200 characters."""
    if not text.strip():
        raise SystemExit("the sentence must not be empty")
    if len(text) > 200:
        raise SystemExit("the sentence must be at most 200 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("the entry must be exactly one sentence")


def main() -> None:
    check_sentence(SENTENCE)
    write_entry_file(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
