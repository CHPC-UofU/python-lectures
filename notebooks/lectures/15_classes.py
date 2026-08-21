import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/classes.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Classes

    * A class is the definition of a data type
    * **Every** object in Python belongs to a class
    * Each class is a collection of data values and methods
    * A single object that belongs to a class is an *instance* of that class
    * Classes provide
      * a namespace inside which your code is isolated from outside complexity
      * a mechanism for code reuse through *inheritance* (more on this later)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Creating new instances of a class
    When a class is defined, Python creates a function with the same name as the class, and that function creates new objects belonging to that class. For example, the function `list()` creates new `list` objects. Typically, the arguments to that function provide the data that is stored within the new object. Initializing the new object with that data is handled by a special method named `__init__()`.

    When we write the code for our own classes we need to provide that `__init__()` method to do the initialization, and it looks like this:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Class example
    Let's write a simple class that represents a person:
    """)
    return


@app.cell
def _():
    class Person:
        """
        This class represents a person.
        (This is the docstring for the whole class.)
        """

        def __init__(self, first_name, last_name, year_of_birth):
            """
            Initialization method of the class Person.
            (This is the docstring for this method.)
            """
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth


    # Creating an instance of class Person by calling the Person() function
    p = Person("George", "Washington", 1732)

    print(p.first_name)
    print(type(p))
    print(p)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note the first argument to the `__init__()` method: `self`. Every method (with the exception of [staticmethods](https://docs.python.org/3/library/functions.html#staticmethod), not discussed here) will have an argument like this, and that argument refers to the object that is getting initialized or otherwise operated on by the method.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Special class methods
    Objects have a variety of special methods that are called behind the scenes:
    * `__init__()`: class constructor, or initializer
    * `__str__()`: provides string representation of object, used when printing an object
    * `__lt__()`: required for the `<` operator, used when comparing objects for sorting
    * `__add__()`: required for the `+` operator
    * `__del__()`: class deconstructor. Called during garbage collection, or when using `del`
    * `__enter__()`: Context manager enter function, used by `with` statement
    * `__exit__()`: Conect manager exit function, used by `with` statement
    * `__iter__()`: Required for an object to be an iterator
    * `__next__()`: Required for an object to be an iterator

    `__enter__` and `__exit__` are not provided; you need to write these if you intend to use your object in a `with` statement.

    `__iter__` and `__next__` are not provided; you must write these if you intend to use your object as an iterator.

    These methods are all detailed [on the Python documentation](https://docs.python.org/3.7/reference/datamodel.html#special-method-names).

    Let's improve on our `Person` class:
    """)
    return


@app.cell
def _():
    import time


    class Person:
        """Here's an improved Person example."""

        def __init__(self, first_name, last_name, year_of_birth):
            """Constructor method of the class Person. (This is the docstring for this method.)"""  # This is a required argument!
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth

        def __str__(self):
            """Returns the string representation of the object"""
            return f"{self.last_name}, {self.first_name}: born {self.year_of_birth}"

        def __lt__(self, other):
            """Used to compare this Person object with another Person object for sorting."""
            return self.last_name < other.last_name

        def approximate_age(self):
            """Returns person's (approximate) age in years"""
            current_year = time.localtime(time.time()).tm_year
            return current_year - self.year_of_birth


    scientists = [
        Person("Isaac", "Newton", 1643),
        Person("Marie", "Curie", 1867),
        Person("Dorothy", "Hodgkin", 1910),
        Person("Albert", "Einstein", 1879),
        Person("Galileo", "Galilei", 1564),
        Person("Ada", "Lovelace", 1815),
        Person("Johannes", "Kepler", 1571),
    ]
    scientists.sort()

    for scientist in scientists:
        print(
            f"{scientist}, (approximate) age {scientist.approximate_age()} years"
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    How does this work? The lines with `Person(…)` inside of the `scientists` list call the `__init__()` function of the `Person` class. Here, we create a few different *instances* of the class:

    <div>
    <code style="line-height: 2em; color: black !important;">

      <div style="display: inline-block; vertical-align: top; border: 0.1em solid #be0000; border-left: 0.2em solid #be0000; margin: 0.2em 0; background-color: #fff5f5; box-sizing: border-box; border-radius: 0.2em;">
        <div style="width: 100%; padding: 1em; box-sizing: border-box; background-color: #be0000; color: #ffffff;">
          Person
        </div>

        <div style="padding: 1em;">
          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__init__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>, …): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__str__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__lt__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>, …): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">approximate_age</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">first_name</span> = "Isaac"
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">last_name</span> = "Newton"
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">year_of_birth</span> = 1643
          </div>
        </div>
      </div>

      <div style="display: inline-block; vertical-align: top; border: 0.1em solid #be0000; border-left: 0.2em solid #be0000; margin: 0.2em 0; background-color: #fff5f5; box-sizing: border-box; border-radius: 0.2em;">
        <div style="width: 100%; padding: 1em; box-sizing: border-box; background-color: #be0000; color: #ffffff;">
          Person
        </div>

        <div style="padding: 1em;">
          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__init__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>, …): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__str__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__lt__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>, …): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">approximate_age</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">first_name</span> = "Marie"
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">last_name</span> = "Curie"
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">year_of_birth</span> = 1867
          </div>
        </div>
      </div>

      <div style="display: inline-block; vertical-align: top; border: 0.1em solid #be0000; border-left: 0.2em solid #be0000; margin: 0.2em 0; background-color: #fff5f5; box-sizing: border-box; border-radius: 0.2em;">
        <div style="width: 100%; padding: 1em; box-sizing: border-box; background-color: #be0000; color: #ffffff;">
          Person
        </div>

        <div style="padding: 1em;">
          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__init__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>, …): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__str__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">__lt__</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>, …): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            def <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">approximate_age</span>(<span style="border-left: 0.2em dashed #228be6; background-color: #a5d8ff; border-radius: 0.2em; padding: 0.1em 0.2em;">self</span>): <span style="border: 0.1em solid #228be6; border-left: 0.2em dashed #228be6; margin: 0.2em 0; background-color: #e7f5ff; padding: 0.1em 0.2em; border-radius: 0.2em;">…</span>
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">first_name</span> = "Dorothy"
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">last_name</span> = "Hodgkin"
          </div>

          <div>
            <span style="border-left: 0.2em solid #be0000; background-color: #ffc9c9; border-radius: 0.2em; padding: 0.1em 0.2em;">year_of_birth</span> = 1910
          </div>
        </div>
      </div>

    </code>

    &dtdot;
    </div>

    These are bundles of methods (functions) and data. When we loop through the `scientists` list (`for scientist in scientists`), we are addressing each of the instances we created, one by one; in the example, we call the `approximate_age()` method of each instance. Notably, we didn't need to pass it any arguments, even though the function is defined as `approximate_age(self)`. The first argument to a method like this is the object itself, and since we called this function as `scientist.approximate_age()`, Python knows that `self` is (the instance referred to by) `scientist` here. This is a quirk of the language and its object-oriented nature, and it will take some time to learn. With practice, you won't need to think twice about it.

    The variable `self` could actually be named something else entirely; however, [the name `self` is used in this context by convention](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style), and almost all Python programmers use it.

    Classes are probably confusing if you haven't used an object-oriented language before, but they are very powerful tools. We recommend [reading the Python tutorial on classes](https://docs.python.org/3/tutorial/classes.html) to learn more.

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about classes is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/classes.html">Read more about classes&nbsp;&rarr;</a>
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
