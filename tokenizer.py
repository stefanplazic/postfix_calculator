# -*- coding: utf-8 -*-
"""Modul omogućava parsiranje aritmetičkih izraza."""
import re


__author__ = 'me'


REGEX = r'(?:[-]?\d*\.\d+|\d+)|(?:-?\d+)|(?:[()+\-\^/*]|(?:[A-Za-z]+))'


def tokenize(expression):
    """Funkcija kreira tokene na osnovu zadatog izraza.

    Postupak formiranja liste tokena koristi regularni izraz
    zadat putem REGEX varijable. Omogućeno je pronalaženje
    sledećih tipova tokena:
        - floating-point vrednosti
        - celobrojne vrednosti
        - operatori +, -, *, /, ^
        - zagrade

    Args:
        expression (string): Izraz koji se parsira.

    Returns:
        list: Lista pronađenih tokena.

    Raises:
        AssertionError: Ako izraz nije zadat kao string.
    """
    assert isinstance(expression, str), "Expression should be string!"
    return re.findall(REGEX, expression)


if __name__ == '__main__':
    #
    # key: izraz, value: očekivana lista tokena
    #
    test_cases = {
        # test floats
        "-3.14   ^2": ['-3.14', '^', '2'],
        "(2.08- .03) ^  2": ['(', '2.08', '-', '.03', ')', '^', '2'],
        "(2.08-.03) ^  2": ['(', '2.08', '-.03', ')', '^', '2'],
#
#        # test integers
#        "2+(3*4)": ['2', '+', '(', '3', '*', '4', ')'],
#        "22     56": ['22', '56'],
#        "-44 -     56": ['-44', '-', '56'],
        "-44  -56": ['-44', '-56'],
        "-24-(-55)": ['-24', '-', '(', '-55', ')'],
        "3 + -3": ['3', '+', '-3']
#        "-24-(-55)": ['-24', '-', '(', '-', '55', ')'],    #AssertionError
#
        #"a b": ['a', 'b']
        # test invalid
#        "ab cd": [],
#        "10,22": ['10', '22']
    }

    for expression, expected in test_cases.items():
        assert expected == tokenize(expression)