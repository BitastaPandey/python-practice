num1,num2,num3=input("Please enter 3 integers:").split()
def check_input(num):
    while num>6 or num <1:
        # try:
              num = int(input('Enter a number: '))
              return num
    else:
        return num
    
        # except ValueError:
            # print('Invalid Input. Try again.')


n1=int(num1)
n2=int(num2)
n3=int(num3)

n1=check_input(n1)
n2=check_input(n2)
n3=check_input(n3)
print(n1,n2,n3)
if n1==n2 and n2==n3:
    get_prize=100+n1*10
    print(get_prize)
elif n1==n2 or n1==n3 :
    get_prize=10+n1*1
    print(get_prize)
elif n2==n1 or n2==n3:
    get_prize=10+n2*1
    print(get_prize)
elif n1!=n2 and n2!=n3 and n3!=n1:
    if n1>n2 and n1>n3:
        get_prize=n1*1
        print(get_prize)
    elif n2>n1 and n2>n3:
        get_prize=n2*1
        print(get_prize)
    elif n3>n1 and n3>n2:
        get_prize=n3*1
        print(get_prize)
