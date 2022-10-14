class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

    def __str__(self):
        return f"Node({self.element}, {self.next})"


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, element):
        if self.head is None:
            self.head = Node(element)
        else:
            new_node = Node(element)
            new_node.next = self.head
            print(new_node)
            self.head = new_node

    def pop(self):

        if self.isempty():
            raise RuntimeError("Stack is empty")
        else:
            headnode = self.head
            self.head = self.head.next
            headnode.next = None
            return headnode.element

    def peek(self):
        if self.isempty():
            raise RuntimeError("Stack is empty")
        else:
            return self.head.element

    def to_str(self):
        iterator = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while iterator is not None:
                print(iterator.element, "->", end=" ")
                iterator = iterator.next
            return


# Driver code
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    # print stack elements
    stack.to_str()

    # Print top element of stack
    print("\nTop element is ", stack.peek())

    # Delete top elements of stack
    stack.pop()
    stack.pop()

    # print stack elements
    stack.to_str()

    # Print top element of stack
    print("\nTop element is ", stack.peek())

# This code is contributed by Mathew George