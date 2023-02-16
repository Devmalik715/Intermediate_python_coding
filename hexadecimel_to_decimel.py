def convert(hex):
    
    
    length=len(hex)
    decimel=0
    pos=0
    
    for i in range(length-1,-1,-1):
        
        if '0'<= hex[i] <='9':
            
            digit=ord(hex[i])-48
            decimel=decimel+ digit*pow(16,pos)
            pos+=1
            
        elif 'A'<= hex[i] <='F':
            digit =ord(hex[i])-55
            decimel+=digit*pow(16,pos)
            pos+=1
            
    return decimel

hex=input("enter the hexadecimel number: ")
print(convert(hex))