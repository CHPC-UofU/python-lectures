import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="public/dictionaries.svg" style="width: 10em; margin: auto; margin-bottom: 5em;" />

    # Dictionaries
    * A dictionary (also known as a "hash" or "associative array") is a collection of `key:value` pairs
    * You can create dictionaries with the `dict()` command or with `key:value` pairs between the `{`and `}` (**curly brace**) symbols
      * Recall that `{` and `}` were also used to define a set; dictionaries and sets are distinct, and you can tell them apart because dictionaries *always* have pairs of associated values separated by `:`
        * `{1, 2, 3, 4}` is a set
        * `{1: 2, 3: 4}` is a dictionary
    * The keys in a dictionary must be unique
    * The values can be of any type
    * The lookup on a key is **extremely** fast
    """)
    return


@app.cell
def _():
    # What's the type of the variable below? How does this differ from a set?
    elements = {"H": "hydrogen", "He": "helium", "Li": "lithium", "Be": "berylium"}

    elements["B"] = "boron"

    print(f"The element whose symbol is H is {elements['H']}.")
    print(f"Does the dictionary include carbon? {'C' in elements}.")
    print("Here are the symbols:", list(elements.keys()))
    print(f"The element name for symbol 'Po' is: {elements.get('Po', 'unknown')}.")
    return (elements,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What if the key isn't in the dictionary?
    """)
    return


@app.cell
def _(elements):
    print(f"The element whose symbol is N is {elements['N']}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An attempt to access a missing key generates a `KeyError` exception. We'll learn about exception handling next (in the next notebook).

    <div style="margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da; display: flex; flex-wrap: nowrap; overflow: hidden;">
      <div style="background-color: #be0000; width: 10%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;"><img src="public/tutorial.svg" style="width: 100%; height: auto; max-height: 100%; object-fit: contain; display: block;"></div>
      <div style="padding: 1.5em;">
        <p style="font-weight: bold; margin: 0; font-size: 1.2em; color: #be0000;">Tutorial</p>
        <p style="margin: 0;">More information about dictionaries is available in the Python tutorial.</p>
        <a style="background-color: #be0000; color: white; text-decoration: none; padding: 0.5em 1em; margin-top: 1em; margin-bottom: 0; border-radius: 0.25em; display: inline-block; font-weight: bold;" href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">Read more about dictionaries&nbsp;&rarr;</a>
      </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="public/exercise.svg" style="height: 2.5em; margin: 0;" />

    <h2>Exercise: Improved <em>Hello, world</em> function</h2>

    <p>Revise this <code>hello_world()</code> function so that it can greet you in several different languages. Your function must accept one argument, which is the name of the language to use for the greeting, and that argument should default to some language if no value is given.</p>

    <p><em>Hint: this is a nice use case for a dictionary.</em></p>

    </div>
    """)
    return


@app.function
def hello_world():
    print("Hello, world!")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="padding: 1.5em; margin-top: 1em; border-radius: 0.5em; box-shadow: 0 0 0.5em #ced4da;">

    <img src="public/exercise.svg" style="height: 2.5em; margin: 0;" />

    <h2>Exercise: Bioinformatics! DNA to protein translation</h2>

    <p>This exercise puts it all together: functions, strings, modules, and dictionaries.</p>

    <p>The <a href="https://en.wikipedia.org/wiki/Genetic_code">genetic code</a> provides a mapping from the 4-letter alphabet of DNA (A, C, G, and T) to the 20-letter code of amino acids, that make up proteins. Three consecutive DNA "letters," called a codon, maps onto a single amino acid letter. For example, the DNA string "ATG" maps onto the amino acid letter "M." Using the provided module geneticcode.py, which defines the genetic code as a dictionary named <code>codons</code>, write a function that translates a DNA string to its amino acid sequence.</p>

    </div>
    """)
    return


@app.cell
def _():
    # Here's a DNA sequence to translate:
    dna_sequence = "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCC"
    # Write a function that translates this into an amino acid sequence using the codons dictionary from the
    # geneticcode module and call your function with this sequence. This 36-letter DNA sequence should translate
    # into a 12-letter amino acid sequence.
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
