#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

a=input("input words.")
for i in range(len(a)):
    if(a[i]!=a[len(a)-i-1]):
        print("NOT palindrome.")
        exit()
print("palindrome.")
