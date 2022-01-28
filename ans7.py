speed=80
speed_user=int(input("Please tell your speed: "))
while speed_user <=0:
    print("Please provide your correct speed.")
    speed_user=int(input("Please tell your speed: "))
else:
    my_birthday=input("If today is your birthday then say 'True' otherwise say 'False': ")
    if my_birthday=="True":
        if speed_user<=85:
            print("0")
        elif speed_user>85 and speed_user<=105:
            print("1")
        elif speed_user>105:
            print("2")
    elif my_birthday=="False":
        if speed_user<=80:
            print("0")
        elif speed_user>80 and speed_user<=100:
            print("1")
        elif speed_user>100:
            print("2")
    else:
        print("Please type 'True' or 'False': ")

