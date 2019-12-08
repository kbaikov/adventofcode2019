# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("asdf.log")]
# )

# log = logging.getLogger(__name__)


def add(tape, register):
    instruction_pointer = register["instruction_pointer"]
    input1 = tape[instruction_pointer + 1]
    input1 = input1 if register["parameter1_mode"] else tape[input1]
    input2 = tape[instruction_pointer + 2]
    input2 = input2 if register["parameter2_mode"] else tape[input2]
    output = tape[instruction_pointer + 3]
    tape[output] = input1 + input2
    return tape


def mult(tape, register):
    instruction_pointer = register["instruction_pointer"]
    input1 = tape[instruction_pointer + 1]
    input1 = input1 if register["parameter1_mode"] else tape[input1]
    input2 = tape[instruction_pointer + 2]
    input2 = input2 if register["parameter2_mode"] else tape[input2]
    output = tape[instruction_pointer + 3]
    tape[output] = input1 * input2
    return tape


def input_(tape, register, input_value):
    instruction_pointer = register["instruction_pointer"]
    input_value_position = tape[instruction_pointer + 1]
    tape[input_value_position] = input_value
    return tape


def output_(tape, register):
    instruction_pointer = register["instruction_pointer"]
    output = tape[instruction_pointer + 1]
    output = output if register["parameter1_mode"] else tape[output]
    return output


def jump_if_true(tape, register):
    instruction_pointer = register["instruction_pointer"]
    input1 = tape[instruction_pointer + 1]
    input1 = input1 if register["parameter1_mode"] else tape[input1]
    input2 = tape[instruction_pointer + 2]
    input2 = input2 if register["parameter2_mode"] else tape[input2]
    if input1:
        register["instruction_pointer"] = input2
    else:
        register["instruction_pointer"] += 3
    return register


def jump_if_false(tape, register):
    instruction_pointer = register["instruction_pointer"]
    input1 = tape[instruction_pointer + 1]
    input1 = input1 if register["parameter1_mode"] else tape[input1]
    input2 = tape[instruction_pointer + 2]
    input2 = input2 if register["parameter2_mode"] else tape[input2]
    if not input1:
        register["instruction_pointer"] = input2
    else:
        register["instruction_pointer"] += 3
    return register


def less_than(tape, register):
    instruction_pointer = register["instruction_pointer"]
    input1 = tape[instruction_pointer + 1]
    input1 = input1 if register["parameter1_mode"] else tape[input1]
    input2 = tape[instruction_pointer + 2]
    input2 = input2 if register["parameter2_mode"] else tape[input2]
    output = tape[instruction_pointer + 3]
    if input1 < input2:
        tape[output] = 1
    else:
        tape[output] = 0
    return tape


def equals(tape, register):
    instruction_pointer = register["instruction_pointer"]
    input1 = tape[instruction_pointer + 1]
    input1 = input1 if register["parameter1_mode"] else tape[input1]
    input2 = tape[instruction_pointer + 2]
    input2 = input2 if register["parameter2_mode"] else tape[input2]
    output = tape[instruction_pointer + 3]
    if input1 == input2:
        tape[output] = 1
    else:
        tape[output] = 0
    return tape


def parse_opcode(opcode_number, register):
    """Parse the opcode_number and update the register accordingly"""
    params, _, opcode = str(opcode_number).rpartition("0")
    register["opcode"] = int(str(opcode_number)[-2:])
    register["parameter1_mode"] = register["parameter2_mode"] = register[
        "parameter3_mode"
    ] = 0
    if params:
        register["parameter1_mode"] = int(params[-1])
        try:
            register["parameter2_mode"] = int(params[-2])
        except IndexError:
            return register
        try:
            register["parameter3_mode"] = int(params[-3])
        except IndexError:
            return register
    return register


def process_tape(tape, input_value):
    register = dict(
        instruction_pointer=0,
        opcode=0,
        parameter1_mode=0,
        parameter2_mode=0,
        parameter3_mode=0,
    )
    while True:

        parse_opcode(tape[register["instruction_pointer"]], register)
        if register["opcode"] == 99:
            return tape
        elif register["opcode"] == 1:
            tape = add(tape, register)
            register["instruction_pointer"] += 4
        elif register["opcode"] == 2:
            tape = mult(tape, register)
            register["instruction_pointer"] += 4
        elif register["opcode"] == 3:
            tape = input_(tape, register, input_value)
            register["instruction_pointer"] += 2
        elif register["opcode"] == 4:
            print(output_(tape, register))
            register["instruction_pointer"] += 2
        elif register["opcode"] == 5:
            register = jump_if_true(tape, register)
        elif register["opcode"] == 6:
            register = jump_if_false(tape, register)
        elif register["opcode"] == 7:
            tape = less_than(tape, register)
            register["instruction_pointer"] += 4
        elif register["opcode"] == 8:
            tape = equals(tape, register)
            register["instruction_pointer"] += 4


if __name__ == "__main__":

    with open("day05_input.txt") as f:
        original_tape = [int(x) for x in f.readline().split(",")]
    tape = original_tape.copy()
    process_tape(tape, 1)  # 9961446
    tape = original_tape.copy()
    process_tape(tape, 5)  # 742621

