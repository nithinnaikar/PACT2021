Welcome to the Lecture 1 folder!

In this lecture, the Stable Matching problem is covered.

This folder contains all the files pertaining to the introductory StableMatching problem, including an input.in file, the Gale-Shapely program file, and the output.out file.

The StableMatching problem is as follows:

Consider a set of n people and n pets. Each person has a list of preferences for each of the n pets, and each of the n pets has a list of preferences for each of the people. Our goal is to pair these n people and n pets such that no instabilities are present in the matching. What is an instability? An instability occurs if any two people and pets prefer each other over there current partners. The Gale-Shapely algorithm does exactly this.

In the first step, all people and pets are considered free, meaning they are unpaired. While there exists a free person who hasn't proposed to every pet, then do the following- let the person be assigned to the variable p. Then, assign t to be the highest ranked pet in m's preference list who m has not yet proposed to. Two cases arise: if t is free, then form a pair (p, t). However, if t is not free (i.e. t is in a pair), then let p' = t's current partner. If t prefers p over p', then (p, t) form a pair and p' is now free. Otherwise, (p', t) remains the pair, p is still free, and the algorithm moves on. At the end of the algorithm, the set of engaged pairs is returned.

I implement this algorithm in Python by representing the set of people as {0, 1, 2, ..., n} and the set of pets as {0, 1, 2, ..., n}. An element i of the set of people corresponds to the ith person in the set of people and an element i of the set of pets corresponds to the ith pet in the set of pets. We need to have a preference list for each person and pet. This information is gathered through input. In the first line of input the integer n (the number of people/pets) is retrieved. In the next n lines of input, the preference list of person p, 0 <= p <= n, is gathered. In another n lines of input, the preference list of pet t, 0 <= t <= n, is also gathered. 

Now with the input collected, several arrays were needed to keep track of intermediate values processed in the algorithm. The first two array's are PeoplePref, which is a collection of all the preference lists of the people gathered in the input, and PetPref, which is a collection of all the preference lists of the pet gathered in the input. More precisely, PeoplePref[p][i] denotes the i+1 pet on person p's preference list and similarly for PetPref. 

Keep in mind the while loop of the Gale-Shapely algorithm can run at most n^2 iterations. The Gale Shapely algorithm has an asymptotic upper bound of O(n^2). This means that all the steps implemented in the body of the while loop need to be executed in constant time. This involves doing the four following things in constant time: 1) identify a free person, 2) identify a person's highest ranked pet to who they have not yet proposed to, 3) determine if a pet is currently engaged and, if so, determine its current partner, and 4) between p and p', who is preferred by t? 

The selection of a free person is done by maintaining the set of free people as a list. When we need to select a free person at the beginning, we take the first person on the list (-1 index). If this person gets engaged, then we remove it from the list. If another person becomes free, we add them to the list. Insertion and removal of elements into arrays is a constant time operation.

Okay, so once we have the person p, we need to identify the highest ranked pet they have not yet proposed to. This can be done by keeping an array Next that indicates for each person the position of the next pet they propose to. We initialize Next to be equal to 0 for all people at the beginning (they all propose to their highest ranked person first, or index 0). If a person needs to propose to a pet, then they propose to PeoplePref[p][Next[p]]. At the end of the proposal, regardless of whether they got rejected or not, we increment the value of Next[p] += 1 since they already proposed to that person. 

Next, say a person proposes to a pet. We need to be able to identify a pet is free or not. We can do this by maintaining another array Current that indicates for all the pets their current partner. This array is initialized to a null value at the beginning, or the None keyword, for all pets because all pets are free at the beginning (unpaired). 

The heart of the algorithm is step 4 and is the comparison of p to p'. This is inherently a comparison operator to determine who is higher in the preference list of t and therefore is executed in constant time (since comparisons are grouped under constant time operations, like indexing into an array). Therefore, we have successfully implemented the Gale Shapely algorithm in O(n^2) time.

**NOTE: I tried to model the input, program, and output files after the United States Computing Olympiad standard input and output procedures. In this case, this meant using two for loops to retrieve input, which is typical in most USACO problems. This adds unwanted 2n time to the algorithm since each loop iterates through n people/pets and there are two loops. Asymptotically speaking for inputs >= n_0, this can be ignored. However, for small inputs < n_0 this may be significant.
