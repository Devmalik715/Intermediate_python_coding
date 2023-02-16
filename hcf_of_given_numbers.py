num1=int(input("enter the first number: "))
num2=int(input("enmter the 2nd number: "))

smaller=num1 if num2>num1 else num2
hcf=1

for i in range(1,smaller+1):
    if (num1%i==0) and (num2%i==0):
        hcf=i
        
print(hcf,"is the hcf of",num1,"and",num2)
        