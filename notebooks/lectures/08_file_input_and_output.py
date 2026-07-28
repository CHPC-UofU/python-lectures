import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/io.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # File input/output (I/O)
    It is useful to read data from files or write data to files. This is done through file objects, which are created using the `open()` function. Files can be opened for reading (`"r"`), writing (`"w"`), or appending (`"a"`):
    """)
    return


@app.cell
def _():
    _input_file = open('../static/popular_dog_names.txt', 'r')  # Open a file for reading
    first_line = _input_file.readline()  # Read one line
    _input_file.close()  # Close the input file
    print(f'Read this data from the file: "{first_line}"')
    output_file = open('../static/tmpfile.txt', 'w')
    output_file.write(first_line)  # Open another file for writing
    output_file.close()  # Writing overwrites the file if it exists, so be careful!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can also read all the lines of a file into a list with `input_file.readlines()`, but be careful! The file might be big!

    If you are working with binary data files (rather than text files) you need to open them in the `"rb"`, `"wb"`, or `"ab"` modes, and you may find the [struct](https://docs.python.org/3/library/struct.html) library helpful.

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about file input and output is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files">Read more about file input and output&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## File I/O and the `with` statement
    A common pattern in Python is

    ```
    1. Try to open a file; if that works,
       2. Read from or write to the file
       3. Close the file
    ```

    This pattern is so common that Python provides a statement to simplify this: the `with` statement does everything!
    """)
    return


@app.cell
def _():
    with open('../static/popular_dog_names.txt', 'r') as _input_file:
        all_lines = _input_file.readlines()
        print(f'The file contains {len(all_lines)} lines of data.')
        print(f"The first line is '{all_lines[0]}'")
        print(f"The last line is '{all_lines[-1]}'")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At the end of the `with` clause, the file is closed.

    You can use `with` for more than just file I/O. For all this to work, the object created in the `with` statement must have the methods `__enter__()` and `__exit__()`. See the documentation [here](https://docs.python.org/3/reference/compound_stmts.html#with).
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
