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

def evaluate_rpn(tokens):
    stack = Stack()
    for i in tokens:
        if i == "+": stack.push(stack.pop() + stack.pop())
        elif i == "-": 
            a, b = stack.pop(), stack.pop()
            stack.push(b - a)
        elif i == "*": stack.push(stack.pop() * stack.pop())
        elif i == "/":
            a, b = stack.pop(), stack.pop()
            stack.push(b / a)
        else: stack.push(i)
    return stack.pop()
