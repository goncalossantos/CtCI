from data_structures.trees.base import BinaryNode, BinarySearchTree


def successor(node: BinaryNode):
    """ Returns the successor Node

    I implemented this directly in the binary search tree class. Check the Introduction to Algorithms bible
    to find out how it works, but the gist of it is: if the node has right children, the successor is the minimum
    in the right subtree. Else, the successor is the first parent of node that is bigger than node

    :param node:
    :return:
    """
    bst = BinarySearchTree(None)
    return bst.tree_successor(node)
