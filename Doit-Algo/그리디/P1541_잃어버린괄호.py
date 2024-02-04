answer = 0
A = list(map(str, input().split("-")))          # 들어온 데이터를   "-" 기준으로 split.  


def mySum(i):                           # -로 나뉘 그룹들의 합을 구하는 함수
    sum = 0
    temp = str(i).split("+")            # 현재 들어온 string값을 "+" 기호 기준으로 split()
    for i in temp:
        sum += int(i)                   # str -> int 변환해 더하기
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        answer += temp          # 가장 앞에 있는 값만 더하기
    else:
        answer -= temp          # 뒷부분의 값은 합쳐서 빼기
print(answer)
