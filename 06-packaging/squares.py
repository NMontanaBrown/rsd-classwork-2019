"""Computation of weighted average of squares."""
from argparse import ArgumentParser
from numpy import sqrt

def average_of_squares(list_of_numbers, list_of_weights=None):
    """
    Return the weighted average of the square of each item in a list of values.
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.

    Example:
    -------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length
    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return float(sum(squares) /len(squares))


def convert_numbers(list_of_strings):
    """
    Convert a list of strings into numbers, ignoring whitespace.

    Example:
    -------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]
    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]


if __name__ == "__main__":
    # python squares.py <numbers file> <weights file>
    parser = ArgumentParser(description="Type two numbers")
    parser.add_argument('--numberFile', '-n')
    parser.add_argument('--weightFile', '-w')
    parser.add_argument('--sqrt', '-sqrt')

    arguments = parser.parse_args()

    with open(arguments.numberFile, "r") as numbers_file:
        numbers_strings = numbers_file.readlines()

    numbers = convert_numbers(numbers_strings)
    # TODO Can we make this optional, so that we don't need a weights file?
    if (arguments.weightFile):
        with open(arguments.weightFile, "r") as weights_file:
            weight_strings = weights_file.readlines()

        weights = convert_numbers(weight_strings)
        
    else:
        weights = None

    result = average_of_squares(numbers, weights)

    # TODO Can we add the option of computing the square root of this result
    if(arguments.sqrt):
        root = sqrt(result)

    # TODO Can we write the result in a file instead of printing it?

    print(result, root)
