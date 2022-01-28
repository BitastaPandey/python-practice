
# from typing import Counter


# def digit_count(number):
#     list=[]
#     for i in range(10):
#         if i in number:
#             n1=Counter(number)
#             n=n1[i]
#             return n
#         list=list.append(n)
#     return list
               
# def main():

#     a=int(input("Please provide the first positive no: "))
#     b=int(input("Please provide the second positive no: "))
#     c=int(input("Please provide the third positive no: "))
#     if a>0:
#         if b>0:
#             if c>0:
#                 product=a*b*c
#                 print(product)
#                 number=product
#                 print(digit_count(number))

#             else:
#                 print("Please provide a positive no.")
#         else:
#             print("Please provide a positive no.")

#     else:
#         print("Please provide a positive no.")

# main()
        # 0...count of 0
        # 1..count of 1


digitCount=[0,0,0,0,0,0,0,0,0,0]
a=int(input("Please provide the first positive no: "))
while a<0 or a>1000:
    print("Please provide proper input ")
    a=int(input("Please provide the first positive no: "))
    
b=int(input("Please provide the second positive no: "))
while b<0 or b>1000:
    print("Please provide proper input ")
    b=int(input("Please provide the first positive no: "))

c=int(input("Please provide the third positive no: "))
while c<0 or c>1000:
    print("Please provide proper input ")
    c=int(input("Please provide the first positive no: "))
    

product=a*b*c
print(product)
product = str(product)
for digit in product:
    digit = int(digit)
    print(digit)
    digitCount[digit] = digitCount[digit] + 1

print(digitCount)


      




