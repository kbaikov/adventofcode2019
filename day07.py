# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("asdf.log")]
# )

# log = logging.getLogger(__name__)


def part1():
    pass


if __name__ == "__main__":

    with open("day07_input.txt") as f:
        original_tape = [int(x) for x in f.readline().split(",")]

