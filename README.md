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

[![Downloads](https://pepy.tech/badge/advent-of-code-ocr)](https://pepy.tech/project/advent-of-code-ocr)
[![Supported Versions](https://img.shields.io/pypi/pyversions/advent-of-code-ocr.svg)](https://pypi.org/project/advent-of-code-ocr)
[![Testing](https://img.shields.io/github/workflow/status/bsoyka/advent-of-code-ocr/Test%20with%20pytest?label=tests)](https://github.com/bsoyka/advent-of-code-ocr/actions?query=workflow%3A%22Test+with+pytest%22)
[![License](https://img.shields.io/pypi/l/advent-of-code-ocr)](https://github.com/bsoyka/advent-of-code-ocr/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/advent-of-code-ocr?label=latest)](https://pypi.org/project/advent-of-code-ocr)

## Installation

Advent of Code OCR is available on PyPI:

```sh
$ pip install advent-of-code-ocr
```

Advent of Code OCR officially supports Python 3.7+.

## API Reference

By default, this module recognizes `#` as a filled pixel and `.` as an empty
pixel. However, you can change this using the `fill_pixel` and `empty_pixel`
keywork arguments respectively.

```py
from advent_of_code_ocr import convert_6

print(convert_6(".##.\n#..#\n#..#\n####\n#..#\n#..#"))
# A

print(convert_6(" $$ \n$  $\n$  $\n$$$$\n$  $\n$  $", fill_pixel="$", empty_pixel=" "))
# A
```

You can also convert data that you have in a NumPy array or a nested list:

```py
from advent_of_code_ocr import convert_array_6

array = [
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
]
print(convert_array_6(array, fill_pixel=1, empty_pixel=0))
# AOC
```

---

Advent of Code is a registered trademark of Eric K Wastl in the United States.
