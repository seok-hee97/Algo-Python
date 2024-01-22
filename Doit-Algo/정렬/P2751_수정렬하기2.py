import sys
input = sys.stdin.readline
print = sys.stdout.write


# 병합 정렬 구현
def merge_sort(s, e):           # s: 시작점, e(종료점), m(중간점)
    if e - s < 1: return
    m = int(s + (e - s) / 2)        #중간점
    #재귀함수 형태로 구현           
    merge_sort(s, m)
    merge_sort(m + 1, e)
    
    for i in range(s, e + 1):
        tmp[i] = A[i]           #tmp list에 저장
    
    # 두 그룹을 병합하는 로직
    k = s
    index1 = s
    index2 = m + 1 
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())            # 정렬할 수 개수
A = [0] * int(N + 1)        # 정렬할 리스트 선언
tmp = [0] * int(N + 1)      # 정렬할 때 잠시 사용할 임시 리스트 선언

for i in range(1, N + 1):
    A[i] = int(input())         # A리스트에 데이터 저장하기

merge_sort(1, N)                #병합 병렬 수행


for i in range(1, N + 1):
    print(str(A[i]) + '\n')         #결과값 출력
