from re import escape

from pytest import mark, raises

from advent_of_code_ocr import convert_6, convert_array_6
from advent_of_code_ocr.characters import ALPHABET_6


@mark.parametrize("test_input,expected", ALPHABET_6.items())
def test_single_letter(test_input, expected):
    assert convert_6(test_input) == expected


@mark.parametrize(
    "test_input,expected",
    [
        (
            ".##..###...##.\n#..#.#..#.#..#\n#..#.###..#...\n####.#..#.#...\n#..#.#..#.#..#\n#..#.###...##.",
            "ABC",
        )
    ],
)
def test_three_letters(test_input, expected):
    assert convert_6(test_input) == expected


@mark.parametrize(
    "test_input,fill_char,empty_char",
    [
        (
            "abbaabbbaaabba\nbaababaababaab\nbaababbbaabaaa\nbbbbabaababaaa\nbaababaababaab\nbaababbbaaabba",
            "b",
            "a",
        ),
        (
            "!@@!!@@@!!!@@!\n@!!@!@!!@!@!!@\n@!!@!@@@!!@!!!\n@@@@!@!!@!@!!!\n@!!@!@!!@!@!!@\n@!!@!@@@!!!@@!",
            "@",
            "!",
        ),
    ],
)
def test_different_characters(test_input, fill_char, empty_char):
    assert (
        convert_6(test_input, fill_pixel=fill_char, empty_pixel=empty_char)
        == "ABC"
    )


def test_long_string():
    # Split into list of lines for readability/formatting
    string = "\n".join(
        [
            ".##..###...##..####.####..##..#..#..###...##.#..#.#.....##..###..###...###.#..#.#...#####",
            "#..#.#..#.#..#.#....#....#..#.#..#...#.....#.#.#..#....#..#.#..#.#..#.#....#..#.#...#...#",
            "#..#.###..#....###..###..#....####...#.....#.##...#....#..#.#..#.#..#.#....#..#..#.#...#.",
            "####.#..#.#....#....#....#.##.#..#...#.....#.#.#..#....#..#.###..###...##..#..#...#...#..",
            "#..#.#..#.#..#.#....#....#..#.#..#...#..#..#.#.#..#....#..#.#....#.#.....#.#..#...#..#...",
            "#..#.###...##..####.#.....###.#..#..###..##..#..#.####..##..#....#..#.###...##....#..####",
        ]
    )
    assert convert_6(string) == "ABCEFGHIJKLOPRSUYZ"


@mark.parametrize("rows", [0, 1, 5, 7, 10])
def test_number_of_rows(rows):
    with raises(
        ValueError, match=escape("incorrect number of rows (expected 6)")
    ):
        convert_6("\n".join("" for _ in range(rows)))


def test_strange_width_characters():
    # Split into list of lines for readability/formatting
    string = "\n".join(
        [
            "####.####.####.#...##..#.####.###..####..###...##.",
            "#....#....#....#...##.#..#....#..#.#......#.....#.",
            "###..###..###...#.#.##...###..#..#.###....#.....#.",
            "#....#....#......#..#.#..#....###..#......#.....#.",
            "#....#....#......#..#.#..#....#.#..#......#..#..#.",
            "####.#....####...#..#..#.#....#..#.#.....###..##..",
        ]
    )
    assert convert_6(string) == "EFEYKFRFIJ"


def test_array_nested_list():
    array = [
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    ]
    assert convert_array_6(array, fill_pixel=1, empty_pixel=0) == "AOC"
