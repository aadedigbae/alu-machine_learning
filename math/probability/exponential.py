#!/usr/bin/env python3
"""
Script to define an Exponential distribution class with methods
to compute the Probability Density Function (PDF) and Cumulative Distribution Function (CDF).
"""

class Exponential:
    """
    Represents an Exponential distribution, providing methods
    to calculate the PDF and CDF based on the rate parameter (lambtha).
    """

    e = 2.7182818285  # Approximation of Euler's number

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Exponential distribution.

        Args:
            data (list): A list of data points from which to calculate the rate parameter `lambtha`.
            lambtha (float): The rate parameter (inverse of the expected value), must be positive.
        
        Raises:
            ValueError: If `lambtha` is not positive or if `data` contains fewer than two values.
            TypeError: If `data` is not a list.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate lambtha as the inverse of the mean of the data
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """
        Calculates the Probability Density Function (PDF) for a given value `x`.

        Args:
            x (float): The value to calculate the PDF for (must be non-negative).

        Returns:
            float: The PDF value for the given `x`. Returns 0 if `x` is negative.
        """
        if x < 0:
            return 0
        # PDF of an Exponential distribution: f(x) = λ * e^(-λx)
        return self.lambtha * (Exponential.e ** (-self.lambtha * x))

    def cdf(self, x):
        """
        Calculates the Cumulative Distribution Function (CDF) for a given value `x`.

        Args:
            x (float): The value to calculate the CDF for (must be non-negative).

        Returns:
            float: The CDF value for the given `x`. Returns 0 if `x` is negative.
        """
        if x < 0:
            return 0
        # CDF of an Exponential distribution: F(x) = 1 - e^(-λx)
        return 1 - (Exponential.e ** (-self.lambtha * x))
