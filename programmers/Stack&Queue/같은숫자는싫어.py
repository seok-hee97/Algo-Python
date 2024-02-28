def solution(arr):
    answer = [arr[0]]       #arr배열의 첫번째 값을 리스트에 담음
    for i in range(1, len(arr)):        #1 부터니깐 arr[1:] 부터
        if arr[i] != arr[i-1]:          # 조건문 값은 값이 아니면
            # arr[i-1]하는 이유는 첫번째 값과도 비교하기 위해서
            answer.append(arr[i])
    return answer