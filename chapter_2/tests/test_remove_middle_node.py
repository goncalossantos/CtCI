from unittest import TestCase
from chapter_2.linked_list import LinkedList
from chapter_2.remove_middle_node import remove_middle_node


class TestRemoveMiddleNode(TestCase):

    def test_remove_middle_node(self):
        test_cases = [
            ([1, 2, 3, 4], 1, [1, 3, 4]),
            ([1, 2, 3, 4], 2, [1, 2, 4]),
        ]

        for test in test_cases:
            ll = LinkedList(test[0])
            result = LinkedList(test[2])

            # Grab the node to remove
            node = ll.head
            count = 0
            while count != test[1]:
                node = node.next
                count += 1
            # Remove it
            remove_middle_node(node)
            assert ll == result
