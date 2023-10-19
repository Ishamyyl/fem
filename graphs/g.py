from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any, Optional
from collections import deque
from array import array
from heapq import heappop, heappush
from math import inf


@dataclass(frozen=True)
class Edge:
    to: int = field(compare=False)
    weight: int = field(hash=False)


Node = list[Edge]
AdjList = list[Node]


##########
#    <1-
# (0)-1>(1)
#  | \
#  4  5
#  v   >
# (2)-2> (3)-5>(4)
##########

al: AdjList = [
    [Edge(1, 1), Edge(2, 4), Edge(3, 5)],
    [Edge(0, 1)],
    [Edge(3, 2)],
    [Edge(4, 5)],
    [],
]

vs = [2, 5, 3, 4, 1]


def dijkstras_walk(idx: int, start: int = 0) -> int | float:
    dists = [inf] * len(al)
    dists[start] = 0
    if not al[start]:
        return 0
    q = [(0, start)]

    while q:
        d, cur = heappop(q)
        if d > dists[cur]:
            continue
        for e in al[cur]:
            dist = d + e.weight
            if dist < dists[e.to]:
                dists[e.to] = dist
                heappush(q, (d, e.to))
    return dists[idx]


def dfs_rec(v: Any) -> Optional[Sequence[int]]:
    start = 0
    seen = array("B", (False for _ in range(len(al))))
    path: Sequence[int] = deque()

    def walk(cur: int) -> bool:
        if seen[cur]:  # base case
            return False
        seen[cur] = True  # pre-order work
        path.append(cur)  # pre-order work
        if vs[cur] == v:  # base case
            return True
        for e in al[cur]:  # recurse
            if walk(e.to):
                return True  # handle base case
        path.pop()  # post-order work
        return False  # handle default base case

    walk(0)
    return path


def dfs(v: Any) -> Optional[list[int]]:
    start = 0
    seen = array("B", (False for _ in range(len(al))))
    prev = array("b", (-1 for _ in range(len(al))))
    seen[start] = True
    q = deque()
    q.append(start)
    cur = start
    while len(q):
        cur = q.popleft()
        if vs[cur] == v:
            break
        for e in al[cur]:
            if seen[e.to]:
                continue
            seen[e.to] = True
            prev[e.to] = cur
            q.append(e.to)
    if prev[cur] == -1:
        return None
    out = []
    while prev[cur] != -1:
        out.append(cur)
        cur = prev[cur]
    out.append(start)
    out.reverse()
    return out


if __name__ == "__main__":
    print(dijkstras_walk(4))
