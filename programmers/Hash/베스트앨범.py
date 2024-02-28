def solution(genres, plays):
    answer = [] #베스트 앨범에 들어갈 노래의 고유번호를 저장할 리스트
    dic1 = {}   #장르별 노래 정보를 저장할 dict
    dic2 = {}   #장르별 총 재생횟수를 저장할 dict

    for i, (g, p) in enumerate(zip(genres, plays)):
        # dic1[g].append((i, p)): g 장르에 (i, p) 튜플을 추가
        #i:노래고유번호
        #g:노래 장르
        #p:노래 재생횟수
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    '''
    sorted(dic2.items(), key=lambda x:x[1], reverse=True): dic2를 장르별 총 재생 횟수 기준으로 내림차순 정렬합니다.

(k, v): 정렬된 dictionary의 각 요소를 unpacking합니다.

k: 장르
v: 장르별 총 재생 횟수
sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]: k 장르의 노래를 재생 횟수 기준으로 내림차순 정렬하고, 상위 2개만 선택합니다.

(i, p): 선택된 노래 정보를 unpacking합니다.

i: 노래 고유 번호
p: 노래 재생 횟수
answer.append(i): 베스트 앨범에 i번 노래를 추가합니다.
    '''

    return answer