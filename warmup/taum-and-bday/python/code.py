# Author: Tom Pauwaert
# Date: 14 March 2015
# Challenge: algorithms/warmup/taum-and-bday

T = input()

for _ in range(T):
    nr_b, nr_w = map(int, [x for x in raw_input().split(" ")])
    cost_b, cost_w, convert = map(int, [x for x in raw_input().split(" ")])

    if abs(cost_b - cost_w) > convert:
        initial_purchase = (nr_b + nr_w) * min(cost_b, cost_w)  
        to_convert = nr_w if cost_b < cost_w else nr_b
        print initial_purchase + to_convert * convert

    else:
        print nr_b * cost_b + nr_w * cost_w
