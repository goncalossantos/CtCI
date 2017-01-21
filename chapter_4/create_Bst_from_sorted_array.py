from typing import List, Union

from data_structures.trees.base import BinaryNode


# TODO: Add test
# TODO: Add comments


def create_bst(array: List[int], left: int, right: int) -> Union[BinaryNode, None]:
    if right <= left:
        return None

    partition_point = (right + left) // 2
    root = BinaryNode(array[partition_point])
    new_right = partition_point
    new_left = partition_point + 1
    root.left = create_bst(array, left, new_right)
    root.right = create_bst(array, new_left, right)

    if root.left:
        root.left.parent == root
    if root.right:
        root.right.parent == root

    return root
