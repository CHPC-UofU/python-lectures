import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/tuples.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Tuples
    * Tuples are _immutable_, ordered collections of objects
    * The objects can be of various types
    * You can create them with the `(` and `)` symbols (**parentheses**), or with the `tuple()` function
    * Tuples are sequences, so we can
       * iterate through them
       * access elements by index
    """)
    return


@app.cell
def _():
    days_of_the_week = (
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    )
    print(f"Day 6 is {days_of_the_week[6]}")

    # Tuples are immutable! We can't change them.
    days_of_the_week[3] = "Mittwoch"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These are handy for returning multiple values from a function: `return (mean + sd, mean - sd)`

    There's an oddity with tuple syntax: A tuple with a single element must be defined using a comma, such as `(5,)`. The expression `(5)` is the same as `5` while `(5,)` is a tuple with the single element `5`. In other words, a comma is necessary to initialize a tuple, as parentheses are used *both* to define operation precedence and to initialize tuples.
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
