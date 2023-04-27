#!/usr/bin/python3
"""
Implements the text_indentation method
"""


def text_indentation(text):
    """
    indent text? insert new lines in weird places
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
