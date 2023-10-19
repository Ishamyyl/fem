from collections import deque
from typing import Generic, Optional, TypeVar
from dataclasses import dataclass

K = TypeVar("K")
V = TypeVar("V")


@dataclass(slots=True)
class Node(Generic[K, V]):
    value: V
    key: K
    prev: "Node[K, V]"
    next: "Node[K, V]"


class LRU(Generic[K, V]):
    cache: dict[K, Node[K, V]]
    lru: list
    root: Node

    def __init__(self):
        self.lru = []
        self.cache = {}
        self.root = Node(None, None, None, None)

    def __len__(self):
        return len(self.cache)

    def __getitem__(self, key: K) -> Optional[V]:
        node = self.cache.get(key)
        if node is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            p = self.root.prev
        return node.value

    def __setitem__(self, key: K, value: V):
        node = self.cache.get(key)
        if node is None:
            node = value

        return None


if __name__ == "__main__":
    a = LRU()
