# @main

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-main)](https://pypi.org/project/python-main/)
[![PyPI - Version](https://img.shields.io/pypi/v/python-main)](https://pypi.org/project/python-main/)


`@main` decorator which runs the tagged function if the current module is being executed as a script.

No more `if __name__ == "__main__":` all over the place.

That's it!

### Installation

```bash
pip install python-main # or
poetry add python-main # ...
```

### Usage

```python
from python_main import main

A = 10
B = 20


@main
def do_print():
    """This will run if this module is executed."""
    print(A + B)
```
