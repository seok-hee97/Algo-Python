"""삽입 정렬 insert sort"""
N = int(input())                    # 사람의 수 
A = list(map(int, input().split())) # 자ㅏ리수별로 구분해 저장한 리스트
S = [0]*N   # A 합 배열: 각 사람이 인출을 완료하는데 필요한 시간을 저장



for i in range(1, N):    # 삽입 정렬
    insert_point = i     # 십입 위치(index)
    insert_value = A[i]  # 삽입 값
    for j in range(i-1, -1, -1):      # 현재 범위에서 삽입 위치 찾기
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        #삽입을 위해 삽입윛이에서 i까지 데이터를 한 칸씩 뒤로 밀기
        A[j] = A[j-1]
    A[insert_point] = insert_value      # 삽입위치에 현재데이터 저장
S[0] = A[0]
for i in range(1, N):    # 합 배열 만들기
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0, N):    # 합 배열 총합 구하기
    sum += S[i]
print(sum)