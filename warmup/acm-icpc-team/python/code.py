# Author: Tom Pauwaert
# Date: 14 March 2015
# Challenge: Algorithms/warmup/acm-icpc-team

N, M = map(int, raw_input().split(" "))
persons = []
max_skills = 0
nr_of_teams = 0
for i in xrange(N):
    persons.append([ int(skill) for skill in raw_input()])
    for j in range(i):
        combined_skillset = sum(persons[i][index] or persons[j][index] for index in xrange(M))
        if combined_skillset > max_skills:
            max_skills = combined_skillset
            nr_of_teams = 1
        elif combined_skillset == max_skills:
            nr_of_teams += 1

print max_skills
print nr_of_teams

