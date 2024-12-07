# @python_main

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-main)](https://pypi.org/project/python-main/)
[![PyPI - Version](https://img.shields.io/pypi/v/python-main)](https://pypi.org/project/python-main/)


`@python_main` is a decorator which:
- Automatically calls the function(s) tagged with it, if the current module is being **executed as a script**.
- Does nothing if the current module is being **imported**.

It is, essentially, equivalent to the `if __name__ == "__main__":` construct, but as a decorator.

That's all it does.

### Installation

```bash
pip install python-main # or
poetry add python-main # ...
```

### Usage

```python
from python_main import python_main

A = 10
B = 20

@python_main
def do_print():
    """This will run if this module is executed."""
    print(A + B)
```

You can also tag multiple functions with `@python_main` and they will all run if the module is executed, in the order they are defined.

```python
from python_main import python_main

A = 10
B = 20
C = 0

@python_main
def add_a_to_c():
    global C
    C += A

# ... other functions/ definitions ...

@python_main
def add_b_to_c():
    global C
    C += B

# At this point:
# - C will be 30 if this module is executed as a script.
# - C will be untouched if this module is imported.
```
