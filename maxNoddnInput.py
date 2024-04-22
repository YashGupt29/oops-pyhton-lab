def max(a,b):
    if(a>=b):
        return a
    else:
        return b


n=int(input("Enter the size of the list : "))
print("Enter the elements of the list")
ans=0
for i in range(n):
    n=int(input())
    if(n%2==1):
        ans=max(ans,n)


if(ans==0):
    print("No odd number")
else:
    print("Largest odd number : ",ans)
