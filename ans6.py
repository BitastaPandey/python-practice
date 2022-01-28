import math
hour=int(input("Please enter the time in hour: "))
while hour>23 or hour<0:
    print("Please provide correct time.")
    hour=int(input("Please enter the time in hour: "))
else:
    minute= int(input("Please enter the time in minute: "))
    while minute<0 or minute > 59:
      print("Please provide correct time in minute.")
      minute= int(input("Please enter the time in minute: "))
    else:
        if hour>0:
            minutes=hour*60+minute
            alarm=minutes-35
            alarm_hour=math.floor(alarm/60)
            alarm_minute=alarm%60
            print(alarm_hour,alarm_minute)
        elif hour==0:
            minutes=24*60+minute
            alarm=minutes-35
            alarm_hour=math.floor(alarm/60)
            alarm_minute=alarm%60
            print(alarm_hour,alarm_minute)
