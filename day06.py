from anytree import Node, RenderTree

# import logging

# logging.basicConfig(
#     level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler("asdf.log")]
# )

# log = logging.getLogger(__name__)


def parse_tree(input_list):
    """Process string and return the anytree object"""
    for pair in input_list.copy():
        left, _, right = pair.partition(")")
        globals()[left] = Node(left)
        globals()[right] = Node(right)
    for pair in input_list.copy():
        left, _, right = pair.partition(")")
        globals()[right].parent = globals()[left]
    return globals()


def part1(tree_root):
    depth = 0
    for descendant in tree_root.descendants:
        depth += descendant.depth
    return depth


if __name__ == "__main__":

    with open("day06_input.txt") as f:
        tree = parse_tree(f.readlines())

    parse_tree(tree)
    print(part1(HQT.root))

