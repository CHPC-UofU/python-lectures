import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/flow_control.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Flow control: `if`, `elif`, and `else`

    It is imperative that your code can *branch* depending on certain critera, so you can handle different situations in different ways. The `if` statement lets you do this:
    """)
    return


@app.cell
def _():
    animal = "dog"

    if animal == "dog":
        print("The animal is a dog")
    elif animal == "cat":
        print("The animal is a cat")
    else:
        print("The animal is neither dog nor cat!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Both the `elif` (a contraction of "else if") and `else` clauses are optional. Note the whitespace before the `print` statements; that indentation is significant!

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about flow control is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/controlflow.html#if-statements">Read more about flow control&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="public/exercise.svg" style="height: 2.5em; margin: 0;" />

    <h2>Exercise: <em>odd or even</em> function</h2>

    Create a function that takes one argument and returns the string <code>"odd"</code> or <code>"even"</code>, depending on whether the argument is an odd number or an even number. Assume for now that the argument is a positive integer.

    </div>
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
