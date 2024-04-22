def Fib1(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        n-=2
        ans=0
        a,b=0,1
        while(n>0):
            ans=a+b
            a=b
            b=ans
            n-=1
    return ans

def Fib2(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    return Fib2(n-1)+Fib2(n-2)
    

n = int(input("Enter the value of n : "))
print("Nth Fibonacci number via iteration :",Fib1(n))
print("Nth Fibonacci number via recursion : ",Fib2(n))