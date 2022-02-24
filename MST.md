In this lecture, we covered Minimum Spanning Trees (MST). 

The input is a connected undirected graph with positive edge weights. 

Our objective is to find a minimum weight spanning subgraph of the input graph that is still connected. 

The output must be a tree (acyclic and connected). 

Let's see Prim's algorithm: 

For each vertex u in V,

Set the distance attribute of u to be infinite.

Set the predecessor attribute of u to be None. 

Once out of the loop, set the discovery time of starting vertex s to be 0. 

Initialize a set S. 

While S does not equal V (there are vertices still left in V that are not in S),

Let u be the vertex in V / S (all vertices in V not in S) which has the smallest distance value. 

Append u to the set S. 

Now, for each neighbor v of u, 

If the current distance value of v is larger than the weight value from u to v, then change the distance value of v to precisely that edge weight from u to v. 

Then, set the predecessor attribute of v to be u. 

Now let's see kruskal's algorithm:

First, sort edges in increasing order of weight value. 

Then, simply process edges in that particular order and add each edge as long as it does not create a cycle. 

Reverse kruskal algorithm does the opposite: it processes the edges in decreasing order of edge weight, instead processing from largest edge weight to smallest edge weight. 
Then, it processes edges in the above order and removes an edge if removing that edge does not disconnect the graph. 

Formal proofs of correctness for these algorithms are laid out in the lecture notes. 

