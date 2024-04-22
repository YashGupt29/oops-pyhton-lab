def print_name(First_name, Last_name, Reverse):
    if Reverse == "True" or Reverse=="true":
        print(Last_name[::-1],First_name[::-1])
    else:
        print(First_name,Last_name)


a = input("Enter first name : ")
b = input("Enter last name : ")
rev = input("Enter the bool value of reverse : ")
print_name(a,b,rev)
