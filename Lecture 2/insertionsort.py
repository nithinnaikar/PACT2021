# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:55:02 2022

@author: Nithin
"""

a = list(map(int, input().split()))

def insertion_sort(array):
    '''
    Insertion Sort function used to sort array of numbers in place.

    Parameters
    ----------
    array : one-dimensional sequence of real numbers

    Returns
    -------
    None

    '''
    for j in range (1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key

insertion_sort(a)
print(a)
