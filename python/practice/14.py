def double(a):    
    b=[]
    for i in a:
        if(not(i in b)):
            b.append(i)
    return b

a=[1,2,3,4,5,1,2,8,5,3,6,78,4,2,4,1,9]
b=double(a)
print(b)
        
