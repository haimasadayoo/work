#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

today=datetime.date.today()

#testing module works or not.
#print(today.year)

name=str(input("enter your name:"))
age =int(input("enter your age:"))

print(name+" will be 100 years old in the "+str((today.year-age)+100))
