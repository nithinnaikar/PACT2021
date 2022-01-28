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

Idea: Algorithm should operate in increasing order of processing times. 



