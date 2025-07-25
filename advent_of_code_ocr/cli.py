"""Command line interface for the Advent of Code OCR library."""

import argparse
import sys

from .height_6 import convert_6


def parse_args(args: list[str]) -> argparse.Namespace:
    """Parse command line arguments.

    Args:
        args: List of command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_text',
        help='Input text',
        nargs='?',
        default=sys.stdin,
    )
    parser.add_argument('-f', '--fill-pixel', help='Fill pixel character', default='#')
    parser.add_argument(
        '-e', '--empty-pixel', help='Empty pixel character', default='.'
    )
    return parser.parse_args(args)


def main(sys_args: list[str]) -> str:
    """Convert Advent of Code ASCII art to characters from the command line.

    Args:
        sys_args: List of raw command line arguments.

    Returns:
        str: The converted characters.
    """
    args = parse_args(sys_args)
    if args.input_text is sys.stdin:
        args.input_text = args.input_text.read()
    return convert_6(**vars(args))
