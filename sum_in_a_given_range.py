low,high= input("enter two numbers for range: ").split()

a=int(low)
b=int(high)


#for loop
'''sum=0
for i in range(a,b+1):
    sum=sum+i
    
print(sum)'''

#while loop

'''sum=0
while b>=a:
    sum=sum+b
    b=b-1
    
print(sum)'''

# here again for loop and while loop time complexity is o(n)

#for time complexity o(1) , we need to look for formula again

sum = (b*(b+1)/2)-(a*(a+1)/2)+a

print(int(sum))
