# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")]
# )

# log = logging.getLogger(__name__)
import numpy as np
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d
from PIL import Image


def select_visible(a):
    for element in a:
        if element == 0:
            return 0
        elif element == 1:
            return 1
        elif element == 2:
            continue
        else:
            return 2


def part1(array):
    array = array.reshape(-1, 6, 25)
    number_of_zeros_per_layer = np.sum(np.count_nonzero(array == 0, axis=1), axis=1)
    fewest_zeros_index = np.argmin(number_of_zeros_per_layer)
    number_of_1_digits = np.sum(array[fewest_zeros_index] == 1)
    number_of_2_digits = np.sum(array[fewest_zeros_index] == 2)
    return number_of_1_digits * number_of_2_digits


def part2(array):
    # 0 is black, 1 is white, and 2 is transparent
    # from https://stackoverflow.com/questions/16492830/colorplot-of-2d-array-matplotlib
    array = array.reshape(-1, 6, 25)
    # array[array == 0] = 255
    # array[array == 1] = 0
    # array[array == 2] = 155
    z = np.apply_along_axis(select_visible, axis=0, arr=array)
    plt.imshow(z, alpha=0.5)
    # img = Image.fromarray(array[0])
    # img.save("testgrey.png")
    # img.show()
    plt.show()

    # fig = plt.figure(figsize=(6, 3.2))
    # ax = fig.add_subplot(111)
    # ax.set_title("colorMap")
    # ax.set_aspect("equal")
    # fig = plt.figure()
    # ax = fig.gca(projection="3d")
    # voxels = array[:2]
    # colors = np.array([[[(1.0, 2.0, 3.0, 4.0)], [(1.0, 0.0, 0.0, 0.5)], [(1.0, 0.0, 0.0, 0.5)]]])
    # ax.voxels(voxels)
    # fig = plt.figure(figsize=(4, 4))
    # ax = fig.add_subplot(111, title="Test scatter")
    # ax.scatter(array[0][0], array[0][1], s=100, color="blue", alpha=0.5)
    # fig.savefig("test_scatter.png")
    # plt.show()


if __name__ == "__main__":

    with open("day08_input.txt") as f:
        array = np.fromiter(f.readline().rstrip(), dtype=np.int)

    print(part1(array))  # 1206
    part2(array)  # EJRGP
