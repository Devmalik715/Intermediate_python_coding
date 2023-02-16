#best way using for loop
from math import sqrt

a=int(input("enter the lower limit: "))
b=int(input("enter the higher limit: "))

def isprime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    
    for i in range(3,int(sqrt(n)+1),2):
        if n%i==0:
            return False
    
    return True

for i in range(a,b+1):
    if isprime(i):
        print(i,end=" ")