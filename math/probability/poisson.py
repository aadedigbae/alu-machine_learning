#!/usr/bin/env python3
"""
This module represents the Poisson distribution.
"""

class Poisson:
    """
    Represents a Poisson distribution for discrete probability analysis.
    """

    def factorial(self, k):
        """
        Calculates the factorial of a given non-negative integer `k`.

        Args:
            k (int): The number to calculate the factorial for.

        Returns:
            int:Returns 1 for k = 0 or 1, and 0 if k is negative.
        """
        if k < 0:
            return 0
        if k in [0, 1]:
            return 1
        return k * self.factorial(k - 1)

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes a Poisson distribution.

        Args:
            data (list): 
            lambtha (float)
            
        Raises:
            ValueError: If `lambtha` is not positive
            TypeError: If `data` is not a list.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the Probability Mass Function (PMF)
        for a given number of successes `k`.

        Args:
            k (int): The number of events to calculate the PMF for.

        Returns:
            float: The PMF value for the given number of successes.
        """
        if k < 0:
            return 0
        k = int(k)
        e = 2.7182818285  # Euler's number (approximate value)
        return (self.lambtha ** k) * (e ** (-self.lambtha)) / self.factorial(k)

    def cdf(self, k):
        """
        Calculates the Cumulative Distribution Function (CDF)
        for a given number of successes `k`.

        Args:
            k (int): The number of events to calculate the CDF for.

        Returns:
            float: The CDF value up to the given number of successes.
        """
        k = int(k) if isinstance(k, (int, float)) else k
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
