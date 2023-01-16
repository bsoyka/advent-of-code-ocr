from __future__ import annotations
import sys
import argparse
from .aoc_ocr import convert_6
from typing import List


def parse_args(args: List[str]) -> argparse.Namespace:
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
    args = parse_args(sys_args)
    if args.input_text is sys.stdin:
        args.input_text = args.input_text.read()
    # print(convert_6(**vars(args)))
    print(convert_6(**vars(args)))
