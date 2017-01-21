from unittest import TestCase

from chapter_3.queue_with_stacks import QueueWithStacks


class TestQueueWithStacks(TestCase):
    def test_queue(self):
        queue = QueueWithStacks()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert len(queue.stacks.push_stack) == 3
        assert queue.stacks.pop_stack.is_empty()
        res = queue.pop()
        assert res == 1
        assert len(queue.stacks.pop_stack) == 2
        assert queue.stacks.push_stack.is_empty()
