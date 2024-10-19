#!/usr/bin/env python3
"""let's get the correlation matrix"""
import numpy as np


def correlation(C):
    """let's get the correlation matrix"""
    if not isinstance(C, np.ndarray):
        raise TypeError('C must be a numpy.ndarray')
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError('C must be a 2D square matrix')

    var_values = np.diag(np.sqrt(np.diag(C)))
    cor = var_values @ C @ var_values  # Correlation matrix
    return cor
