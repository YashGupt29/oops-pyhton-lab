left=1
right=25
ans=0
while(left<=right):
    mid=int((left+right)/2)
    if(mid**2==25):
        ans=mid
        break
    elif(mid**2>25):
        right=mid-1
    else:
        left=mid+1

print("Squre root of 25 : ",ans)
