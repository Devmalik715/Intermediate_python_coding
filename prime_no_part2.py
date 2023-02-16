#solution based on sqrt of n

from math import sqrt
'''
num=int(input("enter a number: "))
isprime= True

if num<2:
    isprime=False
else:
    for i in range(2,int(sqrt(num)+1)):
        if num%i==0:
            isprime=False
            break
            
result="is a prime number" if isprime else "is not a prime number"

print(num,result)'''

#solution by using 2 , bcz 2 is the only even prime number


num=int(input("enter a number: "))
    

def isprime(num):
    
    if num<=1:
        return False;
    
    elif num==2:
        return True;
        
    elif num%2==0:
        return False;
    
    for i in range(3,int(sqrt(num)+1),2):
        if num%i==0:
            return False
            
    return True

if isprime(num):
    print(str(num),"is a prime number")
    
else:
    print(str(num),"is not a prime number")
    