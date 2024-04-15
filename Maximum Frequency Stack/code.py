from collections import deque

class FreqStack:

    def __init__(self):
        self.stack1 = deque()

    def push(self, val: int) -> None:
        self.stack1.append(val)

    def pop(self) -> int:
        max_val = None
        max_freq = 0
        self.stack1.reverse()
        for val in self.stack1:
            freq = self.stack1.count(val)
            if freq > max_freq:
                max_freq = freq
                max_val = val
            if freq == max_freq:
                if self.stack1.index(val) < self.stack1.index(max_val):
                    max_val = val
                    max_freq = freq
        self.stack1.remove(max_val)
        self.stack1.reverse()
        return max_val
