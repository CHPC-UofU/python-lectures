import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/strings.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Strings

    * A string is a sequence of characters enclosed in single quotes like `'…'` or double quotes like `"…"`
      * The quotation marks themselves are not part of the string
    * "Short" strings fit onto one line, like `"here is a string"`
    * "Long" strings don't fit on one line, and are enclosed in triple quotes, `\"\"\"` and `\"\"\"`
    """)
    return


@app.cell
def _():
    s1 = 'Here is a string. Note that it contains "quotation marks."'  # Strings enclosed in '' can contain "

    s2 = "Here's another string. Note that it contains a single quote (an apostrophe)."  # Strings enclosed in "" can contain '

    s3 = "Here's another string. It contains \"quotation marks,\" but they have been \"escaped\" with backslashes so they don't end the string."

    s4 = """This is a long string.
    Its content includes multiple lines of text."""

    print(s1 + s2 + s3)
    print(s4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Strings have some useful operators and methods
    """)
    return


@app.cell
def _():
    # You can multiply and add them:
    s1_1 = "abc-" * 3 + "xyz"
    print("s1:", s1_1)

    # You can split them by some delimiter character using the string's split method:
    print("s1 split by - characters:", s1_1.split("-"))

    # Strings have a length:
    print("s1 is", len(s1_1), "characters long")

    print("s1 contains", s1_1.count("a"), "\"a\" characters")
    print("s1 converted to uppercase:", s1_1.upper())
    return


@app.cell
def _():
    # help on class str shows all the methods available:
    help(str)
    return


app._unparsable_cell(
    r"""
    # You can also typically reveal the object's methods with the Tab key in an IDE or notebook environment:
    s1.
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about strings is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/introduction.html#text">Read more about strings&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## f-strings
    f-strings provide a simple way to format text, and were introduced in Python version 3.6. f-strings are convenient, easy to read, and fast.
    """)
    return


@app.cell
def _():
    # f-strings are an easy way to format text!
    version_number = 3.6
    s4_1 = f"It's easy to format text with f-strings, which were added in Python {version_number}."
    print(s4_1)

    role = "student"
    organization = "the University of Utah"
    print(f"I am a {role} at {organization}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Any Python expression can appear within the curly braces; you can call functions, use operators, and so on.

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about f-strings is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals">Read more about f-strings&nbsp;&rarr;</a>
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
