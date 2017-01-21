from unittest import TestCase

from data_structures.trees.base import BinaryNode

from chapter_4.common_ancestor import common_ancestor


class TestCommon_ancestor(TestCase):
    def test_common_ancestor(self):
        b1 = BinaryNode(1)
        b2 = BinaryNode(2)
        b3 = BinaryNode(3)
        b4 = BinaryNode(4)
        b5 = BinaryNode(5)
        b1.left = b2
        b2.parent = b1
        b2.left = b3
        b2.right = b4
        b3.parent = b4.parent = b2
        b5.right = b4
        b5.parent = b4
        assert common_ancestor(b3, b5) == b2
