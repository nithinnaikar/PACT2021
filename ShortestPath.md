In this lecture we consider the shortest path problem on graphs. 

The input is a directed weighted graph G. 

In other words, the input is a directed graph with positive numerical values, or weights, on each edge. 

We are also given a target vertex s. 

Given this graph, our objective is to compute a shortest path tree rooted at s. 

Graphically, we want to synthesize a tree rooted at s such that as we traverse down the tree, we are traversing along the shortest path through the graph. The bottom-most node is
farthest away from s while the closest node is adjacent to s. We quantify the notion of distance from s via the edge weights. We quantify the notion of direction through the graph
via the directed edges. 

A naive greedy implementation would be, at every step, to choose the edge with the smallest weight that crosses the cut (S, V/S), or in other words it would, given a set of edges
to choose from that cross the barrier between processed set of nodes including S and those nodes that we have not yet seen, we should choose the one with the minimum edge weight.

Unfortunately, this greedy algorithm does not work.

Here is a well-known Djikstra's Shortest Path Algorithm:

For each vertex u in v,

Set the distance estimate from vertex s to u to be infinite. 

Set its predecessor attribute to be a None object. 

After the loop, set the distance estimate for s to be 0, clearly. 

Now, set S to be the empty set. 

While S does not equal V, that is there exists vertices in V that are still not added to S (we are assuming that all vertices in V are reachable from S), then

Let u be the vertex with the smallest distance estimate value in V/S

Add u to S. 

For each neighboring vertex of u, 

If the current distance estimate of the neighboring vertex is greater than the distance estimate of u + weight of edge (u, v), then

Update distance estimate of that neighbor to be distance estimate of u + weight of edge (u, v), and

Update neighbor's predecessor attribute to be u. 

Proof of Correctness- Theorem: For each vertex u in S, the distance estimate of vertex u is the shortest path distance from s to u in G. 

We will do induction on the cardinality of the set S. 

Base Case: Let cardinality of S be 1. In other words, S contains the vertex s by itself. The distance from s is clearly defined as 0 which is indeed the shortest path distance
from s to s. 

Inductive Hypothesis: Let k be a positive integer. Assume that if the cardinality of the set S is equal to k, the distance estimate from s to u is the shortest path distance
for each and every vertex u in S. 

Inductive Step: We want to prove the claim when the cardinality of set S is k + 1. Let v be the k+1th vertex brought into S by Djikstra's algorithm. Let the predecessor
attribute of v be u. Assume for purpose of contradiction that the path from s -> u -> v is not the shortest path distance from s to v. Let instead the path P from 
s -> x -> y -> v be the true shortest path distance from s to v. 

Note that the distance estimate of v is simply the distance estimate of u + edge weight (u, v). Similarly, the cumulative edge weight/distance of path P is distance estimate
of x + edge weight (x, y) + cumulative weighting of y -> v. This expression collapses to distance estimate of y + cumulative edge weighting from y -> v. Since P is previously
defined as the shortest path from s -> v, the distance estimate of y MUST BE less than the distance estimate of v, by shortest path logic. This is a contradiction because, 
as previously defined by Djikstra algorithm, vertex y would have been the one to be k+1th vertex to be brought in across the cut rather than v. 

Note we have only covered the algorithm assuming edge weights are positive. If they are negative, then we simply add a large positive constant to all edges in G. 
