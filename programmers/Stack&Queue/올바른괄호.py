def solution(s):
    answer = True
    
    stack = []
    
    #문자열 s크기만큼 반복  
    for i in s:
        if i == '(':
            stack.append('(')
        
        #')'일 경우
        else:
        	#스택이 빈 경우 ')'가 들어올 때
            if stack == []:
                return False
            
         	#스택 안에 '('가 있고 ')'가 들어와 올바른 괄호 
            else:
                stack.pop()
    
    #for문이 다 끝났는데도 '(' 괄호가 남아있는 경우
    if stack != []:
        return False
    
    return True




'''

문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
'''