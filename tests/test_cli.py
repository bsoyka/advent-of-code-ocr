from pytest import mark

from advent_of_code_ocr.aoc_ocr import convert_6
from advent_of_code_ocr.main import parse_args


@mark.parametrize(
    "test_input,expected",
    [
        (
            [
                "test_input",
            ],
            {
                "input_text": "test_input",
                "fill_pixel": "#",
                "empty_pixel": ".",
            },
        )
    ],
)
def test_arg_parse(test_input, expected):
    assert vars(parse_args(test_input)) == expected


@mark.parametrize(
    "test_input,expected",
    [
        (
            ["test_input", "-f", "b", "-e", "a"],
            {
                "input_text": "test_input",
                "fill_pixel": "b",
                "empty_pixel": "a",
            },
        )
    ],
)
def test_arg_parse_optionals(test_input, expected):
    assert vars(parse_args(test_input)) == expected


@mark.parametrize(
    "test_input,expected",
    [
        (
            [
                ".##.\n#..#\n#..#\n####\n#..#\n#..#",
            ],
            "A",
        )
    ],
)
def test_main(test_input, expected):
    assert convert_6(**vars(parse_args(test_input))) == expected
