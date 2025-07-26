# Advent of Code® OCR

This Python module converts [Advent of Code](https://adventofcode.com/) ASCII
art letters to plain characters.

At the moment, it supports 6-pixel-tall characters as seen in 2016 Day 8, 2019
Days 8 and 11, and 2021 Day 13. (Support for 10-pixel-tall characters, as seen
in 2018 Day 10, is coming soon.)

Put simply, it converts something like this to plain text:

```txt
 ██  ███   ██
█  █ █  █ █  █
█  █ ███  █
████ █  █ █
█  █ █  █ █  █
█  █ ███   ██
```

[![PyPI - Downloads](https://img.shields.io/pypi/dm/advent-of-code-ocr)](https://pypi.org/project/advent-of-code-ocr/)
[![Supported Versions](https://img.shields.io/pypi/pyversions/advent-of-code-ocr.svg)](https://pypi.org/project/advent-of-code-ocr)
[![Testing Status](https://img.shields.io/github/actions/workflow/status/bsoyka/advent-of-code-ocr/test.yml?branch=main&label=tests)](https://github.com/bsoyka/advent-of-code-ocr/actions?query=workflow%3A%22Test+with+pytest%22)
[![License](https://img.shields.io/pypi/l/advent-of-code-ocr)](https://github.com/bsoyka/advent-of-code-ocr/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/advent-of-code-ocr?label=latest)](https://pypi.org/project/advent-of-code-ocr)
[![Codecov](https://codecov.io/github/bsoyka/advent-of-code-ocr/branch/main/graph/badge.svg?token=JLGSYTAVZS)](https://codecov.io/github/bsoyka/advent-of-code-ocr)
[![GitHub Repo stars](https://img.shields.io/github/stars/bsoyka/advent-of-code-ocr)](https://github.com/bsoyka/advent-of-code-ocr)

## Installation

Advent of Code OCR is [available on PyPI](https://pypi.org/project/advent-of-code-ocr/).
Install it with your preferred package manager:

```sh
$ uv add advent-of-code-ocr
$ pip install advent-of-code-ocr
```

Advent of Code OCR officially supports Python 3.10+.

**[See the full documentation for this project on Read the Docs.](https://aoc-ocr.bsoyka.me/en/latest/)**

---

Advent of Code is a registered trademark of Eric K Wastl in the United States.
