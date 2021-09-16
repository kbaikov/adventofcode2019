import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from day08 import part1


def test_example():
    array = np.fromiter("123456789012", dtype=np.int)
    array = array.reshape(-1, 2, 3)
    number_of_zeros_per_layer = np.sum(np.count_nonzero(array == 0, axis=1), axis=1)
    fewest_zeros_index = np.argmin(number_of_zeros_per_layer)
    number_of_1_digits = np.sum(array[fewest_zeros_index] == 1)
    number_of_2_digits = np.sum(array[fewest_zeros_index] == 2)
    assert number_of_1_digits * number_of_2_digits == 1


def test_part1():
    with open("day08_input.txt") as f:
        array = np.fromiter(f.readline().rstrip(), dtype=np.int)
    assert part1(array) == 1206
