
#method 1

num=int(input("enter the number: "))

count=0

for i in range(1,num):
    if num%i==0:
        count=count+1
        
if num<2 or count>2:
    print(num,"is not a prime number")
    
else:
    print(num,"is a prime number")
    
#method 2

num=int(input("enter the number: "))
isprime=True

if num<2:
    isprime=False
    
else:
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
        
result="is a prime number" if isprime else "is not a prime number"

print(num,result)    

#here time complexity is o(n)
    
# there should be slightly change in the range bcz numbers dont have any divisor after their half 
#for ex 32 does not have divisors after 16

#method 3

num=int(input("enter the number: "))
isprime=True

if num<2:
    isprime=False
    
else:
    for i in range(2,int(num/2)):
        if num%i==0:
            isprime=False
            break
        
result= "is a prime number"if isprime else "is not a prime number"

print(num,result)