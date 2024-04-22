def sum_through_string(s):
    numbers = s.split(',')
    sum=0
    for i in numbers:
        sum+=(float(i))

    print("Sum of numbers in string : ",sum)

str = input("Enter the string : ")
sum_through_string(str)
