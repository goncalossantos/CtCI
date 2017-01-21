from collections import defaultdict
from typing import List, Dict

from data_structures.trees.base import BinaryNode


def create_lists_with_same_depth(bst_root: BinaryNode) -> Dict[List[BinaryNode]]:
    """ Creates linked lists of all elements in the BST that have the same depth

    It does this by recursing with a depth parameter and appending into an outer scope default dic
    where the key is the depth

    :param bst_root:
    :return:
    """

    output = defaultdict(list)

    def recurse(node, depth):

        if not node:
            return

        output[depth].append(node)
        if node.left:
            recurse(node.left, depth + 1)
        if node.right:
            recurse(node.right, depth + 1)

    recurse(bst_root, 0)
    return output
