
# Author: Tom Pauwaert
# Date: 13 April 2015
# Challenge: algorithms/warmup/chocolate-feast

T = int(raw_input())
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().split(' ')]
    chocs = N/C
    if chocs > 0:
        wraps = chocs
        while wraps >= M:
           chocs += wraps / M 
           wraps = wraps % M + wraps / M
        
    print chocs
