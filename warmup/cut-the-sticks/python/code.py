
# Author: Tom Pauwaert
# Date: 31 March 2015
# Challenge: Hackerrank - Algorithms/Warmup/Cut-The-Sticks

input()
sticks = map(int, raw_input().strip().split())
sticks.sort()
cut_length = 0

while len(sticks) > 0:
    print len(sticks)
    cut_length += sticks.pop(0) - cut_length
    while len(sticks) > 0 and sticks[0] == cut_length:
        del sticks[0]
