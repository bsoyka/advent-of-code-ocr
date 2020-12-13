# Advent of Code® OCR

This Python module helps with converting Advent of Code ASCII art letters into plain characters. At the moment, it only supports 6-pixel-tall characters as seen in 2016 Day 8 and 2019 Days 8 and 11.

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

Note that letters must be separated by one or more columns of empty pixels, as they are displayed in Advent of Code answers that way.

---

Advent of Code is a registered trademark of Eric K Wastl in the United States.
