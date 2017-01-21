from unittest import TestCase

from data_structures.stacks.stack import Stack

from chapter_3.sort_stack import sort_stack


class TestSortStack(TestCase):
    def test(self):
        stack = Stack()
        for i in [4, 3, 6, 1, 9, 2, 7, 5, 8]:
            stack.push(i)
        sorted_stack = sort_stack(stack)
        ls = list()
        while not sorted_stack.is_empty():
            ls.append(sorted_stack.pop())
        assert ls == [1, 2, 3, 4, 5, 6, 7, 8, 9]
