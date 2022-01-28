number=input("Please provide a positive number: ")
while int(number)<=0:
    print("Please provide a positive number.")
    number=input("Please provide a positive number: ")
else:
    number = ''.join(sorted(number,reverse=True))
    number1 = int(number)
    print(number1)

