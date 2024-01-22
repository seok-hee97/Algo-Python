N = int(input())                #정렬할 수 개수
A = [0]*N                       # 수 저장 리스트 선언 및 입력 데이터 저장

for i in range(N):
    A[i] = int(input())        


for i in range(N-1):
    for j in range(N-1-i):
        
        # swap 기능 이게 전부
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])