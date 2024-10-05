#!/usr/bin/env python3
"""Module that defines a function to calculate the derivative of a polynomial."""

def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial.

    Args:
        poly (list): A list of coefficients representing a polynomial, where the index represents the power of the variable.
    
    Returns:
        list: A list of coefficients representing the derivative of the polynomial.
        None: If the input is not a valid polynomial (i.e., not a list or an empty list).
    """
    
    # Initialize an empty list to store the derivative
    deriv = []

    # Check if the input is a valid non-empty list
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    # If the polynomial is a constant (degree 0), return [0]
    if len(poly) == 1:
        return [0]

    # Calculate the derivative by multiplying each coefficient by its corresponding power
    for i in range(1, len(poly)):
        deriv.append(poly[i] * i)

    # Return the derivative as a list of coefficients
    return deriv