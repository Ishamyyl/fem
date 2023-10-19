from typing import Any
from collections import UserList


class MinHeap(UserList):
    def _sift_up(self, idx: int):
        iv = self[idx]
        lidx = 2 * idx + 1
        while lidx < len(self):
            ridx = lidx + 1
            if ridx < len(self) and not self[lidx] < self[ridx]:
                lidx = ridx
            self[idx] = self[lidx]
            idx = lidx
            lidx = 2 * idx + 1
        self[idx] = iv
        self._sift_down(idx)

    def _sift_down(self, cidx: int):
        # set the recent value aside
        # pull down parents if they're bigger than that value
        # if not, slot the recent value in
        cv = self[cidx]
        while cidx > 0:  # find a spot for cv
            pidx = (cidx - 1) >> 1
            pv = self[pidx]
            if cv >= pv:  # if current value is greater than or equal to parent value
                break  # then stop checking (heap invariant is met)
            self[cidx] = pv  # otherwise, set current value to parent, bubbling up
            cidx = pidx  # then check the parent
        self[cidx] = cv  # update parent, finishing the bubble up

    def insert(self, value: Any):
        self.append(value)
        self._sift_down(len(self) - 1)

    def delete(self) -> Any:
        r = self.pop()
        if len(self) == 0:
            return r
        i, self[0] = self[0], r
        self._sift_up(0)
        return i


if __name__ == "__main__":
    h = MinHeap()
    h.insert(1)
    h.insert(3)
    h.insert(2)
    h.insert(4)
    h.insert(0)
    print(h)
    from random import sample

    # l = 50
    # for i in sample(range(1, l + 1), l):
    #     h.insert(i)
    # for _ in range(l):
    #     print(h.delete())
