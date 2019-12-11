import logging
from copy import deepcopy
from tests.test_day05 import list_to_defaultdict

logging.basicConfig(
    level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")]
)

log = logging.getLogger(__name__)

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
        relative_base=0,
    )
    while True:

        parse_opcode(tape[register["instruction_pointer"]], register)
        opcode = register["opcode"]
        if opcode == 99:
            return tape, register
        else:
            tape, register = operation[opcode](tape, register)


def process_tape2(tape, register):
    while True:

        parse_opcode(tape[register["instruction_pointer"]], register)
        opcode = register["opcode"]
        if opcode == 99:
            return tape, register
        if opcode == 4:
            tape, register = operation[opcode](tape, register)
            return tape, register
        else:
            tape, register = operation[opcode](tape, register)


def part1(tape):
    max_signal = dict()
    for permutation in permutations(range(5), 5):
        signal = 0
        for phase in permutation:
            input_list = [signal, phase]  # input signal, phase
            t, r = process_tape(tape, input_list)
            signal = r["output"]
        max_signal[permutation] = signal
    max_key_by_value = sorted(max_signal.items(), key=lambda x: x[1])
    return max_key_by_value[-1][1]  # ((2, 1, 3, 4, 0), 199988)


def part2(tape):
    max_signal = dict()
    for permutation in permutations(range(5, 10), 5):
        register = dict(
            instruction_pointer=0,
            opcode=0,
            parameter1_mode=0,
            parameter2_mode=0,
            parameter3_mode=0,
            input_list=[],
            output=0,
            relative_base=0,
        )
        signal = 0
        amps = {s: [tape.copy(), deepcopy(register)] for s in "ABCDE"}
        amps["A"][1]["input_list"] = [permutation[0]]
        amps["B"][1]["input_list"] = [permutation[1]]
        amps["C"][1]["input_list"] = [permutation[2]]
        amps["D"][1]["input_list"] = [permutation[3]]
        amps["E"][1]["input_list"] = [permutation[4]]

        while amps["E"][1]["opcode"] != 99:
            for amplifier, (tape, register) in amps.items():
                register["input_list"].insert(0, signal)
                t, r = process_tape2(tape, register)
                # tape, register = t, r
                # input_list = [signal, phase]  # input signal, phase
                signal = r["output"]
            signal = amps["E"][1]["output"]
        max_signal[permutation] = amps["E"][1]["output"]

    max_key_by_value = sorted(max_signal.items(), key=lambda x: x[1])
    return max_key_by_value[-1][1]  # ((2, 1, 3, 4, 0), 199988)


if __name__ == "__main__":

    with open("day07_input.txt") as f:
        original_tape = [int(x) for x in f.readline().split(",")]

    t = list_to_defaultdict(original_tape)
    # log.info("Part 1 solution: %s", part1(original_tape))  # 199988
    log.info("Part 2 solution: %s", part2(t))  # 17519904 not 1153638 not 2286232 not 2343436
