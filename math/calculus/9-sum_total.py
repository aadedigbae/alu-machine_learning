#!/usr/bin/env python3
#Function that squares up the summation game


def summation_i_squared(n):
    # If n is 1, return 1 since 1^2 = 1
    if n == 1:
        return 1
    
    # If n is less than 1, return None to indicate an invalid input
    if n < 1:
        return None
    
    result = (n*(n+1)*(2*n+1))//6
    return result
