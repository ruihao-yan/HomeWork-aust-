class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.tail = -1

    def add(self, value):
        if (self.tail + 1) % self.size == self.front:
            print("Queue is full!")
            return
        if self.front == -1:  # First element
            self.front = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value

    def poll(self):
        if self.front == -1:
            print("Queue is empty!")
            return None
        removed_value = self.queue[self.front]
        if self.front == self.tail:
            self.front = self.tail = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed_value
