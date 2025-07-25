"""Command line interface for the Advent of Code OCR library."""

import click

from advent_of_code_ocr import convert_6


@click.command()
@click.argument('input_text', required=False)
@click.option('-f', '--fill-pixel', help='Fill pixel character', default='#')
@click.option('-e', '--empty-pixel', help='Empty pixel character', default='.')
def convert(input_text: str | None, fill_pixel: str, empty_pixel: str) -> None:
    """Convert height-6 OCR text to readable string."""
    if input_text is None:
        input_text = click.get_text_stream('stdin').read()

    # Convert \n to newlines so input can be passed as a single string
    input_text = input_text.replace('\\n', '\n')

    # Strip trailing whitespace and empty lines
    input_text = '\n'.join(
        line.rstrip() for line in input_text.strip().splitlines() if line.strip()
    )

    result = convert_6(input_text, fill_pixel=fill_pixel, empty_pixel=empty_pixel)
    click.echo(result)
