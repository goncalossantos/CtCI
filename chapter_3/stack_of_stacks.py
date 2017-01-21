from typing import Any

from data_structures.stacks.stack import Stack, PopEmpty


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
        if self.is_empty():
            self._bottom = None
        return value

    def pop_bottom(self):
        if not self._bottom:
            raise PopEmpty()
        value = self._bottom.value
        self._bottom = self._bottom.before
        return value

    @property
    def bottom(self):
        return self._bottom


class StackOfStacks(object):
    def __init__(self, limit):
        self._limit = limit
        self.stacks = list()
        self.stacks.append(StackWithBottom())

    def push(self, value):
        if not self.stacks:
            self.stacks.append(StackWithBottom())

        if len(self.stacks[-1]) >= self._limit:
            self.stacks.append(StackWithBottom())
        self.stacks[-1].push(value)

    def pop(self) -> Any:
        if not self.stacks:
            raise PopEmpty
        value = self.stacks[-1].pop()
        if self.stacks[-1].is_empty():
            # Remove empty stack
            self.stacks.pop()
        return value

    def pop_at(self, index):
        if len(self.stacks) < index:
            raise Exception("No such stack")

        stack = self.stacks[index]
        value = stack.pop()
        if not stack.bottom:
            del self.stacks[index]
        else:
            self.left_shift(index)
        return value

    def left_shift(self, index):

        if len(self.stacks) > index + 1:
            value = self.stacks[index + 1].pop_bottom()
            self.stacks[index].push(value)
            index += 1
            if not self.stacks[index].bottom:
                del self.stacks[index]
            else:
                self.left_shift(index)
