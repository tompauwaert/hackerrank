# Author: Tom Pauwaert
# Date: 14 March 2015
# Challenge: algorithms/warmup/sherlock-and-squares
import math

T = input()
for _ in range(T):
    A, B = [int(x) for x in raw_input().split(" ")]
    print len(range(int(math.ceil(math.sqrt(A))), int(math.sqrt(B))+1))
