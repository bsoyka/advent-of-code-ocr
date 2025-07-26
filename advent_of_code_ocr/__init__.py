"""A library to parse Advent of Code ASCII art."""

from importlib.metadata import version as get_version

from .height_6 import convert_6 as convert_6
from .height_6 import convert_array_6 as convert_array_6

__version__ = get_version(__package__)
