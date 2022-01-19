In this lecture, Merge Sort and O(nlogn) divide and conquer algorithms are discussed.

Merge Sort is an algorithm that attempts to solve the previously-discussed sorting problem. In particular, Merge Sort can be seen as an improved version of Insertion Sort. 

Merge Sort keeps the same base case. That is, if the length of the array to be sorted is equal to 1, then we just return the array itself, since an array of size 1 is considered
already sorted. 

In the recursive step, we define a midpoint of the array to be sorted, sort all the values to the left of the midpoint (by inductive hypothesis), sort all values to the right
of the midpoint (by inductive hypothesis), and then merge the two sorted arrays together such that the final merged array is, too, sorted. 

To determine the runtime recurrence, it is important to note that Merge Sort has two recursive calls, one to sort the sub-array left of the midpoint (first-half) and one to sort the
sub-array to the right of the midpoint (second-half). On top of that, it has a merge procedure which merges the two sorted sub-arrays. The two recursive calls clearly take 
T(n/2) time, as the procedure is evaluating a half-sized input, and the merge procedure takes O(n) time. Together, the runtime recurrence can be expressed as T(n) = 2T(n/2) + cn.
Expanding this recurrence yields a runtime of O(nlgn). 

To quickly determine recurrence relations, we discussed the Simplified Master Theorem (SMT), which is a set of common runtime recurrences. 

We also discussed the counting inversions problem. Formally, the counting inversions problem takes an array of values as input and returns the number of inversions present in that array.
Two elements i, j of an array are considered inverted if i < j but A[i] > A[j]. We see that setting a target runtime of O(nlgn) is helpful in guiding us toward a solution by 
gifting us the methodology similar to merge sort. I will write that up soon. 
