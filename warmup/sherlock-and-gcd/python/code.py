# Author: Tom Pauwaert
# Date: 14 March 2015
# Challenge: algorithms/warmup/sherlock-and-gcd
import itertools

def all_subsets(iterable):
    for subset_size in xrange(1,len(iterable)+1):
        for combination in itertools.combinations(iterable, subset_size):
            yield combination

for _ in range(input()):
    N = input()
    numbers = map(int, raw_input().split(" "))
    numbers.sort()

    if numbers[0] == 1:
        print "YES"
        continue

    done = False
    for comb in all_subsets(numbers):
        if done:
            break

        # Find all divisors of the smallest integer in the array
        # and see if there is one element in there that can divide
        # all the other elements
        divisors = [x for x in range(2, comb[0]+1) if comb[0] % x == 0]
        div_count = dict.fromkeys(divisors,0)

        for i in range(len(comb)):
            if i > 0 and comb[i-1] == comb[i]:
                print "NO"
                done = True
                break
            
            for divider in divisors:
                if comb[i] % divider == 0:
                    div_count[divider] += 1
                    
    if div_count[max(div_count)] == len(comb):
        print "NO"
    else: 
        print "YES"
