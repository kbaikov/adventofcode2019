import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from day07 import part1, input_


@pytest.mark.parametrize(
    "tape, register, result",
    [
        (
            [3, 0, 0, 3, 99],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
                input_list=[5, 6],
            ),
            [6, 0, 0, 3, 99],
        ),
    ],
)
def test_input_(tape, register, result):
    t, r = input_(tape, register)
    assert t == result
    assert r["instruction_pointer"] == 2

