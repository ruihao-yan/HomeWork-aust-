class queue:
    # queue is LILO
    def __init__(self):
        self.list = []

    def add(self, val):
        self.list.append(val)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop(0)


