'''
- [프로그래머스 Lv2][완전탐색] 소수 찾기(python)
https://yuna0125.tistory.com/150
https://velog.io/@highero-k/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-Python-Level-2


- permutations
https://pearlluck.tistory.com/468
'''

from itertools import permutations

# for check is it Prime??
def isPrime(x):
    if x < 2 :
        return False
    for i in range(2, x) :
        if x % i == 0 :
            return False

    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    temp = []
    
    for i in range(1, len(numbers)+1):
        temp += list(permutations(numbers, i)) 
        # print(temp)
    num = [int(''.join(t)) for t in temp] 
    
    print(num)
    for i in num:
        if isPrime(i):
            answer.append(i)
    
    return len(set(answer))




'''소수인지 확인하는 함수 isPrime
def isPrime(n):
    if n ==1:
        return False
        
    for i in range(2, int(n**0.5)+1):
        if n %1 ==0:
            return False
            
    return True
'''


'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
'''