from datetime import datetime
name = input("What is your name? \n")
allowedUsers = ["Seyi", "Mike", "Love"]
allowedPassword = ["passwordSeyi", "passwordMike", "passwordLove"]
balance = 0
now = datetime.now()
dateData = now.strftime("%B %d, %Y. %H:%M:%S")
if (name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if (password == allowedPassword[userId]):
        print("Welcome %s \n%s" % (name,dateData))
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
    
        selectedOption = int(input("Please select an option: "))

        if (selectedOption ==  1):
            input("How much would you like to withdraw? ")
            print("Take your cash")
        
        elif(selectedOption == 2):
            deposit = input("How much would you like to deposit? ")
            currentBalance = int(deposit) + balance
            print("Current Balance is: %d only" %currentBalance)

        elif(selectedOption == 3):
            input("What issue would you like to report? ")
            print("Thank you for contacting us")
        
        else:
            print("Invalid Option Selected, please try again")

else:
    print("Name not found, please try again")