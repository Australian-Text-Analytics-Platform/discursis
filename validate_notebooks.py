#!/usr/bin/env python3
import pathlib
import sys
from typing import Union

import click
import nbformat


@click.command()
@click.argument("filename")
def validate(filename):
    try:
        is_notebook_valid(filename)
        print(f"{filename} is valid")
        sys.exit(0)
    except nbformat.ValidationError as error:
        print(f"{filename}", error)
        sys.exit(1)


def is_notebook_valid(path: Union[str, pathlib.Path]):
    with open(path) as file_in:
        notebook = nbformat.read(file_in, nbformat.NO_CONVERT)
    format_version = notebook["nbformat"]

    return nbformat.validate(notebook, version=format_version)


if __name__ == "__main__":
    validate()
