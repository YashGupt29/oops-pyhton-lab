def solve(n,r):
    left=1
    right=n
    ans=0
    while(left<=right):
        mid=int((left+right)/2)
        if(mid**r==n):
            ans=mid
            break
        elif(mid**r>n):
            right=mid-1
        else:
            left=mid+1

    return ans

n=int(input("Enter the value of n : "))
r=int(input("Enter the valus of r : "))

result=solve(n,r)
if(result==0):
    print("No such number exists")
else:
    print("Required number : ",result)
