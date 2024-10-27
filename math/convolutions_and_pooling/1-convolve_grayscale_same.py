#!/usr/bin/env python3
"""Performs same convolution on grayscale using a given kernel"""


import numpy as np


def convolve_grayscale_same(images, kernel):
    """Applies same convolution keeping input and output equal"""
    kh, kw = kernel.shape
    m, hm, wm = images.shape
    ph = int(kh / 2)
    pw = int(kw / 2)
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    convoluted = np.zeros((m, hm, wm))
    for h in range(hm):
        for w in range(wm):
            square = padded[:, h: h + kh, w: w + kw]
            insert = np.sum(square * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = insert
    return convoluted
