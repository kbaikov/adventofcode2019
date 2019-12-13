# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")]
# )

# log = logging.getLogger(__name__)

import numpy as np
import re
from itertools import combinations


def step_gravity(p, v):
    for p1, p2 in list(combinations(p, 2)):
        if p1[0] > p2[0]:
            pass


def step_velocity(p, v):
    return p + v, v


def total_energy(p, v):
    return np.sum(np.sum(np.abs(p), axis=1) * np.sum(np.abs(v), axis=1))


def part1(p, v, n=None):
    number_of_steps = n or 10
    for step in range(number_of_steps):
        p, v = step_gravity(p, v)
        p, v = step_velocity(p, v)
    return total_energy(p, v)


def part2(array):
    pass


if __name__ == "__main__":

    with open("day12_input.txt") as f:
        # find only numbers in the file read as string
        pos = np.fromiter(re.findall("[0-9]{1,2}", f.read()), dtype=np.int).reshape(4, 3)

    vel = np.zeros((4, 3), dtype=np.int)
    print(pos, vel)  #
    # part2(array)  #
