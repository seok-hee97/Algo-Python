"""
투 포인터 이동 원칙
A[i] + A[j] >  M: j--; #번호의 합이 M보다 크므로 큰 번호 index를 내립니다
A[i] + A[j] <  M: i++; #번호의 합이 M보다 작으므로 작은 번호 index를 올립니다.
A[i] + A[j] == M: i++; j--; count++; #양쪽 포인터를 모두 이동시키고 count를 증가시킵니다.
"""


import sys
input = sys.stdin.readline
N = int(input());
M = int(input());
A = list(map(int, input().split()))
A.sort()                #리스트 정렬하기
count = int(0)
i = int(0)
j = int(N-1)

while i < j:            # 투 포인터 이동 원칙 따라 포인터를 이동하며 처리
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
        
print(count)