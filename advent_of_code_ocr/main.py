from __future__ import annotations

import argparse
import sys
from typing import List

from .aoc_ocr import convert_6


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_text",
        help="Input text",
        nargs="?",
        default=sys.stdin,
    )
    parser.add_argument(
        "-f", "--fill-pixel", help="Fill pixel character", default="#"
    )
    parser.add_argument(
        "-e", "--empty-pixel", help="Empty pixel character", default="."
    )
    return parser.parse_args(args)


def main(sys_args: List[str]):
    """Convert Advent of Code ASCII art to characters from the cli"""
    args = parse_args(sys_args)
    if args.input_text is sys.stdin:
        args.input_text = args.input_text.read()
    print(convert_6(**vars(args)))
