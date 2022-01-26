In this lecture, we cover Greedy algorithms with the interval scheduling problem.

The interval scheduling problem is as follows:

We are given a set of n intervals. Each interval 1 <= i <= n has a start time s_i and a finish time f_i. 

Our objective is to find a set of non-overlapping/disjoint intervals of maximum size. 

Let's convert this to a graph problem.

We can represent each interval as a vertex in a graph.

Let there exist an edge between two vertices if their corresponding intervals overlap.

Our objective now is to find a maximum independent set in the graph (a maximum independent set is the set of vertices in G of largest size such that no two vertices in the set 
share an edge in G. Going back to our original objective, this makes sense because we want to include as many intervals as possible (maximum size) such that no two intervals
overlap (no edge is shared between them). 

However, to find a maximum independent set of a graph G in an efficient manner is very, very hard. 

Let's try an algorithm:

Let s be the empty set. 

While there are more intervals left, add the interval with the earliest finish time to S and remove all overlapping intervals with the interval just chosen. 

Now let's prove this algorithm.

Theorem: Our algorithm yields an optimal solution.

Proof: Assume for purpose of contradiction that our algorithm does not lead to an optimal solution. Note that the set s is our solution. Let OPT be the optimal solution that 
has the maximum number of intervals that are shared/common with s. 

Now consider all intervals of s and opt in increasing order of finish times. 

Note the first instance/pair where s and OPT differ in intervals. Let I_s be the differing interval in s and let I_OPT be the differing interval in OPT. 

Since our algorithm always chooses an interval with the earliest finish time, our algorithm COULD NOT have chosen I_s when I_OPT (with an earlier finish time) was available. 
That cannot happen. 

Now consider OPT' = OPT U {I_s} / {I_OPT} (i.e. Intervals of OPT combined with I_s except I_OPT).

Note that OPT' is valid solution because it contains non-overlapping intervals. 

The cardinality of OPT' is still equal to cardinality of OPT. 

This means that OPT' is ANOTHER optimal solution that has more intervals common to S than OPT, which is clearly a contradiction. 

Now let's consider the interval coloring problem.

Again, we are given a set of n intervals each with a start and finish time. 

Our objective is to schedule all intervals so that we use the smallest number of rooms. 

A graph coloring problem would be to color the vertices of the interval-representing graph G such that no two vertices that share an edge (i.e. overlap) are colored the same
and we want to minimize the number of colors we use where colors represent rooms in this case. 

Algorithm

Process intervals in increasing order of start times. 

Assign an interval the smallest numbered room where it "fits" (based on the fact that no two overlapping intervals can be labeled the same room). 

Proof of Correctness:

Let k be the number of rooms that our solution uses. Is k == OPT? Here's an elegant observation: OPT >= max number of intervals a vertical line intersects? Why? Because
the maximum number of interval a vertical line intersects represents the maximum number of overlapping intervals at that particular point point (vertical line). Each one of
those overlapping intervals must be colored using a distinct color and thus OPT >= max number of intervals a vertical line intersects. 

Let I be the first interval assigned to room k. Question: why is I assigned to room k and not to any of the preceding/earlier rooms? This is because in each of the previous I
rooms there is an interval that OVERLAPS with I, thus creating a need for I to be assigned to room k rather than a preceding room. 

With this being said, note that OPT >= k, because k (the number of rooms that our solution uses) is == to the max number of intervals a vertical line intersects. This implies 
that our solution is, indeed, optimal.

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage.



