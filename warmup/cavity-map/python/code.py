# Author: Tom Pauwaert
# Date: 13 March 2015
# Challenge: algorithms/warmup/cavity-map
import sys

n = input()
cmap = []
cmap.append([int(x) for x in raw_input()])
print ''.join(map(str,cmap[0]))

if n > 1:
    cmap.append([int(x) for x in raw_input()])

for row in range(1,n-1):
    cmap.append([int(x) for x in raw_input()])

    sys.stdout.write(str(cmap[row][0]))
    for column in range(1,n-1):
        if(cmap[row][column] > cmap[row-1][column] and
                cmap[row][column] > cmap[row+1][column] and
                cmap[row][column] > cmap[row][column-1] and
                cmap[row][column] > cmap[row][column+1]):
            sys.stdout.write("X")
        else:
            sys.stdout.write(str(cmap[row][column]))
    sys.stdout.write(str(cmap[row][n-1]) + '\n' )

if len(cmap) > 1:
    print ''.join(map(str,cmap[len(cmap)-1]))
