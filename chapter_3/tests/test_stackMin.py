from unittest import TestCase

from chapter_3.stack_min import StackMin


class TestStackMin(TestCase):
    def test_min(self):
        stack = StackMin()
        assert stack.min is None
        stack.push(2)
        assert stack.min == 2
        stack.push(3)
        assert stack.min == 2
        stack.push(1)
        assert stack.min == 1
        stack.push(4)
        assert stack.min == 1

        stack.push(1)
        assert stack.min == 1

        assert stack.pop() == 1
        assert stack.min == 1

        assert stack.pop() == 4
        assert stack.min == 1

        assert stack.pop() == 1
        assert stack.min == 2

        assert stack.pop() == 3
        assert stack.min == 2

        assert stack.pop() == 2
        m = stack.min
        assert stack.min is None
