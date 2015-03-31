
# Author: Tom Pauwaert
# Date: 31 March 2015
# Challenge: Algorithms/Warmup/Halloween-Party

T = input()
for _ in range(T):
    K = input()
    print (K/2)**2 if K % 2 == 0 else ((K/2)+1) * (K/2)
