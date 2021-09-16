import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from day06 import parse_tree, part1

test_tree = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


def test_parse_tree():
    result = parse_tree(test_tree.split())
    assert "E" in result


@pytest.mark.parametrize(
    "tree, combined_depths",
    [
        (test_tree, 543),
    ],
)
def test_part1(tree, combined_depths):
    d = parse_tree(tree.split())
    combined_depths == part1(d["E"].root)
