# Programmers 알고리즘 문제 풀이

프로그래머스 알고리즘 고득점 Kit의 유형별 문제 풀이와 핵심 개념을 정리한
인덱스입니다.

## 알고리즘 분류

| 분류 | 폴더 | 핵심 개념 |
| --- | --- | --- |
| 해시 | [Hash](./Hash/) | 키와 값을 이용한 빠른 조회, 빈도 계산, 중복 제거, 그룹화 |
| 스택/큐 | [Stack & Queue](./Stack&Queue/) | LIFO, FIFO, `deque`, 순서가 있는 작업 처리와 시뮬레이션 |
| 힙 | [Heap](./Heap/) | 우선순위 큐, 최솟값·최댓값의 반복 추출, 작업 스케줄링 |
| 정렬 | [Sort](./Sort/) | 정렬 기준 설정, 사용자 정의 비교, 정렬 후 순위·통계 계산 |
| 완전탐색 | [Brute Force Search](./Brute-Force-Search/) | 모든 경우의 수 탐색, 순열·조합, 백트래킹과 가지치기 |
| 탐욕법 | [Greedy](./Greedy/) | 매 단계의 최선 선택, 정렬 기반 선택, 최적해 성립 조건 |
| 동적 계획법 | [Dynamic Programming](./Dynamic-Programming/) | 상태 정의, 점화식, 중복 부분 문제, 메모이제이션·테이블 채우기 |
| 깊이/너비 우선 탐색 | [DFS / BFS](./DFS-BFS/) | 그래프 탐색, 연결 요소, 최단 거리, 재귀·스택·큐 |
| 이분 탐색 | [Binary Search](./Binary-Search/) | 정렬된 범위 탐색, 탐색 구간 축소, 파라메트릭 서치 |
| 그래프 | [Graph](./Graph/) | 정점과 간선, 인접 리스트, 경로·도달성·연결 관계 |

## 폴더별 개념 및 문제

### [Hash](./Hash/)

해시 테이블은 키를 기준으로 값을 저장하여 평균적으로 빠른 조회·삽입·삭제를
제공합니다. 문제의 대상을 고유 키로 바꾸고 개수를 세거나 그룹으로 묶는 문제에
적합합니다. 파이썬에서는 주로 `dict`, `set`, `collections.Counter`를 사용합니다.

- [베스트앨범](./Hash/베스트앨범.py)
- [완주하지못한선수](./Hash/완주하지못한선수.py)
- [의상](./Hash/의상.py)
- [전화번호목록](./Hash/전화번호목록.py)
- [폰켓몬](./Hash/폰켓몬.py)

### [Stack & Queue](./Stack&Queue/)

스택은 나중에 들어온 값부터 처리하는 LIFO 구조이고, 큐는 먼저 들어온 값부터
처리하는 FIFO 구조입니다. 처리 순서, 대기열, 괄호 검사, 이전 상태 추적이 핵심인
문제에 활용하며 효율적인 큐 연산에는 `collections.deque`를 사용합니다.

- [개념 정리](./Stack&Queue/Stack-Queue.md)
- [같은숫자는싫어](./Stack&Queue/같은숫자는싫어.py)
- [기능개발](./Stack&Queue/기능개발.py)
- [다리를지나는트럭](./Stack&Queue/다리를지나는트럭.py)
- [올바른괄호](./Stack&Queue/올바른괄호.py)
- [주식가격](./Stack&Queue/주식가격.py)
- [프로세스](./Stack&Queue/프로세스.py)

### [Heap](./Heap/)

힙은 우선순위가 가장 높은 원소를 빠르게 꺼내기 위한 자료구조입니다. 파이썬의
`heapq`는 최소 힙이며, 삽입과 삭제는 `O(log N)`에 수행됩니다. 최솟값을 반복해서
합치거나 우선순위에 따라 작업을 처리하는 문제에 적합합니다.

- [개념 정리](./Heap/Heap.md)
- [더맵게](./Heap/더맵게.py)
- [디스크컨트롤러](./Heap/디스크컨트롤러.py)
- [이중우선순위큐](./Heap/이중우선순위큐.py)

### [Sort](./Sort/)

정렬은 데이터를 일정한 기준으로 재배치하여 이후 탐색이나 비교를 단순하게
만듭니다. `sorted()`와 `list.sort()`의 `key`를 활용하며, 숫자를 문자열처럼
비교하는 등 문제에 맞는 정렬 기준을 정의하는 것이 중요합니다.

- [H-Index](./Sort/H-Index.py)
- [K번째수](./Sort/K번쟤수.py)
- [가장큰수](./Sort/가장큰수.py)

### [Brute Force Search](./Brute-Force-Search/)

완전탐색은 가능한 모든 후보를 확인하여 답을 찾는 방법입니다. 입력 크기를 먼저
확인하고 순열, 조합, 중복 순열, DFS 기반 백트래킹을 선택합니다. 탐색 중 답이 될
수 없는 경우를 미리 제외하는 가지치기로 실행 시간을 줄일 수 있습니다.

- [모음사전](./Brute-Force-Search/모음사전.py)
- [모의고사](./Brute-Force-Search/모의고사.py)
- [소수찾기](./Brute-Force-Search/소수찾기.py)
- [전력망을둘로나누기](./Brute-Force-Search/전력망을둘로나누기.py)
- [최소직사각형](./Brute-Force-Search/최소직사각형.py)
- [카펫](./Brute-Force-Search/카펫.py)
- [피로도](./Brute-Force-Search/피로도.py)

### [Greedy](./Greedy/)

탐욕법은 각 단계에서 현재 가장 좋아 보이는 선택을 하여 전체 해를 구성합니다.
정렬 후 선택하거나 구간을 끝점 기준으로 처리하는 방식이 자주 사용됩니다. 지역
최적 선택이 전체 최적해로 이어지는지 교환 논증이나 반례 검토로 확인해야 합니다.

- [구명보트](./Greedy/구명보트.py)
- [단속카메라](./Greedy/단속카메라.py)
- [섬연결하기](./Greedy/섬연결하기.py)
- [조이스틱](./Greedy/조이스틱.py)
- [체육복](./Greedy/체육복.py)
- [큰수만들기](./Greedy/큰수만들기.py)

### [Dynamic Programming](./Dynamic-Programming/)

동적 계획법은 큰 문제를 중복되는 작은 문제로 나누고 결과를 저장해 재사용합니다.
상태가 의미하는 값과 상태 사이의 점화식, 초기값을 명확히 정의하는 것이 핵심이며,
위에서 내려가는 메모이제이션과 아래에서 올라가는 테이블 방식으로 구현할 수 있습니다.

- [N으로표현](./Dynamic-Programming/N으로표현.py)
- [정수삼각형](./Dynamic-Programming/정수삼각형.py)

### [DFS / BFS](./DFS-BFS/)

DFS는 한 경로를 깊게 탐색한 뒤 되돌아오며 재귀나 스택으로 구현합니다. BFS는
가까운 정점부터 탐색하며 큐를 사용하므로 가중치가 없는 그래프의 최단 거리 계산에
적합합니다. 두 방식 모두 방문 여부를 관리하여 중복 탐색을 막아야 합니다.

- [개념 정리](./DFS-BFS/DFS-BFS.md)
- [게임맵최단거리](./DFS-BFS/게임맵최단거리.py)
- [네트워크](./DFS-BFS/네트워크.py)
- [단어변환](./DFS-BFS/단어변환.py)
- [아이템줍기](./DFS-BFS/아이템줍기.py)
- [여행경로](./DFS-BFS/여행경로.py)
- [타겟넘버](./DFS-BFS/타겟넘버.py)
- [퍼즐조각채우기](./DFS-BFS/퍼즐조각채우기.py)

### [Binary Search](./Binary-Search/)

이분 탐색은 정렬된 탐색 범위를 절반씩 줄여 `O(log N)`에 원하는 값을 찾습니다.
특정 값의 존재 여부뿐 아니라 조건을 만족하는 최솟값·최댓값을 찾는 파라메트릭
서치에도 사용하며, 경계값과 종료 조건을 일관되게 관리하는 것이 중요합니다.

- [개념 정리](./Binary-Search/BinarySearch.md)
- [입국심사](./Binary-Search/입국심사.py)
- [징검다리](./Binary-Search/징검다리.py)

### [Graph](./Graph/)

그래프는 정점과 간선으로 대상 사이의 관계를 표현합니다. 인접 리스트나 인접
행렬로 저장하고, BFS·DFS로 경로와 연결 요소를 탐색합니다. 문제에 따라 최단 거리,
도달 가능성, 위상 관계, 사이클과 같은 특성을 분석합니다.

- [개념 정리](./Graph/Graph.md)
- [가장먼노드](./Graph/가장먼노드.py)
- [방의개수](./Graph/방의개수.py)
- [순위](./Graph/순위.py)

## SQL 고득점 Kit 학습 항목

- SELECT
- SUM, MAX, MIN
- GROUP BY
- IS NULL
- JOIN
- String, Date
