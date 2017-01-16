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

    def test_stacks(self):
        stacks = StackOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))

    def test_pop_at(self):
        stacks = StackOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        self.assertEqual(lst, list(range(35)[4:]))
