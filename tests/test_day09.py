import logging
import os
import sys

from test_day05 import list_to_defaultdict

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")],
# )

log = logging.getLogger(__name__)

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day09 import adjust_base, process_tape

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
    relative_base=-1,
)


@pytest.mark.parametrize(
    "tape, result",
    [
        ([109, 19], 19),
    ],
)
def test_adjust_base(init_register, tape, result):
    init_register["parameter1_mode"] = 1
    d = list_to_defaultdict(tape)
    t, r = adjust_base(d, init_register)
    assert r["relative_base"] == result
    assert r["instruction_pointer"] == 2


@pytest.mark.parametrize(
    "tape, result",
    [
        (
            [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99],
            99,
        ),
        (
            [104, 1125899906842624, 99],
            1125899906842624,
        ),
        (
            [1102, 34915192, 34915192, 7, 4, 7, 99, 0],
            1219070632396864,
        ),
    ],
)
def test_process_tape(tape, result):
    d = list_to_defaultdict(tape)
    t, r = process_tape(d, [1])
    # result_dict = list_to_defaultdict(result)
    # log.debug("output %s", r["output"])
    assert r["output"] == result
