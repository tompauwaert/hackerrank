import random
import sys

n=input()
print n
for x in range(n):
    for y in range(n):
        sys.stdout.write(str(random.randint(1,9)))
    print ""
