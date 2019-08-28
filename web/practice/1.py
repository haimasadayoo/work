#!/usr/bin/python3

import sys
import re
import os
import cgi
import urllib.parse

def one(a):
    hiragana = re.compile(r'^[あ-ん]+$')
    katakana =re.compile(r'^[ア-ン]+$')
    eigo =re.compile(r'^[a-z]+$')
    EIGO =re.compile(r'^[A-Z]+$')
    suuji =re.compile(r'^[0-9]+$')
    eigo2 = re.compile(r'^[ａ-ｚ]+$')
    EIGO2 = re.compile(r'^[Ａ-Ｚ]+$')
    status1 = hiragana.fullmatch(a)
    status2 = katakana.fullmatch(a)
    status3 = eigo.fullmatch(a)
    status4 = EIGO.fullmatch(a)
    status5 = suuji.fullmatch(a)
    status6 = eigo2.fullmatch(a)
    status7 = EIGO2.fullmatch(a)
    if(status1==None and status2==None and status3==None and status4==None and status5==None and status6 ==None and status7 ==None):
        return a
    else:
        return ""

def toKanji(text):
    text=str(text)
    res=""
    for i in range(len(text)):
        print(str(i)+": "+text[i]+"   type: "+str(type(text[i]))+"<br>")
        res=res+one(text[i])
    return res
print("Content-type: text/html")
print("")
print("")


if 'QUERY_STRING' in os.environ:
    query=os.environ['QUERY_STRING']
    temp = urllib.parse.unquote(query)
    test=toKanji(temp)
else:
    query =""
    temp=""
    test=""

print("query:"+query+"<br>")
print("temp:"+temp+"<br>")
print("test:"+test+"<br>")

"""
query2=input("input txt:")
temp2=urllib.parse.unquote(query2)
test2=toKanji(temp2)
print("query:"+query2)
print("temp:"+temp2)
print("test:"+test2)
"""
