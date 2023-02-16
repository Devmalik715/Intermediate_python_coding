'''
#method 1
num1=int(input("enter the first number: "))
num2=int(input("enter the 2nd number: "))

max=num1 if num1>num2 else num2

lower=max
higher=int(num1*num2)

lcm=1
for i in range(lower,higher+1,max):
    if (i%num1==0 and i%num2==0):
        lcm=i
        
        print(lcm,"is the lcm of ",num1,"and",num2)
        break
    
#method 2
num1=int(input("enter the first number: "))
num2=int(input("enter the 2nd number: "))

min=num1 if num2>num1 else num2

hcf=1

for i in range(2,min+1):
    if (num1%i==0 and num2%i==0):
        hcf=i
        
lcm= int((num1*num2)/hcf)

print("lcm of",num1,"and",num2,"is",lcm )'''

#method 3
#usimg while loop

num1=int(input("enter first number: "))
num2=int(input("enter the 2nd number: "))

def lcm_finder(num1,num2):
    if num1>num2:
        max=num1
    else:
        max=num2
    lcm=1
    temp=max
    while True:
        if (max%num1==0 and max%num2==0):
            lcm=max
            break
        max=max+temp
    
    print(lcm,"is the lcm of",num1,"and",num2) 
    
lcm_finder(num1,num2)