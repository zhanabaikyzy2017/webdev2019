import math
a=2
n=int(input())
if n==0:
    print("0")
while a < n+1:
    if n % a==0:
        print(a)
        break
    a=a+1