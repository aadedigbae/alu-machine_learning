#!/usr/bin/env python3
"""Let's get the correlation matrix"""
import numpy as np


def correlation(C):
    """Calculates the correlation matrix from a covariance matrix"""
    if not isinstance(C, np.ndarray):
        raise TypeError('C must be a numpy.ndarray')
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError('C must be a 2D square matrix')

    stddevs = np.sqrt(np.diag(C))  # Standard deviations
    outer_stddevs = np.outer(stddevs, stddevs)  # Outer product

    cor = C / outer_stddevs  # Normalize matrix to get correlation 
    cor[C == 0] = 0  # Prevent division

    return cor
