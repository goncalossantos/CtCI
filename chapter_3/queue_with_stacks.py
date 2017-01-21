from collections import namedtuple
from typing import Any

from chapter_3.data_structure.stack import Stack, PopEmpty

QueueStacks = namedtuple("QueueStacks", ["push_stack", "pop_stack"])


class QueueWithStacks(object):
    """ Queue with two stacks works by having one queue for pushing and another for popping.
    When we try to pop from the popping stack and it is empty, we move all the elements that exist
    on the pushing stack into the popping stack.
    """

    def __init__(self) -> None:
        self.stacks = QueueStacks(push_stack=Stack(), pop_stack=Stack())

    def push(self, value: Any) -> None:
        self.stacks.push_stack.push(value)

    def pop(self) -> Any:

        if self.stacks.pop_stack.is_empty():
            self._move()
        if self.stacks.pop_stack.is_empty():
            raise PopEmpty
        return self.stacks.pop_stack.pop()

    def _move(self):

        while not self.stacks.push_stack.is_empty():
            self.stacks.pop_stack.push(self.stacks.push_stack.pop())
