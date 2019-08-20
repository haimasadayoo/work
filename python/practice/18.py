import random
import copy

answer=[]
count=0
for i in range(4):
    answer.append(random.randint(0,9))
#print(answer)
while(1):
    count+=1
    c=copy.copy(answer)
    guess=input("["+str(count)+"] input 4 number: ")
    if(len(guess)==4):
        cow=0
        bull=0
        for i in range(4):
            if( int(guess[i]) in c):
                bull+=1
                c.remove(int(guess[i]))
                
                if( answer[i] == int(guess[i])):
                    cow+=1
                    
                    if(cow==4):
                        print("Cong! answer:"+guess)
                        exit()
        print("cow : "+str(cow) +" bull: "+str(bull))
    else:
        print("ERROR. input 4 number")
                        
