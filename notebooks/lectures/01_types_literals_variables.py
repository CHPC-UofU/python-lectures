import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/variables.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Types, literals, and variables
    We will look more closely at different types as we proceed through the course. You don't need to try to memorize all of this information right now!

    There are different types of information in Python:

    * Simple values
      * **Numbers** (integers like `1`, real numbers like `1.0`, complex numbers like `1+2.5j`)
      * **Character strings** like `"Hello, world!"`
      * **Boolean values** `True` and `False`
      * `None` (the empty/unknown value)
    * Compound values
      * **Lists** like `[1, 2.0, "three"]`
        * Lists are *ordered*; the order of the elements in a list will be the same every time you iterate over it, and you can choose to add elements to the beginning, middle, or end of a list
      * **Dictionaries** like `{"cat": "Felis catus", "dog": "Canis lupus familiaris"}`
      * **Sets** like `{1, 2.0, "three"}`
        * Like a list, but *without repeats* and *unordered* (for pedants: sets *are* ordered, but not in a way that is particularly useful to humans)
      * **Tuples** like `(1, 2.0, "three")`
        * Like a list, but *immutable* (tuples can't be changed after they are created)
      * Complex or custom objects that we design
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Let's create some variables!
    """)
    return


@app.cell
def _():
    # Let's define some variables using the assignment operator "=", then print their values and types.
    _x = 1
    y = "Here is a character string"
    print("The value of x is", _x, "and its type is", type(_x))
    # What are the values assigned to x and y, what are the types of data assigned to x and y?
    print("The value of y is", y, "and its type is", type(y))
    z = True
    # Assign the value of True or False to a variable. What data type is assigned to the variable?
    print("The type of z is", type(z))
    return


@app.cell
def _():
    # Now assign the value "Hello, world!" to x. What is the type of x now?
    _x = "Hello, world!"
    print("The type of data assigned to x is", type(_x))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how the type of value assigned to `x` has changed. Python is a **dynamically typed** language.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="public/exercise.svg" style="height: 2.5em; margin: 0;" />

    <h2>Exercise: Now it's your turn!</h2>

    In the cell below, create the variables <code>major</code> and <code>graduation_year</code>, then assign your major to <code>major</code> and your graduation year (or expected graduation year) to <code>graduation_year</code>. Then, print them using the <code>print()</code> function to produce the output <code>My major is … and I graduated (or expect to graduate) in …</code>.

    </div>
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
