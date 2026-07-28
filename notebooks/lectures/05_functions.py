import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/functions.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Functions
    Functions are reusable chunks of Python code. They (usually) have a name, they can take zero or more arguments, and they return a value. If you don't explicitly return a value, a function returns `None`.

    This is the general layout of a function definition in Python:
    """)
    return


@app.cell
def _():
    def test_function(argument1, argument2, argumentn="default_value"):
        """This is the documentation string (or docstring) for the function"""
        print("Value of argument1:", argument1)  # The body of the function goes here:
        print("Value of argument2:", argument2)
        print("Value of argumentn:", argumentn)

    _x = test_function("a", 2)
    print("test_function returned", _x)
    help(test_function)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. The function is announced with the `def` keyword;
    2. followed by the function name;
    3. followed by 0 or more arguments (inputs) in parentheses, `(…)`;
       * positional arguments must come before "keyword arguments"; keyword arguments specify a default value and are optional when calling the function
    5. followed by a colon, `:`;
    6. followed by an optional (but recommended) documentation string;
    7. followed by the body of the function, indented relative to the `def` statement, which will
        * `return` a value if specified, or
        * `return None` automatically if no `return` statement is given
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A quick note on *scope*
    """)
    return


@app.cell
def _():
    subject = "The quick brown fox"
    action = "jumps over the lazy dog"

    def tell_story(subject):
        "Tell a little story"
        note = "This variable only exists within this function!"
        print(f"{subject} {action}")

    tell_story(subject="The slow tortoise")  # What does "subject=…" do?
    tell_story(subject)  # Did we reassign the variable subject?
    tell_story(subject=subject)  # … what? Python doesn't make any sense!
    return


@app.cell
def _(note):
    # Let's confirm the statement in the "note" variable!
    print(note)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wait! Didn't we *change* the value of `subject` when we called the function the first time? What happened here? This is related to the **scope** of the variables.

    <code style="line-height: 2em; color: black !important;">
    <div style="display: inline-block; border: 0.1em solid #228be6; border-left: 0.2em solid #228be6; margin: 0.2em 0; background-color: #e7f5ff; box-sizing: border-box; padding: 1em; border-radius: 0.2em;"><span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span> = "The quick brown fox"
    <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">action</span> = "jumps over the lazy dog"<br>
    def <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">tell_story</span>(<span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>):
    <div style="display: inline-block; border: 0.1em solid #fab005; border-left: 0.2em dashed #fab005; margin: 0.2em 0; background-color: #fff9db; width: 100%; box-sizing: border-box; padding: 1em; border-radius: 0.2em;">"Tell a little story"
    <span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">note</span> = "This variable only exists within this function!"
    print(f"{<span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>} {<span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">action</span>}")</div><br>
    <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">tell_story</span>(<span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>="The slow tortoise")
    <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">tell_story</span>(<span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>)
    <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">tell_story</span>(<span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>=<span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>)
    </div>
    </code>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since `subject` is a variable *within* `tell_story()`, its value is the argument passed to the function, but *only within the scope of the function*. Note that this does *not* overwrite the `subject` variable outside of the function. **In the above example, the variable `action` *is* accessible in the scope of the function; however, the variable `note` *is not* accessible outside of the scope of the function. This is a one-way relationship.** The inner scope is aware of variables defined in the outer scope, but the outer scope is not aware of variables defined in the inner scope. (The keywords `global` and `nonlocal` can change this behavior, but they can also make programs more confusing—especially for new programmers—so we recommend avoiding these for now.)

    This concept of scope applies to **functions** and **classes**; we'll talk about classes later! The concept of scope does not apply to loops or `if` statements.

    <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; color: black !important; border-radius: 0.2em; padding: 0.1em 0.2em;">tell_story</span>(<span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; color: black !important; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>=<span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; color: black !important; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>) is something you might see; it may look a little strange, but it is perfectly valid in Python for managing scope. It's assigning the value of <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; color: black !important; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span> to the variable <span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; color: black !important; border-radius: 0.2em; padding: 0.1em 0.2em;">subject</span>, which is used in the other scope.

    Note that this concept of scope also means that

    <code style="line-height: 2em; color: black !important;">
    <div style="display: inline-block; border: 0.1em solid #228be6; border-left: 0.2em solid #228be6; margin: 0.2em 0; background-color: #e7f5ff; box-sizing: border-box; padding: 1em; border-radius: 0.2em;">def <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">x</span>():
    <div style="display: inline-block; border: 0.1em solid #fab005; border-left: 0.2em dashed #fab005; margin: 0.2em 0; background-color: #fff9db; width: 100%; box-sizing: border-box; padding: 1em; border-radius: 0.2em;"><span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">message</span> = "Hello!"
    def <span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">y</span>():
    <div style="display: inline-block; border: 0.1em solid #fa5252; border-left: 0.2em dotted #fa5252; margin: 0.2em 0; background-color: #fff5f5; width: 100%; box-sizing: border-box; padding: 1em; border-radius: 0.2em;">print(<span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">message</span>)</div>
    </div>
    <span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">y</span>()
    </div>
    </code>

    will not work because `y` is out of scope on the last line:
    """)
    return


@app.cell
def _(y):
    def _x():
        message = "Hello!"

        def y():
            print(message)

    y()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    However,

    <code style="line-height: 2em; color: black !important;">
    <div style="display: inline-block; border: 0.1em solid #228be6; border-left: 0.2em solid #228be6; margin: 0.2em 0; background-color: #e7f5ff; box-sizing: border-box; padding: 1em; border-radius: 0.2em;">def <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">x</span>():
    <div style="display: inline-block; border: 0.1em solid #fab005; border-left: 0.2em dashed #fab005; margin: 0.2em 0; background-color: #fff9db; width: 100%; box-sizing: border-box; padding: 1em; border-radius: 0.2em;"><span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">message</span> = "Hello!"
    def <span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">y</span>():
    <div style="display: inline-block; border: 0.1em solid #fa5252; border-left: 0.2em dotted #fa5252; margin: 0.2em 0; background-color: #fff5f5; width: 100%; box-sizing: border-box; padding: 1em; border-radius: 0.2em;">print(<span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">message</span>)</div>
    <span style="border-left: 0.2em dashed #fab005; background-color: #ffec99; border-radius: 0.2em; padding: 0.1em 0.2em;">y</span>()
    </div>
    <span style="border-left: 0.2em solid #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">x</span>()
    </div>
    </code>

    will work:
    """)
    return


@app.cell
def _():
    def _x():
        message = "Hello!"

        def y():
            print(message)

        y()

    _x()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `return` statement
    You will often want to return one or more values from a function back to the code that called it. To do this, we use the `return` statement:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # Return a single value:
    return x

    # Return multiple values as a tuple (more on tuples later):
    return (mean, std_deviation)

    # Return the outcome of a logical test as a True or False value:
    return x < 5
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You have probably seen functions before in your math classes, even if you didn't have a name for them. For example, perhaps you've seen something like $y=f(x)$, where $f(x)=x^2$. In this example, $f$ is the *function*, $x$ is the *argument* (the input), and $x^2$ is the value the function outputs or *returns*. Python functions are a little different than the functions from your math classes because they can do things like read from or write to files and print results to the screen, like `test_function()` above. Otherwise, they're quite similar. In Python, the example $y=f(x)$ where $f(x)=x^2$ and $x=5$ might look like
    """)
    return


@app.cell
def _():
    def f(x):
        """This function squares the argument"""
        return _x**2

    y = f(x=5)
    print(y)
    return (y,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is a trivial function, but it illustrates that functions may be something you've seen before in another context.

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about functions is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">Read more about functions&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="../../images/exercise.svg" style="height: 2.5em; margin-bottom: -1em;" />

    <h2>Exercise: <em>Hello, world</em> function</h2>

    In the following cell, create a function named `hello_world()` that takes no arguments. It should print `"Hello, world!"` when you call the function.

    Then, modify your function to take one optional argument that defaults to `"world"`. If called without an argument, your function should print `"Hello, world!"`. If you pass a value to the function, like `"Bob"`, your function should print `"Hello, Bob!"`.

    </div>
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
