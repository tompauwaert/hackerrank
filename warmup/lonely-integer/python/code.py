
# Author: Tom Pauwaert
# Date: 31 March 2015
# Challenge: Algorithms/Warmup/Lonely-Integer

N = input()
array = map(int, raw_input().split())
isSingle = {}

for number in array:
    if number in isSingle:
        del isSingle[number]
    else:
        isSingle[number] = True

print isSingle.keys()[0]
