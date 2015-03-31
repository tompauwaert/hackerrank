
# Author: Tom Pauwaert
# Date: 31 March 2015
# Challenge: Algorithms/Warmup/Find-Digits

T = input()
for _ in range(T):
    N = raw_input()
    print len([1 for digit in N if (digit !=  "0" and int(N) % int(digit) == 0)])

