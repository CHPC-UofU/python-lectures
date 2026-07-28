import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/operators.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Operators

    Python has all the operators you typically find in a programming language. **We will use most of these as we learn more about the language, so you don't need to try to memorize them now.**

    * Assignment operator `=`
    * Arithmetic operators `+`, `-`, `*`, `/`, `+=`, `-=`, `*=`, `/=`, `**` (exponentiation), `%` (modulo), and `//` (floor division)
    * Comparison operators `==`, `!=`, `<`, `>`, `<=`, and `>=`
    * Logical operators `and`, `or`, and `not`
      * the `and` and `or` operators use [short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation)
    * Operator precedence with parentheses `(` and `)` (see https://docs.python.org/3/reference/expressions.html#operator-precedence)
    * Identity/membership operators: `is` and `in`
    * Bitwise operators `<<` (left shift), `>>` (right shift), `|` (bitwise or), `&` (bitwise and), and `^` (complement)
    * Assignment expressions with `:=`

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/documentation.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Documentation</p>
        <p style="margin: 0;">A list of operators is available on the Python documentation.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/library/stdtypes.html">Read more about operators&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Supplemental material: Examples of using operators in practice

    The examples below use features of Python that we haven't seen yet. We'll learn more about operators as we use them, but if you're not sure what they're used for, looking at some of the examples here may help contextualize them.
    """)
    return


@app.cell
def _():
    # Assignment
    my_variable = 12345
    return


@app.cell
def _():
    # Arithmetic operators
    my_variable_1 = 1 + 1  # similar for - (subtraction), * (multiplication), / (division)
    my_variable_1 = my_variable_1 + 1  # similar for -= (subtract from current value), *= (multiply current value by), /= (divide current value by)
    #           ^ shorthand for my_variable = my_variable + 1
    my_variable_1 = 5 ** 2
    my_variable_1 = 23 % 5  # 23 / 5 = 4 remainder 3, and % keeps only the remainder, so 23 % 5 is 3
    my_variable_1 = 23 // 5  # 23 / 5 = 4 remainder 3, and // drops the remainder, so 23 // 5 is 4
    return


@app.cell
def _():
    # Comparison operators
    my_variable_2 = True and True  # True and True == True
    my_variable_2 = True and (not False)  # True and (True) == True
    my_variable_2 = True or not True  # True or (False) == True
    # See https://en.wikipedia.org/wiki/Boolean_algebra#Basic_operations for more information

    def infinite_loop():
        while True:
            pass
    my_variable_2 = True or infinite_loop()  # This has been "short-circuited" to True because "True or …" will always be True  # The infinite loop never runs
    return


@app.cell
def _():
    # Bitwise operators
    # Unless you know you will be working with individual bits, you can likely ignore these altogether
    # Most new Python users, and perhaps most Python users more generally, do not need to know how to use bitwise operators
    my_variable_3 = 1 << 5  # 1 * 2**5 = 32
    my_variable_3 = 64 >> 1  # 64 // 2**1 = 32
    my_variable_3 = 1 | 1  # 1 or 1 = 1
    my_variable_3 = 1 & 1  # 1 and 1 = 1
    my_variable_3 = 1 ^ 1  # 1 xor 1 = 0 (exclusive or)
    return


@app.cell
def _():
    my_variable_4 = 'hello'
    my_variable_4 = 'h' in my_variable_4  # "h" is in "hello", so this is True
    a = (1,)
    # Be careful! "is" tests whether two objects are the exact same object
    # Use == to test for equality
    b = (1,)
    print('a:', a)
    print('b:', b)
    print('a is b:', a is b)
    print('a == b:', a == b)
    print('id(a):', id(a))
    print('id(b):', id(b))
    b = a
    print('a:', a)
    print('b:', b)
    print('a is b:', a is b)
    print('a == b:', a == b)
    print('id(a):', id(a))
    print('id(b):', id(b))
    return


app._unparsable_cell(
    r"""
    my_variable = \"The quick brown fox jumps over the lazy dog\"

    # The walrus operator, :=, can be used to set a variable in the middle of an expression
    # It can make some scripts more concise, but it is never necessary to use the walrus operator (see example below*)
    if (index := my_variable.find(\"fox\")) != -1:  # -1 is the index .find() returns if there are no matches
        print(my_variable[index:])

    # *This is identical to doing the following:
    index = my_variable.find(\"fox\")
    if index != -1:
        print(my_variable[index:])

    # Note that parentheses are essential when using the walrus operator:
    if (a := True) and (b := False):
        pass

    # Without the parentheses, Python doesn't know where the inline definition ends
    if a := True and b := False:
        pass
    """,
    name="_"
)


@app.cell
def _():
    # Operator precedence
    print("(2 * 3) + 1 is", (2 * 3) + 1)
    print("2 * (3 + 1) is", 2 * (3 + 1))
    return


if __name__ == "__main__":
    app.run()
