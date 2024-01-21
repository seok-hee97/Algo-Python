n = input()                 # 숫자 개수
numbers = list(input())     #Numbers 변수에 list함수 이용하여 숫자를 한자리씩 나누어 받기
sum = 0
for i in numbers:
    sum = sum + int(i)  #number에 있는 각 자리 수를 가져와 더해주기
print(sum)
