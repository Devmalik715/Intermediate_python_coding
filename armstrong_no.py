num=int(input("enter the number: "))

temp=num
order=len(str(num))
sum=0

while temp!=0:
    digit=temp%10
    
    sum=sum+pow(digit,order)
    temp=temp//10
    

if sum==num:
    print(num,"is armstrong no.")
else:
    print(num,"is not an armstrong no.")