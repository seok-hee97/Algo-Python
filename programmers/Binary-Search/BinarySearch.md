

- 이분 탐색 함수 (반복문)
```
def binary_search(target, data):
    data.sort()
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return



```



- 이분 탐색 함수 (재귀)
```
def binary_search(target, start, end):
    if start > end:		 # 범위를 넘어도 못찾는다면 -1을 반환
        return -1

    mid = (start + end) // 2  # 중간값

    if data[mid] == target:	# 중간값의 데이터가 target과 같다면 mid를 반환
        return mid 

    elif data[mid] > target: # target이 작으면 왼쪽 탐색
        end = mid - 1
    else:                    # target이 크면 오른쪽 탐색
        start = mid + 1

    return binary_search(target, start, end) # 줄어든 범위를 더 탐색





def solution(target, data):
    data.sort()  # 정렬(필수)
    start = 0
    end = len(data) - 1
    return binary_search(target, start, end)

```