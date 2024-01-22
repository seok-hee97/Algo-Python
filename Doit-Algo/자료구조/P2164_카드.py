from collections import deque           # deque lib

N = int(input())                # 카드의 개수
myQueue = deque()               # 카드 저장 자료구조 큐

for i in range(1, N+1):         # 큐에 카드 저장
    myQueue.append(i)               
    
while len(myQueue) > 1:     # 카드가 1장 남을 때까지
    myQueue.popleft()       # 맨 위의 카드를 버림
    myQueue.append(myQueue.popleft())   # 맨 위의 카드를 가장 아래 카드 밑으로 이동
print(myQueue[0])   # 마지막으로 남은 카드 출력