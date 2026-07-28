import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <img src="public/thanks.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Wrapping up

    We've made it to the end of the course! You now know enough about the Python language to start practicing and using it in your own work. This won't be easy at first, but you can always refer back to this presentation or read through the documentation if you get stuck.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## What *haven't* we discussed?
    * Creating iterators and generators (see more_on_iterators.ipynb)
    * Decorators (touched on here: https://github.com/bmilash/dataclasses-and-yaml)
    * Type checking in Python ([good article here](https://realpython.com/python-type-checking))
    * IDEs (integrated development environments)
        * Coding assistants (AI)
    * Debugging
    * Benchmarking
    * Unit testing
    * Defining functions using `*args` and `**kwargs` (arbitrary number of arguments)
    * Parallel programming

    There's still much to learn about the Python language!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Programming advice
    * Don't rely on the operating system's Python; it's old, and you don't control it
        * At the CHPC, load a `python` module with, for example, `module load python/3.12.4`
    * Use Python 3; Python 2 support ended on January 1, 2020
    * When editing, save early and save often
    * Save versions of your scripts with [Git](https://www.chpc.utah.edu/documentation/software/git-scm.php) locally, and ideally into a remote software repository
    * Write test code and consider using testing frameworks
    * Learn to use a debugger ([pdb](https://docs.python.org/3/library/pdb.html), [PyCharm](https://www.jetbrains.com/pycharm/), [IDLE](https://docs.python.org/3.10/library/idle.html), [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html), [VSCode](https://www.chpc.utah.edu/documentation/software/vscode.php)); this can be much quicker than `print()` statements!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Resources
    * Python Tutorial: https://docs.python.org/3/tutorial/index.html
    * Python Standard Library: https://docs.python.org/3/library/index.html
    * PyCon: excellent meeting!
      - https://us.pycon.org
      - YouTube channel: https://www.youtube.com/@PyConUS

    ## Questions?
    Please contact us at helpdesk@chpc.utah.edu if you have any questions.

    **Have fun coding, and thank you for attending!**
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
