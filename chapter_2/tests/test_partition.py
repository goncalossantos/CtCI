from unittest import TestCase

from chapter_2.linked_list import LinkedList
from chapter_2.partition import partition


class TestListPartition(TestCase):
    def test_list_partition(self):

        test_cases = [
            ([2, 5, 10, 3, 12, 5, 3, 6, 1], 5),  # Tests normal execution
            ([2, 10, 3, 12, 3, 6, 1], 5),  # Tests empty equal sublist
            ([10, 12, 6, ], 5),  # Tests empty before sublist
            ([], 5),  # Tests empty list
            ([1], 5),  # Tests list with one value
            ([-1], 5),  # Tests list with one value
            ([5], 5),  # Tests list with one value
        ]

        for test in test_cases:
            input_list = LinkedList(test[0])
            result = partition(input_list, test[1])
            ptr = result.head
            before = True
            after = equal = False
            while ptr:
                if ptr.value < test[1]:
                    assert before
                    assert not equal
                    assert not after
                elif ptr.value == test[1] and before:
                    equal = True
                    before = False
                elif ptr.value == test[1]:
                    assert not before
                    assert equal
                    assert not after
                elif ptr.value > test[1] and equal:
                    after = True
                    equal = False
                elif ptr.value > test[1] and before:
                    after = True
                    before = False
                elif ptr.value > test[1]:
                    assert not before
                    assert not equal
                    assert after
                ptr = ptr.next
