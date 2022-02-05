In this lecture we explore a classic application of Depth First Search (DFS): Strongly Connected Components (SCC's). 

Why is this important? Many graph algorithms first decompose a graph into its strongly connected components, run their algorithm separately on each component, and then combine the 
solution according to the structure of the connections among the components in a recursive-decomposition (divide and conquer)-esque algorithm.

Formally, a strongly connected component of a directed graph maximal subset of vertices of the vertex set of G such that for every two-sized subset of vertices in the component, 
there exists a path from vertex 1 to vertex 2 and a path from vertex 2 to vertex 1. 

The accepted algorithm for finding SCC's of a graph uses the transpose of G, G_t. G_t = (V, E_t), where E_t consists of all edges in G except with their directions reversed. 

Given an adjacency list representation of G, the computational time needed to generate G_t is O(V + E). It is important to note that G and G_t have exactly the same strongly connected
components. In particular, vertices u and v are reachable from each other in G if and only if they are reachable from each other in G_t. 

The following linear-time algorithm computes the strongly connected components of directed graph G using two DFS searches: one on G and one on G_t. 

Step 1: Call DFS(G) to compute finishing times for each vertex. 

Step 2: Compute G_t

Step 3: Call DFS(G_t), but consider vertices in decreasing order of finish time in the main loop of DFS. 

Step 4: Output the vertices of each tree in the DFS forest as a separate strongly connected component of G. 

The idea behind this algorithm is derived from a property of the component graph G_SCC. What is G_SCC? Let G have connected components c_1, c_2, c_3 ...  c_k. The vertex set of 
G_SCC consists of c1, c2, c3 ... ck each represented as a single vertex. There is an edge between vertices of G_SCC iff G contains a directed edge (x, y) for some vertex x in
one SCC and another vertex y in another SCC. 

We shall prove the component graph of G is a DAG which the following lemma implies. 

Let C and C' be distinct SCC's in G. Let two vertices u and v belong in C and other two vertices u' and v' belong in C'. Suppose that G contains a path u to u'. Then G cannot have 
a path from v' to v (intuition: or else there would be a cycle and we are trying to prove the graph is a DAG - Directed ACYCLIC Graph). 

Proof: Assume otherwise for purpose of contradiction. That is, there exists a path from v' to v in G. G already contains a path from u to u' to v', and now it also has a path
from v' to v to u. Therefore, u and v' are clearly reachable from each other because there exists bidirectional paths to and from each vertex. This contradicts the initial assumption
that C and C' are distinct SCC's. Therefore, the component graph cannot have a path from v' to v and therefore it is a DAG. 

We will now see that considering vertices in the second DFS in decreasing order of finish times computed in the first DFS essentially makes it so that we are visiting the vertices
of the component graph in topologically sorted order. 

New notation: if U is a subset of vertices from V, then d(U) returns the minimum discovery time of all vertices in that subset and f(U) returns the maximum finishing time of all 
vertices in that subset. In other words, d(U) returns the earliest discovery time and f(U) returns the latest finishing time given a subset of vertices U. 

Lemma: Let C and C' be distinct SCC's in G. Let there be an edge (u, v) in G such that u exists in C and v exists in C'. Then, f(C) > f(C'). In other words, the latest finishing
time of vertices in C is greater than the latest finishing time of vertices in C'. In other words, there exists a vertex in C that was finished later than the latest finished vertex
in C'. Just to help understand better. 

Proof: There are two cases depending on which SCC C or C' had the first discovered vertex during DFS. 

Case 1: d(C) < d(C') -> earliest discovery time of C is less than earliest discovery time of C'. 

Let x be the first vertex discovered in C. At discovery time of x, clearly all vertices in C and C' are white. By the White Path Theorem, G contains a path from x to each vertex in C
consisting of only white vertices. Since there exists an edge (u, v), for any vertex w in C', there is also a path in G at discovery time of x from x to w consisting of only white 
vertices. The path is x -> u -> v -> w. By WPT, all vertices in C and C' become descendants of x. By WPT, all vertices in C and C' become descendants of x in the DFS tree. X has
the latest finishing time than any of its descendants. Therefore, f(C) > f(C'). 

A similar argument can be made for the second case in which d(C) > d(C'). 

We have therefore related SCC's and finishing times in the first DFS. 

Next corollary: relating SCC's and finishing times in the second DFS on G_t. 

Let C and C' be distinct SCC's in G. Suppose there exists an edge (u, v) in the set of transposed edges where u exists in C and v exists in C'. Then f(C) > f(C'). 

Proof: Since (u, v) exists in the transposed edge set, we know there must exist (v, u) in the original edge set. Since we know that the SCC's of G and G' are the same, previous
lemma implies that f(C) < f(C')

The above corollary provides the key to understanding why the SCC algorithm works. 

The magic happens in the 2nd DFS which is on G_t. In this, we start with we start with the SCC whose f(C) is maximum, since we process vertices in decreasing order of finish times 
(largest to smallest). The search starts from some vertex x in C and ends up visiting all vertices in the connected component C.  By previous collary, G_t contains no edges
from C to any other SCC, and thereby the search from x will ot visit any other vertices in any other component besides C. Therefore, the DFS tree rooted at x contains all the vertices
of C. Having completed visiting all other vertices in C, the DFS search selects a root starting vertex from another connected component in G besides C and continues the search from
there. This other SCC labeled C' who has a finishing time of f(C') is maximum over all components other than C. By previous corollary, the only edges in G_t C' to any other component
must be to C, which we have already visited. In general, when the DFS search of G_t visits any other SCC, any edges out of that component must be to components that the DFS search
has already visited. Therefore, each DFS tree is exactly one SCC in G. 

