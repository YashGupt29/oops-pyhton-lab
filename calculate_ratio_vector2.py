def ratio_calculator(u,v):
    if len(u)!=len(v):
        print("Sizes not equal, ratio cannnot be calculated")
    else:
        w=[]
        for i in range(0,len(u)):
            temp = float(u[i]/v[i])
            w.append(temp)
        print("Ratio vector : ",w)


u,v=[],[]
print("Enter elements of vector u")
while True:
    n=input()
    if n=="":
        break
    u.append(int(n))
        
print("Enter elements of vctor v")
while True:
    n=input()
    if n=="":
        break
    v.append(int(n))

ratio_calculator(u,v)