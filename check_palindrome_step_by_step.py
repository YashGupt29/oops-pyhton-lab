def Palindrome_Step_By_Step(s):
    i=0
    n=len(s)
    while(i<=n/2):
        if(s[i]!=s[n-i-1]):
            return False
        i+=1
    return True

s = input("Enter a string : ")
print("Is it palindrome : ",Palindrome_Step_By_Step(s))
