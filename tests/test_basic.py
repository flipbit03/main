import pytest

from python_main import main


class NotSet:
    pass


EXIT_CODE_RECEIVED = NotSet


@pytest.fixture
def mock_exit():
    import builtins

    original_exit = builtins.exit

    def mock_exit(code):
        global EXIT_CODE_RECEIVED
        EXIT_CODE_RECEIVED = code

    # Apply Mock
    builtins.exit = mock_exit

    yield

    # Clean up
    builtins.exit = original_exit
    EXIT_CODE_RECEIVED = NotSet


def test_assert_function_actually_gets_called(mock_exit):
    """
    Assert that the @main decorator actually calls the function if the module is being run as a script.
    """

    # We patch __name__ here because doing so via a proper pytest fixture would be _A Lot Of Work (TM)_, because
    # of the insane amount of stack manipulation that would be required to get the desired effect.
    # The "noqa" flag here is important, or else our pre-commit hooks (flake) will remove this assignment.
    __name__ = "__main__"  # noqa

    @main
    def my_main_func():
        """
        The answer to life, the universe, and everything.
        """
        builtins.exit(42)

    # Ensure that our main function was able to call mock_exit with the expected value.
    assert EXIT_CODE_RECEIVED == 42
