from typing import Any

from chapter_3.stack import Stack, PopEmpty


class StackWithBottom(Stack):
    def __init__(self):
        self._bottom = None
        super(StackWithBottom, self).__init__()

    def push(self, value: Any):

        super(StackWithBottom, self).push(value)
        if not self._bottom:
            self._bottom = self._top

    def pop(self):
        value = super(StackWithBottom, self).pop()
        if self._length == 0:
            self._bottom = None


class StackOfStacks(object):
    def __init__(self, limit):
        self._limit = limit
        self.stacks = list()
        self.stacks.append(Stack())

    def push(self, value):
        if not self.stacks:
            self.stacks.append(Stack())

        if len(self.stacks[-1]) >= self._limit:
            self.stacks.append(Stack())
        self.stacks[-1].push(value)

    def pop(self) -> Any:
        if not self.stacks:
            raise PopEmpty
        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return value

    def pop_at(self, index):
        if len(self.stacks) < index:
            raise Exception("No such stack")

        stack = self.stacks[index]
        value = stack.pop()
        if not stack.bottom:
            del self.stacks[index]
