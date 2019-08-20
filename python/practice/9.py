#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

import random,sys
a = random.randint(1, 9)

b=0

while(1):
    b=input("input number:")
    b=int(b)
    if(a<b):
        print(str(b)+":too HIGH.")
    elif(a>b):
        print(str(b)+":too LOW.")
    elif(a==b):
        print(str(b)+":answer.")
        sys.exit()
    else:
        print("ERROR")
        
