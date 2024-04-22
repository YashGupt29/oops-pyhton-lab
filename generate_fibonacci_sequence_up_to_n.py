def Fibonacci(n):
    if(n==0):
        return [0]
    
    a,b=0,1
    ans=[0,1]
    res=1
    while(a+b<=n):
        ans.append(a+b)
        temp = b
        b=a+b
        a=temp

    return ans

n = int(input("Enter a value of n : "))
ans = Fibonacci(n)
print(ans)