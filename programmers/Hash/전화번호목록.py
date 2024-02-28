def solution(phone_book):
    answer = True
    hash_map = {}               # init dict
    for phone_number in phone_book:     
        hash_map[phone_number] = 1
        # {phone_number1 : 1, phone_number2 : 1, ...}
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            #if phone_number 119-> number 1,1,9
            temp += number
            
            if temp in hash_map and temp != phone_number:
                answer = False
        

    return answer
