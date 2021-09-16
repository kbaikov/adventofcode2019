import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day02 import add, mult, process_tape, process_tape_with_parameters


@pytest.mark.parametrize(
    "tape, instruction_pointer, result",
    [
        ([1, 0, 0, 0, 99], 0, [2, 0, 0, 0, 99]),
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            0,
            [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
    ],
)
def test_add(tape, instruction_pointer, result):
    assert result == add(tape, instruction_pointer)


@pytest.mark.parametrize(
    "tape, instruction_pointer, result",
    [
        ([2, 3, 0, 3, 99], 0, [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], 0, [2, 4, 4, 5, 99, 9801]),
        (
            [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
            4,
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
    ],
)
def test_mult(tape, instruction_pointer, result):
    assert result == mult(tape, instruction_pointer)


@pytest.mark.parametrize(
    "tape, result",
    [
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
    ],
)
def test_process_tape(tape, result):
    assert result == process_tape(tape)


def test_process_tape_with_parameters():
    with open("day02_input.txt") as f:
        tape = [int(x) for x in f.readline().split(",")]
    assert 2552 == process_tape_with_parameters(tape, 19690720)
