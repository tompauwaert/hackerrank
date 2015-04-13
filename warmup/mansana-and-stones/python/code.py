# Author: Tom Pauwaert
# Date: 13 March 2015
# Challenge: Algorithms/warmup/mansana-and-stones
import sys

T = input()
for _ in range(T):
    n = input()
    a = input()
    b = input()

    diff = abs(a-b)
    previous = (n-1) * min(a,b)
    sys.stdout.write(str(previous) + " ")

    if diff > 0:
        for i in range(0,n-1):
            previous += diff
            sys.stdout.write(str(previous) + " ")
    sys.stdout.write('\n')
