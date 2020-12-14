from itertools import groupby

import numpy as np

from .characters import ALPHABET_6


def convert_6(input_text: str, *, fill_pixel: str = "#", empty_pixel: str = "."):
    input_text = input_text.replace(fill_pixel, "1").replace(empty_pixel, "0")

    array = np.array([[int(char) for char in row] for row in input_text.split("\n")])

    rows, cols = array.shape

    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")

    indices = [
        list(g) for k, g in groupby(range(cols), lambda x: (x + 1) % 5 != 0) if k
    ]

    result = ""

    for index in indices:
        string = "\n".join(
            ["".join([str(char) for char in row]) for row in array[:, index]]
        )
        string = string.replace("0", ".").replace("1", "#")

        letter = ALPHABET_6[string]
        result += letter

    return result
