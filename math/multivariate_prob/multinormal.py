#!/usr/bin/env python3
"""let's get the class MultiNormal"""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Constructor"""
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError('data must be a 2D numpy.ndarray')
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean, self.cov = self.mean_cov(data)

    @staticmethod
    def mean_cov(X):
        """Calculates the mean and covariance of a dataset"""
        d, n = X.shape
        m = np.mean(X, axis=1, keepdims=True)  # Mean vector
        C = np.matmul(X - m, (X - m).T) / (n - 1)  
        return m, C

    def pdf(self, x):
        """Calculates the PDF at a data point"""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError(f'x must have the shape ({d}, 1)')

        m = self.mean
        cov = self.cov
        bottom = np.sqrt(((2 * np.pi) ** d) * np.linalg.det(cov)) 
        inv = np.linalg.inv(cov)  # Covariance inverse
        exp = (-0.5 * np.matmul(np.matmul((x - m).T, inv), (x - m)))
        result = (1 / bottom) * np.exp(exp[0][0])
        return result
