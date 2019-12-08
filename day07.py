# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("asdf.log")]
# )

# log = logging.getLogger(__name__)

from itertools import permutations

from day05 import (
    add,
    mult,
    output_,
    jump_if_true,
    jump_if_false,
    less_than,
    equals,
    parse_opcode,
)


def input_(tape, register):
    instruction_pointer = register["instruction_pointer"]
    input_value_position = tape[instruction_pointer + 1]
    tape[input_value_position] = register["input_list"].pop()
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
}


def process_tape(tape, input_list):
    register = dict(
        instruction_pointer=0,
        opcode=0,
        parameter1_mode=0,
        parameter2_mode=0,
        parameter3_mode=0,
        input_list=input_list,
        output=0,
    )
    while True:

        parse_opcode(tape[register["instruction_pointer"]], register)
        opcode = register["opcode"]
        if opcode == 99:
            return tape, register
        else:
            tape, register = operation[opcode](tape, register)


def part1():
    pass


if __name__ == "__main__":

    with open("day07_input.txt") as f:
        original_tape = [int(x) for x in f.readline().split(",")]

    max_signal = dict()
    for permutation in permutations(range(5), 5):
        tape = original_tape.copy()
        signal = 0
        for phase in permutation:
            input_list = [signal, phase]  # input signal, phase
            t, r = process_tape(tape, input_list)
            signal = r["output"]
        max_signal[permutation] = signal
    max_key_by_value = sorted(max_signal.items(), key=lambda x: x[1])
    print(max_key_by_value[-1])  # ((2, 1, 3, 4, 0), 199988)
