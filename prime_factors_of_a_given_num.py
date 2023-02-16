from math import sqrt

num=int(input("enter a number: "))
def prime_factor(num):
    
    for i in range(2,int(sqrt(num)+1)):
        while num%i==0:
            
            print(i,end=" ")
            num=num/i
        
    
    if num>2:
        print(int(num))
    

prime_factor(num)