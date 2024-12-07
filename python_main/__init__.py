from typing import Callable, TypeVar

__RAN_AS_SCRIPT_MODULE = "__main__"
__CALLABLE_MODULE_PROP = "__module__"

__MAIN_RETURN_TYPE = TypeVar("__MAIN_RETURN_TYPE")


def python_main(
    main_function_to_be_called: Callable[[], __MAIN_RETURN_TYPE]
) -> Callable[[], __MAIN_RETURN_TYPE]:
    if (
        getattr(main_function_to_be_called, __CALLABLE_MODULE_PROP)
        == __RAN_AS_SCRIPT_MODULE
    ):
        main_function_to_be_called()
    return main_function_to_be_called


# Only export the main function
__all__ = ["python_main"]
