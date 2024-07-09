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
if task == 1 :
    print("your balance is 5000")
    print("thank you for visiting!")
elif task == 2 :
    deposite_amount = int(input("please enter deposite amount : "))
    print("your deposite amount is : ",deposite_amount)
    total_amount = deposite_amount + 5000
    print("your total amount is : ",total_amount)
    print("thank you for visiting!")
elif task == 3 :
    withdraw_amount = int(input("please enter withdraw amount : "))
    if withdraw_amount > 5000 : 
        print("Sorry, you can't withdraw more than 5000")
        print("thank you for visiting!")
    else :
        print("your withdraw amount is : ",withdraw_amount)
        remaining_amount = 5000 - withdraw_amount
        print("Now, your remaining amount is : ",remaining_amount)
        print("thank you for visiting!")
else :
    print("Sorry, you are not select valid task")
    print("thank you for visiting!")        