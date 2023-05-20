#avg of subject-score by new-way
#(not the normal way)


n = input() # input subject-count num

score_list = list(map(int, input().split()))

max_score = max(score_list) #Use built-in library

sum = sum(score_list)   #Use built-in library

print(sum*100/ max_score/ int(n))