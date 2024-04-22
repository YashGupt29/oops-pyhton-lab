def Palindrome(s):
    t = s[::-1]
    if(t==s):
        return True
    return False

s = input("Enter a string : ")
print("Is it palindrome : ",Palindrome(s))
