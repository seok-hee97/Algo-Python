def solution(distance, rocks, n):
    # 커트라인 최솟값 = 1
    left =1
    # 커트라인 최댓값  = distance
    right = distance
    
    # 바위 위치를 정렬하고, 도착지점 append
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left+right)//2
        #제거한 바위 개수
        delete = 0
        #이전 바위의 위치
        prev_rock = 0
        for rock in rocks:
            dist = rock - prev_rock
            #거리가 커트라인보다 적다면, 바위를 제거
            if dist < mid:
                delete +=1
                #제거한 바위가 너무 많다면 break
                if delete > n:
                    break
            
            #바위를 제거하지 않았다면, prev_rock을 갱신
            else:
                prev_rock = rock
                
        # 초과 제거한 경우 : 커트라인이 너무 높음
        if delete > n:
            right = mid -1
        # 이하 제거한 경우 : 커트라인이 적절하거나 너무 낮음
        else:
            answer = mid
            left = mid +1
    
    return answer



'''
https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''

'''문제 설명
출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

제거한 바위의 위치	각 바위 사이의 거리	거리의 최솟값
[21, 17]	[2, 9, 3, 11]	2
[2, 21]	[11, 3, 3, 8]	3
[2, 11]	[14, 3, 4, 4]	3
[11, 21]	[2, 12, 3, 8]	2
[2, 14]	[11, 6, 4, 4]	4
위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

제한사항
도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
바위는 1개 이상 50,000개 이하가 있습니다.
n 은 1 이상 바위의 개수 이하입니다.
입출력 예
distance	rocks	n	return
25	[2, 14, 11, 21, 17]	2	4
입출력 예 설명
문제에 나온 예와 같습니다.

출처

※ 공지 - 2020년 2월 17일 테스트케이스가 추가되었습니다.
※ 공지 - 2023년 5월 15일 테스트케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.

'''