class Ring_buffer:
    """
    Class Ring-buffer
    """

    def __init__(self, size):
        """
        :param size: Size of Ring-buffer
        """
        self.size = size
        self.buffer = [None] * size
        self.write_index = 0
        self.read_index = 0
        self.is_overloading = False

    def _next_(self, index):
        if index < self.size - 1:
            index += 1
        else:
            index = 0
        return index

    def add(self, value):
        """
        :param value: Adding the value
        :return: void
        """
        self.buffer[self.write_index] = value
        next_index = self._next_(self.write_index)
        self.write_index = next_index
        if self.buffer[next_index] is not None:
            self.read_index = self.write_index
            self.is_overloading = True

    def read(self):
        """
        :return: The value of ring-buffer. After reading the value is removed.
        """
        result = self.buffer[self.read_index]
        self.buffer[self.read_index] = None
        self.is_overloading = False
        self.read_index = self._next_(self.read_index)
        return result


import collections


class Ring_buffer2:
    """
    Class Ring-buffer. Use collection library
    """

    def __init__(self, buffer_size):
        """
        :param buffer_size: Size of buffer
        """
        self.buffer = collections.deque(maxlen=buffer_size)

    def add(self, value):
        """
        :param value: Adding value
        :return: void
        """
        self.buffer.append(value)
