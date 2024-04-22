def Fact1(n):
    if(n==0):
        return 1
    ans=1
    while(n>0):
        ans*=n
        n-=1
    
    return ans

def Fact2(n):
    if(n==0):
        return 1
    return n*Fact2(n-1)

n = int(input("Enter a number : "))
print("Factoral via iteration : ",Fact1(n))
print("Factoral via recursion : ",Fact2(n))
