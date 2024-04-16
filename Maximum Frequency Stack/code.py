from collections import deque

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.deq = {}
        self.stack1 = deque()

    def push(self, val: int) -> None:
        self.stack1.append(val)
        self.freq[val] = self.freq.get(val, 0) + 1
        if self.freq[val] in self.deq:
            self.deq[self.freq[val]].append(val)
        else:
            self.deq[self.freq[val]] = deque([val])

    def pop(self) -> int:
        max_freq = max(self.freq.values())
        val = self.deq[max_freq].pop()
        if not self.deq[max_freq]:
            del self.deq[max_freq]
        self.freq[val] -= 1
        if not self.freq[val]:
            del self.freq[val]
        return val
