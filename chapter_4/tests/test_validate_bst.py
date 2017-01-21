from unittest import TestCase

from data_structures.trees.base import BinaryNode

from chapter_4.validate_bst import validate


class TestBSTValidation(TestCase):
    def test(self):
        b1 = BinaryNode(2)
        b2 = BinaryNode(1)
        b3 = BinaryNode(3)

        b1.left = b2
        b1.right = b3
        assert validate(b1)

        b1.right = b2
        b1.left = b3
        assert not validate(b1)
