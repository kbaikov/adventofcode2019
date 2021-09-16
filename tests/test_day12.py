import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from day12 import part1, part2, step_gravity, step_velocity, total_energy


@pytest.mark.parametrize(
    "pos, vel, result",
    [
        (
            "2 1 -3 1 -8 0 3 6 1 2 0 4",
            "-3 -2 1 -1 1 3 3 2 -3 1 -1 -1",
            179,
        ),
        (
            "8 -12 -9 13 16 -3 -29 -11 -1 16 -13 23",
            "-7 3 0 3 -11 -5 -3 7 4 7 1 1",
            1940,
        ),
    ],
)
def test_total_energy(pos, vel, result):
    p = np.fromstring(pos, dtype=np.int, sep=" ").reshape(4, 3)
    v = np.fromstring(vel, dtype=np.int, sep=" ").reshape(4, 3)

    assert total_energy(p, v) == result


@pytest.mark.parametrize(
    "pos, vel, result",
    [
        (
            "2 1 -3 1 -8 0 3 6 1 2 0 4",
            "-3 -2 1 -1 1 3 3 2 -3 1 -1 -1",
            "-1 -1 -2 0 -7 3 6 8 -2 3 -1 3",
        ),
    ],
)
def test_step_velocity(pos, vel, result):
    p = np.fromstring(pos, dtype=np.int, sep=" ").reshape(4, 3)
    v = np.fromstring(vel, dtype=np.int, sep=" ").reshape(4, 3)
    r = np.fromstring(result, dtype=np.int, sep=" ").reshape(4, 3)

    new_p, new_v = step_velocity(p, v)

    assert np.array_equal(new_p, r)


@pytest.mark.parametrize(
    "pos, vel_result",
    [
        (
            "-1 0 2 2 -10 -7 4 -8 8 3 5 -1",
            "3 -1 -1 1 3 3 -3 1 -3 -1 -3 1",
        ),
    ],
)
def test_step_gravity(pos, vel_result):
    p = np.fromstring(pos, dtype=np.int, sep=" ").reshape(4, 3)
    v = np.zeros((4, 3), dtype=np.int)
    r = np.fromstring(vel_result, dtype=np.int, sep=" ").reshape(4, 3)

    new_p, new_v = step_gravity(p, v)

    assert np.array_equal(new_v, r)


@pytest.mark.parametrize(
    "pos, steps, total_energy",
    [
        (
            "-1 0 2 2 -10 -7 4 -8 8 3 5 -1",
            10,
            179,
        ),
        (
            "-8 -10 0 5 5 10 2 -7 3 9 -8 -3",
            100,
            1940,
        ),
        (
            "-1 0 2 2 -10 -7 4 -8 8 3 5 -1",
            1,
            229,
        ),
    ],
)
def test_part1(pos, steps, total_energy):
    p = np.fromstring(pos, dtype=np.int, sep=" ").reshape(4, 3)
    v = np.zeros((4, 3), dtype=np.int)

    assert part1(p, v, steps) == total_energy


@pytest.mark.xfail
@pytest.mark.parametrize(
    "pos, steps",
    [
        (
            "-1 0 2 2 -10 -7 4 -8 8 3 5 -1",
            2772,
        ),
        (
            "-8 -10 0 5 5 10 2 -7 3 9 -8 -3",
            4_686_774_924,
        ),
    ],
)
def test_part2(pos, steps):
    p = np.fromstring(pos, dtype=np.int, sep=" ").reshape(4, 3)
    v = np.zeros((4, 3), dtype=np.int)

    assert part2(p, v) == steps
