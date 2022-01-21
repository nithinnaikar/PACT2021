In this lecture, we expand on the graph search problem by examining another popular algorithm called Depth First Search, or DFS.

Unlike BFS, DFS searches through the tree by "going deep" into one particular path through the tree and then backtracking, whereas BFS searches across the graph breadth-wise
(i.e. DFS searches deeper in the graph whenever possible).

DFS explores edges out of the most recently discovered vertex that still has unexplored edges leaving it. Once all of that particular vertex's edges have been explored, then 
DFS backtracks to explore edges leaving the vertex from which it was discovered. This process continues until we have discovered all vertices reachable from the original source
vertex (i.e. all vertices in connected component containing source). If any undiscovered vertices remain, then DFS repeats the same process from that new source. DFS repeats
this process until it has discovered every vertex. 

Whenever DFS discovers a neighboring vertex from an already discovered vertex in its scan of the adjacency list, it records this event by setting the neighbors predecessor
attribute to the discovered vertex. For example, if we input an undirected connected graph consisting of a handful of vertices, BFS will return a tree with more breadth whereas DFS will return a long, skinny 
depth-wise tree.

Unlike BFS, the predecessor subgraph produced by DFS may consist of several trees because the search may be done from multiple source vertices. This is called the DFS forest. 

DFS also colors vertices to indicate what state they are in regarding the search. Initially, each vertex is colored white, then gray when it is discovered, and black when
it is processed (i.e all neighbors are considered- adjacency list has been scanned completely). 

DFS also contains the notion of time in a graph search. In particular, each vertex is timestamped, once when it is discovered/colored gray and once when it is finished/colored 
black. For every vertex in G, the discovery time is always less than the finish time, clearly. Also note that a vertex is colored white before the discovery time, colored gray
between the discovery and finish time, and then colored black from finish time onward. 

Compactly, the DFS algorithm is as follows:

First, for each vertex u in G, color u white, where white indicates that a particular vertex is undiscovered. At the start, like BFS, all vertices are undiscovered. Also, again
for each vertex, set it predecessor attribute to a None object. 

Next, set a time counter to be 0 at the beginning. 

For each vertex u in G, if u is white, then visit u by calling DFS_VISIT(G, u). 

DFS_VISIT works by first incrementing the time by 1 unit. Then, it set's the vertex u discovery time to be the current time and color's u gray.

Then, for each neighbor v of u, if the color of v is white (indicating that it is undiscovered), then set v's predecessor attribute to be equal to u. After that, simply make
a recursive call DFS_VISIT(G, v). 

Once you have processed/visited all the neighbors of a particular vertex, then color the vertex black (to indicate that it and its neighbors are fully processed) and increment 
the time by 1 unit. Then, mark the finish time of that vertex to be the current time. 

It is important to note that every time DFS_VISIT is called on a vertex, that vertex becomes the root of a new tree in the DFS forest. When DFS returns, every vertex in G
has both a discovery and finish time. 

The results of DFS may depend upon the order in which DFS examines the vertices and the order in which DFS examines the neighbors of a vertex. This variability is negligible. 


Let's determine the running time. 

Note that DFS_VISIT is called exactly once for each vertex in G, held in check by examining and updating the color of each vertex in G to prevent discovering the same vertex twice. 

Also note that DFS_VISIT(vertex) takes O(degree(vertex)) time. 

Therefore, it is easy to see that the running time of DFS is O(n + sum degree of all vertices) = O(n + 2m) = O(n + m). 

There are a few properties of DFS important to note.

DFS yields valuable information about the structure of a graph. One such property is that the predecessor subgraph does form a forest of trees because the structure of the 
DFS trees are aligned with the structure of recursive calls of DFS_VISIT. In particular, a vertex u is a predecessor of v iff DFS_VISIT(G, v) was called during a scan of u's 
adjacency list/neighbors. Basically, vertex v is a descendant of u iff v is discovered when u is colored gray. 

One of the most profound discoveries is that the discovery and finish times have a "parenthesis" structure. This is originally described visually but there is a more concrete
way to express this. That is, in any depth first search of an undirected or directed graph G, for any two vertices u and v, exactly one of the following three conditions must
hold: 

1. interval from discovery of u to finish of u and discovery of v to finish of v are entirely disjoint, and neither u nor v is a descendant of the other in the DFS forest. 
2. interval from discovery of u to finish of u is entirely contained within the interval between the discovery of v and the finish of v and u is a descendant of v in a DFS tree.
3. Same as above with u and v swapped 

Basically what the last two statements are saying is that for u to be a descendant of v in a DFS tree, then u's "lifespan" (discovery -> finish interval) must be entirely contained
in v's lifespan. In a way this makes sense, right, by the recursive properties defined in DFS. 



