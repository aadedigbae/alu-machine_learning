#!/usr/bin/env python3
"""
Script to define an Exponential distribution class with methods
"""


class Exponential:
    """
    Represents an Exponential distribution, providing methods
    to calculate the PDF and CDF based on the rate parameter.
    """
    e = 2.7182818285  # Approximation of Euler's number

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Exponential distribution.
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
        Calculates the Probability Density Function (PDF)
        for a given value `x`.
        """
        if x < 0:
            return 0
        # PDF of an Exponential distribution: f(x) = λ * e^(-λx)
        return self.lambtha * (Exponential.e ** (-self.lambtha * x))

    def cdf(self, x):
        """
        Calculates the Cumulative Distribution Function (CDF)
        for a given value `x`.
        """
        if x < 0:
            return 0
        # CDF of an Exponential distribution: F(x) = 1 - e^(-λx)
        return 1 - (Exponential.e ** (-self.lambtha * x))
