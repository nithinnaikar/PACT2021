The searching problem is covered.

The searching problem is as follows:

Given a sequence of length n and a target element, the searching algorithm aims to return whether the element is present in the array or not. Two algorithms, linear and binary
search are presented.

Linear search is a brute-force method that involves iterating over every element of the array and continuously checking whether the element at the current index is the target
element. If it is, the algorithm returns True. If the algorithm exits the loop without returning True, the target element is not present and therefore it returns False.

We can derive the running time for Linear Search without performing any tedious algebraic expressions by simply looking at the dominant blocks of code in the program. With that
being said, consider the overarching for loop. In the worst case, the target element is not in the array and the algorithm has to perform n iterations with the body of the for loop
executed in constant time, and therefore the worst case running time is O(n).

Linear search can also be seen as an inductive/recursive algorithm. 

First, sketch out a base case. This is the simplest possible version of the problem. In this case, the base case is when n = 1. 
Then, write out the recursive step. This generalizes the solution. In this case, it is done by returning True if the last element of the array is the target element or 
LinearSearch(array[1...n-1], element) returns True. 

This is an abstract concept, so it may be better to understand it with a small example, say n = 3 and array = [1, 2, 3], element = 2.

First, check if n == 1. No. Move on to the next block. Is the last element == 2? False. Create a new scope and evaluate LinearSearch(array[1..2], element = 2)

First, check if n == 1. No. Move on to the next block. Is the last element == 2? Yes. Return True to the function that called it in previous scope. 

Main program returns True.

This being a recursive solution, let's try evaluating the running time with a runtime recurrence. Let T(n) denote the running time. For linear search, the base case is when
n = 1, so T(n = 1) = T(1 - 1) = T(0) = 1 (constant time). Else, for n >= 1, generalize the form to be of T(n) = T(n - 1) + c, where c is some constant to account for miscellaneous
operations. Solving this recurrence yields a running time T(n) = O(n). 

That was linear search on an array. But what kind of array? An unsorted array.

If the array was sorted, much more computationally-efficient algorithms are present- like Binary Search.

Formally, Binary Search is as follows:

First,  assert that the input array is sorted.

Next, set variables called 'low' and 'high' to be pointers that point to the start and end of the array, respectively. Set a variable called 'mid' to be the midpoint index
of the array, integer-floored if needed. 

Next, if the array indexed at mid is == to the target element, then hooray. We have just won the lottery, at least for large n. But this is unlikely, let's continue.

Else, if the array indexed at mid is < target element, then we can simply reduce the array search space to array[mid+1...high]. Why? Since the array sorted and we know that
the element in the midth position is < target element, then it only follows that the target element can be to the right of the midpoint, since all values to the left are less
than the target element and would be a waste of time to search in that portion. 

Likewise, if the array indexed at mid is > target element, then we can reduce the array search space to array[low...mid-1] using the same reasoning.

Once we have identified what halve of the array the target element is in, we simply use a recursive call BinarySearch(halved-array, element) and then evaluate recursively.

This is the main benefit for having a sorted array. 

Let's evaluate the running time.

Since Binary Search is recurrent in nature, let's use a runtime recurrence. Let T(n) denote the running time. Base case is same as linear search, T(0) = 1. Elsewise, for larger
values of n, the recurrence is of the form T(n) = T(n/2) + c. Why? Since at each step of binary search we are halving the search space, we recursively evaluate the algorithm
on an input of size n/2. Expanding the recurrence yields a general form of T(n) = T(n/2^k) + kc, where k is the number of steps in binary search. Since we are most interested in
the worst-case, we want to evaluate the runtime whenever binary search has halved the array down to a single element, since that is precisely the worst case. This is represented
by n/2^k < 1, which evaluates to k > lgn. Thus, we get T(n) = T(0) + c(lgn + 1), which is O(lgn).

Note that logarithmic complexity is your friend. It is a very slow-growing function of n relative to linear complexity and polynomial complexity. When given a sorted array,
Binary search is much, much better than linear search for asympotically large values of n.

Now that we have understand recurrences, we can revisit our first sorting algorithm, Insertion Sort, and build a recursive version of that. 

Base case, if n == 1, then return the array as is, since an array of one element is itself a sorted array. In the recursive step, set a variable array_prime to be the sorted version of elements 1 through n - 1 (i.e. set array_prime = InsertionSort(array[1:n-1])), by the Induction Hypothesis we assume that the procedure can sort an array of size k, where k is some positive integer. In the inductive step, we insert the last element of the array (i.e. array[n]) into the sorted array array_prime. It is important to note that the Insert function is not a simple appendage, but works by comparing the value of the element to be sorted with the already-sorted array in order to determine where it goes. The Insert function in recursive insertion sort works analogous to the while loop of the original sort, continually swapping the element in hand with values in the sorted array until the array is fully sorted. This, as previously seen, takes precisely O(n) time. 

Let T(n) be the worst-case running time of Insertion Sort on an input array whose length is denoted n. If n = 1 (base case), then Insertion Sort runs in constant time and T(n) = O(1). Otherwise, we can simply abstract the running time for an input larger than size 1 behind the recurrent function T(n - 1) + cn, since it takes T(n - 1) time to evaluate the InsertionSort function and O(n) time to evaluate the Insert function, and therefore T(n - 1) + cn time total. Evaluating this recurrence yields a solution of T(n) = O(nlgn), or a log-linear complexity. 

