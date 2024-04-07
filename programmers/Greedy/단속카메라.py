def solution(routes):
    #routes : [[-20,-15], [-14,-5], [-18,-13], [-5,-3]] 진입 시점, 나간시점
    
    # 진출지점에 대해서 오름차순 정렬
    routes.sort(key = lambda x: x[1])
    
    # 기준은 제한사항 참조
    key = -30001
    
    #필요한 카메라 수
    answer = 0
    
    for route in routes:
        # 기준(카메라)보다 진입지점이 뒤에 있으면
        if route[0] > key:
            # 단속이 안되기에 카메라 하나 더 필요
            answer +=1
            # 새로운 기준은 해당 경로의 진출지점(맨끝)
            key = route[-1]
    return answer



'''
- [프로그래머스, 파이썬] 단속카메라,Greedy
https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A8%EC%86%8D%EC%B9%B4%EB%A9%94%EB%9D%BC-Greedy
'''
'''문제 설명
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

제한사항

차량의 대수는 1대 이상 10,000대 이하입니다.
routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.
입출력 예

routes	return
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	2
입출력 예 설명

-5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.

-15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.

'''