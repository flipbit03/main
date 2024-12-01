from typing import Callable, TypeVar

__RAN_AS_SCRIPT_MODULE = "__main__"
__CALLABLE_MODULE_PROP = "__module__"

__MAIN_RETURN_TYPE = TypeVar("__MAIN_RETURN_TYPE")


def main(f: Callable[[], __MAIN_RETURN_TYPE]) -> Callable[[], __MAIN_RETURN_TYPE]:
    if getattr(f, __CALLABLE_MODULE_PROP) == __RAN_AS_SCRIPT_MODULE:
        f()
    return f


# Only export the main function
__all__ = ["main"]
