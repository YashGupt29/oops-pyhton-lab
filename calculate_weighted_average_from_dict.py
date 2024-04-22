def average_calculator(data):
    sum:int = 0
    sum_freq:int = 0
    for i,j in data.items():
        sum += i*j
        sum_freq += j
    
    print("Avergae of given data : ",float(sum/sum_freq))


n=int(input("Enter the number of distinct values of x : "))
data = {}
for i in range(0,n):
    x = int(input(("Enter value of x : ")))
    f = int(input(f"Enter the frequency of {x} : "))
    data[x]=f

average_calculator(data)