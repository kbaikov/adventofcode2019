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
    for v_index, p1 in enumerate(p):
        for p2 in p:
            velocity_index = np.where(p == p1)
            v_change = np.select([p1 < p2, p1 > p2, p1 == p2], [1, -1, 0])
            v[v_index] += v_change
    return p, v


def step_velocity(p, v):
    return p + v, v


def total_energy(p, v):
    potential_energy = np.sum(np.abs(p), axis=1)
    kinetic_energy = np.sum(np.abs(v), axis=1)
    return np.sum(potential_energy * kinetic_energy)


def part1(p, v, n=10):
    for step in range(n):
        p, v = step_gravity(p, v)
        p, v = step_velocity(p, v)
    return total_energy(p, v)


def part2(array):
    pass


if __name__ == "__main__":

    path = Path() / "day12_input.txt"
    f = path.read_text(encoding="utf-8")
    pos = np.fromiter(re.findall("[-0-9]{1,2}", f), dtype=np.int).reshape(4, 3)
    vel = np.zeros((4, 3), dtype=np.int)
    print(part1(pos, vel, 1000))  # 8362 not 1343490 not 34804 not 37562 not 5324
    # part2(array)  #
