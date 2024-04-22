def integer_part(s,i):
    j=i
    ans=0
    num=1
    while(j>=0):
        if(s[j]=='1'):
            ans+=num
        j-=1
        num*=2
    return ans

def fraction_part(s,i):
    j=i+1
    n=len(s)
    num=1
    ans=0
    while(j<n):
        num=float(num/2)
        if(s[j]=='1'):
            ans += num
        j+=1
    return ans

s=input("Enter a binary number : ")
i=0
while(s[i]!='.' and i<len(s)-1):
    i+=1

result = integer_part(s,i)+(float)(fraction_part(s,i))
print("Decimal number : ",result)