name = input("plz enter your name : ")
print(f"hello",name)

message = """
how may i help you sir,

please select any of them option,
type 1 >>> CHECK BALANCE,
type 2 >>> DEPOSITE,
type 3 >>> WITHDRAW
"""

print(message)
task = int(input("please select your optin : "))
avialable_amount = 5000

if task >=1 and task <=3 :
    print("welcome to you in virtual bank")
    if task == 1 :
        # check balance program
        print("your available amount is :",avialable_amount,'INR')
    elif task == 2 :
        # deposite program
        deposite_amount = int(input("please enter your deposite amount : "))
        if deposite_amount > 0 :
            avialable_amount += deposite_amount
            print("you have successfully deposite your amount : ",deposite_amount,'INR')
            print("your avialable amount is : ",avialable_amount,'INR')
        else :
            print("plz enter valid amount")    
    else :
        # withdraw program
        withdraw_amount = int(input("please enter your withdraw amount : ",))
        if withdraw_amount > 0 and withdraw_amount <= avialable_amount :
            avialable_amount -= withdraw_amount
            print("you have successfully withdraw your amount : ",withdraw_amount,'INR')
            print("your avialable amount is : ",avialable_amount,'INR')
        else :
                print("you don't have sufficient amount!")
                print("your avialable amount is : ",avialable_amount,'INR')
else :
    print("plz choose valid option in between 1 to 3 :")
print("Thank you for visiting!")    
    
