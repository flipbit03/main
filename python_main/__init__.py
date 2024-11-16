import builtins
from typing import Callable, Optional


def main(f: Callable[[], Optional[int]]) -> None:
    if f.__module__ == "__main__":
        f()
    return f