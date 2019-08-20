#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
def wow(a):
    b=[]
    b.append(a[0])
    b.append(a[len(a)-1])
    return b


a=[1,2,3,5]
print(a)
print(wow(a))
