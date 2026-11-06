class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = [None] * 4

    @property
    def capacity(self):
        return len(self.data)

    def append(self, item):
        if self.length + 1 > len(self.data): 
            self.data += [None] * len(self.data)
        self.data[self.length] = item
        self.length += 1
        
    def pop(self):
        if self.length == 0: raise IndexError
        self.length -= 1
        return self.data[self.length]

    def __getitem__(self, index):
        if index < 0 or index >= self.length: raise IndexError
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length: raise IndexError
        self.data[index] = value

    def __len__(self):
        return self.length
