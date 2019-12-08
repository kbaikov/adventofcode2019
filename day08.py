# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("asdf.log")]
# )

# log = logging.getLogger(__name__)
import numpy as np

if __name__ == "__main__":

    with open("day08_input.txt") as f:
        array = np.fromiter(f.readline().rstrip(), dtype=np.int)
    array = array.reshape(-1, 6, 25)
    number_of_zeros_per_layer = np.sum(np.count_nonzero(array == 0, axis=1), axis=1)
    fewest_zeros_index = np.argmin(number_of_zeros_per_layer)
    number_of_1_digits = np.sum(array[fewest_zeros_index] == 1)
    number_of_2_digits = np.sum(array[fewest_zeros_index] == 2)
    result1 = number_of_1_digits * number_of_2_digits
    print(result1)  # 1206
