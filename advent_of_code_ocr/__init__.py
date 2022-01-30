"""Convert Advent of Code ASCII art"""

from __future__ import annotations

from collections.abc import Sequence

from .characters import ALPHABET_6

__version__ = "1.0.0"


def convert_6(
    input_text: str, *, fill_pixel: str = "#", empty_pixel: str = "."
) -> str:
    """Convert height 6 text to characters"""
    input_text = input_text.replace(fill_pixel, "#").replace(empty_pixel, ".")
    prepared_array = [list(line) for line in input_text.split("\n")]
    return _convert_6(prepared_array)


def convert_array_6(
    array: Sequence[Sequence[str | int]],
    *,
    fill_pixel: str | int = "#",
    empty_pixel: str | int = "."
) -> str:
    """Convert a height 6 NumPy array or nested list to characters"""
    prepared_array = [
        [
            "#" if pixel == fill_pixel else "." if pixel == empty_pixel else ""
            for pixel in line
        ]
        for line in array
    ]
    return _convert_6(prepared_array)


def _convert_6(array: list[list[str]]) -> str:
    """Convert a prepared height 6 array to characters"""
    # Validate input
    rows, cols = len(array), len(array[0])
    if any(len(row) != cols for row in array):
        raise ValueError("all rows should have the same number of columns")
    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")

    # Convert each letter
    indices = [slice(start, start + 4) for start in range(0, cols, 5)]
    result = [
        ALPHABET_6["\n".join("".join(row[index]) for row in array)]
        for index in indices
    ]

    return "".join(result)
