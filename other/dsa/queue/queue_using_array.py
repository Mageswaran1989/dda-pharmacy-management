

class Queue(object):
    """

      | | | | | | | | |
     Rear           Front
    Enqueue          Dequeue
    """
    def __init__(self, N):
        self._array = [None] * N
        self.N = N
        self.f = 0
        self.r = 0

    def size(self):   # O(1)
        """

        5 - 3 -
        :return:
        """
        return (self.N - self.f + self.r) % self.N  # modulus for circular array

    def is_empty(self):   # O(1)
        return self.f == self.r

    def enqueue(self, o):  # O(1)
        if self.size() == self.N - 1:
            raise RuntimeError("Queue full")
        self._array[self.r] = o
        self.r = (self.r + 1) % self.N

    def dequeue(self):   # O(1)
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        element = self._array[self.f]
        self._array[self.f] = None
        self.f = (self.f + 1) % self.N
        return element