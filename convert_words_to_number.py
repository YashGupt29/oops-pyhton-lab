def words_to_number(s):
    ones = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    teens = {"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,
            "seventeen":17,"eighteen":18,"nineteen":19}
    tens = {"ten":10,"twenty":20,"thirty":30,"fourty":40,"fifty":50,
            "sixty":60,"seventy":70,"eighty":80,"ninety":90}
    
    ans=int(0)
    i=0
    while i<len(s):
        # print(s[i])
        if s[i] in ones:
            temp=ones[s[i]]

        elif s[i] in teens:
            temp=teens[s[i]]

        elif s[i] in tens:
            temp=tens[s[i]]
            if i+1<len(s):
                if s[i+1] in ones:
                    temp+=ones[s[i+1]]
                    i+=1
                    
        if i+1<len(s):
            if s[i+1]=="hundred":
                temp*=100
            elif s[i+1]=="thousand":
                temp*=1000
            elif s[i+1]=="lakhs":
                temp*=100000
        ans+=temp
        temp=0
        i+=1

    return ans


n=input("Enter a number in words within 99 lakhs: ")
temp=""
s=[]
for x in n:
    if x==" ":
        s.append(temp)
        temp=""
    else:
        temp+=x

s.append(temp)

print("Number in digits : ", words_to_number(s))
