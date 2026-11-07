class Deque:
    def __init__(self):
        self.data = [None] * 4
        self.head = 0
        self.length = 0

    @property
    def capacity(self):
        return len(self.data)

    def increase(self):
        new = [None] * (len(self.data) * 2)

        for i in range(self.length):
            new[i] = self.data[(self.head + i) % len(self.data)]

        self.data = new
        self.head = 0

    def push_back(self, item):
        if self.length == len(self.data): self.increase()

        self.data[(self.head + self.length) % len(self.data)] = item
        self.length += 1
    
    def push_front(self, item):
        if self.length == len(self.data): self.increase()

        self.head = (self.head - 1) % len(self.data)
        self.data[self.head] = item
        self.length += 1

    def pop_back(self):
        if self.length == 0: raise IndexError()

        index = (self.head + self.length - 1) % len(self.data)
        item = self.data[index]
        self.data[index] = None
        self.length -= 1
        
        return item

    def pop_front(self):
        if self.length == 0: raise IndexError()

        item = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.length -= 1
        
        return item

    def back(self):
        if self.length == 0: raise IndexError()
        return self.data[(self.head + self.length - 1) % len(self.data)]

    def front(self):
        if self.length == 0: raise IndexError()
        return self.data[self.head]

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0
