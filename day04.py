def increasing(numbers):
    for x, y in list(zip(numbers, numbers[1:])):
        if x > y:
            return False
    return True


def double(numbers):
    return any(x == y for x, y in list(zip(numbers, numbers[1:])))


def part1(from_, to_):
    count = 0
    for x in range(from_, to_ + 1):
        if increasing(str(x)) and double(str(x)):
            count += 1
    return count


if __name__ == "__main__":

    print(part1(265275, 781584))  # 960
