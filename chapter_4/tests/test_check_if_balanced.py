from unittest import TestCase

from data_structures.trees.base import BinaryNode

from chapter_4.check_if_balanced import check_if_balanced


class TestCheck_if_balanced(TestCase):
    def test(self):
        b1 = BinaryNode(1)
        b2 = BinaryNode(2)
        b3 = BinaryNode(3)

        b1.left = b2
        b1.right = b3

        b4 = BinaryNode(1)
        b5 = BinaryNode(2)
        b6 = BinaryNode(3)

        b4.left = b5
        b5.left = b6

        assert check_if_balanced(b1)
        assert not check_if_balanced(b4)
