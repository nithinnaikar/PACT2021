# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:39:23 2022

@author: Nithin
"""

a = list(map(int, input().split()))

def linear_search(array, element):
    '''
    Non-recursive linear search function used to search for an element in an array.

    Parameters
    ----------
    array : one-dimensional sequence of real numbers

    Returns
    -------
    Boolean: True if element is in array, False otherwise

    '''
    for i in range(len(array)):
        if array[i] == element:
            return True
    return False

def recursive_linear_search(array, element):
    '''
    Recursive linear search function used to search for an element in an array.

    Parameters
    ----------
    array : one-dimensional sequence of real numbers

    Returns
    -------
    Boolean: True if element is in array, False otherwise

    '''
    # Base case n = 1
    if len(array) == 1:
        return array[0] == element
    # Recursive step
    else:
        return (array[-1] == element) or (recursive_linear_search(array[:-1], element))
