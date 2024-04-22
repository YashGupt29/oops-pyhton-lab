def average_calculator():
    n=5
    f=[1,2,3,4,5]
    x=[2,3,5,7,1]
    sum:int=0
    sum_freq:int=0
    for i in range(0,n):
        sum+=x[i]*f[i]
        sum_freq+=f[i]
    
    print("Averge of entered data : ",float(sum/sum_freq))

average_calculator()