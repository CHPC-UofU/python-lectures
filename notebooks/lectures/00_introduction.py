import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <h1 style="color: #be0000; font-weight: bold; font-size: 4em;">Hands-on Introduction to Python</h1>

    Welcome to the Hands-on Introduction to Python course from the Center for High Performance Computing at the University of Utah. This is an introduction to the Python language for beginners, written by Brett Milash, Wim Cardoen, and Robben Migacz.

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/video.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Videos</p>
        <p style="margin: 0;">Recordings of this lecture series are available. Each video has closed captions.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://www.youtube.com/watch?v=9FfLpe30cys&list=PLPPvrxDFPZ43NzlBPZEePVaCJE7BXHOw8">View lectures on YouTube&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Why is Python useful?

    Like all scripting and programming languages, Python allows its users to manipulate and transform data. All computer programs provide instructions that tell a computer how to operate on information; they give **a sequence of steps to produce output (such as simulation results, plots, summary statistics, graphics, audio, or video) from input (such as datasets or input files, initial conditions, or user-provided information)**. A program or script is like the blueprint for a factory that operates on—and produces—information.

    The Python _interpreter_ reads and executes Python scripts, like the one given below.
    """)
    return


@app.cell
def _():
    def hands_on_intro_to_python():
        """
        This is a hands-on introduction to the Python language from the Center for
        High Performance Computing. You can run this code cell by typing Shift+Return.
        """
        import sys

        print("We will use Python version", sys.version)

    hands_on_intro_to_python()
    return (hands_on_intro_to_python,)


@app.cell
def _(hands_on_intro_to_python):
    help(hands_on_intro_to_python)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Characteristics of the Python language
    * **Python is interpreted**
    * **Python is object-oriented**
      * Data and functions (called "methods") are packaged together into objects
      * An object's methods are used to manipulate that object's data
      * Objects are organized into "classes," which define the objects' methods and data
      * "Inheritance" makes it easy to create new classes from existing ones
      * Great way to organize your code (and your thinking!)
    * **Python is modular**
      * A lot of Python's functionality is found in *modules*
        * We need to `import` those modules to use them
      * Python comes installed with many modules; many, many more can be installed later
    * **Leading white space (indentation) is significant in Python**
      * Level of indentation defines "blocks" of code
      * Either tabs *or* spaces; choose one *or* the other!
      * Some editors take care of this for you
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Running Python code

    It's possible to run Python

    * **Interactively** (typing Python statements at the interpreter)
    * In a **script**
        * Run the interpreter with your script as an argument: `python scriptname.py` from the command line
        * As an executable script
            * Add `#!/usr/bin/env python` at the top of the script
            * Make sure the script is executable: `chmod +x scriptname.py`
            * Run the script from the command line: `./scriptname.py`
    * In a cell in a **Jupyter Notebook**, **marimo notebook**, or similar technology
    """)
    return


@app.cell
def _():
    # This is a comment; it doesn't get executed by Python!
    import math

    radius = 1.0
    area = math.pi * radius * radius
    print("The area of a circle with radius", radius, "unit is", area, "square units")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Big concepts in Python
    * **Variables** are names for data, which can be
      * a simple object like a number or a character string
      * a complex object like a list of values or a dictionary of values
    * **Statements** (and **operators**), which are like are the verbs of the language and act on data
    * **Functions**, which are reusable blocks of code
    * **Classes**, which define all the different types of objects, including data and *methods* (more on this later)
    * **Modules**, which are entire files of Python code, containing variables, functions, and classes
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
