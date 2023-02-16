'''num=int(input("enter the number: "))

reverse=0
rem=0

while num!=0:
    rem =num%10
    reverse= (reverse*10)+rem
    num=num//10
    
print(reverse)'''

#the problem in the above code is that , we cant find reverse of negative numbers

num=int(input("enter the number: "))
def reverse(num):
    if num<0:
        num =str(abs(num)) + "-"
        
    return int(str(num)[::-1])

print(reverse(num))