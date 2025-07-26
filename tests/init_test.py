"""Test the package __init__ module."""

from pathlib import Path

import toml

from advent_of_code_ocr import __version__


def test_version() -> None:
    """Test that the package version matches the pyproject.toml."""
    pyproject_path = Path(__file__).parent.parent / 'pyproject.toml'
    pyproject = toml.load(pyproject_path)

    assert __version__ == pyproject['project']['version']
