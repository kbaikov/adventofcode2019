from anytree import Node, Walker

# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("log.log")]
# )

# log = logging.getLogger(__name__)


def parse_tree(input_list):
    """Process string and return the anytree object"""
    for pair in input_list.copy():
        left, _, right = pair.rstrip().partition(")")
        globals()[left] = Node(left)
        globals()[right] = Node(right)
    for pair in input_list.copy():
        left, _, right = pair.rstrip().partition(")")
        globals()[right].parent = globals()[left]
    return globals()


def part1(tree_root):
    depth = 0
    for descendant in tree_root.descendants:
        depth += descendant.depth
    return depth


def part2(node1, node2):
    w = Walker()
    upwards, common, downwards = w.walk(node1, node2)

    # minus 2 since you to parent and san to parent transfers ommited
    return len(upwards) + len(downwards) - 2


if __name__ == "__main__":

    with open("day06_input.txt") as f:
        tree = f.readlines()

    parse_tree(tree)
    root = globals()["YOU"].root
    print(dir(root))
    print(part1(root))  # 273985
    print(part2(globals()["YOU"], globals()["SAN"]))  # 460
