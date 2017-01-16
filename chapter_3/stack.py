from typing import Any

from chapter_2.linked_list import Node


class PopEmpty(Exception):
    pass


class Stack(object):
    def __init__(self):
        self._top = None
        self._length = 0

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self._top
        self._top = new_node
        self._length += 1

    def pop(self) -> Any:
        if not self._top:
            raise PopEmpty
        value = self._top.value
        self._top = self._top.next
        self._length -= 1
        return value

    def __len__(self):
        return self._length
