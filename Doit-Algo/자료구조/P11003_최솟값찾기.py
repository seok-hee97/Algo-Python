from collections import deque
# appendleft(), popleft() | append(), pop()


N, L = map(int, input().split())            # N(데이터 개수)/ L(최솟값을 구하는 범위)
mydeque = deque()                           # 데이터를 담을 덱 자료구조
now = list(map(int, input().split()))       # 주어진 숫자 데이터를 자니느 리스트

for i in range(N):                          # now 리스트를 탐색 (now[i]를 현재 값으로 세팅)
    # now[i]를 현재 값으로 세팅
    while mydeque and mydeque[-1][0] > now[i]:
        # 덱의 마지막 값이 현재 값보다 크다면 덱에서 제거
        mydeque.pop()
    mydeque.append((now[i],i))
    # 현재 값을 덱에 추가
    
    if mydeque[0][1] <= i - L: # 범위에서 벗어난 값은 덱에서 제거
        # 덱의 첫 번째 값의 인덱스가 범위에서 벗어났다면 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ')           #덱의 첫번째 값을 출력




