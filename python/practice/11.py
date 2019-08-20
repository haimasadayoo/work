#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

a=int(input("INPUT NUMBER:"))

b = list(range(2,a))

for i in b:
    if(a%i==0):
        print("NOT PRIME")
        exit()
print("PRIME")
