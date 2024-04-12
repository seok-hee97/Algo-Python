# DFS / BFS


- DFS
  

- 재귀로 표현 
```python
# g = graph
# v = visit
# visited = visited
def DFS(g,v,visited):
	visited[v] = True
	print(v,end =' ')
	for i in g[v]:
		if not visited[i]:
			dfs(g,i,visited)
```


```python
def dfs_iteration(graph, root):
    # visited = 방문한 꼭지점들을 기록한 리스트
    visited = []
    # dfs는 stack, bfs는 queue개념을 이용한다.
    stack = [root]
    
    while(stack): #스택에 남은것이 없을 때까지 반복
        node = stack.pop() # node : 현재 방문하고 있는 꼭지점
        
        #현재 node가 방문한 적 없다 -> visited에 추가한다.
        #그리고 해당 node의 자식 node들을 stack에 추가한다.
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
    return visited
# 출처: https://juhee-maeng.tistory.com/entry/Python-깊이-우선-탐색DFS-구현하기 [simPLE:티스토리]
```




- BFS

```python
from collections import deque

def BFS(g,start,visited):
	queue = deque([start])
	visited[start] = True

	while queue:
		v = queue.popleft()
		print(v,end=' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visitied[i] = True
```