from unittest import TestCase

from chapter_2.linked_list import LinkedList
from chapter_2.remove_kth_from_last import remove_kth_from_last


class TestRemove_kth_from_last(TestCase):
    def test_remove_kth_from_last(self):
        test_cases = [
            ([1, 2, 3, 4], 1, [1, 2, 4]),
            ([1, 2, 3, 4], 2, [1, 3, 4]),
            ([1, 2, 3, 4], 3, [2, 3, 4]),
            ([1, 2, 3, 4], 0, [1, 2, 3]),
        ]

        for test in test_cases:
            ll = LinkedList(test[0])
            result = LinkedList(test[2])
            remove_kth_from_last(ll, test[1])
            print(ll, result)
            # assert ll == result
