# pyright: reportOptionalMemberAccess=false

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data, prev=self.tail)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def prepend(self, data):
        node = Node(data, next=self.head)
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
    
    def delete(self, data):
        if self.head:
            pointer = self.head
            if pointer.data == data:
                if self.head.next:
                    self.head.next.prev = None
                    self.head = pointer.next
                else:
                    self.head = None
                    self.tail = None
                return
            while pointer.next:
                if pointer.data == data:
                    pointer.next.prev, pointer.prev.next = pointer.prev, pointer.next
                    return
                pointer = pointer.next
            if pointer.data == data:
                if self.tail.prev:
                    self.tail.prev.next = None
                    self.tail = pointer.prev
                else:
                    self.tail = None

    def to_list(self):
        result = []
        if self.head:
            pointer = self.head
            while pointer.next:
                result.append(pointer.data)
                pointer = pointer.next
            result.append(pointer.data)
        return result

    def to_list_reverse(self):
        result = []
        if self.tail:
            pointer = self.tail
            while pointer.prev:
                result.append(pointer.data)
                pointer = pointer.prev
            result.append(pointer.data)
        return result
