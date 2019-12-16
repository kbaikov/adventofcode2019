# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")]
# )

# log = logging.getLogger(__name__)

import re
from itertools import permutations
from pathlib import Path
import numpy as np


def step_gravity(p, v):
    for p1, p2 in list(permutations(p, 2)):
        velocity_index = np.where(p1 == p)
        v_change = np.select([p1 < p2, p1 > p2, p2 == p2], [1, -1, 0])
        v[velocity_index[0][0]] += v_change
    return p, v


def step_velocity(p, v):
    return p + v, v


def total_energy(p, v):
    return np.sum(np.sum(np.abs(p), axis=1) * np.sum(np.abs(v), axis=1))


def part1(p, v, n=10):
    number_of_steps = n
    for step in range(number_of_steps):
        p, v = step_gravity(p, v)
        p, v = step_velocity(p, v)
    return total_energy(p, v)


def part2(array):
    pass


if __name__ == "__main__":

    path = Path() / "day12_input.txt"
    f = path.read_text(encoding="utf-8")
    pos = np.fromiter(re.findall("[0-9]{1,2}", f), dtype=np.int).reshape(4, 3)
    vel = np.zeros((4, 3), dtype=np.int)
    print(part1(pos, vel, 1000))  # not 1343490 not 34804
    # part2(array)  #
