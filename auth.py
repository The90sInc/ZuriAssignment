from random import randint
from datetime import datetime #import date from date time library

now = datetime.now()
timeData = now.strftime("%B %d, %Y. %H:%M:%S") #format of date month day, year. TIME - hour:minute:second
database = {
    1286556106 : ["Emmanuel", "Oladele", "niyotokunlola@zuri.com", "password", 0] #data base for users
}

def init():
    
    print("Welcome to the bank of Spain \n%s" % timeData)
    
    haveAccount = int(input("Do you have an account with us? Press 1 (YES) and 2 (NO):\n"))
       
    # if statement confirm if user is in data base, and if not registering user
    if (haveAccount == 1):
        login()
    elif (haveAccount == 2):
        print(register())
    else:
        print("You have selected an invalid option")
        init()

#func. for logining 
def login():

    print("Kindly Login to your account")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
    
    login()

#creating a function to register new user into data base
def register():
    print ("***** Kindly fill in the details below to register. *****")

    email = input("What is your email address?\n")
    first_name =  input("What is your first name?\n")
    last_name =  input("What is your last name?\n")
    password = input("Create a password for yourself?\n")
    balance = 0

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password, balance]

    print("Your account has been created")
    print(f"== ==== ===== ====== \nYour account number is: {accountNumber} \nMake sure to keep it safe \n== ==== ===== ======"  )

    login()

#different operations registered user can performed 
def bankOperation(user):

    print("Welcome %s %s" % (user[0], user[1]))
 
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Complaints (5) Check account balance (6) Exit \n"))

    if (selectedOption == 1):
        depositOperation(user)
    elif (selectedOption == 2):
        withdrawalOperation(user)
    elif (selectedOption == 3):
        logOut()
    elif (selectedOption == 4):
        complaintsOperation(user)
    elif (selectedOption == 5):
        checkBalance(user)   
    elif (selectedOption == 6):
        exit()
    else:
        print("Invalid option selected, TRY AGAIN.")
        bankOperation(user)

#creating a withdrawal function
def  withdrawalOperation(user):
    print("Current Balance as at  %s is: %s naira" %(timeData, user[-1]))
    amount_to_withdraw = int(input("How much would you like to withdrawl? \n"))
    if amount_to_withdraw > user[-1]:
        deposit = int(input("You have insufficient funds. Would you like to make a deposit or withdraw a lesser amount? (1) Yes or (2) No, I would withdraw a lesser amount. \n"))
        if deposit == 1:
            depositOperation(user)
            another_operation(user)
        elif deposit == 2:
            withdraw_different_amount = int(input("Would you like to withdraw a different amount or log out? (1) Yes or (2) No \n"))
            if withdraw_different_amount == 1:
                withdrawalOperation(user)
            else: 
                logOut()
    else:
        user[-1] -= amount_to_withdraw
        print("Take Cash. \nNew account balance is: %s" % user[-1])
        another_operation(user)

#creating a deposit function
def depositOperation(user):
    amount_deposited = int(input("How much would you like to  deposit? \n"))
    user[-1] += amount_deposited
    print("New account balance as at %s is: %s naira" % (timeData, user[-1]))
    another_operation(user)

#creating a complaints function
def complaintsOperation(user):
    input("Kindly input your complaints here.\n")
    print("Thanks for the feedback %s %s, we would get back to you in the next 24 hours. Till then STAY JIGGY." %(user[0], user[1]))
    another_operation(user)

#creating a function to check balance
def checkBalance(user):
    print("Your balance as at %s is: %s naira" %(timeData, user[-1]))
    another_operation(user)

#creatinig a log out func.
def logOut():
    print("********* Logging Out... ********* \n********* LOGGED OUT *********")
    exit()
    login()

#creating a loop function
def another_operation(user):
    option = int(input("Would you like to perform another operation? (1) Yes or (2) No\n"))
    if option == 1:
        bankOperation(user)
    elif option == 2:
        logOut()
    else:
        print("Invalid option, read carefully before selecting.")
        another_operation(user)


#function to generate specific account numbers for registered users in a data base
def generateAccountNumber():
    print("Generating Account Number")
    n = 10
    rangeStart = 10**(n-1)
    rangeEnd = (10**n) - 1
    return randint(rangeStart, rangeEnd)

init()
