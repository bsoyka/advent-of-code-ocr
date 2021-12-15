# Advent of Code® OCR

This Python module helps with converting [Advent of Code](https://adventofcode.com/) ASCII art letters into plain characters. At the moment, it only supports 6-pixel-tall characters as seen in 2016 Day 8, 2019 Days 8 and 11, and 2021 Day 13.

Support for 10-pixel-tall characters (2018 Day 10) is coming soon.

Put simply, it converts this to `ABC`:

```txt
 ██  ███   ██
█  █ █  █ █  █
█  █ ███  █
████ █  █ █
█  █ █  █ █  █
█  █ ███   ██
```

# Installation

This module can be installed from PyPI:

```sh
$ pip install advent-of-code-ocr
```

# Usage

Using this module is pretty easy. By default, this module recognizes `#` as a filled pixel and `.` as an empty pixel. However, you can change this using the `fill_pixel` and `empty_pixel` keywork arguments respectively.

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
