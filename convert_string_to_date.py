def string_to_date(s:str):
    months = {"January":"01", "February":"02","March":"03","April":"04"
              ,"May":"05","June":"06","July":"07","August":"08",
              "September":"09","October":"10","November":"11","December":"12"}
    d:str = (s[0:2])
    if d[1]=='-':
        d = '0'+d[0]
    date = s.split()
    m:str = months[date[1]]

    return d+"/"+m+"/"+date[2]


date = input("Enter a date in words : ")
print("Date in dd/mm/yyyy format : ",string_to_date(date))
