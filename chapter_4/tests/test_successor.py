from unittest import TestCase

from data_structures.trees.base import BinaryNode

from chapter_4.successor import successor


class TestSuccessor(TestCase):
    def test_successor(self):
        b1 = BinaryNode(5)
        b2 = BinaryNode(1)
        b3 = BinaryNode(10)
        b4 = BinaryNode(15)

        b4.left = b1
        b1.parent = b4
        b1.left = b2
        b2.parent = b1
        b1.right = b3
        b3.parent = b1

        assert successor(b1) == b3
        assert successor(b3) == b4
