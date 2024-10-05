#!/usr/bin/env python3

"""
Module that defines a function to calculate the integral of a polynomial.
"""


def poly_integral(poly, C=0):
    """
    Computes the coefficients of the integral of a polynomial function.
    """

    # Check if poly is a valid list and C is a numeric value
    if not isinstance(poly, list) or not isinstance(C, (int, float)) or not poly:
        return None

    # Ensure all elements in the polynomial are numbers (int or float)
    if not all(isinstance(coefficient, (int, float)) for coefficient in poly):
        return None

    # Start the integral with the constant of integration C
    integrals = [C]

    # Apply the integral rule for each coefficient
    for power, coefficient in enumerate(poly):
        integral = coefficient / (power + 1)
        # Append as an integer if the result is an integer, else as a float
        integrals.append(
            int(integral) if integral.is_integer() else integral
        )

    # Remove trailing zeros from the result (except for the constant of integration)
    while integrals[-1] == 0 and len(integrals) > 1:
        integrals.pop()

    return integrals
