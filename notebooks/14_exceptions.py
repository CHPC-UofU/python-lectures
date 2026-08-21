import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/exceptions.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Exceptions
    When something goes wrong, Python "raises" an `Exception` object.
    """)
    return


@app.cell
def _():
    elements = {"H": "hydrogen", "He": "helium", "Li": "lithium", "Be": "berylium"}
    print(elements)
    return (elements,)


@app.cell
def _(elements):
    # Depending on the value of symbol, this code might raise an exception:
    for symbol in ("H", "S"):
        print(f"The name of element {symbol} is {elements[symbol]}.")
    return


@app.cell
def _(elements):
    # Rather than testing "if symbol in elements," just wrap the code in try and except:
    for symbol in ("H", "S"):
        try:
            print(f"The name of element {symbol} is {elements[symbol]}.")
        except KeyError:
            print(f"Symbol {symbol} not found in elements dictionary!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Generic exceptions
    Python defines [lots of exceptions](https://docs.python.org/3/library/exceptions.html), but you may not know what kind of exception to handle, so you can do it "generically":
    """)
    return


@app.cell
def _():
    try:
        quotient = 17 / 0
    except Exception as e:
        print(f'Whoa, just caught unexpected exception: {type(e)}, "{e}"!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can also define your own custom exceptions; we will discuss this later.
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
