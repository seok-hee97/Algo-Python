from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())                # 질의 요청 개수
myQueue = PriorityQueue()       # 파이썬엣서는 데이터의ㅡ 순섣가 정렬의 우선순위가 가능
for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myQueue.put((abs(request), request))            #



# 우선순위 큐 
# https://cocobi.tistory.com/204