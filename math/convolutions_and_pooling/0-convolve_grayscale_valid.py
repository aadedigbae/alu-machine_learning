#!/usr/bin/env python3
"""Performs valid convolution on grayscale using given kernel"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Applies valid convolution between each image and kernel"""
    m, h, w = images.shape
    kh, kw = kernel.shape
    y = h - kh + 1
    x = w - kw + 1
    output = np.zeros((m, y, x))
    for i in range(y):
        for j in range(x):
            output[:, i, j] = (kernel * images[:, i: i + kh, j: j + kw])\
                .sum(axis=(1, 2))
    return output
