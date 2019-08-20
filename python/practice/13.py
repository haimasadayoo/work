def fib(a):
    count=0
    ans=[]
    if(a==0):
        return ans
    ans.append(1)
    count+=1
    if(a==count):
        return ans
    ans.append(1)
    count+=1
    if(a==count):
        return ans
    while(1):
        if(a==count):
            return ans
        ans.append(ans[count-1]+ans[count-2])
        count+=1
num=int(input("input number:"))
print(fib(num))
