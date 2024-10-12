#!/usr/bin/env python3
"""Create a class Binomial that represents a binomial distribution
"""

class Binomial:
    """Class that represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initializes the Binomial distribution.

        Args:
            data (list): List of data points to estimate n (trials) and p (probability of success).
            n (int): Number of trials (used if no data is provided).
            p (float): Probability of success (must be between 0 and 1, exclusive).
        
        Raises:
            ValueError: If n is not positive or if p is not between 0 and 1.
            TypeError: If `data` is not a list.
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
        """Calculates the factorial of a given number k.

        Args:
            k (int): The number to calculate the factorial for.

        Returns:
            int: The factorial of k.
        """
        result = 1
        for i in range(1, k+1):
            result *= i
        return result

    def pmf(self, k):
        """Calculates the Probability Mass Function (PMF) for a given number of successes `k`.

        Args:
            k (int): The number of successes to calculate the PMF for.

        Returns:
            float: The PMF value for `k`.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        # PMF formula: (nCk) * (p^k) * (1-p)^(n-k)
        n_fact = self.factorial(self.n)
        k_fact = self.factorial(k)
        n_k_fact = self.factorial(self.n - k)
        return (n_fact / (k_fact * n_k_fact)) * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the Cumulative Distribution Function (CDF) for a given number of successes `k`.

        Args:
            k (int): The number of successes to calculate the CDF for.

        Returns:
            float: The CDF value for `k`.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return sum([self.pmf(i) for i in range(0, k+1)])
