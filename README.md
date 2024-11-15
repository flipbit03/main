# @main

`@main` decorator which runs the tagged function if the current module is being run.

No more `if __name__ == "__main__":` all over the place.

That's it!

### Usage

```python
from python_main import main

A = 10
B = 20


@main
def do_print():
    """This will run if this module is called directly."""
    print(A + B)
```
