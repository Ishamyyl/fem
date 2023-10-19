from array import array

# TODO: Impl `del rb[i]` and `rb.insert(i, v)`


class RingBuffer:
    def __init__(self, size: int = 32):
        self._cap = size
        self._head = 0
        self._tail = 0
        self._len = 0
        self._buf = array("I", [0] * self._cap)

    def __str__(self):
        return f"<RingBuffer ({self._len}|{self._cap}) {[n for n in self]} - {self._buf}>"

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self._len

    def __getitem__(self, i: int):
        if i < 0:
            offset = self._tail
            len_check = abs(i + 1)
        else:
            offset = self._head
            len_check = i
        if len_check >= self._len:
            raise IndexError("list index out of range")
        return self._buf[(offset + i) % self._cap]

    def __setitem__(self, i: int, v: int):
        if i < 0:
            offset = self._tail
            len_check = abs(i + 1)
        else:
            offset = self._head
            len_check = i
        if len_check >= self._len:
            raise IndexError("list index out of range")
        self._buf[(offset + i) % self._cap] = v

    def __iter__(self):
        for i in range(self._len):
            yield self._buf[(self._head + i) % self._cap]

    def _double_cap(self, scale=2):
        cap = scale * self._cap
        n = array("I", [0] * cap)
        for i, v in enumerate(self):
            n[i] = v
        del self._buf
        self._buf = n
        self._cap = cap
        self._head = 0
        self._tail = self._len

    def push(self, v: int):
        if self._len + 1 > self._cap:
            self._double_cap()
        self._len += 1
        self._buf[self._tail % self._cap] = v
        self._tail += 1

    def pop(self) -> int:
        self._tail -= 1
        self._len -= 1
        r = self._buf[self._tail % self._cap]
        return r

    def enqueue(self, v: int):
        if self._len + 1 > self._cap:
            self._double_cap()
        self._len += 1
        self._head -= 1
        self._buf[self._head % self._cap] = v

    def deque(self):
        self._len -= 1
        r = self._buf[self._head % self._cap]
        self._head += 1
        return r


if __name__ == "__main__":
    rb = RingBuffer(10)
    print(">", rb)
    rb.push(1)
    rb.push(2)
    rb.push(3)
    rb.push(4)
    print(">", rb)
    for i in rb:
        print(i)
    print("[-3]", rb[-3])
    print("pop", rb.pop())
    print(">", rb)
    print("[0 1 2]", rb[0], rb[1], rb[2])
    # print(rb[3])
    print("[-1 -2 -3]", rb[-1], rb[-2], rb[-3])
    rb.enqueue(9)
    rb.enqueue(10)
    print(rb)
    print(rb.deque())
    print(rb.deque())
    print(rb)
    rb.enqueue(11)
    rb.enqueue(12)
    rb.enqueue(13)
    print(rb)
    rb.deque()
    rb.deque()
    rb.deque()
    print(rb)
    rb.push(14)
    rb.push(15)
    rb.push(16)
    rb.push(17)
    rb.push(22)
    rb.push(23)
    rb.push(24)
    print(rb)
    for n in rb:
        print(n)
    del rb
    rb = RingBuffer()
    for i in range(40):
        rb.push(i)
    print(rb)
