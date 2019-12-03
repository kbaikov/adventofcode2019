import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day03 import process_directions, closest_intersection_distance, part1, part2


@pytest.mark.parametrize(
    "steps, result",
    [
        (["R1"], [(0, 0), (1, 0)],),
        (["R3"], [(0, 0), (1, 0), (2, 0), (3, 0)],),
        (["L1"], [(0, 0), (-1, 0)],),
        (["L3"], [(0, 0), (-1, 0), (-2, 0), (-3, 0)],),
        (["U1"], [(0, 0), (0, 1)],),
        (["U3"], [(0, 0), (0, 1), (0, 2), (0, 3)],),
        (["D1"], [(0, 0), (0, -1)],),
        (["D3"], [(0, 0), (0, -1), (0, -2), (0, -3)],),
        (["R1", "U1", "L1", "D1"], [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],),
    ],
)
def test_process_directions(steps, result):
    assert result == process_directions(steps)


@pytest.mark.parametrize(
    "c1, c2, result", [([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0)], 1),],
)
def test_closest_intersection_distance(c1, c2, result):
    assert result == closest_intersection_distance(c1, c2)


@pytest.mark.parametrize(
    "c1, c2, result",
    [
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
        ),
    ],
)
def test_part1(c1, c2, result):
    assert result == part1(c1, c2)


@pytest.mark.parametrize(
    "c1, c2, result",
    [
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 610),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            410,
        ),
    ],
)
def test_part2(c1, c2, result):
    assert result == part2(c1, c2)
