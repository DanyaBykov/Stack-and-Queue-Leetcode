class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def is_empty(self):
        return self.size == 0

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        
    def push(self, x: int) -> None:
        self.queue1.enqueue(x)

    def pop(self) -> int:
        while self.queue1.size > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        value = self.queue1.dequeue()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return value

    def top(self) -> int:
        while self.queue1.size > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        value = self.queue1.peek()
        self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return value

    def empty(self) -> bool:
        return self.queue1.is_empty() and self.queue2.is_empty()
