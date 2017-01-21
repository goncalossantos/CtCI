from data_structures.linked_lists.linked_list import LinkedList, Node


# Todo: Add tests for the merge subroutine


def partition(linked_list: LinkedList, value: int) -> LinkedList:
    """ Partitions a LinkedList object around a value

    It does this using three LinkedLists objects:
        before_list: Will hold all the values smaller than the partition value
        equal_list: Will hold all the values equal than the partition value
        after_list: Will hold all the values bigger than the partition value

    First, we iterate through the linked list and append each value to the correct sublist
    Afterwards, we just neeed to merge the three lists together.

    :param linked_list:
    :param value:
    :return:
    """

    before_list, after_list, equal_list = LinkedList(), LinkedList(), LinkedList()

    ptr = linked_list.head  # type: Node

    while ptr:
        append_correct_list(after_list, before_list, equal_list, ptr, value)
        ptr = ptr.next
    merge(after_list, before_list, equal_list)
    return before_list


def append_correct_list(after_list, before_list, equal_list, ptr, value):
    if ptr.value == value:
        equal_list.append(ptr.value)
    elif ptr.value < value:
        before_list.append(ptr.value)
    else:
        after_list.append(ptr.value)


def merge(after_list: LinkedList, before_list: LinkedList, equal_list: LinkedList) -> None:
    """
        Merges the sublists

        If we can assumer that before list and equal list are not empty,
        then the code wouldn't need those if statements.

    :param after_list: List with values bigger than the partition value
    :param before_list: List with values smaller than the partition value
    :param equal_list: List with values equal to the partition value
    :return:
    """
    if not equal_list.head:
        equal_list.head = equal_list.tail = after_list.head
    else:
        equal_list.tail.next = after_list.head
    if not before_list.head:
        before_list.head = before_list.tail = equal_list.head
    else:
        before_list.tail.next = equal_list.head
