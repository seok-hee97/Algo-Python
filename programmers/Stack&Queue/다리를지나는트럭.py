from collections import deque       #import deque lib

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)       #save truck_weight in deque
    wait = deque()                      #init wait deque
    sum_weight = 0                      #total weigth
    time = 0                            #init time
    while trucks:                       #truck deque가 빌때까지
        time += 1                       #시간을 1초 증가
        while wait and wait[0][0] <= time: # 큐 wait에 트럭이 있고, 가장 앞에 있는 트럭의 다리를 건너는 시간이 현재 시간보다 작거나 같은 경우
            t,w = wait.popleft()    #큐 wait에서 가장 앞에 있는 트럭의 정보(다리 건너는 시간, 무게)를 꺼냄
            sum_weight -= w         #다리 위 트럭들의 총 무게에서 꺼낸 트럭의 무게를 뻄
        if sum_weight+trucks[0] <= weight:  #다리 위 트럭들의 총 무게와 큐 trucks의 가장 앞에 있는 트럭의 무게가 다리의 최대 무게를 넘지 않는 경우
            truck = trucks.popleft()        #큐 trucks에서 가장 앞에 있는 트럭 꺼냄
            wait.append((bridge_length+time,truck)) #꺼낸 트럭을 다리 건너는 시간(현재시간+ 다리 길이)과 함께 큐 wait에 추가
            sum_weight += truck
    return wait[-1][0]      #마지막으로 다리를 건너는 트러그이 다리 건너는 시간을 변환