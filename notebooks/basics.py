import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python Basics
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return (mo,)


@app.cell
def _():
    print("Hello world!")
    return


if __name__ == "__main__":
    app.run()
