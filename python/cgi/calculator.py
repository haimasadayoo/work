#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os

def errorcheck(text):
    for i in text:
        if( not(i.isdecimal())):
            if( not( i=="+" or i=="-" or i=="*" or i=="/")):
                return "ERROR"
    return
#txt = os.environ['QUERY_STRING']

txt="3+5+2*5/3"
print("Content-Type: text/html")
print("")
if( errorcheck(txt) == "ERROR"):
    print("ERROR")
else:
    print(txt+" = "+str(round(eval(txt))))
