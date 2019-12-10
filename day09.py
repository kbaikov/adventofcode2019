import logging
from collections import defaultdict

logging.basicConfig(
    level=logging.INFO, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")],
)

log = logging.getLogger(__name__)


from day05 import (
    add,
    mult,
    output_,
    input_,
    jump_if_true,
    jump_if_false,
    less_than,
    equals,
    parse_opcode,
    parse_parameters,
)


def adjust_base(tape, register):
    """Opcode 9 adjusts the relative base by the value of its only parameter.
    The relative base increases (or decreases, if the value is negative)
    by the value of the parameter."""
    instruction_pointer = register["instruction_pointer"]
    relative_base = register["relative_base"]
    input1 = tape[instruction_pointer + 1]

    if register["parameter1_mode"] == 0:
        input1 = tape[input1]
    elif register["parameter1_mode"] == 2:
        input1 = tape[input1 + relative_base]

    register["relative_base"] += input1
    register["instruction_pointer"] += 2
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
        output=0,
        relative_base=0,
    )
    while True:

        parse_opcode(tape[register["instruction_pointer"]], register)
        opcode = register["opcode"]
        log.debug("Current Output: %s", register["output"])
        log.debug("Current OpCode: %s", register["opcode"])
        if opcode == 99:
            return tape, register
        else:
            tape, register = operation[opcode](tape, register)


if __name__ == "__main__":

    with open("day09_input.txt") as f:
        original_list = [int(x) for x in f.readline().split(",")]

    # convert tape from list to default dict
    original_tape = defaultdict(int)
    for k, v in enumerate(original_list):
        original_tape[k] = v

    tape = original_tape.copy()
    t, r = process_tape(tape, [1])
    log.info("Part 1 final output: %s", r["output"])  # 2714716640

    tape = original_tape.copy()
    t, r = process_tape(tape, [2])
    log.info("Part 2 final output: %s", r["output"])  # 58879
