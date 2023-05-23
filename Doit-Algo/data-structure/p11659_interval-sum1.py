
import sys
input = sys.stdin.readline


suNo, quizNo = map(int, input().split())    #input() = sys.std.readline()
numbers = list(map(int, input().split()))

prefix_sum = [0]                #var sum-array
temp = 0                        #var temp for sum numbers

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)     #make sum-array
    
    
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e]- prefix_sum[s])     #use sum-array make to interval-sum
