from chapter_2.linked_list import LinkedList


# Todo: Redo this because it is return, not remove kth from last


def remove_kth_from_last(linked_list: LinkedList, index_to_remove: int) -> None:
    runner = current = linked_list.head

    index = 0
    while runner and index < index_to_remove:
        runner = runner.next
        index += 1

    if not runner:
        raise Exception("List is not long enough")

    while runner:
        runner = runner.next
        current = current.next

    return current.value
