days=["SUN","MON","TUE","WED","THURS","FRI","SAT"]
def find_day(day):
    if day>6:
       i=day%7
       return(days[i])
    elif day<=6:
        i=day
        return(days[i])


def has_numbers(inputString):
    return inputString.isnumeric()

month1=input("Please provide month's no: ")
validMonth = has_numbers(month1)
# if validMonth==False:
#     print("Invalid month")
while (validMonth==False):
      month1=input("Please provide month's no: ")
      validMonth = has_numbers(month1)
    
else:
    month=int(month1)
    while month<1 or month>12:
       month=int(input("Please provide proper month's no."))
    else:
       date1=input("Please provide what is the number of the day: ")
       if has_numbers(date1)==False:
           print("Please provide the month in no.")
       else:
           date=int(date1)
           if date>31 or date<=0:
              print("Please provide a valid date.")
           elif month==1:
              i=date
              print(find_day(i))
           elif month==2:
               if date>29:
                  print("Please provide proper date")
               else:
                  i=31+date
                  print(find_day(i))
           elif month==3:
               i=31+29+date
               print(find_day(i))
           elif month==4:
               if date>30:
                 print("Please provide a proper date")
               else:
                 i=31+29+31+date
                 print(find_day(i))
           elif month==5:
              i=31+29+31+30+date
              print(find_day(i))
           elif month==6:
              if date>30:
                print("Please provide a proper date")
              else:
                i=152+date
                print(find_day(i))
           elif month==7:
              i=182+date
              print(find_day(i))
           elif month==8:
              i=213+date
              print (find_day(i))
           elif month==9:
              if date>30:
                print("Please provide a proper date")
              else:
                i=244+date
                print (find_day(i))
           elif month==10:
               i=274+date
               print(find_day(i))
           elif month==11:
               if date>30:
                  print("Please provide a proper date")
               else:
                  i=305+date
                  print(find_day(i))
           else:
              i=335+date
              print(find_day(i))

        



