This lecture we continue with divide and conquer algorithms.

In particular, we cover the closest pair problem, which is as follows:

Given a set of n points in a coordinate plane, find the closest pair of points. 

A naive solution would be to simply iterate through all possible 2-sized subsets of coordinate pairs and determine the distance between them in constant time. Then, simply return
the pair with the minimum distance. 

We can do better by considering a divide-and-conquer approach, which consists of three overarching steps:

1. Divide: We want to divide the problem into multiple sub-problems. If the coordinate plane P has sufficiently few points, then we can just utilize the brute-force method (i.e.
examine every pair and compute distances). If P has a significant amount of points, we can divide P into two halves with a vertical line L, into a set P_L and P_R. 
2. Conquer: We can recursively call the ClosestPair procedure on each half of the coordinate plane (i.e. ClosestPair(P_L) and ClosestPair(P_R)). Let delta_L be the closest pair
distance of all pairs in P_L and delta_R be the closest pair distance of all pairs in P_R. Therefore, our overall solution is delta = min(delta_L, delta_R). 
3. Combine: The above isn't right, though. Consider MergeSort. MergeSort utilizes two recursive calls to sort the left and right half of the array. But even if one sorts the left
and right halves, that doesn't necessarily make the entire array sorted because the two halves haven't been considered together. The same can be said for ClosestPair. It might be
the case that the vertical line L passes in between the closest pair of points, meaning that the minimum distance isn't delta_L or delta_R. We need to check whether there is a
closest pair with one point to the left of L and one point to the right. In order to make this less daunting, we don't necessarily need to check points whose absolute distance is 
very far from L. If a point of the closest pair whose distance from L is larger than delta, then there is no point in checking that point ("ha"). We know there cannot be a neighbor
on the other side of L that is closer than delta. With this in mind, lets create a set of points P' such that each point in P lies within delta distance from L. Then we run the 
ClosestPair procedure on P' and receive in return a distance of delta'. Our final answer is min(delta, delta'). Note that in implementation the algorithm will return the pair with
this distance, not simply the minimum distance itself. 

That was a bit brief, so let's dive into how exactly the above procedure worked.

Like the Merge function in MergeSort, we want the function that returns the minimum distance of pairs across the vertical line L to run in O(n) time. To get the desired running
time, we need to assume that the points in P' are sorted in increasing order of y-coordinate (we will come back to this later). 

Given this condition, consider a point i in P' (i.e. P'[i]). What point in P' is the closest, nearest neighbor of P'[i]? Is the closest point P'[i+1]? Just because a point
has a closer y-coordinate than other points in consideration doesn't mean its automatically closer. How far away do we need to look at? 

Lemma: If P'[i] and P'[j] are the closest points in P' and the distance between them is less than delta, then j - i <= 7. 

Proof: Let P'[i] and P'[j] be the closest points in P' whose distance from each other is less than delta. Since both points are in P' in the first place, we know that they are both
within delta of the vertical line L, since points beyond that distance are not taken into consideration. Since both points are closer to each other than delta, their y-coordinates
can differ by at most delta, clearly. Therefore, we can say that both points reside in a rectangle with width 2delta and height delta centered about the vertical line L. 

Split this rectangle into 8 equal-sized squares by dividing 2delta^2 by 8, yielding an area for each square of (delta/2)^2, and therefore a side length of delta/2. Through a 
little geometry, we can work out that the diagonal of each of these 8 squares is at most delta in length. 

Since each square lies entirely on one side of L or the other, no square can contain two points of P, or else these two points would contradict the fact that delta is the closest
pair distance on each side of the vertical line L. Therefore, there can be at most 8 points of P' in this rectangle, and therefore j - i <= 7. 

In implementation, for each P'[i], we only need to search a constant number of points, which yields a target runtime of O(n). 

The last unresolved problem was how to sort the points of P' by increasing y-coordinate. Why does this matter? Sorting by y-coordinate allowed us to restrict the nearest
neighbor search space of a given point in P' to at most 7 indices away in the array. With this in mind, we cannot afford to call a sorting algorithm, which will take 
O(nlogn) time, on a procedure who has a target O(n) running time. 

The solution is to presort the points. In particular, we store the points redundantly into two arrays X and Y sorted by their x and y coordinates respectively. This is done
by calling a sorting algorithm on P twice before the start of the algorithm. 

We no longer need the list P. 

When we split P into P_L and P_R we are actually splitting X and Y into X_L and X_R. 

To form the list P', we extract the elements of Y that are within delta distance of L and copy them to a new sorted list Y' which we search. 

We covered a lot of material, so let's review quickly. 

Presort: Given the list P, make two copies in X and Y and sort X according to x-coordinates and Y according to Y-coordinates.
Note: I don't presort in the implementation for sake of simplicity

Recursive Procedure: ClosestPair(X, Y)
Basis: If number of elements is <= 3, then brute-force and return the closest pair distance delta. 
Divide: Otherwise, let L be the median value of X (vertical line splitting plane into halves). Split both lists about this line and create new lists X_L, X_R, and Y_L, Y_R.
Conquer (with recursive procedure): delta_L = ClosestPair(X_L, Y_L), delta_R = ClosestPair(X_R, Y_R)
Combine: Let delta = min(delta_L, delta_R). Create list Y' by copying all elements of Y that are within distance delta of L. For i running from 1 to the length of Y' and for j
running from i+1 to i+7 (nested loops), compute distances between Y'[i] and Y'[j] in constant time. Let delta' be the minimum of the set of distances produced. Let the final 
answer be min(delta, delta')

Let's determine the running time. In the worst case, P' contains all n points. The presort takes O(nlogn) time. To determine running time of the recursive part, we need to set 
up a recurrence (reminder: a recursively defined function to measure running time). Like before, we can draw ties to MergeSort and notice that dividing up the coordinate plane
about the vertical midpoint L lends itself to 2 recursive calls, each taking T(n/2) time. Note that we also include the combine operation defined above, which takes O(n) time.
(You might be thinking why? Why is the nested loops defined above in the combine operation executed in O(n) and not something like O(n^2). This is because the nested loop
is executed 7 times, which is a constant, rather than a variable length). The total recurrence for n > 3 is T(n) = 2T(n/2) + cn. For n < 3, as previously defined, is constant O(1) time. 

This is an extremely friendly recurrence, because it is the recurrence that is behind popular O(nlogn) algorithms like MergeSort. You can also derive the O(nlogn) using the 
SMT (Simplified Master Theorem) as well.



