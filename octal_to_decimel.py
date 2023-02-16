def convert(num):
    num1=num
    decimel=0
    i=0
    
    base=8
    
    while num!=0:
        digit=num%10
        decimel+= digit*pow(base,i)
        num=num//10
        i=i+1
        
    print(decimel,"is the decimel of octal number",num1)
    
    
num=int(input("enter the octal number: "))

convert(num)