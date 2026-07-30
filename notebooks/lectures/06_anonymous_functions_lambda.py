import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/lambda.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Anonymous functions (lambda expressions)
    Functions are objects, like everything else in Python. Most functions are associated with an identifier, like `hello_world()`. There are situations where we want to pass a function as an argument to another function, and one way to do that is with the function's name. Here is an example using the `map()` function, which applies a function to each element of a list:
    """)
    return


@app.cell
def _():
    def fahrenheit_to_celsius(x):
        """This function converts temperatures in Fahrenheit to temperatures in Celsius"""
        return (x - 32) * 5 / 9

    _temperatures_f = [-40, 0, 32, 70, 100, 451]
    _temperatures_c = list(map(fahrenheit_to_celsius, _temperatures_f))
    # Here is a list of temperatures we want to convert:
    print(_temperatures_f)
    # Now we use the map() statement to apply the fahrenheit_to_celsius() function to each element in the list:
    # Print temperatures in both Fahrenheit and Celsius
    print(_temperatures_c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But defining a new function for something we're only going to use once is unnecessary. Instead, we can use a "lambda expression" to create an anonymous function right where we need it:
    """)
    return


@app.cell
def _():
    _temperatures_f = [-40, 0, 32, 70, 100, 451]
    _temperatures_c = list(map(lambda x: (x - 32) * 5 / 9, _temperatures_f))
    # As above, use map() on the list of numbers
    # Note the extra whitespace here, which is added for clarity
    # This is possible, even though Python is whitespace-dependent, because Python will look for a ) to close (
    print(_temperatures_f)
    print(_temperatures_c)  # An unnamed function of x
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Assigning a lambda expression to an identifier
    """)
    return


@app.cell
def _():
    divide_by_ten = lambda x: x / 10.0
    divide_by_ten(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about lambda expressions is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions">Read more about lambda expressions&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
