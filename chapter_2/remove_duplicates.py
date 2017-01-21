from chapter_2.linked_list import LinkedList, Node


def remove_duplicates(linked_list: LinkedList) -> LinkedList:
    unique_elements = set()
    ptr = linked_list.head

    while ptr:
        unique_elements.add(ptr.value)
        ptr = ptr.next

    return LinkedList.build([element for element in unique_elements])


def remove_duplicates_inplace(linked_list: LinkedList) -> LinkedList:
    ptr = linked_list.head  # type: Node
    search_ahead = ptr
    while ptr:
        while search_ahead.next is not None:
            if search_ahead.next.value == ptr.value:
                search_ahead.next = search_ahead.next.next
            else:
                search_ahead = search_ahead.next

        ptr = ptr.next
        search_ahead = ptr

    return linked_list
