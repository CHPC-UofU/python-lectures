import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/lists.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Lists
    Lists are denoted with square brackets, `[` and `]`.

    * Lists are an *ordered* collection of 0 or more elements
        * `[]` is a valid list
    * Elements in a list don't have to be unique
        * `[1, 1, 1]` is a valid list
    * Elements in a list can be various types—even other lists
        * `[[1, 2, 3], ["a", "b", "c"]]` is a valid list of lists: <pre style="display: inline-block; color: black !important;"><span style="padding: 0.2em; background-color: #e7f5ff; border-radius: 0.2em; border: 0.1em solid #a5d8ff;">[<span style="padding: 0.05em; background-color: #fff9db; border-radius: 0.2em; border: 0.1em solid #ffec99;">[1, 2, 3]</span>, <span style="padding: 0.05em; background-color: #fff0f6; border-radius: 0.2em; border: 0.1em solid #fcc2d7;">["a", "b", "c"]</span>]</span></pre>
    * Lists are mutable (you can change the order of elements and add and remove elements)
    * To create a list, you can use
      * **Square brackets**, `[` and `]`, which denote a list
      * `list()`, which turns its single argument into a list
      * List comprehension, which we'll cover later
    * Lists are *very flexible* but can be *slow*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## List operators
    """)
    return


@app.cell
def _():
    # Let's create some lists:
    a1 = ["a", "x", "b", "w", "d", "e"]
    a2 = list("z")
    print(f"List a1 is: {a1}")
    print(f"List a2 is: {a2}")

    # Lists have a length:
    print(f"Length of a1 is {len(a1)}.")

    # Some operators work on lists:
    print(f"a1 + a2 = {a1 + a2}, a2 * 3 = {a2 * 3}")
    return (a1,)


@app.cell
def _(a1):
    # And some operators don't:
    print(f"a1 / 2 = {a1 / 2}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## List objects have some methods
    """)
    return


@app.cell
def _():
    l = ["a", "x", "b", "w", "d", "e"]

    l.remove("a")
    print("With 'a' removed:", l)

    l.sort()
    print("Sorted:", l)

    l.reverse()
    print("Reversed:", l)

    l.append("p")
    print("With 'p' appended:", l)

    print("Last element (which has been removed):", l.pop())
    print("First element (which has been removed):", l.pop(0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A note on performance
    Suppose you want to add an element to list `l` above. You could do it like this:
    ```python
    l = l + ["x"]
    ```
    or you could do it like this:
    ```python
    l.append("x")
    ```
    Both lines of code accomplish the same thing, but the second is **much** faster.

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about lists is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists">Read more about lists&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Accessing sequence elements by index
    * Strings and lists are examples of **sequences**
      * You can access one or more elements of a sequence with index numbers in square brackets, `[]` (this is contextual; square brackets mean *create a list* in some contexts and *get the element at a given index* in others)
        * Indexes range from `0` up to `sequence length - 1`
        * Negative indexes count backwards from the end: `-1` is the last element, `-2` the second from last, etc.
        * Within the brackets, you can provide information as `[start:end + 1:stepsize]`, where `start` defaults to `0`, `end + 1` defaults to the end of the list, and `stepsize` defaults to `1`
    """)
    return


@app.cell
def _():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    print(letters)
    print(letters[0])
    print(letters[-1])
    print(letters[0:3])
    print(letters[3:12:2])

    # You can use the default for one or more fields by omitting a value:
    print(letters[::3])  # Use the default start and end position, but use a step size of 3
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
