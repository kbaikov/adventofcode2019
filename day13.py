import logging
from collections import defaultdict

import numpy as np

logging.basicConfig(
    level=logging.INFO, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")],
)

log = logging.getLogger(__name__)


from day05 import (
    add,
    mult,
    input_,
    jump_if_true,
    jump_if_false,
    less_than,
    equals,
    parse_opcode,
    parse_parameters,
)

from day09 import adjust_base


def output_(tape, register):

    output, _, _ = parse_parameters(tape, register)
    # instruction_pointer = register["instruction_pointer"]
    # output = tape[instruction_pointer + 1]
    # output = output if register["parameter1_mode"] else tape[output]
    register["output"].append(output)
    register["instruction_pointer"] += 2
    # log.debug("Output: %s", output)
    return tape, register


operation = {
    1: add,
    2: mult,
    3: input_,
    4: output_,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
    9: adjust_base,
}


def process_tape(tape, input_list):
    register = dict(
        instruction_pointer=0,
        opcode=0,
        parameter1_mode=0,
        parameter2_mode=0,
        parameter3_mode=0,
        input_list=input_list,
        input=input_list[0],
        output=[],
        relative_base=0,
    )
    while True:

        parse_opcode(tape[register["instruction_pointer"]], register)
        opcode = register["opcode"]
        # log.debug("Current Output: %s", register["output"])
        # log.debug("Current OpCode: %s", register["opcode"])
        if opcode == 99:
            return tape, register
        else:
            tape, register = operation[opcode](tape, register)


if __name__ == "__main__":

    with open("day13_input.txt") as f:
        original_list = [int(x) for x in f.readline().split(",")]

    # convert tape from list to default dict
    original_tape = defaultdict(int)
    for k, v in enumerate(original_list):
        original_tape[k] = v

    tape = original_tape.copy()
    t, r = process_tape(tape, [1])
    output_array = np.array(r["output"], dtype=np.int).reshape(-1, 3)

    picture = np.zeros((50, 50), dtype=np.int)
    for sequence in output_array:
        x, y, symbol = sequence
        picture[x][y] = symbol

    print(np.sum(picture == 2))  # 341

