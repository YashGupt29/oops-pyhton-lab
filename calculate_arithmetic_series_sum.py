def sum_calculator(i,d,n):
    sum=0
    while(sum+(i+d)<=n):
        sum += (i+d)
    
    print("Sum : ",sum)

i = int(input("Enter the value of i : "))
d = int(input("Enter ther value of d : "))
n = int(input("Enter the value of n : "))
sum_calculator(i,d,n)