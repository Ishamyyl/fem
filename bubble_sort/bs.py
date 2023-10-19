from collections.abc import MutableSequence
from typing import TypeVar

# TODO: use Protocol for rich comparison operators, like __eq__ and >, etc
T = TypeVar("T", int, float, str)


##
# Perform in-place bubble sort, swapping whenever a bigger element is found.
# O(m * n^2)
##
def bubble_sort_swap(arr: MutableSequence[T]):
    l = len(arr)
    for i in range(l):
        for j in range(l - 1 - i):
            j1 = j + 1
            if arr[j] > arr[j1]:
                arr[j], arr[j1] = arr[j1], arr[j]


##
# Perform in-place bubble sort, swapping only once the index of the biggest element is known.
# O(k * n^2) where k < m from above
##
def bubble_sort_endswap(arr: MutableSequence[T]):
    for i in range(len(arr)):
        biggest_index = 0
        end = len(arr) - i - 1
        for j in range(end + 1):  # inclusive
            if arr[j] > arr[biggest_index]:
                biggest_index = j
        arr[biggest_index], arr[end] = arr[end], arr[biggest_index]


if __name__ == "__main__":
    n = [3, 6, 8, 1, 3, 78, 9, 4, 32]
    m = [*n]
    print(n)
    bubble_sort_swap(n)
    print(n)
    bubble_sort_endswap(m)
    print(m)
