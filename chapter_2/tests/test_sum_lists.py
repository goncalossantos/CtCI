from unittest import TestCase

from chapter_2.sum_lists import sum_lists, sum_lists_follow_up

from chapter_2.linked_list import LinkedList


class TestRemoveMiddleNode(TestCase):
    def test_sum_lists(self):
        test_cases = [
            ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
            ([7, 1, 6], [5, 9, 2, 1], [2, 1, 9, 1]),
        ]

        for test in test_cases:
            list_a = LinkedList(test[0])
            list_b = LinkedList(test[1])
            result = LinkedList(test[2])

            assert sum_lists(list_a, list_b) == result

    def test_sum_lists_follow_up(self):
        test_cases = [
            ([6, 1, 7], [2, 9, 5], [9, 1, 2]),
            ([6, 1, 7], [1, 2, 9, 5], [1, 9, 1, 2]),
        ]

        for test in test_cases:
            list_a = LinkedList(test[0])
            list_b = LinkedList(test[1])
            result = LinkedList(test[2])

            assert sum_lists_follow_up(list_a, list_b) == result
