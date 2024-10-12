#!/usr/bin/env python3
"""
Create a class Binomial that represents a binomial distribution
"""


class Binomial:
    """
    Class that represents a binomial distribution
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initializes the Binomial distribution.
        """
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = float(sum(data) / len(data))
            var = float(sum(map(lambda n: (n - mean) ** 2, data)) / len(data))
            self.p = 1 - (var / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n

    def factorial(self, k):
        """
        Calculates the factorial of a given number k.
        """
        result = 1
        for i in range(1, k+1):
            result *= i
        return result

    def pmf(self, k):
        """
        Calculates the Probability Mass Function (PMF)
        for a given number of successes `k`.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        # PMF formula: (nCk) * (p^k) * (1-p)^(n-k)
        n_fact = self.factorial(self.n)
        k_fact = self.factorial(k)
        n_k_fact = self.factorial(self.n - k)
        binom_coeff = n_fact / (k_fact * n_k_fact)
        p_term = self.p ** k
        q_term = (1 - self.p) ** (self.n - k)
        
        # Return the final result
        return binom_coeff * p_term * q_term

# Return the final result
return binom_coeff * p_term * q_term

    def cdf(self, k):
        """Calculates the Cumulative Distribution Function (CDF)
        afor a given number of successes `k`.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return sum([self.pmf(i) for i in range(0, k+1)])
