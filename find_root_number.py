def solve(n,r):
    ans=0
    if(r==1):
        ans=n
    else:
        for i in range(n):
            if(i**r==n):
                ans=i
                break
            if(i**r>n):
                break

    if(ans==0):
        print("Such number does not exist")
    else:
        print("Required number : ",ans)


n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))
solve(n,r)
