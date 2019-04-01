import math 
a=int(input())
b=int(input())
for x in range (math.ceil(math.sqrt(a)),math.floor(math.sqrt(b))+1):
    print(round(x * x))


       