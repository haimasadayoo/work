import random

def generate(number):
    s="1234567890-^\qwertyuiop@[asdfghjkl;:]zxcvbnm,./\!#$%&()~=~~|QWERTYUIOP`{ASDFGHJKL+*}ZXCVBNM<>?_"
    password=""
    for i in range(number):
        temp=random.randint(0,94)
        password=password+s[temp]
    return password

a=int(input("input passwords length:"))
print(generate(a))

    
