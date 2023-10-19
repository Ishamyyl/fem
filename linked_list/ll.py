from collections.abc import Generator
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class Node:
    val: Any
    next: Optional["Node"] = None
    prev: Optional["Node"] = None

    def __str__(self):
        return f"Node<{self.val}>"

    def __repr__(self):
        return str(self)


@dataclass
class LinkedList:
    length = 0
    head: Optional[Node] = None
    tail: Optional[Node] = None

    def __str__(self):
        return f"LinkedList<[{self.length}] {[n for n in self]}>"

    def __repr__(self):
        return str(self)

    def __iter_nodes__(self) -> Generator[Node, None, None]:
        h = self.head
        while h:
            yield h
            h = h.next

    def __iter__(self) -> Generator[Any, None, None]:
        return (n.val for n in self.__iter_nodes__())

    def push(self, v: Any):
        n = Node(v)
        if not self.head:
            self.head = n
        if self.tail:
            self.tail.next = n
            n.prev = self.tail
        self.tail = n
        self.length += 1

    def pop(self) -> Optional[Any]:
        if self.tail:
            r = self.tail.val
            if self.tail.prev:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return r

    def push_front(self, v: Any):
        n = Node(v)
        if not self.tail:
            t = n
        if self.head:
            self.head.prev = n
            n.next = self.head
        self.head = n
        self.length += 1

    def pop_front(self) -> Optional[Any]:
        if self.head:
            r = self.head
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            r.next = None
            return r.val

    def _get_node(self, i: int) -> Optional[Node]:
        for index, node in enumerate(self.__iter_nodes__()):
            if i == index:
                return node

    def get(self, i: int) -> Optional[Any]:
        if r := self._get_node(i):
            return r.val

    def insert(self, v: Any, i: int):
        if i >= self.length:
            return self.push(v)
        if i <= 0:
            return self.push_front(v)
        n = Node(v)
        if p := self._get_node(i - 1):
            if p.next:
                n.next = p.next
                n.prev = p
                p.next.prev = n
                p.next = n
                self.length += 1

    def set(self, v: Any, i: int):
        if p := self._get_node(i):
            p.val = v

    def delete(self, i: int) -> Optional[Any]:
        if i >= self.length:
            return self.pop()
        if i <= 0:
            return self.pop_front()
        if n := self._get_node(i):
            if n.next and n.prev:
                n.prev.next = n.next
                n.next.prev = n.prev
            self.length -= 1
            return n.val


if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    ll.push(1)
    print(ll)
    ll.push(2)
    print(ll)
    ll.push_front(0)
    print(ll)
    ll.push(3)
    print(ll)
    ll.push_front(3)
    print(ll)
    ll.push(0)
    print(ll)
    ll.insert(4, 2)
    print(ll)
    print(ll.pop_front())
    print(ll)
    ll.insert(5, 0)
    print(ll)
    ll.insert(6, 100)
    print(ll)
    ll.insert(7, 1)
    print(ll)
    print(ll.get(ll.length - 1))
    print(ll.get(0))
    print(ll.get(4))
    ll.set(8, 4)
    print(ll.get(4))
    print(ll)
    ll.delete(4)
    print(ll)
    for n in ll:
        print(n)
