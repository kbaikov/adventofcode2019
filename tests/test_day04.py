import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day04 import double, increasing, only_double, part1, part2


@pytest.mark.parametrize(
    "string_of_numbers, result", [("123789", False), ("1223789", True), ("1111", True),],
)
def test_double(string_of_numbers, result):
    assert result == double(string_of_numbers)


@pytest.mark.parametrize(
    "string_of_numbers, result", [("123780", False), ("1223789", True), ("1111", True),],
)
def test_increasing(string_of_numbers, result):
    assert result == increasing(string_of_numbers)


@pytest.mark.parametrize(
    "string_of_numbers, result", [("112233", True), ("123444", False), ("111122", True),],
)
def test_only_double(string_of_numbers, result):
    assert result == only_double(string_of_numbers)


@pytest.mark.parametrize(
    "c1, c2, result", [(265275, 781584, 960,),],
)
def test_part1(c1, c2, result):
    assert result == part1(c1, c2)


@pytest.mark.parametrize(
    "c1, c2, result", [(265275, 781584, 626,),],
)
def test_part2(c1, c2, result):
    assert result == part2(c1, c2)

