from data_structures.linked_lists.linked_list import Node


def remove_middle_node(node: Node) -> None:
    """
        Function to remove a node from a linked list having only access to that node.
        We further now that this node isn't the head or the tail of the list, hence the "middle" part

        While at first this seems hard to do with only access to the node, by knowing that it isn't
        the head or the tail of the list means that 'node.next' will point to a valid node.
        So we can simply copy the data from node.next into node and then make node.next point to node.next.next
        This way, we have in effect replaced node with the next node.

        We don't need to return anything because the head of the list won't be modified as the node is not the head :)

        Note: This wouldn't work for the tail node

    :param node: node to be removed
    """

    node.value = node.next.value
    node.next = node.next.next