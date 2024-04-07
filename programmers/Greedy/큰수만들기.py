
def solution(number, k):
    # 스택 선언
    stack = []
    
    # number의 길이만큼 for loop
    for num in number:
        # 1. 제거할 수 k가 남았고
        # 2. 스택에 값이 있고
        # 3. 스택의 마지막 값이 num보다 작다면
        # 제거 후 제거할 수 k를 1씩 감소 
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        # 스택에 num 추가
        stack.append(num)
    
    # k가 남아있는 경우 - 테스트 케이스 number: "93939", k: 2, 출력: 999, 실제정답: 99
    if k != 0:
        stack = stack[:-k]
    
    # 배열을 문자열로 바꿔주고 반환
    return ''.join(stack)

'''hint: Use Stack
- PROGRAMMERS | 큰 수 만들기 - Python
https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''    


'''
-
https://aiday.tistory.com/116
'''



'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"

'''