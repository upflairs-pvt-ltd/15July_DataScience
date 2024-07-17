name = input("Plz enter your name : ")     # scanf , cin ,  scanner 
print("Hello ",name)
message = """
How may i help you sir .

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL.
"""
print(message)
# int(),str(),float(),list(),set(),tuple(),dict()
task = int(input('Plz choose any option : '))   # by default str --->  int 
available_amount = 5000 

if task >=1 and task <= 3:  # 1 to 3 
    print('welcome to you in virtual bank')

    if task == 1:   
        # check balance 
        print('Thanks for visiting us, your available amount is : ',available_amount)
        
    elif task == 2:
        # deposit amount
        deposit_amount = int(input("Plz enter your deposit amount : ")) 
        if deposit_amount >= 500:  
            # deposit_task 
            available_amount = available_amount + deposit_amount
            # available_amount += deposit_amount 
            print('You have successfully deposit your amount : ',deposit_amount)
            print('Thanks for visiting us, your available amount is : ',available_amount)
        else:
            print("plz deposit at least 500 Rupees! ")

    else:  # 3 
        pass 
else: 
    print('Plz choose correct option!')







