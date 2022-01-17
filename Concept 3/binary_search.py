# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:56:14 2022

@author: Nithin
"""

import math

a = list(map(int, input().split()))

def binary_search(array, element):
    '''
    Recursive binary search function used to search for an element in a sorted array.

    Parameters
    ----------
    array : one-dimensional sorted sequence of real numbers

    Returns
    -------
    Boolean: True if element is in array, False otherwise

    '''
    low = 0
    high = len(array)
    
    if low > high:
        return False
    else:
        mid = math.floor((low + high) / 2)
        if array[mid] == element:
            return True
        elif array[mid] < element:
            return binary_search(array[mid+1:high], element)
        else:
            return binary_search(array[low:mid-1], element)
        
