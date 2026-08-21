import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/inheritance.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Inheritance
    - Inheritance lets you create a new class using an existing class as a foundation
      - The new class "inherits" data and methods from the existing class
      - This new class is a "child" class derived from a "parent" class
    - Parent classes are also called "base" classes or "super" classes
      - You can add or replace methods and data values of the parent class in the child class
      - A child class can be derived from one (single inheritance) or several (multiple inheritance) base classes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Import the `Person` class from the previous lecture to allow examples from this lecture to work
    """)
    return


@app.cell
def _():
    import time


    class Person:
        "Here's an improved Person example."

        def __init__(
            self, first_name, last_name, year_of_birth  # This is a required argument!
        ):
            """
            Constructor method of the class Person.
            (This is the docstring for this method.)
            """
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth

        def __str__(self):
            "Returns the string representation of the object"
            return f"{self.last_name}, {self.first_name}: born {self.year_of_birth}"

        def __lt__(self, other):
            "Used to compare this Person object with another Person object for sorting"
            return self.last_name < other.last_name

        def approximate_age(self):
            "Returns person's (approximate) age in years"
            # Calculate the current year.
            current_year = time.localtime(time.time()).tm_year
            # Calculate this person's age by subtracting the year they were born from
            # the current year. (Not exactly right, but close enough for our purposes.)
            return current_year - self.year_of_birth


    rockstars = [
        Person("Lou", "Reed", 1942),
        Person("Iggy", "Pop", 1947),
        Person("David", "Bowie", 1947),
    ]
    rockstars.sort()

    for musician in rockstars:
        print(f"{musician}, (approximate) age {musician.approximate_age()} years")
    return (Person,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inheritance example
    """)
    return


@app.cell
def _(Person):
    class Student(Person):
        "A Student is a Person with a GPA"

        def __init__(self, first_name, last_name, year_of_birth, grade_point_average):
            # Call the parent class constructor
            Person.__init__(self, first_name, last_name, year_of_birth)

            # You can also do it like this:
            # super().__init__(first_name, last_name, year_of_birth)

            self.gpa = grade_point_average

        def __str__(self):
            return f"{self.last_name}, {self.first_name}: born {self.year_of_birth}, GPA {self.gpa}"


    s = Student("Alice", "Pythoncoder", 2001, 4.0)
    print(s)
    print(f"{s.first_name} is {s.approximate_age()} years old.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice that the `Student` class definition replaces only the base class (`Person`) methods that need to be modified.

    Also notice that `Student` class objects have an `age()` method; where does that come from?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example of using inheritance: User-defined exceptions
    Python defines [lots of exceptions](https://docs.python.org/3/library/exceptions.html), but you can create your own custom exceptions too:
    """)
    return


@app.cell
def _():
    class MyException(Exception):
        pass

    raise MyException(
        "Something bad happened. Here's some information to help you sort it out."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `pass` statement is used when you want a block of code that does nothing at all. Here, we are creating a new class named `MyException` which is derived from the Python class `Exception`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <img src="public/exercise.svg" style="height: 2.5em; margin: 0;" />

        ## Exercise: Classes and inheritance

        1. In the cell below, create a class named `Dog` that represents dogs. The constructor, `__init__()`, should take one argument in addition to `self`: the dog's name. The class should implement one additional method, which is `speak()`. The `speak()` method should `return` some dog-appropriate sound, for example `"Arf!"`.
        2. Create a list of several instances of the `Dog` class, and iterate through the list printing each dog's name and the sound they return when you call the `speak()` method.
        3. Derive a `Poodle` class from the `Dog` class such that instances of the `Poodle` class return a more poodle-appropriate sound, like `"Yip!"`, when you call the `speak()` method.
        4. Add some instances of the `Poodle` class to your list of dogs, so list contains some `Dog` instances and some `Poodle` instances, and then re-run the code that iterates through the list.
        """
    ).style(
        {
            "padding": "1.5em",
            "margin-top": "1em",
            "border-radius": "0.5em",
            "box-shadow": "0 0 0.5em #ced4da",
        }
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
