from typing import Any

from chapter_3.stack import Stack, PopEmpty


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
