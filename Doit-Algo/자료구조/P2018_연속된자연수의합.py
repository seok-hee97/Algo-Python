"""
투 포인터 이동 원칙
sum >N: sum = sum - start_index; start_index++;
sum <N: end_index++; sum = sum+ end_index;
sum == N: end_index++; sum = sum + end_index; count++:    
"""




n = int(input())                # 변수 저장

# 사용 변수 초기화(count=1, start_index=1, end_index=-1, sum=1)
count = 1
start_index = 1
end_index = 1
sum = 1


while end_index != n:                       #반복문 종료 조건
    if sum == n:                            #sum == n 일때 경우의 수+1
        count += 1
        end_index += 1
        sum += end_index                    
    elif sum > n:                           # sum >n
        sum -= start_index
        start_index += 1
    else:                                   # sum <n
        end_index += 1
        sum += end_index
print(count)
