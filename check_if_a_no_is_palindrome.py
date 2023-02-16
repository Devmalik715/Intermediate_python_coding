num= int(input("enter a number: "))

num1=num

reverse =0
while num1!=0:
    
    reverse=reverse*10 + num1%10
    num1=num1//10

print(reverse)



if reverse==num:
    print(num,"is a palindrome")
    
else:
    print(num,"is not a palindrome")