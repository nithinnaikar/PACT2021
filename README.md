This lecture we continue with greedy algorithms with the job scheduling problem.

Our input consists of one machine and n jobs, where each job contains a start time = 0, processing time, and deadline. 

Our objective is to schedule all jobs non-preemptively (once a job starts processing it cannot be interrupted during that particular processing interval until its deadline) on
one machine so that the max "lateness" of any job is minimized. 

Note that for any job, its lateness is formally defined as max(0, completion time - deadline time). 

Let's take an example. 

Let n = 3 jobs. All jobs have a start time = 0.

Job 1 has a processing time of 30 minutes and a deadline at t = 40. 

Job 2 has a processing time of 15 minutes and a deadline at t = 30. 

Job 3 has a processing time of 60 minutes and a deadline at t = 65. 

A possible scheduling: {job 3, job 1, job 2}

Completion time of job 3 = 60. Completion time of job 1 = 60 + 30 = 90. Completion time of job 2 = 60 + 30 + 15 = 105. 

Lateness of job 3 = 0. Lateness of job 1 = 90 - 40 = 50. Lateness of job 2 = 105 - 30 = 75. 

Cost of the schedule (max lateness of any job) = 75. 

There are 3! total possible orderings. Let's try another one: {job 2, job 3, job 1}

Completion time of job 2 = 15. Completion time of job 3 = 15 + 60 = 75. Completion time of job 1 = 15 + 60 + 30 = 105. 

Lateness of job 2 = 0. Lateness of job 3 = 75 - 65 = 10. Lateness of job 1 = 105 - 40 = 65. 

Cost of schedule: 65. 

Ordering #2 is more optimal than ordering #1 because it has a lower cost. 

Algorithm: Earliest Deadline First (EDF). Meaning that we process job intervals in increasing order of deadline. We start with intervals with the earliest deadlines (i.e.
get them out of the way first) and move on to intervals with later deadlines. As you can see, this is a very intuitive idea and mimics that of how students deal with their own homework. 

Step 1: Sort jobs in increasing order of deadline
Step 2: Process the jobs in the above order non-preemptively one after the other. 

Proof of Correctness:

Observations

- There is an optimal schedule with no idle time
- Our schedule has no idle time

Definition: job i is considered inverted with job j if i precedes j in the schedule but the deadline of i is later than the deadline of j. 

Observation 3: Our schedule has no inversions

Lemma of above observation (without proof):

Two schedules with no inversions and no idle time have the same max lateness. 

Lemma: There is an optimal schedule with no inversions and no idle time. 

Proof: Assume otherwise for purpose of contradiction.  Among all optimal schedules with no idle time, let OPT be the optimal schedule with the smallest number of inversions. 
Let jobs i and j be inverted in OPT. 

Now consider OPT', which is the same as OPT except the jobs i and j are switched in the ordering. 

Wishful thinkings: jobs i and j (inverted jobs) are consecutive in the schedule (adjacent intervals).

It now suffices to show that if an optimal schedule has inversions then there must be two consecutive jobs that are inverted. 

Case 1: i and j are consecutive. Done

Case 2: i and j are not consecutive. 

This is done with a nice visual proof.

Consider a two dimensional graph in which the x-axis represents the jobs in the interval (i, j) (ex. i, i+1, i+2, ... ,j) and the y-axis represents the deadline time. We know
that jobs i and j are inverted, meaning that i appears before j in the ordering but the deadline time of i is greater than that of j. Starting from job i and moving along the
x-axis, we know that the deadline time on the y-axis will increase. However, at job j, we know that the deadline time strictly decreases down toward it, since the deadline time
of j is less than that of i. Consider job j - 1. Job j - 1 is located on this declining slope and therefore has a higher deadline time than that of j and is placed before it in
the ordering, forming a consecutive inversion. Proved.

Note that these consecutive jobs can be swapped without increasing max lateness. Thus  we have found a new OPT ordering with no idle time and one less inversion, contradicting
the fact that OPT was an optimal schedule with min. number of inversions. 





