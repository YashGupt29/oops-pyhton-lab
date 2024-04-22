def date_to_string(s):
    suffix = {"0":"-th","1":"-st","2":"-nd","3":"-rd","4":"-th","5":"-th",
              "6":"-th","7":"-th","8":"-th","9":"-th"}
    month={"01":"January","02":"February","03":"March","04":"April","05":"May",
           "06":"June","07":"July","08":"August","09":"September",
           "10":"October","11":"November","12":"December"}
    date = s.split('/')
    ans = date[0]
    temp = int(date[0])
    if temp >=11 and temp<14:
        ans+="-th"
    else:
        ans+=suffix[date[0][1]]

    return ans+' '+month[date[1]]+' '+date[2]

date = input("Enter a date in dd/mm/yyyy format : ")
print("Date in words : ",date_to_string(date))
