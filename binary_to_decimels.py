def convert(num):
    num1=num
    i=0
    decimel=0
    while num!=0:
        digit=num%10
        decimel=decimel + digit*pow(2,i)
        i+=1
        num=num//10
    print(decimel,"is the decimel conversion of binary number",num1)
    
    
num=int(input("enter a binary number: "))

convert(num)