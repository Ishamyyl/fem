from dataclasses import dataclass
from typing import Any, Optional
from collections import deque


@dataclass
class Node:
    value: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __iter__(self):
        if self.left:
            yield self.left
        if self.right:
            yield self.right


@dataclass
class BinaryTree:
    root: Optional[Node] = None

    # breadth-first search
    def contains2(self, value: Any) -> bool:
        if not self.root:
            return False
        q = deque(self.root)
        while len(q):
            if node := q.popleft():
                if node.value == value:
                    return True
                for n in node:
                    q.append(n)
        return False

    def _post_order_walk(self, cur: Optional[Node], value: Any) -> bool:
        if not cur:
            return False
        if self._post_order_walk(cur.left, value):
            return True
        if self._post_order_walk(cur.right, value):
            return True
        if cur.value == value:
            return True
        return False

    def _in_order_walk(self, cur: Optional[Node], value: Any) -> bool:
        if not cur:
            return False
        if self._in_order_walk(cur.left, value):
            return True
        if cur.value == value:
            return True
        if self._in_order_walk(cur.right, value):
            return True
        return False

    def _pre_order_walk(self, cur: Optional[Node], value: Any) -> bool:
        if not cur:
            return False
        if cur.value == value:
            return True
        if self._pre_order_walk(cur.left, value):
            return True
        if self._pre_order_walk(cur.right, value):
            return True
        return False

    def __contains__(self, value: Any) -> bool:
        if not self.root:
            return False
        return self._pre_order_walk(self.root, value)

    def _compare(self, a: Optional[Node], b: Optional[Node]) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.value != b.value:
            return False
        return self._compare(a.left, b.left) and self._compare(a.right, b.right)

    def __eq__(self, other: "BinaryTree") -> bool:
        return self._compare(self.root, other.root)


if __name__ == "__main__":
    r = BinaryTree()
    r.root = Node(1)
    r.root.left = Node(2)
    r.root.right = Node(3)
    r.root.right.left = Node(4)
    o = BinaryTree()
    o.root = Node(1)
    o.root.left = Node(2)
    o.root.right = Node(3)
    o.root.right.left = Node(4)
    print(r == o)
    print(4 in r)
    # print(r.contains2(4))
