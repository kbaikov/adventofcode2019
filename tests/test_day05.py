import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day05 import add, mult, input_, output_, parse_parameters, parse_opcode, process_tape

register = dict(
    instruction_pointer=0,
    opcode=0,
    parameter1_mode=0,
    parameter2_mode=0,
    parameter3_mode=0,
    input=0,
    output=0,
    relative_base=0,
)
register4 = dict(
    instruction_pointer=4,
    opcode=0,
    parameter1_mode=0,
    parameter2_mode=0,
    parameter3_mode=0,
    input=0,
    output=0,
    relative_base=0,
)


@pytest.mark.parametrize(
    "tape, register, result",
    [
        (
            [1, 0, 0, 3, 99],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
                relative_base=0,
            ),
            (1, 1, 3),
        ),
        (
            [1, 0, 0, 3, 99],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=1,
                parameter2_mode=1,
                parameter3_mode=1,
                relative_base=0,
            ),
            (0, 0, 3),
        ),
        (
            [1, 0, 0, 3, 99],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=2,
                parameter2_mode=2,
                parameter3_mode=2,
                relative_base=1,
            ),
            (0, 0, 99),
        ),
    ],
)
def test_parse_parameters(tape, register, result):
    assert result == parse_parameters(tape, register)


@pytest.mark.parametrize(
    "tape, register, result",
    [
        ([1, 0, 0, 0, 99], register, [2, 0, 0, 0, 99]),
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            register,
            [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
    ],
)
def test_add(tape, register, result):
    assert result, _ == add(tape, register)


@pytest.mark.parametrize(
    "tape, register, result",
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
def test_mult(tape, register, result):
    assert result, _ == mult(tape, register)


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
                relative_base=0,
            ),
            [1, 0, 0, 3, 99],
        ),
    ],
)
def test_input_(tape, register, result):
    assert result, _ == input_(tape, register, 1)


@pytest.mark.parametrize(
    "tape, register, result",
    [
        (
            [4, 3, 0, 3, 99],
            dict(
                instruction_pointer=0,
                opcode=0,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
                relative_base=0,
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
                relative_base=0,
            ),
            99,
        ),
    ],
)
def test_output_(tape, register, result):
    t, r = output_(tape, register)
    assert r["output"] == result


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
                input=0,
                output=0,
                relative_base=0,
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
                input=0,
                output=0,
                relative_base=0,
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
                relative_base=0,
            ),
            dict(
                instruction_pointer=0,
                opcode=2,
                parameter1_mode=0,
                parameter2_mode=0,
                parameter3_mode=0,
                relative_base=0,
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
    t, r = process_tape(tape, 1)
    assert t == result

