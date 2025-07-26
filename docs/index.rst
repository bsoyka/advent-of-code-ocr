Advent of Code OCR documentation
================================

This Python module converts `Advent of Code <https://adventofcode.com/>`_ ASCII art letters to plain characters.

At the moment, it supports 6-pixel-tall characters as seen in 2016 Day 8, 2019 Days 8 and 11, and 2021 Day 13.
(Support for 10-pixel-tall characters, as seen in 2018 Day 10, is coming soon.)

Put simply, it converts something like this to plain text:

.. code::

     ██  ███   ██
    █  █ █  █ █  █
    █  █ ███  █
    ████ █  █ █
    █  █ █  █ █  █
    █  █ ███   ██

.. image:: https://img.shields.io/pypi/dm/advent-of-code-ocr
    :alt: PyPI - Downloads
    :target: https://pypi.org/project/advent-of-code-ocr/

.. image:: https://img.shields.io/pypi/pyversions/advent-of-code-ocr
    :alt: Supported Python Versions
    :target: https://pypi.org/project/advent-of-code-ocr/

.. image:: https://img.shields.io/github/actions/workflow/status/bsoyka/advent-of-code-ocr/test.yml?branch=main&label=tests
    :alt: Testing Status
    :target: https://github.com/bsoyka/advent-of-code-ocr/actions/workflows/test.yml

.. image:: https://img.shields.io/pypi/l/advent-of-code-ocr
    :alt: License
    :target: https://github.com/bsoyka/advent-of-code-ocr/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/v/advent-of-code-ocr?label=latest
    :alt: Version
    :target: https://pypi.org/project/advent-of-code-ocr/

.. image:: https://codecov.io/github/bsoyka/advent-of-code-ocr/branch/main/graph/badge.svg?token=JLGSYTAVZS
    :alt: Codecov
    :target: https://codecov.io/github/bsoyka/advent-of-code-ocr

.. image:: https://img.shields.io/github/stars/bsoyka/advent-of-code-ocr
    :alt: GitHub Repo stars
    :target: https://github.com/bsoyka/advent-of-code-ocr

Installation
------------

Advent of Code OCR is `available on PyPI <https://pypi.org/project/advent-of-code-ocr/>`_.
Install it with your preferred package manager:

.. code::

    $ uv add advent-of-code-ocr
    $ pip install advent-of-code-ocr

Advent of Code OCR officially supports Python 3.10+.

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    height_6
    cli

Advent of Code is a registered trademark of Eric K Wastl in the United States.
This project is not affiliated with nor endorsed by Advent of Code.
