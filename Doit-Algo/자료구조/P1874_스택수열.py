N = int(input());           # 수열 개수
A = [0]*N                   # A 수열 리스트 채우기

for i in range(N):
    A[i] = int(input());
    
stack = []
num = 1
result = True
answer = []
for i in range(N):
    su = A[i]
    if su >= num:           # 현재 수열값 >= 오름차순 자연수
        while su >= num:    # 현재 수열값 >= 오름차순 자연수
            stack.append(num)
            num+=1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:                   # 현재 수열값 <= 오름차순 자연수
        n = stack.pop()
        if n > su:          # 스택 pop 결과값 > 수열의 수
            print("NO")
            result = False
            break
        else:
            answer.append('-')
if result:
    for i in answer:
        print(i)
