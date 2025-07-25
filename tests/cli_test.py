"""Test cases for the CLI of the Advent of Code OCR application."""

import pytest
from click.testing import CliRunner

from advent_of_code_ocr.characters import ALPHABET_6
from advent_of_code_ocr.cli import convert


@pytest.mark.parametrize(('test_input', 'expected'), ALPHABET_6.items())
def test_cli_single_letter(test_input: str, expected: str) -> None:
    """Test conversion of a single letter via CLI."""
    runner = CliRunner()
    result = runner.invoke(convert, [test_input])
    assert result.exit_code == 0
    assert result.output.strip() == expected


def test_cli_three_letters() -> None:
    """Test conversion of three letters via CLI."""
    runner = CliRunner()
    test_input = (
        '.##..###...##.\n'
        '#..#.#..#.#..#\n'
        '#..#.###..#...\n'
        '####.#..#.#...\n'
        '#..#.#..#.#..#\n'
        '#..#.###...##.'
    )
    result = runner.invoke(convert, [test_input])
    assert result.exit_code == 0
    assert result.output.strip() == 'ABC'


def test_cli_from_stdin() -> None:
    """Test conversion of input from stdin via CLI."""
    runner = CliRunner()
    test_input = (
        '.##..###...##.\n'
        '#..#.#..#.#..#\n'
        '#..#.###..#...\n'
        '####.#..#.#...\n'
        '#..#.#..#.#..#\n'
        '#..#.###...##.'
    )
    result = runner.invoke(convert, input=test_input)
    assert result.exit_code == 0
    assert result.output.strip() == 'ABC'
