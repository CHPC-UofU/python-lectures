import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <img src="public/loop.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Looping
    Python provides two different types of loop statements: `while` loops and `for` loops.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## `while` loops
    A `while` loop tests some logical condition and executes the body of the loop while that condition evaluates to `True`:
    """
    )
    return


@app.cell
def _():
    # Calculate the first 10 elements of the Fibonacci sequence:
    fibonacci = [0, 1]
    while len(fibonacci) < 10:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    print(fibonacci)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## `for` loops
    `for` loops let you process each item in a sequence of items, like each item in a list:
    """
    )
    return


@app.cell
def _():
    for _letter in ["a", "e", "i", "o", "u"]:
        print(_letter)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    There are many other functions and statements that are useful in the context of loops.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## The `range()` function
    `range(start, stop[, stepsize=1])` returns a list-like object containing integers from `start` to `stop - 1`. This is useful for all kinds of list processing and `for`-loop control:
    """
    )
    return


@app.cell
def _():
    element_names = [
        "hydrogen",
        "helium",
        "lithium",
        "berylium",
        "boron",
        "carbon",
        "nitrogen",
        "oxygen",
        "fluorine",
    ]
    for _i in range(0, len(element_names)):
        print(f"Item {_i} in the list is {element_names[_i]}.")
    return


@app.cell
def _():
    # The stepsize defaults to 1 and the start value defaults to 0:
    print(list(range(3)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="../../images/exercise.svg" style="height: 2.5em; margin-bottom: -1em;" />

    ## Exercise: *Factorial* function
    Create a function named `factorial()` that takes one argument, `n`, and returns $n!$ (or $1 \times 2 \times 3 \times \ldots \times (n-2) \times (n-1) \times n$). You can implement this with a `for` loop.

    For this exercise, you can assume that the argument is a positive integer. Write the `factorial()` function and try calling it with a few different positive integer values.

    (You could also get fancy and write a recursive function, a function that calls itself. If you do this, **make sure** your code tests when to end the recursion!)

    </div>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Looping flow control: the `continue` statement
    Sometimes you want to skip the rest of the body of a loop, and `continue` with the next iteration:
    """
    )
    return


@app.cell
def _():
    consonants = []
    vowels = ["a", "e", "i", "o", "u"]
    for _letter in "abcdefghijklmnopqrstuvwxyz":
        if _letter in vowels:
            continue
        consonants.append(
            _letter
        )  # Go back to the top of the loop and look at the next item;
    print(
        len(consonants)
    )  # don't go any further in the body of the loop for this particular iteration  # This line won't be run if the letter is a vowel, since we "continue" above for all vowels
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Looping flow control: the `break` statement
    Sometimes you need to `break` out of a loop completely, before you've reached the last iteration:
    """
    )
    return


@app.cell
def _():
    _i = 100
    while _i > 0:
        print(_i)
        if _i % 7 == 0:
            break
        _i -= 1
    print(
        f"The biggest multiple of 7 less than 100 is {_i}."
    )  # Decrement operator, equivalent to i = i - 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## List comprehension
    `for` loops are handy for populating lists. Let's say we want a list of integers from 0 to 9 squared. You could write this as
    """
    )
    return


@app.cell
def _():
    _squared_integers = []
    for _i in range(0, 10):
        _squared_integers.append(_i**2)
    print(_squared_integers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    However, it is also possible to write this loop in one line:
    """
    )
    return


@app.cell
def _():
    _squared_integers = [_i**2 for _i in range(0, 10)]
    print(_squared_integers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    This is "list comprehension." For more details, see the [Python tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions "Python Tutorial").

    List comprehension can also include simple `if` statements:
    """
    )
    return


@app.cell
def _():
    values = [-100, -50, 50, 100]

    negative_values = [value for value in values if value < 0]

    descriptive_strings = ["negative" if value < 0 else "positive" for value in values]

    print(negative_values)
    print(descriptive_strings)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Note that the order of `for` and `if` varies in the examples above; in the first example, we conditionally append values to the list (`if` modifies the `for` loop, not the value), while in the second example, we always append a conditional value (`if` modifies the value).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Iterators
    For loops can _iterate_ across a variety of objects, such as strings, lists, `range()` objects, or open files. These objects are all _iterators_. More on iterators [here](https://docs.python.org/3/tutorial/classes.html#iterators "Python Tutorial").
    """
    )
    return


@app.cell
def _():
    for _letter in "ABC":
        print(_letter)
    for vowel in ["a", "e", "i", "o", "u"]:
        print(vowel)
    for number in range(0, 5):
        print(number)
    with open("../static/popular_dog_names.txt", "r") as dog_file:
        for line in dog_file:
            if line.startswith("M"):
                print(line.strip())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="../../images/exercise.svg" style="height: 2.5em; margin-bottom: -1em;" />

    ## Exercise: Dog name finder
    The file "popular_dog_names.txt" lists the 10 most popular names for female and male dogs in 2016 (according to the [American Kennel Club](https://www.akc.org/expert-advice/news/popular-dog-names-2016/)). Write a function that accepts a proposed dog name and checks the popular_dog_names.txt file to see whether that name is popular. If it is, print that the proposed name is popular, its rank, and for what gender of dog. If the proposed name is not found, print that the name wasn't found.

    </div>
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
