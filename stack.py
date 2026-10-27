class Stack():
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) == 0: raise IndexError
        item = self.data[-1]
        del self.data[-1]
        return item

    def peek(self):
        if len(self.data) == 0: raise IndexError
        return self.data[-1]

    def size(self):
        return len(self.data)
