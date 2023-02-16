low,high=(input("enter the numbers: ")).split()

for num in range(int(low),int(high)+1):
    
    sum=0
    temp=num
    order=len(str(num))
    
    while temp!=0:
        digit=temp%10
        sum=sum+pow(digit,order)
        temp=temp//10
        
    if sum==num:
       
        print(sum,end=" ")
        
    