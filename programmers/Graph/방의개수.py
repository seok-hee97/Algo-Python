dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(arrows):
    r, c = 0, 0
    cycle_cnt = 0
    visited_node = set()
    visited_node.add((0, 0))
    visited_route = set()
    for arrow in arrows:
        for _ in range(2):
            nr, nc = r+dr[arrow], c+dc[arrow]
            if (nr, nc) in visited_node and (r, c, nr, nc) not in visited_route:
                cycle_cnt += 1
            visited_route.add((r, c, nr, nc))
            visited_route.add((nr, nc, r, c))
            visited_node.add((nr, nc))
            r, c = nr, nc
    return cycle_cnt


'''
https://velog.io/@jadenkim5179/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%A9%EC%9D%98-%EA%B0%9C%EC%88%98
'''

'''
문제 설명
원점(0,0)에서 시작해서 아래처럼 숫자가 적힌 방향으로 이동하며 선을 긋습니다.

스크린샷 2018-09-06 오후 4.55.33.png

ex) 1일때는 오른쪽 위로 이동

그림을 그릴 때, 사방이 막히면 방하나로 샙니다.
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 방의 갯수를 return 하도록 solution 함수를 작성하세요.

제한사항
배열 arrows의 크기는 1 이상 100,000 이하 입니다.
arrows의 원소는 0 이상 7 이하 입니다.
방은 다른 방으로 둘러 싸여질 수 있습니다.
입출력 예
arrows	return
[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	3
입출력 예 설명
스크린샷 2018-09-06 오후 5.08.09.png

(0,0) 부터 시작해서 6(왼쪽) 으로 3번 이동합니다. 그 이후 주어진 arrows 를 따라 그립니다.
삼각형 (1), 큰 사각형(1), 평행사변형(1) = 3
'''