import logging
from collections import defaultdict

import numpy as np

logging.basicConfig(
    level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")],
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


def part2(tape):
    tape[0] = 2
    inp = 2
    while True:
        t, r = process_tape(tape, [inp])
        output_array = np.array(r["output"], dtype=np.int).reshape(-1, 3)

        picture = np.zeros((101, 101), dtype=np.int)
        for sequence in output_array:
            x, y, symbol = sequence
            if x == -1 and y == 0:
                current_score = symbol
                continue
            picture[x][y] = symbol
        log.debug("Current score: %s", current_score)
        paddle, _ = np.where(picture == 3)
        ball, _ = np.where(picture == 4)
        paddle = paddle[0]
        ball = ball[0]

        if ball < paddle:
            inp = -1
        elif ball > paddle:
            inp = 1
        else:
            inp = 0


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

    log.info("Part1 solution: %s", np.sum(picture == 2))  # 341
    tape = original_tape.copy()
    log.info("Part2 solution: %s", part2(tape))  #

