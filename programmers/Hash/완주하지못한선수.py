def solution(participant, completion):
    answer = 0
    # participant - completion
    #a_list = list(set(participant) - set(completion)) #fail
    # a_list = [x for x in participant if x not in completion] # [3]
    # 참가자들중 동명이인이 존재
    
    participant.sort()
    completion.sort()
    
    for par, com in zip(participant, completion):
        if par != com:
            answer = par
            return par
    answer = participant[-1]
    return participant[-1]
    
    
    
    return answer








'''test case
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
'''