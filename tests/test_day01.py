import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day01 import fuel_required, fuel_required_recursive


@pytest.mark.parametrize("mass, fuel", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_fuel(mass, fuel):
    assert fuel == fuel_required(mass)


@pytest.mark.parametrize("mass, fuel", [(12, 2), (14, 2), (1969, 966), (100756, 50346)])
def test_fuel_recursive(mass, fuel):
    assert fuel == fuel_required_recursive(mass)
