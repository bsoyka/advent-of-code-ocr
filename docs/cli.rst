Command-line interface
----------------------

Advent of Code OCR provides a command-line interface (CLI) for easy interaction with the tool.

.. code::

    $ python -m advent-of-code-ocr --help
    Usage: python -m advent_of_code_ocr [OPTIONS] [INPUT_TEXT]

      Convert height-6 OCR text to readable string.

    Options:
      -f, --fill-pixel TEXT   Fill pixel character
      -e, --empty-pixel TEXT  Empty pixel character
      --help                  Show this message and exit.

The tool accepts a height-6 character image as input (either as an argument or via stdin) and outputs the recognized characters.
For example:

.. code::

    $ python -m advent_of_code_ocr '.##.\n#..#\n#..#\n####\n#..#\n#..#'
    A

    $ echo -e '.##.\n#..#\n#..#\n####\n#..#\n#..#' | python -m advent_of_code_ocr
    A

You can also specify the characters representing the filled and empty pixels using the `-f` and `-e` options:

.. code::

    $ python -m advent_of_code_ocr -f 'O' -e 'o' 'oOOo\nOooO\nOooO\nOOOO\nOooO\nOooO'
    A
