from itertools import permutations


def add(tape, instruction_pointer):
    input1 = tape[instruction_pointer + 1]
    input2 = tape[instruction_pointer + 2]
    output_position = tape[instruction_pointer + 3]
    tape[output_position] = tape[input1] + tape[input2]
    return tape


def mult(tape, instruction_pointer):
    input1 = tape[instruction_pointer + 1]
    input2 = tape[instruction_pointer + 2]
    output_position = tape[instruction_pointer + 3]
    tape[output_position] = tape[input1] * tape[input2]
    return tape


def process_tape(tape):
    instruction_pointer = 0
    while True:
        if tape[instruction_pointer] == 99:
            return tape
        elif tape[instruction_pointer] == 1:
            tape = add(tape, instruction_pointer)
        elif tape[instruction_pointer] == 2:
            tape = mult(tape, instruction_pointer)
        instruction_pointer += 4


def process_tape_with_parameters(original_tape, output):
    for noun, verb in permutations(range(100), 2):
        tape = original_tape.copy()
        tape[1] = noun
        tape[2] = verb
        result = process_tape(tape)
        if tape[0] == output:
            return 100 * noun + verb


if __name__ == "__main__":

    with open("day02_input.txt") as f:
        original_tape = [int(x) for x in f.readline().split(",")]
        tape = original_tape.copy()
        tape[1] = 12
        tape[2] = 2
        result = process_tape(tape)
        result2 = process_tape_with_parameters(original_tape, 19690720)

    print(result[0], result2)  # 9706670, 2552
