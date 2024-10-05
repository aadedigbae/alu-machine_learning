#!/usr/bin/env python3
"""Function that calculates the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial.

    Args:
        poly (list): A list of coefficients representing a polynomial
        C (int): The constant of integration (default is 0).

    Returns:
        list: A list of coefficients
        representing the integral of the polynomial
    """

    integral = []
    # Check if poly is a valid list and C is an integer
    if not isinstance(poly, list) or len(poly) == 0 or not isinstance(C, int):
        return None
    # Calculate the integral for each coefficient
    for i in range(len(poly) - 1, 0, -1):
        integral.append(poly[i] / (i + 1))
    # Append the coefficient for the constant term
    integral.append(poly[0])
    integral.append(C)
    # Handle the case where the polynomial is a constant zero
    if len(poly) == 1 and poly[0] == 0:
        integral = [C]
    # Convert integral coefficients to integers if they are whole numbers
    for i in range(len(integral)):
        if integral[i] % 1 == 0:
            integral[i] = int(integral[i])
    # Reverse the list to get the correct order of coefficients
    return integral[::-1]
