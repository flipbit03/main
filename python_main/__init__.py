from typing import Callable, Optional

__RAN_AS_SCRIPT_MODULE = "__main__"
__CALLABLE_MODULE_PROP = "__module__"


def main(f: Callable[[], Optional[int]]) -> Callable:
    if getattr(f, __CALLABLE_MODULE_PROP) == __RAN_AS_SCRIPT_MODULE:
        f()
    return f
