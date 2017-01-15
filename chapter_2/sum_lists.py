from collections import namedtuple

from chapter_2.linked_list import LinkedList, Node

SumNodesResult = namedtuple("SumNodesResult", ['digit', 'carry'])


def sum_lists(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
    """ Sum lists together (Exercise 2.5 from CtCI)

    We receive two linked lists as an input and need to return a linked List with the resulting sum.
    Each node represents a digit in a number.
    This routine assumes that the Linked LIst format is Least Significant -> Most Significant

    Example
        list_a = 7 -> 1 -> 6 (617)
        list_b = 5 -> 9 -> 2 (295)
        output = 2 -> 1 -> 9 (912)

    There is also the case where the lists don't have the same size
    Example:
        list_a = 7 -> 1 -> 6      (617)
        list_b = 5 -> 9 -> 2 -> 1 (1295)
        output = 2 -> 1 -> 9 -> 1 (1912)

    In order to this, we iterate through both lists, adding each pair of nodes' values together plus a carry value
    from a previous sum.
    We can only store one digit in a node in the output, so we store the summed_value % 10.
    We also need to save the carry, which is the summed_value // 10. This carry will be used on the next sum

    When we are iterating, if one of the lists is exhausted before the other, we only sum the other list's value
    and the carry (actually we sum zero as the value of the exhausted list)

    :param list_a: List to be summed
    :param list_b: List to be summed
    :return: Returns an output linked list with the result of the sum
    """

    output = LinkedList()
    ptr_a, ptr_b = list_a.head, list_b.head
    carry = 0  # type: int

    # Test Null case
    if not ptr_a and not ptr_b:
        return output

    # Iterate through both lists, performing a sum and appending to the output sub list
    while ptr_a is not None or ptr_b is not None:  # We can only stop when both lists have been exhausted
        next_output_digit, carry = sum_nodes(ptr_a, ptr_b, carry)
        output.append(next_output_digit)
        # Iterate
        ptr_a = ptr_a if not ptr_a else ptr_a.next
        ptr_b = ptr_b if not ptr_b else ptr_b.next

    # If the last time we summed we produced a carry, it has to be added to the list
    if carry > 0:
        output.append(carry)

    return output


def sum_nodes(ptr_a: Node, ptr_b: Node, carry: int) -> SumNodesResult:
    """ Sums two nodes' values together, and returns the resulting least signinficant digit of the sum
    and its carry

    :param ptr_a: Node to be summed
    :param ptr_b: Other Node
    :param carry: carry from the previous sum
    :return: Returns a tuple with the next digit on the output and the carry value
    """

    val_a = 0 if not ptr_a else ptr_a.value
    val_b = 0 if not ptr_b else ptr_b.value

    summed_value = val_a + val_b + carry
    return SumNodesResult(summed_value % 10, summed_value // 10)


def sum_lists_follow_up(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
    """ Sum lists together (Exercise 2.5 from CtCI)

    We receive two linked lists as an input and need to return a linked List with the resulting sum.
    Each node represents a digit in a number.
    This routine assumes that the Linked LIst format is Most Significant -> Least Significant

    Example
        list_a = 6 -> 1 -> 7 (617)
        list_b = 2 -> 9 -> 5 (295)
        output = 9 -> 1 -> 2 (912)

    There is also the case where the lists don't have the same size
    Example:
        list_a =      6 -> 1 -> 7 (617)
        list_b = 1 -> 2 -> 9 -> 5 (1295)
        output = 1 -> 9 -> 1 -> 2 (1912)

    In order to this, first we iterate through each list separably, adding each node found to a stack specific to that
    list. This is effect gives us a means of iterating through the linked list in reversed order.

    Now, we do the same procedure as in the 'sum_list' routine, except that instead of iterating though two linked
    lists, in here we pop from two stacks until both stacks are exhausted.

    Also, contrary to sum_lists, the resulting digits can't be appended to the output list, they need to be pushed
    in the beginning, to respect the digit order.

    :param list_a: List to be summed
    :param list_b: List to be summed
    :return: Returns an output linked list with the result of the sum
    """

    output = LinkedList()
    ptr_a, ptr_b = list_a.head, list_b.head
    carry = 0  # type: int
    stack_a, stack_b = list(), list()

    # Test Null case
    if not ptr_a and not ptr_b:
        return output

    list_to_stack(ptr_a, stack_a)
    list_to_stack(ptr_b, stack_b)

    while stack_a or stack_b:

        ptr_a = None if not stack_a else stack_a.pop()
        ptr_b = None if not stack_b else stack_b.pop()

        next_output_digit, carry = sum_nodes(ptr_a, ptr_b, carry)
        output.push(next_output_digit)

    if carry > 0:
        output.push(carry)
    return output


def list_to_stack(ptr_a, stack_a):
    while ptr_a:
        stack_a.append(ptr_a)
        ptr_a = ptr_a.next
