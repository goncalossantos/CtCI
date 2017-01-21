from unittest import TestCase, expectedFailure

from data_structures.linked_lists.linked_list import LinkedList

from chapter_2.remove_kth_from_last import remove_kth_from_last


# Todo: Redo this because it is return, not remove kth from last


class TestRemoveKthFromLast(TestCase):
    @expectedFailure
    def test_remove_kth_from_last(self):
        test_cases = [
            ([1, 2, 3, 4], 2, [1, 2, 4]),
            ([1, 2, 3, 4], 3, [1, 3, 4]),
            ([1, 2, 3, 4], 4, [1, 3, 4]),
            ([1, 2, 3, 4], 1, [1, 2, 3]),
        ]

        for test in test_cases:
            ll = LinkedList(test[0])
            result = LinkedList(test[2])
            remove_kth_from_last(ll, test[1])
            assert ll == result
