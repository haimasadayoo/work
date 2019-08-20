#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import os
from urllib import parse

### file module ###
def get_dict():
    f=open("data.txt","r")
    txt=f.read()
    f.close()
    if( len(txt) < 2 ):
        di={}
        return di
    di=json.loads(txt)
    return di

def write_dict():
    f=open("data.txt","w")
    sorted(data.items(), key=lambda x: x[0])
    text=json.dumps(data)
    f.write(text)
    f.close()
    return

def get_price():
    f=open("price.txt","r")
    txt=f.read()
    price=int(txt)
    f.close()
    return price

def write_price(x):
    f=open("price.txt","w")
    price=str(x)
    f.write(price)
    f.close()
    return

### file module end ###

### dict module ###

def find_item(name):
    if( len(data) == 0 ):
        return -1
    for i in range( len(data) ):
        if( name == key[i] ):
            return i
    return -1

### dict module end ###

### error module ###

def e_add(name,amount): #1
    if(type(name)!=str):
        print("ERROR")
        sys.exit()
    if(type(amount)!=int):
        print("ERROR")
        sys.exit()
    return 

def e_check(name): #2
    if( len(name) == 0):
        return
    if(type(name)!=str):
        print("ERROR")
        sys.exit()
    return

def e_sell(name,amount,price): #3
    e_add(name,amount)
    if( type(price) != int):
        print("ERROR")
        sys.exit()
    if( find_item(name) == -1):
        print("ERROR")
        sys.exit()
    return

### error module end ###

### 5 modules ###
def add_item(name,amount=1):
    e_add(name,amount)
    i = find_item(name)
    if(i!=-1):
        data[ key[i] ] += amount
        
    else:
        data[name]=amount
    write_dict()

def check_item(name=""):
    e_check(name)
    if( len(name) == 0):
        for i in range(len(data)):
            print(key[i],": ",data[key[i]],sep='')
        return
    i=find_item(name)
    if(i == -1):
        print("ERROR")
        sys.exit()
    else:
        print(key[i],": ",data[key[i]],sep='')
    return

def sell_item(name,amount=1,price=0):
    e_sell(name,amount,price)
    i=find_item(name)
    if( i == -1 ):
        print("ERROR")
        sys.exit()
    if( data[key[i]] < amount ):
        print("ERROR")
        sys.exit()
    else:
        data[key[i]]-=amount
        if(price!=0):
            total_price=get_price()
            total_price+=price*amount
            write_price(total_price)
        write_dict()
    return

def check_sales():
    a=get_price()
    print("sales: ",a,sep='')
    return

def delete_all():
    f=open("data.txt","w")
    f.write("{}")
    f.close()
    f=open("price.txt","w")
    f.write("0")
    f.close()
    return
### 5 modules end ###

### input ###
def get_input():
    txt=os.environ['QUERY_STRING']
    q_dict=parse.parse_qs(txt)
    if("function" in q_dict):
        f=q_dict["function"][0]
    else:
        print("ERROR")
        sys.exit()
        return
    if("name" in q_dict):
        n=q_dict["name"][0]
    else:
        n=None
    if("amount" in q_dict):
        a=q_dict["amount"][0]
        if("." in a):
            print("ERROR")
            sys.exit()
        a=int(a)
    else:
        a=1

    if("price" in q_dict):
        p=q_dict["price"][0]
        p=int(p)
    else:
        p=0
    return f,n,a,p

### input end ###

### RUN ### 
def run(f,n,a,p):
    if(f=="addstock"):
        if(n==None):
            print("ERROR")
            sys.exit()
        add_item(n,a)
        return

    elif(f=="checkstock"):
        if(n==None):
            check_item()
        else:
            check_item(n)
        return

    elif(f=="sell"):
        if(n==None):
            print("ERROR")
            sys.exit()
        else:
            sell_item(n,a,p)
        return
    elif(f=="checksales"):
        check_sales()
        return
    elif(f=="deleteall"):
        delete_all()
    else:
        print("ERROR")
        sys.exit()

### RUN END###
###start main ###
print("Contetn-Type: text/html")
print("")
data=get_dict()
keydict=data.keys()
key=list(keydict)
f,n,a,p=get_input()
run(f,n,a,p)
#print(f,n,a,p)
#print(data)
### main end ###

