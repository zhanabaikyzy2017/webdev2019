import math
a=0
n=int(input())
if n==0:
    print("0")
while a < n+1:
    if pow(2,a)<=n:
        print(pow(2,a))
    a=a+1