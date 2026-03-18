"""Command line interface for the Advent of Code OCR library."""

from __future__ import annotations

import click

from advent_of_code_ocr import convert_6
from advent_of_code_ocr.height_10 import convert_10

SUPPORTED_HEIGHTS = {6: convert_6, 10: convert_10}


@click.command()
@click.argument('input_text', required=False)
@click.option('-f', '--fill-pixel', help='Fill pixel character', default='#')
@click.option('-e', '--empty-pixel', help='Empty pixel character', default='.')
def convert(input_text: str | None, fill_pixel: str, empty_pixel: str) -> None:
    """Convert OCR text to readable string.

    Raises:
        click.BadParameter: If the input height is not supported.
    """
    if input_text is None:
        input_text = click.get_text_stream('stdin').read()

    # Convert \n to newlines so input can be passed as a single string
    input_text = input_text.replace('\\n', '\n')

    # Strip trailing whitespace and empty lines
    input_text = '\n'.join(
        line.rstrip() for line in input_text.strip().splitlines() if line.strip()
    )

    height = len(input_text.splitlines())
    if height not in SUPPORTED_HEIGHTS:
        expected = sorted(SUPPORTED_HEIGHTS)
        msg = f'Unsupported height: {height}. Expected one of {expected}'
        raise click.BadParameter(msg, param_hint="'INPUT_TEXT'")

    converter = SUPPORTED_HEIGHTS[height]
    result = converter(input_text, fill_pixel=fill_pixel, empty_pixel=empty_pixel)
    click.echo(result)
