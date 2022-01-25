In this lecture we expand on the graph search algorithm called Depth First Search, or DFS.

Recall the pseudocode of DFS.

First, we iterate through the vertices of G and color each vertex white and set its predecessor attribute to a NoneType object. Then, set a counter variable labeled time to be 0. 
Next, iterate through the vertices of G and, if that vertex is colored white, visit that vertex by calling DFS_VISIT(vertex).

DFS_VISIT works by first incrementing the global time counter by 1 unit. Then, set the discovery time attribute of the vertex to be the current time. Next, change the color of that
vertex from white to gray. For each neighbor of that vertex, call DFS_VISIT(neighbor) and set its predecessor attribute to the parent vertex if it is colored white. 

Once a vertex's neighbors have all been discovered, increment the time counter by 1, set the vertex's finishing time attribute to the current time, and color that vertex black. 

Now consider the properties of DFS.

When is vertex v a descendant of vertex u in the DFS forest? This is true iff vertex v is discovered when vertex u is colored gray. 

Another important property is the Parenthesis Theorem. It states that DFS on G yields exactly one of the following scenarios:

Let the lifespan of a particular vertex v to the be the total interval of time from the discovery time of v to the finish time of v. 

1. Lifespan of v is contained within the lifespan of u and v is a descendant of u in the DFS forest. 
2. Lifespan of u is contained within the lifespan of v and u is a descendant of v in the DFS forest.
3. The lifespan of u is disjoint with the lifespan of v and neither u nor v are descendant's of one another in the DFS forest. 

We shall quickly prove the Parenthesis Theorem:

Without loss of generality (that is, the same can be proven for the discovery time of v > discovery time of u), let the discovery time of u < discovery time of v (i.e. the vertex
u is discovered before the vertex v). 

Case 1: Finishing time of u is less than the discovery time of v.

If that is the case, then clearly the two intervals are entirely disjoint and by property 1, v and u are not descendants of each other (i.e. when v is discovered u is black not gray

Case 2: Finishing time of u is greater than the discovery time of v

If that is the case, then once v is discovered, the DFS algorithm processes all neighbors of v, then v is finished before the algorithm backtracks to u. Therefore, finishing
time of v is less than the finishing time of u and v is a descendant of u by property 1. 

We can make a corollary based on the above: vertex v is a descendant of vertex u iff discovery time of u < discovery time of v < finish time of v < finish time of u. This is what
we mean by the Parenthesis theorem. The above inequality is essentially nested parenthesis. A child nodes lifespan is always contained in the parent's nodes lifespan. 

Next, let's cover the White Path Theorem, which is property 3: Vertex v is a descendant of vertex u in the DFS forest iff at the discovery time of u, there is a path consisting of 
only white vertices from u to v in G.

This is an if and only if proposition so we have to prove two implications. 

1) if vertex v is a descendant of vertex u, then at discovery time of u there is a white path from u to v in G. 

Since v is a descendant of u in the DFS forest, there must be a unique path P from u to v in the forest. Let w be any vertex along the path P. Note w is a descendant of u
in the DFS forest. By the Parenthesis Theorem, discovery time of u < discovery time of w < finish time of w < finish time of u which means that u is discovered before w (i.e
at the discovery time of u, w is white). Proved.

2) If at the discovery time of u there is a white path from u to v in G, then v is a descendant of u in the DFS forest. 

Let P be the white path from u to v in G. Assume for purpose of contradiction that v is not a descendant of u in the DFS forest. Traversing from u to v along P, let y be the first
vertex that is not a descendant of u in the DFS forest. Let x be the vertex preceding y in P. X is a descendant of u in the DFS forest, and therefore, by the Parenthesis Theorem,
the lifespan of x is entirely contained in the lifespan of u. On the contrary, the lifespan of y is disjoint with the lifespan of u because, by the Parenthesis Theorem, the two
are not descendants of one another. 

So since y is not a descendant of u in the DFS forest, lifespan of y is not completely contained in the lifespan of u. The discovery time of y cannot be greater than the finish
time of u, even though the two are not descendants of each other, because this implies that vertex x was colored black when it had a white neighbor (y), which is entirely
not possible. Thus, the only case possible is that the discovery time of y is less than the discovery time of u. This is a contradiction as, at the discovery time of u, vertex
y is not colored white.

Let's move on to classification of edges. 

After we run DFS on a graph G, we can label each edge of G as follows:

Let e = (u, v) be any edge in G.

We give e one of the following labels based on the very first time e is processed in the algorithm. 

1) e is a free edge if e exists in the DFS forest. 
2) e is a back edge if the other endpoint, in this case vertex v, is an ancestor of vertex u.
3) e is a forward edge if the other endpoint, v, is a descendant, of vertex u.
4) e is a cross edge if it is not the above three. 

Theorem: DFS on an undirected graph yields tree edge and back edge.

Proof:

Let e = (u, v) be any edge in G. Without loss of generality, let the discovery time of u be less than the discovery time of v. 
Claim: v is a descendant of u in the DFS forest. 

Case 1: V is a child of u. 

Therefore, e is a tree edge because (u, v) will directly appear in the DFS forest because of a direct parent-child relationship.

Case 2: V is not a child of u, but a descendant of u. 

The edge (u,v) is processed when the search is at v. Since u is an ancestor of v, e is back edge. 
