def DFS(start, graph, visited, check_link):
    cnt = 1
    visited[start]=True                                             # 일단 v 노드는 방문함
    for adj_v in graph[start]:                                      # v에 연결 되어있는 다른 노드
        if visited[adj_v] == False and check_link[start][adj_v]:    # 인접한 연결되어 있는 노드가 방문한 적없고 
            cnt += DFS(adj_v, graph, visited, check_link)
    return cnt                                                  # 인접 연결 노드들 다 카운트

def solution(n, wires):
    answer = float("inf") 
    
    # 끊은 간선인지 아닌지 체크하기 위한 리스트 
    check_link = [[True]*(n+1) for _ in range(n+1)] 
    graph = [[] for _ in range(n+1)]    # 송전탑 그래프 

    # 그래프 채우기 
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a,b in wires:                               # 간선 정보를 다 확인하면서 
        visited = [False]*(n+1)                     # a, b 그룹의 붙어있는 송전탑 개수를 세기위해
        check_link[a][b] = False                    # a에서 b로 가는 간선을 끊어봄 
        cnt_a = DFS(a, graph, visited, check_link)  # 그때 a랑 붙어 있는 송전탑 개수 
        cnt_b = DFS(b, graph, visited, check_link)  # 그때 b랑 붙어 있는 송전탑 개수 
        check_link[a][b] = True                     # a와 b 사이 끊은 간선을 다시 붙임
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer




'''다른 풀이
from collections import deque

def BFS(start, graph, visited, check_link):
        q = deque([start])
        visited[start] = True
        cnt = 1
        while q:
            s = q.popleft()
            for adj_v in graph[s]:
                if visited[adj_v] == False and check_link[start][adj_v]: 
                    q.append(adj_v)
                    visited[adj_v] = True
                    cnt += 1
        return cnt

def solution(n, wires):
    answer = n
    
    # 끊은 간선인지 아닌지 체크하기 위한 리스트 
    check_link = [[True]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]    # 송전탑 그래프 

    # 그래프 채우기 
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a,b in wires:                               # 간선 정보를 다 확인하면서 
        visited = [False]*(n+1)                     # a, b 그룹의 붙어있는 송전탑 개수를 세기위해
        check_link[a][b] = False                    # a에서 b로 가는 간선을 끊어봄 
        cnt_a = BFS(a, graph, visited, check_link)  # 그때 a랑 붙어 있는 송전탑 개수 
        cnt_b = BFS(b, graph, visited, check_link)  # 그때 b랑 붙어 있는 송전탑 개수 
        check_link[a][b] = True                     # a와 b 사이 끊은 간선을 다시 붙임
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    
    return answer

'''

'''
- [프로그래머스][파이썬] 전력망을 둘로 나누기
https://khw11044.github.io/study/codingtest/2023-04-20-cote21/
'''

'''
문제 설명
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 2 이상 100 이하인 자연수입니다.
wires는 길이가 n-1인 정수형 2차원 배열입니다.
wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
1 ≤ v1 < v2 ≤ n 입니다.
전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.
입출력 예
n	wires	result
9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
4	[[1,2],[2,3],[3,4]]	0
7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	1
입출력 예 설명
입출력 예 #1

다음 그림은 주어진 입력을 해결하는 방법 중 하나를 나타낸 것입니다.
ex1.png
4번과 7번을 연결하는 전선을 끊으면 두 전력망은 각 6개와 3개의 송전탑을 가지며, 이보다 더 비슷한 개수로 전력망을 나눌 수 없습니다.
또 다른 방법으로는 3번과 4번을 연결하는 전선을 끊어도 최선의 정답을 도출할 수 있습니다.
입출력 예 #2

다음 그림은 주어진 입력을 해결하는 방법을 나타낸 것입니다.
ex2.png
2번과 3번을 연결하는 전선을 끊으면 두 전력망이 모두 2개의 송전탑을 가지게 되며, 이 방법이 최선입니다.
입출력 예 #3

다음 그림은 주어진 입력을 해결하는 방법을 나타낸 것입니다.
ex3.png
3번과 7번을 연결하는 전선을 끊으면 두 전력망이 각각 4개와 3개의 송전탑을 가지게 되며, 이 방법이 최선입니다.
'''