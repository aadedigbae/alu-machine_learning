#!/usr/bin/env python3
"""
Script to model and calculate values related to a Poisson distribution.
"""


class Poisson():
    """
    A class representing a Poisson distribution, providing methods 
    to calculate the Probability Mass Function (PMF) and the Cumulative 
    Distribution Function (CDF).
    """
    e = 2.7182818285  # Approximation of Euler's number, used in calculations.
    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson distribution.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)  # Estimate lambtha from data
    def pmf(self, k):
        """
        Calculates the Probability Mass Function (PMF) 
        for a given number of occurrences (k).
        """
        k = int(k)
        if k < 0:
            return 0
        factorial_k = 1
        for i in range(1, k + 1):
            factorial_k *= i  # Calculate the factorial of k
        # PMF formula: (e^(-λ) * λ^k) / k!
        pmf = Poisson.e ** -self.lambtha * self.lambtha ** k / factorial_k
        return pmf
    def cdf(self, k):
        """
        Calculates the Cumulative Distribution Function (CDF)
        for a given number of occurrences (k).
        """
        k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)  # Sum of PMFs from 0 to k
        return cdf
