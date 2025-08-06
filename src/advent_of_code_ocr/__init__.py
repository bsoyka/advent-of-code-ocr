"""A library that converts Advent of Code ASCII art letters to plain characters."""

import importlib.metadata

from advent_of_code_ocr.height_6 import convert_6 as convert_6
from advent_of_code_ocr.height_6 import convert_array_6 as convert_array_6

__version__ = importlib.metadata.version('advent_of_code_ocr')
