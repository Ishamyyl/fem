from typing import TypeVar
from collections.abc import Sequence

# TODO: use Protocol for operators __eq__, __lt__, ==, <, etc.
T = TypeVar("T", int, str, float)


##
# Invariant: `arr` must be sorted
##
def binary_search_while(arr: Sequence[T], n: T) -> bool:
    lo = 0
    hi = len(arr)

    while lo < hi:
        m = lo + (hi - lo) // 2
        v = arr[m]

        if v == n:
            return True
        if v > n:
            hi = m
        else:
            lo = m + 1
    return False


##
# Invariant: `arr` must be sorted
##
def binary_search_rec(arr: Sequence[T], n: T) -> bool:
    lo = 0
    hi = len(arr)

    if lo < hi:
        m = lo + (hi - lo) // 2
        v = arr[m]

        if v == n:
            return True
        if v > n:
            return binary_search_rec(arr[:m], n)
        else:
            return binary_search_rec(arr[m + 1 :], n)
    return False


if __name__ == "__main__":
    n = [1, 3, 6, 89, 123, 1112, 4444, 4445, 4446, 4447, 5555, 12345, 112345]
    c = n + [4448, 12346, 4443, 0, 112346]
    for i in c:
        print(i, binary_search_while(n, i))
    for i in c:
        print(i, binary_search_rec(n, i))
