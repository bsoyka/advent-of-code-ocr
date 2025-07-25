"""Test cases for the CLI of the Advent of Code OCR application."""

import pytest

from advent_of_code_ocr.cli import main, parse_args


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (
            [
                'test_input',
            ],
            {
                'input_text': 'test_input',
                'fill_pixel': '#',
                'empty_pixel': '.',
            },
        )
    ],
)
def test_arg_parse(test_input: list[str], expected: dict[str, str]) -> None:
    """Test the argument parsing functionality with defaults."""
    assert vars(parse_args(test_input)) == expected


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (
            ['test_input', '-f', 'b', '-e', 'a'],
            {
                'input_text': 'test_input',
                'fill_pixel': 'b',
                'empty_pixel': 'a',
            },
        )
    ],
)
def test_arg_parse_optionals(test_input: list[str], expected: dict[str, str]) -> None:
    """Test the argument parsing functionality with custom fill and empty pixels."""
    assert vars(parse_args(test_input)) == expected


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (
            [
                '.##.\n#..#\n#..#\n####\n#..#\n#..#',
            ],
            'A',
        )
    ],
)
def test_main(test_input: list[str], expected: str) -> None:
    """Test the main function with a simple input."""
    assert main(test_input) == expected
