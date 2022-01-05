Welcome to the Lecture 2 folder!

In this folder, the sorting problem is covered.

The sorting problem is as follows:

Given a sequence of length n, the sorting algorithm aims to order the elements of the sequence such that they are returned in increasing order. The Insertion Sort algorithm is the first sorting algorithm presented.

Insertion Sort is intuitive and similar to the way people sort a hand of playing cards. The person starts with an empty left hand (the sorted hand) and a full set of unsorted cards on the table. One by one, a card is removed from the table and is placed among the sorted left hand by comparing the value of the chosen card with the value of the cards already in the sorted hand. At the end, all the cards from the table have been removed and placed in the left hand, where there is now an ordered sequence of length n. 

Formally, the algorithm for Insertion Sort is as follows:

We start by looping through the input array with j using a range from the second element of the array to the nth element of the array (inclusive). In the body of the for loop, we assign a variable named 'key' to be the jth element of the array. Next, we assign a variable 'i' to be the j - 1 element of the array, right before the jth element. Furthermore, in the body of the for loop, we initialize a while loop conditioned on i >= 0 and the ith element of the array > key. While the above conditions hold true, we set the i + 1 element of the array to be equal to the ith element, effectively swapping the two elements. Then, still in the body of the while loop, we decrement the value of i by 1. Once exited the while loop, we set the i + 1 element to be equal to the key.

Note Insertion Sort can be seen as an inductive/recursive algorithm. Its base case is the simplest version of the problem, inserting an element into a sorted array of size 0, so just inserting that element into a now size 1 array, which by itself is considered sorted. Given an already sorted array of size k, it is an algorithm that inserts element k + 1 into the sorted array and sorts that array. 

Consider Insertion Sort's efficiency.

The best case is when the input array is already sorted in increasing order. In this case, the algorithm will still have to progress through n iterations of the for loop, but the while loop is restricted to constant time, since preceding elements will never be larger than succeeding elements. Therefore, the best case running time is O(n).

The worst case is when the input array is sorted in decreasing order. In this case, the algorithm will run n iterations of the for loop. For every iteration of the for loop, the while loop will compare and shift the entire sorted subsection of the array before inserting the next element, which is at most n steps. This yields a worst case running time of O(n * n) = O(n^2).

