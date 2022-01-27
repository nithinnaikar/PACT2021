In this lecture we cover an application of Depth First Search (DFS): Topological Sort. 

Topological sort is an algorithm utilized on directed acylic graphs, or DAG's. In particular, a topological sort of a DAG G = (V, E) is a linear ordering of all G's vertices
such that if G contains an edge e = (u, v), then u precedes v in the ordering. 

We need not worry about the case where a cycle is present in G because we have asserted at the beginning that G must be a directed ACYCLIC graph. 

One of the DAG's most prominent applications is to indicate precedences among events, a kind of temporal heirarchy so to speak. A practical example of a DAG would 
be a representation of the order of clothes you put on first thing in the morning. For example, I might represent each node of my DAG as representing an article of clothing, such 
as pants, belt, socks, shoes, etc, and use the directed edges to indicate the temporal "flow" in which they are put on. That is, a directed edge u -> v in a DAG indicates that
garment u must be worn before garment v. 

A topological sort of this DAG would lead to an ordering of vertices along a horizontal line such that all directed edges go from left to right. 

Overview of Topological Sort Algorithm:

1. Call DFS(G) to compute finishing times v.f for each vertex v in G. 
2. As each vertex is finished (blackened), insert it onto the front of a linked list. 
3. Return the linked list of vertices.

The topologically sorted vertices appear in the reverse order of their finish times. 

We can perform a topological sort in O(V + E) time, since DFS takes O(V + E) time and it takes a constant O(1) time to insert each of the vertices onto the front of a linked list. 

We can prove the correctness of this algorithm using lemma's characterizing DAG's.

Lemma 1: A directed graph G is acyclic iff a DFS of G yields no back edges. 

Proof (=>): if DFS on G yields no back edges, then the DAG is acyclic.

Assume for purpose of contradiction that DFS on G yields a back edge e = (u, v). By definition of back edge, vertex v is an ancestor of vertex u in the DFS forest. Thus, G contains
a path from v to u in G and the back edge (u, v) completes the cyclic, a contradiction. 

Proof (<=): If the DAG is acyclic, then DFS on G yields no back edges. 

Assume for purpose of contradiction that the DAG is cyclic. Our goal is to show that DFS on G yields a back edge, a contradiction. Let v be the first vertex discovered in the
cycle, and let (u, v) be the preceding edge in the cycle. At the discovery time of v, the vertices of the cycle form a path of white colored vertices from v to u. By the
White Path Theorem, vertex u becomes a descendant of vertex v in G, which forms a back edge. 

Next Proposition: Topological sort algorithm defined above produces a valid topological sort of DAG provided as input. 

Suppose that DFS is run on a given DAG to determine finishing times for each of the vertices. It suffices to show that for any pair of distinct vertices u and v in the vertex
set of G, if G contains an edge u -> v, then finishing time of u is greater than the finishing time of v, since that would produce a valid topological sort ordering. Consider
any edge (u, v) explored by DFS(G). When this edge is explored, vertex v cannot be gray since then v would be an ancestor of u and (u, v) would be a back edge in DFS forest and 
contradicts earlier lemma. Therefore, v must be either white or black. If v is white, then v is a descendant of u clearly and so finishing time of v is less than finishing time of
u by Parenthesis Theorem. If v is black, its adjacency list/neighbors have already been considered and the finish time of v has already been set. Because we are still 
searching/exploring vertices from u, we have yet to assign a time to the finishing attribute of u and once we do we will clearly have finishing time of v is less than
finishing time of u. Proved. 

Alternate view of Topological Sort.

Input is a directed acyclic graph DAG G = (V, E)

Our objective is to order all the vertices in a linear fashion such that all edges in E (edge set of G) go from left to right, simply put. 

Initial idea: Roughly speaking, we want to start with a source vertex (vertex with indegree = 0 i.e. no incoming vertices only outgoing vertices) and a sink vertex (vertex with
outdegree = 0 i.e. no outgoing vertices only ingoing vertices). Remember we are referencing DAG's so we need to have some sort of in/out aspect to the edges of G. 

Here's an intermediate lemma: Let G be a DAG. Then G has a source vertex. We can prove that with a quick maximal path proof with u and v has endpoints. The gist is that u is a source
with indegree 0 and v is a sink with outdegree 0. 

Now let's define a recursive version of Topological Sort:

Set u to be the vertex with indegree 0 (i.e. the source) <- Inductive Step
Set G' to be G - u (all vertices in G except u). 
Return vertex u followed by TopologicalSort(G') <- Inductive Hypothesis

This is a classic T(n - 1)-esque recurrence relation that yields a running time of O(n^2).

Refined DFS-based algorithm:

Call DFS on G. 

Sort vertices in decreasing order of finish times. 

The above can be packaged into a concise statement: everytime a vertex becomes black (finished) in DFS, then prepend it to the beginning of the correct output. 

This makes it so that the vertices with the largest finish times are at the very beginning while vertices with smaller finish times are at the end of the ordering. 

Now lets do proof of correctness:

Theorem: Our algorithm works.

Proof: let e = (u, v) be an arbitrary but particular edge in G. Simply put, we want to prove that our algorithm will output u before v, by laws of topological sort. 

Case 1: discovery time of u < discovery time of v

At discovery time of u, there is a white path from u to v in G. By the white path theorem, vertex v is a descendant of u in the DFS forest. By the parenthesis theorem,
we have that discovery time of u < discovery time of v < finish time of v < finish time of u. Since finish time of u > finish time of v, u is placed before v in the output 
ordering. 

Case 2: discovery time of v < discovery time of u. 

At discovery time of v, there is no white path from v to u in G. By the white path theorem, u is therefore not a descendant of v in G. Applying parenthesis theorem, we have
that two lifespans are completely disjoint: lifespan of v completely disjoint with lifespan of u. The finishing time of u is > finishing time of v and u is placed before
v in the output ordering. 







