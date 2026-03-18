"""Test cases for converting height 10 characters."""

from re import escape

import numpy as np
import pytest

from advent_of_code_ocr.characters import ALPHABET_10
from advent_of_code_ocr.exceptions import IncorrectRowCountError
from advent_of_code_ocr.height_10 import convert_10, convert_array_10


@pytest.mark.parametrize(('test_input', 'expected'), ALPHABET_10.items())
def test_single_letter(test_input: str, expected: str) -> None:
    """Test conversion of a single letter."""
    assert convert_10(test_input) == expected


def test_three_letters() -> None:
    """Test conversion of three letters."""
    assert (
        convert_10(
            '..##....#####....####.\n.#..#...#....#..#....#\n#....#..#....#..#.....\n'
            '#....#..#....#..#.....\n#....#..#####...#.....\n######..#....#..#.....\n'
            '#....#..#....#..#.....\n#....#..#....#..#.....\n#....#..#....#..#....#\n'
            '#....#..#####....####.'
        )
        == 'ABC'
    )


@pytest.mark.parametrize(
    ('test_input', 'fill_char', 'empty_char'),
    [
        (
            'aabbaaaabbbbbaaaabbbba\nabaabaaabaaaabaabaaaab\nbaaaabaabaaaabaabaaaaa\n'
            'baaaabaabaaaabaabaaaaa\nbaaaabaabbbbbaaabaaaaa\nbbbbbbaabaaaabaabaaaaa\n'
            'baaaabaabaaaabaabaaaaa\nbaaaabaabaaaabaabaaaaa\nbaaaabaabaaaabaabaaaab\n'
            'baaaabaabbbbbaaaabbbba',
            'b',
            'a',
        ),
        (
            '!!@@!!!!@@@@@!!!!@@@@!\n!@!!@!!!@!!!!@!!@!!!!@\n@!!!!@!!@!!!!@!!@!!!!!\n'
            '@!!!!@!!@!!!!@!!@!!!!!\n@!!!!@!!@@@@@!!!@!!!!!\n@@@@@@!!@!!!!@!!@!!!!!\n'
            '@!!!!@!!@!!!!@!!@!!!!!\n@!!!!@!!@!!!!@!!@!!!!!\n@!!!!@!!@!!!!@!!@!!!!@\n'
            '@!!!!@!!@@@@@!!!!@@@@!',
            '@',
            '!',
        ),
    ],
)
def test_different_characters(test_input: str, fill_char: str, empty_char: str) -> None:
    """Test conversion with different fill and empty characters."""
    assert convert_10(test_input, fill_pixel=fill_char, empty_pixel=empty_char) == 'ABC'


def test_long_string() -> None:
    """Test conversion of a long string with multiple characters."""
    # Split into list of lines for readability/formatting
    string = '\n'.join([  # noqa: FLY002
        '..##....#####....####...######..######...####...#....#.....###..#....#..#.......#....#..#####...#####...#....#..######',
        '.#..#...#....#..#....#..#.......#.......#....#..#....#......#...#...#...#.......##...#..#....#..#....#..#....#.......#',
        '#....#..#....#..#.......#.......#.......#.......#....#......#...#..#....#.......##...#..#....#..#....#...#..#........#',
        '#....#..#....#..#.......#.......#.......#.......#....#......#...#.#.....#.......#.#..#..#....#..#....#...#..#.......#.',
        '#....#..#####...#.......#####...#####...#.......######......#...##......#.......#.#..#..#####...#####.....##.......#..',
        '######..#....#..#.......#.......#.......#..###..#....#......#...##......#.......#..#.#..#.......#..#......##......#...',
        '#....#..#....#..#.......#.......#.......#....#..#....#......#...#.#.....#.......#..#.#..#.......#...#....#..#....#....',
        '#....#..#....#..#.......#.......#.......#....#..#....#..#...#...#..#....#.......#...##..#.......#...#....#..#...#.....',
        '#....#..#....#..#....#..#.......#.......#...##..#....#..#...#...#...#...#.......#...##..#.......#....#..#....#..#.....',
        '#....#..#####....####...######..#........###.#..#....#...###....#....#..######..#....#..#.......#....#..#....#..######',
    ])
    assert convert_10(string) == 'ABCEFGHJKLNPRXZ'


@pytest.mark.parametrize('rows', [1, 5, 7, 9, 11])
def test_number_of_rows(rows: int) -> None:
    """Test conversion with incorrect number of rows."""
    with pytest.raises(
        IncorrectRowCountError,
        match=escape(f'Incorrect number of rows (expected 10), got {rows}'),
    ):
        convert_10('\n'.join('' for _ in range(rows)))


def test_array_nested_list() -> None:
    """Test conversion of a nested list representing a 10-row character array."""
    array = [
        ['X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X'],
    ]
    assert convert_array_10(array, fill_pixel='O', empty_pixel='X') == 'AC'


def test_array_list_of_strings() -> None:
    """Test conversion of a list of strings representing a 10-row character array."""
    array = [
        '..oo.....oooo.',
        '.o..o...o....o',
        'o....o..o.....',
        'o....o..o.....',
        'o....o..o.....',
        'oooooo..o.....',
        'o....o..o.....',
        'o....o..o.....',
        'o....o..o....o',
        'o....o...oooo.',
    ]
    assert convert_array_10(array, fill_pixel='o') == 'AC'


def test_array_numpy() -> None:
    """Test conversion of a NumPy array representing a 10-row character array."""
    array = np.array([
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    ])
    assert convert_array_10(array, fill_pixel=1, empty_pixel=0) == 'APC'  # type: ignore[arg-type]


@pytest.mark.parametrize('rows', [1, 5, 7, 9, 11])
def test_array_number_of_rows(rows: int) -> None:
    """Test conversion of an array with an incorrect number of rows."""
    with pytest.raises(
        IncorrectRowCountError,
        match=escape(f'Incorrect number of rows (expected 10), got {rows}'),
    ):
        convert_array_10(['' for _ in range(rows)])
