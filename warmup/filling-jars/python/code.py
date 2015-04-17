# Author: Tom Pauwaert
# Date: 17 March 2015
# Challenge: algorithms/warmup/filling-jars

no_jars, no_ops = map(int, raw_input().split(' '))
sum = 0
for _ in range(no_ops):
    a, b, k = map(int, raw_input().split(' '))
    sum += (b-a+1) * k

print sum/no_jars
