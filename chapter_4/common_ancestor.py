from typing import Union

from data_structures.trees.base import BinaryNode


def common_ancestor(node_1: BinaryNode, node_2: BinaryNode) -> Union[BinaryNode, None]:
    depth_1 = get_depth(node_1)
    depth_2 = get_depth(node_2)

    while depth_1 > depth_2:
        node_1 = node_1.parent
        depth_1 -= 1

    while depth_1 < depth_2:
        node_2 = node_2.parent
        depth_2 -= 1

    while node_1 and node_2 and node_1 != node_2:
        node_1 = node_1.parent
        node_2 = node_2.parent

    return node_1


def get_depth(node):
    ptr = node
    depth = 0
    while ptr.parent:
        depth += 1
        ptr = ptr.parent
    return depth
