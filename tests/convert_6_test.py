"""Test cases for converting height 6 characters."""

from re import escape

import numpy as np
import pytest

from advent_of_code_ocr.characters import ALPHABET_6
from advent_of_code_ocr.exceptions import IncorrectRowCountError
from advent_of_code_ocr.height_6 import convert_6, convert_array_6


@pytest.mark.parametrize(('test_input', 'expected'), ALPHABET_6.items())
def test_single_letter(test_input: str, expected: str) -> None:
    """Test conversion of a single letter."""
    assert convert_6(test_input) == expected


def test_three_letters() -> None:
    """Test conversion of three letters."""
    assert (
        convert_6(
            '.##..###...##.\n#..#.#..#.#..#\n#..#.###..#...\n####.#..#.#...\n'
            '#..#.#..#.#..#\n#..#.###...##.'
        )
        == 'ABC'
    )


@pytest.mark.parametrize(
    ('test_input', 'fill_char', 'empty_char'),
    [
        (
            'abbaabbbaaabba\nbaababaababaab\nbaababbbaabaaa\nbbbbabaababaaa\nbaababaababaab\nbaababbbaaabba',
            'b',
            'a',
        ),
        (
            '!@@!!@@@!!!@@!\n@!!@!@!!@!@!!@\n@!!@!@@@!!@!!!\n@@@@!@!!@!@!!!\n@!!@!@!!@!@!!@\n@!!@!@@@!!!@@!',
            '@',
            '!',
        ),
    ],
)
def test_different_characters(test_input: str, fill_char: str, empty_char: str) -> None:
    """Test conversion with different fill and empty characters."""
    assert convert_6(test_input, fill_pixel=fill_char, empty_pixel=empty_char) == 'ABC'


def test_long_string() -> None:
    """Test conversion of a long string with multiple characters."""
    # Split into list of lines for readability/formatting
    string = '\n'.join([  # noqa: FLY002
        '.##..###...##..####.####..##..#..#..###...##.#..#.#.....##..###..###...###.#..#.#...#####',
        '#..#.#..#.#..#.#....#....#..#.#..#...#.....#.#.#..#....#..#.#..#.#..#.#....#..#.#...#...#',
        '#..#.###..#....###..###..#....####...#.....#.##...#....#..#.#..#.#..#.#....#..#..#.#...#.',
        '####.#..#.#....#....#....#.##.#..#...#.....#.#.#..#....#..#.###..###...##..#..#...#...#..',
        '#..#.#..#.#..#.#....#....#..#.#..#...#..#..#.#.#..#....#..#.#....#.#.....#.#..#...#..#...',
        '#..#.###...##..####.#.....###.#..#..###..##..#..#.####..##..#....#..#.###...##....#..####',
    ])
    assert convert_6(string) == 'ABCEFGHIJKLOPRSUYZ'


@pytest.mark.parametrize('rows', [1, 5, 7, 10])
def test_number_of_rows(rows: int) -> None:
    """Test conversion with incorrect number of rows."""
    with pytest.raises(
        IncorrectRowCountError,
        match=escape(f'Incorrect number of rows (expected 6), got {rows}'),
    ):
        convert_6('\n'.join('' for _ in range(rows)))


def test_strange_width_characters() -> None:
    """Test conversion with characters that have unusual widths."""
    # Split into list of lines for readability/formatting
    string = '\n'.join([  # noqa: FLY002
        '####.####.####.#...##..#.####.###..####..###...##.',
        '#....#....#....#...##.#..#....#..#.#......#.....#.',
        '###..###..###...#.#.##...###..#..#.###....#.....#.',
        '#....#....#......#..#.#..#....###..#......#.....#.',
        '#....#....#......#..#.#..#....#.#..#......#..#..#.',
        '####.#....####...#..#..#.#....#..#.#.....###..##..',
    ])
    assert convert_6(string) == 'EFEYKFRFIJ'


def test_array_nested_list() -> None:
    """Test conversion of a nested list representing a 6-row character array."""
    array = [
        ['X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'X'],
    ]
    assert convert_array_6(array, fill_pixel='O', empty_pixel='X') == 'AC'


def test_array_list_of_strings() -> None:
    """Test conversion of a list of strings representing a 6-row character array."""
    array = [
        '.oo...oo..oooo..ooo.o..o..ooo..oo..o..o',
        'o..o.o..o.o....o....o..o...o..o..o.o..o',
        'o..o.o....ooo..o....oooo...o..o....oooo',
        'oooo.o....o.....oo..o..o...o..o.oo.o..o',
        'o..o.o..o.o.......o.o..o...o..o..o.o..o',
        'o..o..oo..oooo.ooo..o..o..ooo..ooo.o..o',
    ]
    assert convert_array_6(array, fill_pixel='o') == 'ACESHIGH'


def test_array_numpy() -> None:
    """Test conversion of a NumPy array representing a 6-row character array."""
    array = np.array([
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    ])
    assert convert_array_6(array, fill_pixel=1, empty_pixel=0) == 'AOC'


@pytest.mark.parametrize('rows', [1, 5, 7, 10])
def test_array_number_of_rows(rows: int) -> None:
    """Test conversion of an array with an incorrect number of rows."""
    with pytest.raises(
        IncorrectRowCountError,
        match=escape(f'Incorrect number of rows (expected 6), got {rows}'),
    ):
        convert_array_6(['' for _ in range(rows)])
