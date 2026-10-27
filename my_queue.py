class Queue():
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if len(self.data) == 0: raise IndexError
        item = self.data[0]
        del self.data[0]
        return item

    def front(self):
        if len(self.data) == 0: raise IndexError
        return self.data[0]

    def size(self):
        return len(self.data)
