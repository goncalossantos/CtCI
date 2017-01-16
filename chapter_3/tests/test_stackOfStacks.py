from unittest import TestCase

from chapter_3.stack_of_stacks import StackOfStacks


class TestStackOfStacks(TestCase):
    def test_stack_of_stacks(self):
        stack = StackOfStacks(2)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        assert len(stack.stacks) == 2
        assert len(stack.stacks[0]) == 2
        assert len(stack.stacks[1]) == 1
        stack.pop()
        assert len(stack.stacks) == 1
