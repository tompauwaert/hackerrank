
# Author: Tom Pauwaert
# Challenge: Algorithms/Warmup/Service-Lane
# Date: 30 March 2015

(fwLength, tests) = map(int, raw_input().split())
highway_widths = map(int, raw_input().split())

if(fwLength != len(highway_widths)):
    print "Invalid Input"

for _ in range(tests):
    # In highway array - select min value over range [ i, j]
    (i, j) = map(int, raw_input().split())
    print min(highway_widths[i:j+1])
