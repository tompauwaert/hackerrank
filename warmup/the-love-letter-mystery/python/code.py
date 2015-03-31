
# Author: Tom Pauwaert
# Date: 31 March 2015
# Challenge: Algorithms/Warmup/The-Love-Letter-Mystery

T = input()
counter = 0

# For each word, figure out edit length to palindrome
for _ in range(T):
    counter += 1
    word = raw_input()
    word_len = len(word) #stored for efficiency
    index = 0
    sum_edits = 0

    # Iterate half the word and always compare characters 
    # at equal distance d from the beginning and from 
    # the ending of the word
    while index < word_len/2.0:
        sum_edits += max(ord(word[index]), ord(word[word_len - index - 1])) - min(ord(word[index]), ord(word[word_len - index - 1]))
        index += 1

    print sum_edits

