from typing import Any

from data_structures.stacks.stack import Stack


class StackMin(Stack):
    def __init__(self):
        self._min_value = None
        super(StackMin, self).__init__()

    @property
    def min(self):
        return self._min_value

    def push(self, value: Any):

        if not self._min_value:
            self._min_value = value

        if value <= self._min_value:
            super(StackMin, self).push(self._min_value - value)
            self._min_value = value
        else:
            super(StackMin, self).push(value)

    def pop(self) -> Any:

        value = super(StackMin, self).pop()
        if value <= self._min_value:
            value, self._min_value = self._min_value, self._min_value + value
        if self._length == 0:
            self._min_value = None
        return value
