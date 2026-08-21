import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/module.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Modules
    * Modules are files of Python code (functions, classes, etc.) with names that end in ".py"
    * Modules are a great mechanism for code re-use
    * To use a module, you must `import` it:
    """)
    return


app._unparsable_cell(
    r"""
    # Assume we want to use the cos function from the math module (within Python Standard Library)
    import math
    print(f\"The cosine of pi is: {math.cos(math.pi)}\")

    # Renaming the module locally to make it shorter and easier to type
    import math as m
    print(f\"Euler's constant e has the following value: {m.e}\")

    # We can also proceed as follows (possibly dangerous; can overwrite objects defined locally and lead to confusion)
    from math import sin, pi
    print(f\"The sine of pi/4 is: {sin(pi / 4)}\")

    # Almost never do this (import everything; it is possible to overwrite objects defined locally and it's unclear exactly what is being imported)
    from math import *
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Where does Python find the modules my code imports?
    * `sys.path`, a list of directories that are searched for modules
    * This path is defined when Python installed, and is augmented by the `PYTHONPATH` environment variable
    """)
    return


@app.cell
def _():
    import sys

    for directory in sys.path:
        print(directory)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Python Standard Library
    * Extensive collection of modules that is installed with Python
    * Most commonly used:
        * `sys`, especially `sys.argv` (the list of command-line arguments)
        * `os`, especially `os.path` (tools for manipulating file names)
        * `time` (tools for getting and formatting the system time)
        * `math`
        * `string`
        * `random`
    * The Standard Library is documented here: https://docs.python.org/3/library/index.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If that isn't overwhelming enough, take a look at the [Python Package Index](https://pypi.org/).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What modules are available on my system?
    """)
    return


@app.cell
def _():
    help("modules")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Module or script?
    * Is a .py file a module that I import or a script that I run? *It can be both!*
    * Common practice: include test code in your modules, such that
      * if the file is executed as a script, the test code will run
      * if the file is imported, the test code will not run
    * Has file been executed as script or imported as a module? *The `__name__` variable will tell you.*

    ```python
    def addition(n, m):
        return n + m


    if __name__ == "__main__":
        # This .py file is getting executed as a script, not imported as a module
        # Run tests or other statements that are unnecessary when imported as a module
        assert addition(1, 2) == 3
    ```
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
