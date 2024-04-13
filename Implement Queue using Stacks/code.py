class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def empty(self):
        return self.head is None

class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())
        self.stack1.push(x)

    def pop(self) -> int:
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.empty() and self.stack2.empty()
