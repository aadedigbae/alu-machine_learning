#!/usr/bin/env python3
"""Let's get the mean and covariance of a data set"""
import numpy as np


def mean_cov(X):
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError('X must be a 2D numpy.ndarray')
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")
    m = np.mean(X, axis=0, keepdims=True)  # Mean of the data points
    C = np.matmul((X - m).T, (X - m)) / (n - 1)  # Covariance matrix
    return m, C