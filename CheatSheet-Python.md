# **[Algorithm]Cheat Sheet with Python**


#### TOC
- 탐색 알고리즘
  - DFS
  - BFS
- 정렬 알고리즘
  - Selection Sort
  - Quick Sort
- 탐색 알고리즘
  - Binary Search
- 다이나믹 프로그래밍
  - Top down
  - Bottom up
- 최단경로 알고리즘
  - Dijkstra
  - Floyd-Warshall





#### 탐색 알고리즘

그래프에서 모든 노드를 방문하고자 할때는 깊이 우선 탐색, DFS 가 좀더 선호(구현이 좀더 쉬움)

##### **DFS**
- Depth First Search.
- Data Structure: Stack -> 재귀함수로 구현하기 좋음
- Time complexity: O(N)

1. 탐색 시작 노드를 스택에 삽입 후 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 인접 노드를 스택에 넣고  
   방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

```python
def dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end= ' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```


###### **BFS**
- Breadth First Search. 너비 우선 탐색
- Data Structure: Queue (python deque lib 활용)
- Time complexity : O(N). but, 일반적으로 DFS보다 수행시간은 더 빠름
  
1. 탐색 시작 노드를 큐에 삽입하고 방문처리
2. 큐에서 노드를 꺼내 인접 노드중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리 한다. 



```python
from collections import deque

def dfs(graph, start, visited):
    queue = deque([start])
    # node visited
    visited[start] = True

    #loop till queue is empty
    while queue:
        # visited node 'v'
        v = queue.popleft()
        print(v, end = ' ')

        # v 노드에 연결된 노드들 투입 -> 방문 안한 노드만 queue에 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # print(queue)  # queue 안에 뭐 있나
                visited[i]= True
       
```



#### **정렬 알고리즘**

대부분 이미 구현된 내부 정렬 라이브러리를 활용하게되므로, 직접 정렬 알고리즘을 구현할 일은 많지 않겠지만 각 알고리즘의 특징정도는 알아놔야 본인이 작성한 알고리즘의 시간 복잡도를 계산할 수 있을 것이다.
참고로 Python의 sorted 함수는 내부적으로 병합정렬을 사용한다


- **Time Complexity: O(N²)**
  - Bubbe Sort(버블정렬) : 첫 원소부터 순차로 현재 원소가 그 다음 원소보다 크면 두 원소를 바꿈
  - Selection Sort(선택정렬) : 배열을 선형 탐색(linear scan)하여 가장 작은 원소를 앞으로 보냄
  - Insertion Sort(삽입정렬) : 적절한 위치에 삽입(insertion)하는 정렬. 필요할 대만 위치를 바꾸므로    
                            데이터가 정렬되어있을 때는 효율적임
    
- **Time Complexity: O(NlogN) ~ O(N²)**
  - Quick Sort(퀵정렬): 임의의 기준 대비 큰 수와 작은 수로 나누는 방식

- **Time Complexity: O(NlogN)**
  - Merge Sort(병합정렬) : 배열을 절반씩 나누어 각각 정렬하고 합해서 다시 정렬
  
구현이 가장 간단한 선택정렬과, 가장 보편적으로 사용된느 퀵 정렬 위주로 조금 더 자세히 보자


**Selection Sort**
- 선택정렬 : 가장 기초적인 정렬 알고리즘. 
- Time Complexity: O(N²)

가장 작은 데이터를 선택(Selection)해 맨 앞에 있는 데이터와 바꾸고, 그 다음 데이터를 선택해 두번째 데이터와 바꾸고.. 이 과정을 반복한다.


```python
array = [2, 3, 1, 4]
for i in range(len(array)):
    min_index = i # index of the smallest element
    for j in range(i+1, len(array)):
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

```


**Quick Sort**
- 퀵정렬. 가장 맣이 사용되는 알고리즘. 분할정복(Divide and Conquer) 방식.
- Time Complexity : 평균 O(NlogN), 최악 O(N²)
- Space Complexity : O(log N)

퀵 정렬은 임의의 기준 데이터를 설정하고 분할정복(Divide and Conquer) 해가는 방식으로 동작한다.
기준이 되는 수를 정하고 이보다 큰 수와 작은 수를 교환한 후 리스트를 반으로 나눈다.
여기서 사용되는 기준을 피벗(pivot)이라 한다.

```python
array = [2, 3, 1, 4]
def quick_sort(array):
    #quit if list has one or less elements
    if len(array) <= 1:
        return array
    
    pivot = array[0] # first element as pivot
    tail = array[1:] # list accept pivot
    left = [x for x in tail if x <= pivot] # left side
    right = [x for x in tail if x > pivot] # right side
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

```



#### 탐색 알고리즘

**Binary Search**
- Time Complexity : O(logN)

이진 탐색은, 배열 내부의 데이터가 **정렬되어 있어야** 사용 가능하다. 찾으려는 데이터와 중간점(middle) 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는다.
재귀로도 구현이 가능하지만 여기서는 반복문 형태로 구현한 Binary Search만 보면:



```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None
result = binary_search(array, target, 0, n - 1)

```


#### 다이나믹 프로그래밍

메모리 공간을 더 사용해서 연산 속도를 증가시킬 수 있는 방법 중 대표적인 것이 다이나믹 프로그래밍이다.
다이나믹 프로그래밍을 적용할 수 있는 문제는 다음과 같은 조건을 충족해야 한다.
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

다이나믹 프로그래밍은 기본이 되는 작은 문제를 식으로 쓴 점화식을 그대로 코드로 옮겨서 구현하면 된다. 즉 점화식을 찾아내는 것이 관건이다.

피보나치 수열은 다이나믹 프로그래밍을 만족하는 대표 문제다. 순수하게 재귀함수로 풀어내면 2의 n승이 되어, 100 자리까지도 실제적으로 컴퓨터로 계산할 수 없는 수가 되어 버린다. 이를 다이나믹 프로그래밍으로 O(N) 문제로 풀어낼 수 있다.

피보나치의 점화식: Fn = Fn-1 + Fn-2


- 재귀를 이용하여 큰 문제부터 작은 문제를 해결해나가는 Top-Down 방식, 메모이제이션(Memorization) 방식으로 풀수 있거나

```python
# Memoization 초기화
d = [0] * 100

def fibo(x)
  # base case
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  # 점화식을 그대로 구현
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

```

- 반복문을 이용하여 작은 문제부터 답을 도출하는 Bottom-Up 방식으로 풀어볼 수 있다.

```python
# initiate DP Table
d = [0] * 100
# both first Fibonacci number and second fibonacci number are 1
d[1] = 1
d[2] = 1
n = 99
# bottom up dynamic programming
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]

```




#### **최단경로 알고리즘**


#### Reference
- [[Algorithm]코딩테스트 대비CheatSheat with Python](https://jaemunbro.medium.com/python-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8C%80%EB%B9%84-cheat-sheet-839a0681738f)
