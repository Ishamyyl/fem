from math import floor, sqrt
from itertools import islice, repeat, chain

##
# You're given two identical crystal balls, a task, and a warning.
#   Your task: determine the lowest floor of a tower from which the crystal balls will break when dropped.
#   Your warning: you only get these two crystal balls.
##
##
# You're given a list that contains a bunch of Falses followed by a bunch of Trues, a task, and a warning.
#   Your task: determine the index of the first True in the list.
#   Your warning: you can only get a True result from the list at most twice.
##


##
# The time-complexity of these functions are O(sqrt n).
# This is worse than a binary search of O(log n), but is better than linear time O(n) which is the naive solution.
# This solution arises from a jump-check-walkback algorithm,
#  where we jump through the list in intervals, walk back one jump if we determine we've gone too far,
#  then linear search from there.
# The optimal jump is `sqrt n` - idea being we can eliminate `n` from O(M + n/M) when M is `sqrt n`
#  O(sqrt n + n / sqrt n) -> O(sqrt n + sqrt n) -> O(2 * sqrt n) -> O(sqrt n)
##


def two_crystal_balls2(breaks, floors):
    jump = floor(sqrt(floors))
    i = 0
    if jump > 1:
        for i in range(jump, floors, jump):
            if breaks[i]:
                break
        i -= jump
    for i in range(i, floors):
        if breaks[i]:
            return i
    return -1


def two_crystal_balls(breaks, floors) -> int:
    jump = floor(sqrt(floors))
    i = 0
    if jump > 1:
        for j in islice(breaks, jump, None, jump):
            i += 1
            if j:
                break
    if i:
        i = (i - 1) * jump
    for j in islice(breaks, i, None):
        i += 1
        if j:
            return i
    return -1


def jump_search_istep(arr, e):
    jump = floor(sqrt(len(arr)))
    current = 0
    if jump > 1:
        for j in islice(arr, None, None, jump):
            if j > e:  # if we've gone too far
                break  # then stop
            current += jump
        current -= jump  # back up 1 jump since we've gone too far
    for j in islice(arr, current, None):  # then linear search
        if j == e:
            return current
        current += 1


# Creates a list of `break_floor` Falses followed by Trues up to `floors`
def tower_drop(floors: int, break_floor: int):
    break_floor -= 1
    tower = list(chain(repeat(False, break_floor), repeat(True, floors - break_floor)))
    result = two_crystal_balls2(tower, floors)
    return result


if __name__ == "__main__":
    ps = [
        (1000, 780),
        (1000, 1000),
        (1000, 1),
        (2, 1),
        (1, 1),
        (10000, 4234),
        (1000, 999),
        (10000, 100000),
        (9999, 1000000),
        (99999, 99999),
        (1, 100000000),
        (100000000, 1),
    ]
    for t, f in ps:
        print(t, f, tower_drop(t, f))
