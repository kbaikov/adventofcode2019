import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from test_day05 import list_to_defaultdict

from day07 import input_, part1, part2


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


def test_part1_final_result():
    with open("day07_input.txt") as f:
        original_tape = [int(x) for x in f.readline().split(",")]
    assert part1(original_tape) == 199988


def test_part2_final_result():
    with open("day07_input.txt") as f:
        original_tape = [int(x) for x in f.readline().split(",")]
    t = list_to_defaultdict(original_tape)
    assert part2(t) == 17519904


@pytest.mark.parametrize(
    "tape, result",
    [
        (
            [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
            43210,
        ),
        (
            [
                3,
                23,
                3,
                24,
                1002,
                24,
                10,
                24,
                1002,
                23,
                -1,
                23,
                101,
                5,
                23,
                23,
                1,
                24,
                23,
                23,
                4,
                23,
                99,
                0,
                0,
            ],
            54321,
        ),
        (
            [
                3,
                31,
                3,
                32,
                1002,
                32,
                10,
                32,
                1001,
                31,
                -2,
                31,
                1007,
                31,
                0,
                33,
                1002,
                33,
                7,
                33,
                1,
                33,
                31,
                31,
                1,
                32,
                31,
                31,
                4,
                31,
                99,
                0,
                0,
                0,
            ],
            65210,
        ),
    ],
)
def test_part1_params(tape, result):
    t = list_to_defaultdict(tape)
    assert part1(t) == result


@pytest.mark.skip
@pytest.mark.parametrize(
    "tape, result",
    [
        (
            [
                3,
                26,
                1001,
                26,
                -4,
                26,
                3,
                27,
                1002,
                27,
                2,
                27,
                1,
                27,
                26,
                27,
                4,
                27,
                1001,
                28,
                -1,
                28,
                1005,
                28,
                6,
                99,
                0,
                0,
                5,
            ],
            139629729,
            # ),
            # (
            #     [
            #         3,
            #         52,
            #         1001,
            #         52,
            #         -5,
            #         52,
            #         3,
            #         53,
            #         1,
            #         52,
            #         56,
            #         54,
            #         1007,
            #         54,
            #         5,
            #         55,
            #         1005,
            #         55,
            #         26,
            #         1001,
            #         54,
            #         -5,
            #         54,
            #         1105,
            #         1,
            #         12,
            #         1,
            #         53,
            #         54,
            #         53,
            #         1008,
            #         54,
            #         0,
            #         55,
            #         1001,
            #         55,
            #         1,
            #         55,
            #         2,
            #         53,
            #         55,
            #         53,
            #         4,
            #         53,
            #         1001,
            #         56,
            #         -1,
            #         56,
            #         1005,
            #         56,
            #         6,
            #         99,
            #         0,
            #         0,
            #         0,
            #         0,
            #         10,
            #     ],
            #     18216,
        ),
    ],
)
def test_part2_params(tape, result):
    t = list_to_defaultdict(tape)
    assert part2(t) == result
