def isIn(a,b):
    n = len(a)
    ln = len(b)
    i = 0
    res = False
    for i in range(n-ln+1):
        if a[i:i+ln]==b:
            return True
    return False

a = input("Enter string a : ")
b = input("Enter string b : ")
if(isIn(a,b)==True):
    print("True")
else:
    print("False")
