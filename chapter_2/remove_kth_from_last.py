from chapter_2.linked_list import LinkedList


def remove_kth_from_last(linked_list: LinkedList, index_to_remove: int) -> None:
    fast = slow = linked_list.head
    for _ in range(0, index_to_remove + 1):
        if not fast:
            raise Exception("List to small")
        fast = fast.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
