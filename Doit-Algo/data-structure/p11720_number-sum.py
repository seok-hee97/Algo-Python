
n = input() #input var number count

numbers = list(input()) #input number without whitespace
#ex) list(1234) => ['1', '2', '3', '4']

sum = 0         #var sum(result)

for i in numbers:
    sum = sum + int(i)  #str->int for calc
    

print(sum)          #print result