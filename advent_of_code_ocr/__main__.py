"""Main entry point for the Advent of Code OCR package."""

import sys

from .cli import main

if __name__ == '__main__':
    print(main(sys.argv[1:]))  # noqa: T201 (allow print)
