# Author: Tom Pauwaert
# Date: 15 March 2015
# Challenge: algorithms/warmup/sherlock-and-the-beast

# lenghts of strings of 3's and 5's, in their respective multiples of_
_5_in_mult_of_3 = [3 * x for x in range(0, 100000/3 + 1)]
_3_in_mult_of_5 = [5 * x for x in range(0, 100000/5 + 1)]

def build_string(index_mult_of_3, index_mult_of_5):
    result = ["5" for x in range(0, _5_in_mult_of_3[index_mult_of_3])]
    result.extend(["3" for x in range(0, _3_in_mult_of_5[index_mult_of_5])])
    print ''.join(result)

def run():
    T = input()
    for _ in range(T):
        N = input()

        closest_mult_of_3 = N/3
        closest_mult_of_5 = N/5
        counter = 0
        broke_out = True

        while (counter <= closest_mult_of_5):
            sum = _5_in_mult_of_3[closest_mult_of_3] + _3_in_mult_of_5[counter]
            if( sum == N):
                build_string(closest_mult_of_3, counter)
                break
            
            if closest_mult_of_3-1 >= 0:
                sum = _5_in_mult_of_3[closest_mult_of_3-1] + _3_in_mult_of_5[counter]
                if( sum == N):
                    build_string(closest_mult_of_3-1, counter)
                    break

            if closest_mult_of_3-2 >= 0:
                sum = _5_in_mult_of_3[closest_mult_of_3-2] + _3_in_mult_of_5[counter]
                if( sum == N):
                    build_string(closest_mult_of_3-2, counter)
                    break

            closest_mult_of_3 -= 1
            counter += 1
        else: 
            broke_out = False

        if not broke_out:
            print -1


if __name__ == "__main__":
    run()

