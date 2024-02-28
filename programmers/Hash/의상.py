def solution(clothes):
    d = {}
    answer = 1
    for name, item in clothes:
        d[item] = d.get(item,0) +1
        #.get(item,0)   
        #  item 키가 dictionary d에 존재하는지 확인하고, 존재하면 해당 값을 반환하고, 존재하지 않으면 0을 반환하는 함수
        
    for item, n in d.items():
        answer *=(n+1)
    return answer-1








'''
def solution(clothes):
  cloth_dict = {}
  for cloth in clothes:
    cloth_type = cloth[1]
    if cloth_type not in cloth_dict:
      cloth_dict[cloth_type] = 1
    else:
      cloth_dict[cloth_type] += 1

  total_cases = 1
  for cloth_type in cloth_dict:
    total_cases *= cloth_dict[cloth_type] + 1

  return total_cases - 1
'''