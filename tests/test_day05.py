import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day05 import add, mult, input_, output_, parse_opcode, process_tape

register = dict(
    instruction_pointer=0,
    opcode=0,
    parameter1_mode=0,
    parameter2_mode=0,
    parameter3_mode=0,
)
register4 = dict(
    instruction_pointer=4,
    opcode=0,
    parameter1_mode=0,
    parameter2_mode=0,
    parameter3_mode=0,
)


@pytest.mark.parametrize(
    "tape, instruction_pointer, result",
    [
        ([1, 0, 0, 0, 99], register, [2, 0, 0, 0, 99]),
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            register,
            [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
    ],
)
def test_add(tape, instruction_pointer, result):
    assert result == add(tape, instruction_pointer)


@pytest.mark.parametrize(
    "tape, instruction_pointer, result",
    [
        ([2, 3, 0, 3, 99], register, [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], register, [2, 4, 4, 5, 99, 9801]),
        (
            [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
            register4,
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
    ],
)
def test_mult(tape, instruction_pointer, result):
    assert result == mult(tape, instruction_pointer)


@pytest.mark.parametrize(
    "tape, instruction_pointer, result",
    [
        (
            [3, 0, 0, 3, 99],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
            ),
            [1, 0, 0, 3, 99],
        ),
    ],
)
def test_input_(tape, instruction_pointer, result):
    assert result == input_(tape, instruction_pointer, 1)


@pytest.mark.parametrize(
    "tape, instruction_pointer, result",
    [
        (
            [4, 3, 0, 3, 99],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
            ),
            3,
        ),
        (
            [4, 4, 4, 5, 99, 0],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
            ),
            99,
        ),
    ],
)
def test_output_(tape, instruction_pointer, result):
    assert result == output_(tape, instruction_pointer)


@pytest.mark.parametrize(
    "opcode, initial_register, result_register",
    [
        (
            1002,
            register,
            dict(
                instruction_pointer=0,
                opcode=2,
                parameter1_mode=0,
                parameter2_mode=1,
                parameter3_mode=0,
            ),
        ),
        (
            11101,
            register,
            dict(
                instruction_pointer=0,
                opcode=1,
                parameter1_mode=1,
                parameter2_mode=1,
                parameter3_mode=1,
            ),
        ),
        (
            2,
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
            ),
            dict(
                instruction_pointer=0,
                opcode=2,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
            ),
        ),
    ],
)
def test_parse_opcode(opcode, initial_register, result_register):
    assert result_register == parse_opcode(opcode, initial_register)


@pytest.mark.parametrize(
    "tape, result",
    [
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
        ([1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99],),
    ],
)
def test_process_tape(tape, result):
    assert result == process_tape(tape, 1)

