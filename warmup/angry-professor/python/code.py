
# Author: Tom Pauwaert
# Date: 31 March 2015
# Challenge: Algorithms/Warmup/Angry-Professor

T = input()
for _ in range(T):
    N, K = map(int, raw_input().split()) 
    arrivals = map(int, raw_input().split())

    # Select only the students in the list that arrived on time.
    #
    if len([time for time in arrivals if time <= 0]) >= K:
        print "NO"
    else: 
        print "YES"

