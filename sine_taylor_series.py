def fac(n):
    if(n==0):
        return 1
    return n*fac(n-1)

def sin(x):
    ans = x - (x**3)/fac(3) + (x**5)/fac(5) - (x**7)/fac(7)
    return ans

x = float(input("Enter a value fod finding sin : "))
print(f"Sin({x}) : {sin(x)}")