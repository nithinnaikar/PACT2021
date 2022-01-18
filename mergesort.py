# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:40:07 2022

@author: Nithin
"""
import math

def Merge(array1, array2):
   '''
   Merge function used to merge two sorted arrays into one sorted array.
   
   Parameters
   ----------
   
   array1: one-dimensional sorted sequence of real numbers
   array2: one-dimensional sorted sequence of real numbers
   
   Returns
   -------
   
   sorted_array: sorted one-dimensional sequence of real numbers 
   '''
   
       
   if len(array1) == 0:
       return array2
   elif len(array2) == 0:
       return array1
   elif array1[0] < array2[0]:
       return ([array1[0]] + Merge(array1[1:], array2))
   else:
       return ([array2[0]] + Merge(array1, array2[1:]))
   
def merge_sort(array):
   '''
   Merge sort function used to sort an array of numbers in increasing order.
   
   Parameters
   ----------
   
   array: one-dimensional sequence of real numbers

   
   Returns
   -------
   
   sorted_array: sorted one-dimensional sequence of real numbers (increasing order)
   '''
   n = len(array)
   if n == 1:
       return array
   else:
       return Merge(merge_sort(array[:math.ceil(n/2)]), merge_sort(array[math.ceil(n/2):]))

print(merge_sort([5, 4, 3, 2, 1]))