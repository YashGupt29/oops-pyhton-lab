def extract_numbers(s):
    numbers=[]
    number=''
    for char in s:
        if (char.isdigit()==True):
            number+=char
        elif(number!=''):
            numbers.append(int(number))
            number=''

    if(number!=''):
        numbers.append(int(number))

    return numbers

str = input("Enter a string : ")
answer = extract_numbers(str)
print("Numbers in string : ", answer)

