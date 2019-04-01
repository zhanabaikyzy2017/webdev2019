import math
a=1
n=int(input())
if n==0:
    print("0")
while a < n+1:
    print (a*a)
    a += 1
    if a*a > n:
        break