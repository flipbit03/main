import builtins

import pytest

from python_main import python_main

EXIT_CODE_RECEIVED = -1


@pytest.fixture
def mock_exit():
    global EXIT_CODE_RECEIVED
    original_exit = builtins.exit

    def mock_exit(code):
        global EXIT_CODE_RECEIVED
        EXIT_CODE_RECEIVED = code

    # Apply Mock
    builtins.exit = mock_exit

    yield

    # Clean up
    builtins.exit = original_exit
    EXIT_CODE_RECEIVED = -1


def __my_main_func():
    """
    The answer to life, the universe, and everything.
    """
    builtins.exit(42)


def test_assert_function_actually_gets_called(mock_exit):
    """
    Assert that the @main decorator actually calls the function if the module is being run as a script.
    """

    # We patch my_main_func's __module__ here so that we can emulate that it comes from a module which
    # is being run as a script/
    __my_main_func_original_module = __my_main_func.__module__
    __my_main_func.__module__ = "__main__"

    # Decorate it
    python_main(__my_main_func)

    # Ensure that our main function was able to call mock_exit with the expected value.
    global EXIT_CODE_RECEIVED
    assert EXIT_CODE_RECEIVED == 42

    # Restore
    __my_main_func.__module__ = __my_main_func_original_module


def test_assert_function_does_not_get_called(mock_exit):
    """
    Assert that our decorated function does not get called in normal circumstances
    """

    # Call the function, which is coming from a pytest execution and being imported as a module
    function_returned = python_main(__my_main_func)

    # Exit code will not have been set.
    global EXIT_CODE_RECEIVED
    assert EXIT_CODE_RECEIVED == -1
    assert function_returned == __my_main_func
