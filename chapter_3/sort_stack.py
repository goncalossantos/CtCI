from data_structures.stacks.stack import Stack


def sort_stack(stack: Stack) -> Stack:
    output = Stack()

    while not stack.is_empty():
        stack_value = stack.pop()
        if output.is_empty():
            output.push(stack_value)
        else:
            while not output.is_empty() and stack_value > output.peek():
                output_value = output.pop()
                stack.push(output_value)
            output.push(stack_value)
    return output
