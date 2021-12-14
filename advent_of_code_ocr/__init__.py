"""Convert Advent of Code ASCII art"""

from .characters import ALPHABET_6

__version__ = "1.0.0"


def convert_6(
    input_text: str, *, fill_pixel: str = "#", empty_pixel: str = "."
) -> str:
    """Convert height 6 characters"""
    input_text = input_text.replace(fill_pixel, "#").replace(empty_pixel, ".")
    array = input_text.split("\n")

    # Validate input
    rows, cols = len(array), len(array[0])
    if any(len(row) != cols for row in array):
        raise ValueError("all rows should have the same number of columns")
    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")

    # Convert each letter
    indices = [slice(start, start + 4) for start in range(0, cols, 5)]
    result = [
        ALPHABET_6["\n".join(row[index] for row in array)] for index in indices
    ]

    return "".join(result)
