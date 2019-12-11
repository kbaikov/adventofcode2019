# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")]
# )

# log = logging.getLogger(__name__)
import numpy as np
import matplotlib.pyplot as plt


def part1(array):
    array = array.reshape(-1, 6, 25)
    number_of_zeros_per_layer = np.sum(np.count_nonzero(array == 0, axis=1), axis=1)
    fewest_zeros_index = np.argmin(number_of_zeros_per_layer)
    number_of_1_digits = np.sum(array[fewest_zeros_index] == 1)
    number_of_2_digits = np.sum(array[fewest_zeros_index] == 2)
    return number_of_1_digits * number_of_2_digits


def part2(array):
    # from https://stackoverflow.com/questions/16492830/colorplot-of-2d-array-matplotlib
    array = array.reshape(-1, 6, 25)
    # fig = plt.figure(figsize=(6, 3.2))
    # ax = fig.add_subplot(111)
    # ax.set_title("colorMap")
    plt.imshow(array[0], cmap=plt.cm.bone)
    # ax.set_aspect("equal")
    plt.show()


if __name__ == "__main__":

    with open("day08_input.txt") as f:
        array = np.fromiter(f.readline().rstrip(), dtype=np.int)

    print(part1(array))  # 1206
    part2(array)
