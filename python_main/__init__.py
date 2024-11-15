import builtins
import inspect
from typing import Callable, Optional


def main(f: Callable[[], Optional[int]]) -> None:
    curr_frame = inspect.currentframe()
    assert curr_frame is not None
    assert curr_frame.f_back is not None

    upper_frame = curr_frame.f_back
    if upper_frame.f_locals["__name__"] == "__main__":
        builtins.exit(f() or 0)
