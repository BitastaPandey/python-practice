want_to_withdraw=int(input("Please enter the withdraw amount: "))
while want_to_withdraw<=0:
    print("Please provide the correct amount:")
    want_to_withdraw=int(input("Please enter the withdraw amount: "))
else:
    have_in_account=int(input("Please enter your a/c balance: "))
    while have_in_account<0 or have_in_account==0 or have_in_account<=1 or have_in_account<=want_to_withdraw :
        have_in_account=int(input("Please enter your a/c balance: "))
    
    else:
        transaction_value=1
        n=want_to_withdraw%5
        if n==0:
           i=(have_in_account-want_to_withdraw)-transaction_value
           print(i)
        elif n!=0:
            print(have_in_account)
        