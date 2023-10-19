from collections.abc import Sequence
from typing import Any


def linear_search(arr: Sequence[Any], e: Any) -> bool:
    for i in arr:
        if e == i:
            return True
    return False
