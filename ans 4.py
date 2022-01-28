a1=int(input("Please enter 1st no: "))
a=abs(a1)
b1=int(input("Please enter 2nd no: "))
b=abs(b1)
c1=int(input("Please enter 3rd no: "))
c=abs(c1)
if a>b and a>c :
    print(a1)
if b>a and b>c:
    print (b1)
if c>a and c>b:
    print(c1)
if a==b and b==c:
    print(a1,b1,c1)
