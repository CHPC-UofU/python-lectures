import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/sets.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Sets
    * A set is a collection of *unique* objects
    * You can create sets with the `set()` command or with the `{` and `}` (**curly brace**) symbols
    * You can also do set comprehensions
    * Sets have all the methods and operators you'd expect: union, intersect, difference, etc.

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about sets is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/datastructures.html#sets">Read more about sets&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell
def _():
    vowels = set(["a", "e", "i", "o", "u"])

    import random, string

    # What does this next line do? What is the type of the variable?
    random_letters = {random.choice(string.ascii_lowercase) for i in range(20)}

    print(f"The random_letters set contains {len(random_letters)} unique letters.")
    print(
        f"random_letters contains these vowels: {random_letters.intersection(vowels)}."
    )
    print(
        f"random_letters contains these consonants: {random_letters.difference(vowels)}."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="public/exercise.svg" style="height: 2.5em; margin: 0;" />

    <h2>Exercise: Password generator</h2>

    <p>Write a function named <code>random_password()</code> that uses the string and random modules, and returns a string of 10 random letters, numbers, and symbols. If you want to get fancy, you could give your function an optional password length argument.</p>


    <p><em>Please note that this is intended only as an exercise. If you want to create cryptographically secure passwords in Python, you will want to use the <a href="https://docs.python.org/3/library/secrets.html">secrets module</a>. It is a better idea to use an existing, well tested password manager.</em></p>

    </div>
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
