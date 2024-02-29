'''
https://velog.io/@helenason/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque(priorities)
    names = deque()
    for i in range(len(queue)) :
        names.append(chr(ord('A')+i))
    alp = names[location]
    
    while alp in names :
        back = False
        x = queue.popleft()
        y = names.popleft()
        for q in queue :
            if x < q :
                queue.append(x)
                names.append(y)
                back = True
                break
        if back == False :
            answer += 1
    return answer


