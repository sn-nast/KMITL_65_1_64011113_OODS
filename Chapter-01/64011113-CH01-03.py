# Election

print("*** Election ***")
candidate = 20
candidate_count = []

for i in range(0, candidate):
    candidate_count.append(0)

voters = int(input("Enter a number of voter(s) : "))
ballots = [int(i) for i in input().split()]

for ballot in ballots:
    if ballot in range(1, 21):
        candidate_count[ballot-1] += 1
        
candidate_count.insert(0, 0)
temp_check_winner = 0

for x in candidate_count:
    temp_check_winner += 1 if x == max(candidate_count) else 0
    
winner_candidate = candidate_count.index(max(candidate_count)) if temp_check_winner == 1 else 0

if winner_candidate in range(1, candidate+1) :
    print(winner_candidate)
else:
    print("*** No Candidate Wins ***")