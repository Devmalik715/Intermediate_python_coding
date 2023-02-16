num= int(input("enter a number: "))

#for loop
'''sum=0

for i in range(num+1):
    sum=sum+i
    
print(sum)'''

#while loop
'''sum=0

while num>0:
    sum=sum+num
    num=num-1
    
print(sum)'''

#time complexity for while loop and for loop is o(n)

#but there is a smarter way to do it , for which time complexity will be o(1)

print(int(num*(num+1)/2))
