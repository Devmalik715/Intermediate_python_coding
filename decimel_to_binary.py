#method 1
'''
num=int(input("enter the decimel number: "))

binary=[]
while num>0:
    binary.insert(0,num%2)
    num//=2
    
print(''.join(str(x) for x in binary))
'''

#method 2

num=int(input("enter the decimel number:  "))

def convert(num):
    binary=0
    i=1
    
    while num!=0:
        rem=num%2
        num=num//2
        binary+= rem*i
        
        i*=10
        
    print(binary)
    
convert(num)