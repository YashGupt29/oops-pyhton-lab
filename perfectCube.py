n=int(input("Enter a number to check for perfect cube : "))

ans=0
for i in range(n):
    if(i**3 > n):
        break
    if(i**3 == n):
        ans=i
        break

if(ans==0):
    print("False")


else:
    print("True")

