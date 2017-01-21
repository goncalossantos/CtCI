from data_structures.trees.base import BinaryNode


class NotBalanced(Exception):
    pass


def check_if_balanced(bst_root: BinaryNode) -> bool:
    def recurse(node: BinaryNode) -> int:

        if not node:
            return 0
        depth_left = recurse(node.left)
        depth_right = recurse(node.right)
        if abs(depth_left - depth_right) > 1:
            raise NotBalanced
        return max(depth_left, depth_right) + 1

    try:
        recurse(bst_root)
    except NotBalanced:
        return False
    return True
