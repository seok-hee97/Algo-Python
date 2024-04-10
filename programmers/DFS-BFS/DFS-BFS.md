# DFS / BFS



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
from collections import deque

def bfs(g,start,visited):
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