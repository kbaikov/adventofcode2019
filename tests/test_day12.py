import sys
import os

import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from day12 import total_energy, step_velocity, step_gravity


@pytest.mark.parametrize(
    "pos, vel, result",
    [
        ("2 1 -3 1 -8 0 3 6 1 2 0 4", "-3 -2 1 -1 1 3 3 2 -3 1 -1 -1", 179,),
        ("8 -12 -9 13 16 -3 -29 -11 -1 16 -13 23", "-7 3 0 3 -11 -5 -3 7 4 7 1 1", 1940,),
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
    "pos, vel, result",
    [
        (
            "2 1 -3 1 -8 0 3 6 1 2 0 4",
            "-3 -2 1 -1 1 3 3 2 -3 1 -1 -1",
            "-1 -1 -2 0 -7 3 6 8 -2 3 -1 3",
        ),
    ],
)
def test_step_gravity(pos, vel, result):
    p = np.fromstring(pos, dtype=np.int, sep=" ").reshape(4, 3)
    v = np.fromstring(vel, dtype=np.int, sep=" ").reshape(4, 3)
    r = np.fromstring(result, dtype=np.int, sep=" ").reshape(4, 3)

    new_p, new_v = step_gravity(p, v)

    assert np.array_equal(new_p, r)


def test_part1():
    pass

