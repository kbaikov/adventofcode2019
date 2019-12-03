def process_directions(steps):
    result = [(0, 0)]
    for step in steps:
        last_element = result[-1]
        if step[0] == "R":
            for x in range(1, int(step[1:]) + 1):
                result.append(((last_element[0] + x), last_element[1]))
        if step[0] == "L":
            for x in range(1, int(step[1:]) + 1):
                result.append(((last_element[0] - x), last_element[1]))
        if step[0] == "D":
            for x in range(1, int(step[1:]) + 1):
                result.append(((last_element[0]), last_element[1] - x))
        if step[0] == "U":
            for x in range(1, int(step[1:]) + 1):
                result.append(((last_element[0]), last_element[1] + x))

    return result


def closest_intersection_distance(list1, list2):
    coords1 = set(list1)
    coords2 = set(list2)
    intersection = coords1 & coords2
    intersection.discard((0, 0))
    manhattans = [manhattan(x, (0, 0)) for x in intersection]
    return min(manhattans)


def fewest_steps(list1, list2):
    coords1 = set(list1)
    coords2 = set(list2)
    intersection = coords1 & coords2
    intersection.discard((0, 0))
    steps_to_intersection = [list1.index(z) + list2.index(z) for z in intersection]
    return min(steps_to_intersection)


def manhattan(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[0])


def part1(steps1, steps2):
    steps1 = steps1.split(",")
    steps2 = steps2.split(",")
    visited1 = process_directions(steps1)
    visited2 = process_directions(steps2)
    return closest_intersection_distance(visited1, visited2)


def part2(steps1, steps2):
    steps1 = steps1.split(",")
    steps2 = steps2.split(",")
    visited1 = process_directions(steps1)
    visited2 = process_directions(steps2)
    return fewest_steps(visited1, visited2)


if __name__ == "__main__":

    with open("day03_input.txt") as f:
        steps1, steps2 = f.readlines()

    print(part1(steps1, steps2))  # 1285
    print(part2(steps1, steps2))  # 14228
