class Node(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next

class SingleLinkedList(object):
    """
        Not easy to delete the tail node  /Insertbefore operations
        Start from the head of the list and search all the way through the list.
        Such link hopping operations could take a long time.
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):  # O(1) if we store the size otherwise O(n)
        return self._size

    def first(self):
        pass

    def last(self):  # O(1) if we store the last ptr
        pass

    def after(self, node):  # O(1) if we store the last ptr
        """ what is there after the node"""
        pass

    def before(self, node, element):  # O(n)
        pass

    def replace_element(self, node, element):
        node.element = element

    def swap(self, this, that):
        temp = this.element
        this.element = that.element
        that.element = temp

    def insert_at_head(self, element):  # O(1) if we store the last ptr
        node = Node(element=element, next=self._head)
        self._head = node
        if self._tail is None:
            self._tail = node

    def insert_at_tail(self, element):  # O(1) if we store the last ptr
        pass

    def insert_after(self, n, o):  # O(1) if we store the last ptr
        pass

    def insert_before(self, n, o):  # O(1) if we store the last ptr
        pass

    def remove(self, node):  # O(n) if we store the last ptr
        pass


class DNode(object):
    def __init__(self, prev, element, next):
        self.prev = prev
        self.element = element
        self.next = next


class DoubleLinkedList(object):
    def __init__(self):
        self._head: DNode = None
        self._tail: DNode = None
        self._size = 0

    def size(self):  # O(1) if we store the size otherwise O(n)
        return self._size

    def remove_last(self):
        """

        ||1|| -> ||2|| -> ||3||
        :return:
        """
        if self.size() == 0:
            raise RuntimeError("List empty")

        last_previous = self._tail.prev
        last_last_previous = last_previous.prev

        las