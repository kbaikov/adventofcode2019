import math


def fuel_required(mass):
    return math.floor(mass / 3) - 2


def fuel_required_recursive(mass):
    result = 0
    x = fuel_required(mass)
    while True:
        result += x
        x = fuel_required(x)
        if x <= 0:
            return result


if __name__ == "__main__":

    with open("day01_input.txt") as f:
        part1_result = sum([fuel_required(int(x)) for x in f])
        f.seek(0)
        part2_result = sum([fuel_required_recursive(int(x)) for x in f])

    print(part1_result, part2_result)  # 3278434 4914785
