The graph search problem is covered.

The graph search problem is as follows:

Given an undirected graph G consisting of both a vertex set and edge set and a starting vertex s in the vertex set of G, output all vertices reachable from s (i.e. all vertices
in the connected component containing s). In this lecture, we focused on one particular algorithm: Breadth-First Search, or BFS.

Before we talk about the algorithm, let's talk about graph representation in computers. A graph is typically represented as either as an adjacency list or adjacency matrix. 
In an adjacency matrix, the dimension is n x n, where each row i corresponds to a vertex i and similarly each column j corresponds to a vertex j in the graph. The intersection
of these two points (i.e. M[i, j]) is equal to 1 if there exists an edge between these two vertices and 0 otherwise. On the other hand, an adjacency list is a linked-list
structure in which each index of the list corresponds to a particular vertex and whose element at that index points to a list containing the neighbors of that particular
vertex. When determining the optimal representation between these two for your problem, it is important to note the space complexity of both data structures. An adjacency matrix is 
O(n^2) while an adjacency list is O(n + sum of all degrees in the graph) = O(n + 2m) = O(n + m). In terms of time complexity, if you want to contact all the neighbors of a 
particular edge, it takes O(n) time for the adjacency matrix while it takes O(deg(n)) time for the adjacency list. If you want to check whether an edge (x, y) exists in G, 
then an adjacency matrix will perform that in constant O(1) time while an adjacency list will perform that in O(deg(x)) time, clearly. Typically, an adjacency list is 
more efficient than an adjacency matrix. 

With that being said, the BFS algorithm is as follows:

First, initialize an array labeled 'discovered' whose length is the number of vertices and at each vertex indicates whether that particular vertex is discovered by BFS yet or not.
In the beginning, all vertices beside the starting vertex are initialized to False because they have not yet been discovered. 

Next, initialize a set T to be the empty set, which will be our BFS tree that we return at the end of the procedure. 

Next, initialize a set L_0 which indicates the collection of vertices at a particular level i in the BFS tree and set variable i to be 0. At the 0th level, 
only the starting node s is present. 

While L_i is not empty (i.e. there are still remaining nodes to be processed in a particular layer), then create the set L_i+1. Then, for each vertex in L_i, iterate through
all the neighbors of that vertex. If that neighbor is discovered (i.e. discovered[neighbor] = False), then set discovered[neigbhor] to be True, add the neigbhor vertex to the 
set L_i+1, and finally add the edge connection (vertex, neigbhor) to the BFS tree T. 

Once you have processed all the vertices in a particular layer, increment the value of i by 1 and continue. Once all the nodes have been processed, return the BFS tree T. 

Some important properties of BFS is that 1) the output of BFS is a tree, 2) The distance from a vertex v in L_i from the starting node s is exactly i, and 3) if (x, y) is an 
edge in G and x exists in L_i and j exists in L_j, then |i - j| <= 1. 

To determine the running time of BFS, note that each vertex belongs to exactly 1 layer, and for each vertex we contact all its neighbors. Therefore, we can say the running time
is O(n + sum of all degrees of vertices in the graph) = O(n + 2m) = O(n + m). 
