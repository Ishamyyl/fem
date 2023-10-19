def hoare_quicksort(arr: list):
    def _quicksort(lo, hi):
        if lo < hi:
            p = _partition(lo, hi)
            _quicksort(lo, p)
            _quicksort(p + 1, hi)

    def _partition(lo, hi):
        p = arr[(hi - lo) // 2 + lo]
        while True:
            while arr[lo] < p:
                lo += 1
            while arr[hi] > p:
                hi -= 1
            if lo >= hi:
                return hi
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1

    _quicksort(0, len(arr) - 1)
    return arr


def hoare_partition(arr: list, lo: int, hi: int) -> int:
    pivot = arr[(hi - lo) // 2 + lo]
    while True:
        while arr[lo] < pivot:
            lo += 1
        while arr[hi] > pivot:
            hi -= 1
        if lo >= hi:
            return hi
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1


def hoare_qs(arr: list, lo: int, hi: int):
    if lo >= 0 and hi >= 0 and lo < hi:
        pivot = hoare_partition(arr, lo, hi)
        hoare_qs(arr, lo, pivot)
        hoare_qs(arr, pivot + 1, hi)


def qs(arr: list, lo: int, hi: int):
    if lo >= hi:
        return
    pivot_index = partition(arr, lo, hi)
    qs(arr, lo, pivot_index - 1)
    qs(arr, pivot_index + 1, hi)


def partition(arr: list, lo: int, hi: int) -> int:
    pivot = arr[hi]
    idx = lo - 1
    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    return idx


def quick_sort(arr: list):
    hoare_quicksort(arr)


if __name__ == "__main__":
    arr = [9, 3, 7, 4, 69, 420, 42]
    print(arr)
    quick_sort(arr)
    print(arr)
