import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <img src="public/module.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Modules
    * Modules are files of Python code (functions, classes, etc.) with names that end in ".py"
    * Modules are a great mechanism for code re-use
    * To use a module, you must `import` it:
    """
    )
    return


app._unparsable_cell(
    r"""
    # Assume we want to use the cos function from the math module (within Python Standard Library)
    import math
    print(f\"The cosine of pi is: {math.cos(math.pi)}\")

    # Renaming the module name
    import math as m
    print(f\"Euler's constant e has the following value: {m.e}\")

    # We can also proceed as follows (rather dangerous)
    from math import sin, pi
    print(f\"The sine of pi/4 is: {sin(pi / 4)}\")

    # And almost never do this:
    from math import *
    """,
    name="_",
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Where does Python find the modules my code imports?
    * `sys.path`, a list of directories that are searched for modules
    * This path is defined when Python installed, and is augmented by the `PYTHONPATH` environment variable
    """
    )
    return


@app.cell
def _():
    import sys

    for directory in sys.path:
        print(directory)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## The Python Standard Library
    * Extensive collection of modules that is installed with Python
    * Most commonly used:
        * `sys`, especially `sys.argv` (the list of command-line arguments)
        * `os`, especially `os.path` (tools for manipulating file names)
        * `time` (tools for getting and formatting the system time)
        * `math`
        * `string`
        * `random`
    * Documented here: https://docs.python.org/3/library/index.html
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    If that isn't overwhelming enough, take a look at the [Python Package Index](https://pypi.org/).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## What modules are available on my system?
    ```python
    help("modules")
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Module or script?
    * Is a .py file a module that I import or a script that I run? *It can be both!*
    * Common practice: include test code in your modules, such that
      * if the file is executed as a script, the test code will run
      * if the file is imported, the test code will not run
    * Has file been executed as script or imported as a module? *The `__name__` variable will tell you.*
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ```python
    # Example module code

    # Imports go here

    # Function definitions
    # Maybe some class or variable definitions

    if __name__ == "__main__":
        # This .py file is getting executed as a script, not imported as a module
        execute_test_code_here()
    ```
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
