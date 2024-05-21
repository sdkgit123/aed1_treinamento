def print_stack(stack):
    temp_stack = []
    while stack:
        temp_stack.append(stack.pop())
    while temp_stack:
        print(temp_stack.pop(0))


my_stack = [1, 2, 3, 4, 5]
print_stack(my_stack)
