def max(a,b):
    if(a>=b):
        return a
    else:
        return b

ans=0
print("Enter 10 numbers one by one")
for i in range(10):
    n=int(input())
    if(n%2==1):
        ans=max(ans,n)


if(ans==0):
    print("No odd number")
else:
    print("Largest odd number : ", ans)
