class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, item, priority):
        self.data.append((priority, item))

    def get(self, remove = False):
        if len(self.data) == 0: raise IndexError
        min_element = self.data[0]
        for i in self.data:
            if i[0] < min_element[0]:
                min_element = i
        if remove: self.data.remove(min_element)
        return min_element[1]

    def pop(self):
        return self.get(True)

    def peek(self):
        return self.get()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0
