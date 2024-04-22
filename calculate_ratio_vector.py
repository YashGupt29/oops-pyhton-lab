def ratio_calculator(u,v):
    try:
        w=[]
        for i in range(0,max(len(u),len(v))):
            temp = float(u[i]/v[i])
            w.append(temp)
        print("Ratio vector : ",w)

    except IndexError:
        print("Sizes of u and v not equal")

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
