class Stack(object):
    """
    LIFO
    Used in:
        - Procedure calls
        - Recursion
    """
    def __init__(self, N):  # Needs the number of elements upfront which can be an issue to set
        self._data = [None] * N   # There is an upper bound, N, on the size of the stack.
        self.N = N #
        self.t = -1  # top position pointer

    def size(self):
        return self.t + 1

    def is_empty(self):
        return self.t < 0

    def push(self, element):  # O(1)
        """
        Insert element at the top of the stack i.e end of the array
        Args:
            element: element to be inserted

        Returns:

        """
        if self.size() == self.N:
            raise RuntimeError("Stack is full")
        self.t = self.t + 1
        self._data[self.t] = element

    def pop(self):  # O(1)
        """
        Remove from the stack and return the top object on the stack. Error occurs for empty stack.

        Returns: element
        """
        if self.is_empty():
            raise RuntimeError("Stack empty")
        element = self._data[self.t]
        self._data[self.t] = None
        self.t = self.t - 1
        return element

    def top(self):
        """
        Return value of top object on the stack. Error occurs for empty stack.
        """
        if self.is_empty():
            raise RuntimeError("Stack empty")
        return self._data[self.t]

    def __str__(self):
        return str(self._data)


if __name__ == "__main__":
    stack = Stack(5)
    try:
        stack.pop()
    except Exception as e:
        print("Stack is empty")
    stack.push(1)
    print(stack)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    try:
        stack.push(6)
    except Exception as e:
        print("Stack is full")

    print(f"Pop 5th element: {stack.pop()}")
    print(f"Pop 4th element: {stack.pop()}")
    print(f"Pop 3rd element: {stack.pop()}")
    print(f"Pop 2nd element: {stack.pop()}")
    print(f"Pop 1st element: {stack.pop()}")
    print(stack)

    try:
        print(f"Pop 1st element: {stack.pop()}")
    except Exception as e:
        print("no more elements to pop")


