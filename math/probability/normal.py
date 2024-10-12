#!/usr/bin/env python3
"""
Script to calculate a Normal distribution
for continuous variables.
"""

class Normal:
    """
    Represents a Normal (Gaussian) distribution.
    """

    pi = 3.1415926536  # Approximation of Pi
    e = 2.7182818285   # Approximation of Euler's number

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initializes the Normal distribution.

        Args:
            data (list): List of data points to calculate the mean and standard deviation.
            mean (float): Mean of the distribution (used if no data is provided).
            stddev (float): Standard deviation of the distribution (must be positive).
        
        Raises:
            ValueError: If `stddev` is not positive or if `data` contains fewer than two values.
            TypeError: If `data` is not a list.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            sigma = 0
            for i in range(0, len(data)):
                x = (data[i] - self.mean) ** 2
                sigma += x
            self.stddev = (sigma / len(data)) ** 0.5

    def z_score(self, x):
        """
        Calculates the z-score of a given value `x`.

        Args:
            x (float): Value for which to calculate the z-score.

        Returns:
            float: The z-score of `x`.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value corresponding to a given z-score `z`.

        Args:
            z (float): Z-score for which to calculate the x-value.

        Returns:
            float: The x-value corresponding to `z`.
        """
        return self.stddev * z + self.mean

    def pdf(self, x):
        """
        Calculates the Probability Density Function (PDF) for a given value `x`.

        Args:
            x (float): Value for which to calculate the PDF.

        Returns:
            float: The PDF value for `x`.
        """
        p1 = 1 / (self.stddev * ((2 * Normal.pi) ** 0.5))
        p2 = ((x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        return p1 * Normal.e ** (-p2)

    def cdf(self, x):
        """
        Calculates the Cumulative Distribution Function (CDF) for a given value `x`.

        Args:
            x (float): Value for which to calculate the CDF.

        Returns:
            float: The CDF value for `x`.
        """
        xa = (x - self.mean) / ((2 ** 0.5) * self.stddev)
        errof = (((4 / Normal.pi) ** 0.5) * (xa - (xa ** 3) / 3 +
                                             (xa ** 5) / 10 - (xa ** 7) / 42 +
                                             (xa ** 9) / 216))
        cdf = (1 + errof) / 2
        return cdf
