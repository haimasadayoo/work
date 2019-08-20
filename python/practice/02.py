#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

number = int(input("enter number:"))

if(number % 2 == 0):
    print(str(number)+" is even")
else:
    print(str(number)+" is odd")
    
