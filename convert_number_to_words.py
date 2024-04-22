def number_to_words(n):
    ones = {1:"one", 2:"two", 3:"three",4:"four",
            5:"five", 6:"six", 7:"seven", 8:"eight",9:"nine"}
    teens = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
            15:"fifteen",16:"sixteen", 17 :"seventeen",18:"eighteen",19:"nineteen"}
    tens = {1:"ten", 2:"tweny", 3:"thirty", 4:"fourty", 5:"fifety",
            6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

    def two_digits(n):
        if n<10:
            return ones[n]
        elif n<20:
            return teens[n]
        else:
            if n%10==0 :
                return tens[n//10]
            else:
                return tens[n//10]+' '+ones[n%10]
    
    def three_digits(n):
        if n<100:
            return two_digits(n)
        else:
            if n%100==0:
                return ones[n//100]+" hundred"
            else:
                return ones[n//100]+" hundred "+two_digits(n%100)
    
    def four_to_five_digits(n):
        if n<1000:
            return three_digits(n)
        else:
            if n%1000==0:
                return three_digits(n//1000)+" thousand"
            else:
                return three_digits(n//1000)+" thousand "+three_digits(n%1000)
    
    def six_digits(n):
        if n<100000 :
            return four_to_five_digits(n)
        else:
            if n%100000==0 :
                return two_digits(n//100000)+" lakhs"
            else:
                return two_digits(n//100000)+" lakh "+four_to_five_digits(n%100000)

    return six_digits(n)


n = int(input("Enter a number to convert into words : "))
if(n>=10000000):
    print("number out of range, enter a number within 10 lakh")
else:
    print(number_to_words(n))
