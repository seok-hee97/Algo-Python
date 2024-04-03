import heapq


def solution(jobs):
    jobs.sort()             # 오름차순으로 정렬
    num = len(jobs)         # 작업개수
    waiting = []            # (소요시간, 요청시점)
    count = []              # 각 작업이 몇초 걸렸는지
    now = 0                 # 현재 시점

    # 모든 작업이 완료될떄까지 반복
    while len(count) != num:
        #현재 시점보다 요청 시점이 빠른 작업들을 힙에 추가
        while jobs and now >= jobs[0][0]:
            top = jobs.pop(0)
            heapq.heappush(waiting, (top[1], top[0]))

        # 대기열이 비어있고 요청 시점이 아직 안된 작업들이 있는 경우
        if jobs and waiting == []:
            top = jobs.pop(0)
            now = top[0]
            heapq.heappush(waiting, (top[1], top[0]))
  
        # 힙에서 소요 시간이 가장 짧은 작업 선택
        x,y = heapq.heappop(waiting)
        now += x 
        count.append(now-y)

    return sum(count)//num




'''
다른 풀이
import heapq

def solution(jobs):
	# 요청시각이 빠른 순서대로 정렬하며, 요청시각이 같을 경우에는 소요시간이 적게 걸리는 순서대로 정렬한다.
    tasks = sorted([(x[1], x[0]) for x in jobs],
                   key=lambda x: (x[1], x[0]), reverse=True)
    q = []
    heapq.heappush(q, tasks.pop())
    current_time, total_response_time = 0, 0
   
   # 큐(대기리스트) 에 남아있는 작업이 있을 때까지 반복문을 실행한다.
    while len(q) > 0:
        dur, arr = heapq.heappop(q) # dur은 작업 소요시간, arr은 작업 요청시각
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[-1][1] <= current_time:
            heapq.heappush(q, tasks.pop())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.pop())
    return total_response_time // len(jobs)


'''


'''
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

예를들어

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청
와 같은 요청이 들어왔습니다. 이를 그림으로 표현하면 아래와 같습니다.
Screen Shot 2018-09-13 at 6.34.58 PM.png

한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.
Screen Shot 2018-09-13 at 6.38.52 PM.png

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면
Screen Shot 2018-09-13 at 6.41.42 PM.png

- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
입출력 예
jobs	return
[[0, 3], [1, 9], [2, 6]]	9
입출력 예 설명
문제에 주어진 예와 같습니다.

0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.
문제가 잘 안풀린다면😢
힌트가 필요한가요? [코딩테스트 연습 힌트 모음집]으로 오세요! → 클릭
'''