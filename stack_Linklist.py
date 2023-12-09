class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

def merge_sorted_lists(list1, list2):
    merged_list = Stack()
    while list1 is not None or list2 is not None:
        if list1 is None:
            merged_list.push(list2.data)
            list2 = list2.next
        elif list2 is None:
            merged_list.push(list1.data)
            list1 = list1.next
        elif list1.data < list2.data:
            merged_list.push(list1.data)
            list1 = list1.next
        else:
            merged_list.push(list2.data)
            list2 = list2.next

    # Reverse the stack to get the correct order
    reversed_stack = Stack()
    while not merged_list.is_empty():
        reversed_stack.push(merged_list.pop())

    return reversed_stack.top

# Example usage
list1 = Stack()
list1.push(4)
list1.push(2)
list1.push(1)

list2 = Stack()
list2.push(4)
list2.push(3)
list2.push(1)

print("List 1:")
list1.print_stack()

print("List 2:")
list2.print_stack()

merged_head = merge_sorted_lists(list1.top, list2.top)

print("Merged List:")
current_node = merged_head
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")
