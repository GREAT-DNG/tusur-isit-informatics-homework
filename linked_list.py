# pyright: reportOptionalMemberAccess=false

class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None

    def append(self, data):
        node = LinkedList.Node(data)
        if not self.head:
            self.head = node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node

    def prepend(self, data):
        self.head = LinkedList.Node(data, next=self.head)
    
    def delete(self, data):
        if self.head:
            pointer = self.head
            if pointer.data == data:
                self.head = pointer.next
            while pointer.next:
                if pointer.next.data == data:
                    pointer.next = pointer.next.next
                    break
                pointer = pointer.next

    def to_list(self):
        result = []
        if self.head:
            pointer = self.head
            while pointer.next:
                result.append(pointer.data)
                pointer = pointer.next
            result.append(pointer.data)
        return result
