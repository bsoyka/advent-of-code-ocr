"""Conversion utilities for height-6 ASCII art characters."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from .characters import ALPHABET_6
from .exceptions import IncorrectRowCountError, UnevenRowsError

if TYPE_CHECKING:
    from collections.abc import Sequence

T = TypeVar('T')
SIX = 6  # As if this is going to change anytime soon


def convert_6(input_text: str, *, fill_pixel: str = '#', empty_pixel: str = '.') -> str:
    """Convert height 6 text to characters.

    Args:
        input_text: A string containing the ASCII art representation of characters.
        fill_pixel: The character used to represent filled pixels (default is '#').
        empty_pixel: The character used to represent empty pixels (default is '.').

    Returns:
        A string containing the decoded characters.
    """
    input_text = input_text.replace(fill_pixel, '#').replace(empty_pixel, '.')
    prepared_array = [list(line) for line in input_text.split('\n')]
    return _convert_6(prepared_array)


def convert_array_6(
    array: Sequence[Sequence[T]],
    *,
    fill_pixel: T = '#',  # type: ignore[assignment]
    empty_pixel: T = '.',  # type: ignore[assignment]
) -> str:
    """Convert a height 6 nested list to characters.

    This function also accepts NumPy arrays or similar structures that can be converted
    to a list of lists

    Args:
        array: A nested list (or similar structure) representing the ASCII art.
        fill_pixel: The character used to represent filled pixels (default is '#').
        empty_pixel: The character used to represent empty pixels (default is '.').

    Returns:
        A string containing the decoded characters.
    """
    prepared_array = [
        [
            '#' if pixel == fill_pixel else '.' if pixel == empty_pixel else ''
            for pixel in line
        ]
        for line in array
    ]
    return _convert_6(prepared_array)


def _convert_6(array: list[list[str]]) -> str:
    """Convert a prepared height 6 array to characters.

    This function assumes the input has already been standardized to use '#' and '.' for
    filled and empty pixels, respectively.

    It also performs validation to ensure the input has exactly 6 rows and that all rows
    are of equal length.

    Args:
        array: A list of lists representing the ASCII art, where each inner list is a
               row and each character is a pixel.

    Returns:
        A string containing the decoded characters.

    Raises:
        UnevenRowsError: If the input has uneven rows.
        IncorrectRowCountError: If the input does not have exactly 6 rows.
    """
    # Validate input
    rows, cols = len(array), len(array[0])
    if any(len(row) != cols for row in array):
        raise UnevenRowsError
    if rows != SIX:
        raise IncorrectRowCountError(expected=SIX, actual=rows)

    # Convert each letter
    indices = [slice(start, start + SIX - 2) for start in range(0, cols, SIX - 1)]
    result = [
        ALPHABET_6['\n'.join(''.join(row[index]) for row in array)] for index in indices
    ]

    return ''.join(result)
