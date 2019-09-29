import random
import matplotlib.pyplot as plt
import numpy as np
import math

### setting start ###
depth=300    # number of machine
number=500   # number of sample
typeg=2      # shape of answer 1=circle 2=trident 3=square
### setting end ###


#a 1st: 0 or 1
#  0: x=
#  1: y=
#b 2nd: 0-6
#c 3rd 0 or 1
#  0: under or equal
#  1: over 
#x 4th: x
#y 5th: y

# return: 1 or -1
# 1:true
# 2:false

def weak(a,b,c,x,y):
    temp=0
    if(a==0):
        if(x<b or x==b):
            if(c==0): 
                temp= 1
            else: 
                temp= -1
        elif(c==0): 
            temp= -1
        else: 
            temp= 1
    else:
        if(y<b or y==b):
            if(c==0):
                temp= 1
            else:
                temp= -1
        elif(c==0):
            temp= -1
        else:
            temp= 1
    return temp

def train_data(number,typeg):
    if(typeg==1):
        return circle(number)
    elif(typeg==2):
        return trident(number)
    elif(typeg==3):
        return square(number)

def circle(number):
    x=[]
    y=[]
    label=[]
    weight=[]
    for i in range(number):
        xtemp=random.random()*4
        ytemp=random.random()*4
        x.append(xtemp)
        y.append(ytemp)
        if((xtemp-2)*(xtemp-2)+(ytemp-2)*(ytemp-2)<=1):
            label.append(1)
        else:
            label.append(-1)
        weight.append(1/number)
    x=np.array(x)
    y=np.array(y)
    return x,y,label,weight

def trident(number):
    x=[]
    y=[]
    label=[]
    weight=[]
    for i in range(number):
        xtemp=random.random()*4
        ytemp=random.random()*4
        x.append(xtemp)
        y.append(ytemp)
        if( 1<xtemp and xtemp<=2 and 1<ytemp and ytemp<=3):
            if(ytemp<2*xtemp-1):
                label.append(1)
            else:
                label.append(-1)
        elif( 2<xtemp and xtemp <3 and 1<ytemp and ytemp<3):
            if(ytemp<-2*xtemp+7):
                label.append(1)
            else:
                label.append(-1)
        else:
            label.append(-1)
        weight.append(1/number)
    x=np.array(x)
    y=np.array(y)
    return x,y,label,weight
def square(number):
    x=[]
    y=[]
    label=[]
    weight=[]
    for i in range(number):
        xtemp=random.random()*4
        ytemp=random.random()*4
        x.append(xtemp)
        y.append(ytemp)
        if(1<xtemp and xtemp< 3 and 1<ytemp and ytemp<3):
            label.append(1)
        else:
            label.append(-1)
        weight.append(1/number)
    x=np.array(x)
    y=np.array(y)
    return x,y,label,weight
def print_data(x,y,label,number,a,b,c,d,s):
    for i in range(number):
        if(label[i]==1):
            plt.scatter(x[i], y[i],color="r")
        else:
            plt.scatter(x[i], y[i],color="b")
    
    for i in range(80):
        for j in range(80):
            ia=(i+1)/20
            ja=(j+1)/20
            if(function(a,b,c,d,s,ia,ja)>0):
                plt.scatter(ia, ja,color="m",s=1)
            #else:
                #plt.scatter(ia, ja,color="c",s=10)
                    
    plt.show()

def calcR(a,b,c,x,y,label,weight,number):
    sums=0
    for i in range(number):
        sums= sums + ( 0.5* weight[i] ) * (1- (weak (a,b,c,x[i],y[i]) * label[i] ) )
    return sums

def argR(x,y,label,weight,number):
    mina=0
    minb=0
    minc=0
    mini=800

    for a in range(2):
        for c in range(2):
            for bj in range(400):
                b=bj/100
                res=calcR(a,b,c,x,y,label,weight,number)
                if(res<mini):
                    mina=a
                    minb=b
                    minc=c
                    mini=res
    return mina,minb,minc,mini

def weight_update(x):
    if(x==0):
        return 0.01
    sita=1/2*math.log((1-x)/x)
    return sita

def function(a,b,c,d,s,x,y):
    res=0
    for i in range(d):
        res+=s[i]*weak(a[i],b[i],c[i],x,y)
    return res

# abc: machine data
# d: depth
# s: cita
# label: (x,y)data's answer
# number: number of sample

def weight_updates(a,b,c,d,s,label,number,x,y):
    res=[]
    total=0
    for i in range(number):
        temp=math.exp(-1*function(a,b,c,d,s,x[i],y[i])*label[i])
        res.append(temp)
        total+=temp
    for i in range(number):
        res[i]=res[i]/total
    return res

def testing(a,b,c,d,s,g):
    x=[]
    y=[]
    tp=0
    fp=0
    fn=0
    tn=0
    for i in range(1000):
        x=random.random()*4
        y=random.random()*4
        if(g==1):
            if((x-2)*(x-2)+(y-2)*(y-2)<=1):
                answer=1
            else:
                answer=-1
        elif(g==2):
            if( 1<x and x<=2 and 1<y and y<=3):
                if(y<2*x-1):
                    answer=1
                else:
                    answer=-1
            elif( 2<x and x <3 and 1<y and y<3):
                if(y<-2*x+7):
                    answer=1
                else:
                    answer=-1
            else:
                answer=-1
        elif(g==3):
            if(1<x and x< 3 and 1<y and y<3):
                answer=1
            else:
                answer=-1



        
        predict=function(a,b,c,d,s,x,y)
       
        if(0<=predict):
            if(answer==1):
                tp+=1
            else:
                fp+=1
        else:
            if(answer==1):
                fn+=1
            else:
                tn+=1
    if(tp+fp==0):
        Pre=1
    else:
        Pre=tp/(tp+fp)
        
    if(tp+fn==0):
        Rec=1
    else:
        Rec=tp/(tp+fn)
    if(Pre+Rec==0 ):
        F="-"
    else:
        F=2*Pre*Rec/(Pre+Rec)
        
    print("tp:"+str(tp))
    print("fp:"+str(fp))
    print("fn:"+str(fn))
    print("tn:"+str(tn))
    print("Accuracy: "+str((tp+tn)/(tp+fp+fn+tn)))
    print("Precision: "+str(Pre))
    print("Recall: "+str(Rec))
    print("F: "+str(F))            
        


### initialize start ###
As=[]    # instance of machine
Bs=[]    # same
Cs=[]    # same
Citas=[] # [depth.length]

# initialize data set
train_x,train_y,train_label,point_weight=train_data(number,typeg)

### initialize end ###
for i in range(depth):
    if(i%10==0 and i!=0):
        print("")
        print(i)
        testing(As,Bs,Cs,i,Citas,typeg)
    tempa,tempb,tempc,tempi=argR(train_x,train_y,train_label,point_weight,number)
    As.append(tempa)
    Bs.append(tempb)
    Cs.append(tempc)
    Citas.append(weight_update(tempi))
    point_weight=weight_updates(As,Bs,Cs,i,Citas,train_label,number,train_x,train_y)
print("")
print("result")
testing(As,Bs,Cs,depth,Citas,typeg)
print("")
print("generating image...")
#print_data(train_x,train_y,train_label,number,As,Bs,Cs,depth,Citas)

print("done!")
