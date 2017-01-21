from data_structures.trees.base import BinaryNode


class InvalidBST(Exception):
    pass


def validate(bst_root: BinaryNode) -> bool:
    def recurse(node: BinaryNode) -> None:

        if node.left:
            if node.left.data >= node.data:
                raise InvalidBST
            else:
                recurse(node.left)
        if node.right:
            if node.right.data <= node.data:
                raise InvalidBST
            else:
                recurse(node.right)

    try:
        recurse(bst_root)
    except InvalidBST:
        return False
    return True
