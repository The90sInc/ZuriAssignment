#create class budget
#different budget categories
#create functions : 1. deposit funds to each category 2. withdraw funds fromm each category 3. compute category balance 4. transfer balance amounts btw categories

class Budget:
    budget_balance = [0,0,0]
    budget_category = ["Food", "Accomodation", "Utility bills" ]

    def __init__(self, category):
        self.category = category - 1
        

    def budget_operation(self):
        selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Compute category balance (4) Transfer balance amount \n"))
        if selectedOption == 1:
            depositFunds()
        elif selectedOption == 2:
            withdrawFunds()
        elif selectedOption == 3:
            compute_balance()
        elif selectedOption == 4:
            transferFunds()
        else: 
            print("invalid input")

        def depositFunds(self):
            print("Your current %s is %s naira" %(self.budget[self.category], self.budget_balance[self.category]))
            amount = int(input("How much would you like to deposit? \n"))
            self.budget_balance[self.category] += amount
            print("Your current %s is %s naira" %(self.budget[self.category], self.budget_balance[self.category]))
               

        def withdrawFunds(self):
            print("Your current %s is %s naira" %(self.budget[self.category], self.budget_balance[self.category]))
            amount = int(input("How much would you like to withdraw? \n"))
            if amount > self.budget_balance[self.category]:
                another_option = input("You have insufficient funds. Would you like to withdraw a lower amount? (Y) Yes or (N) No.")
                if another_option == "Y":
                    withdrawFunds(self)
                else:
                    print("Your transaction is being processed...")
                    self.budget_balance[self.category] -= amount
                    print("Your transaction has been completed.")
        
        def compute_balance(self):
            print("Processing Transaction......")
            print("You have %s in your %s budget" %(self.budget_balance[self.category], self.budget[self.category]))
            print("Transaction completed")

        def transferFunds(self):
            print("Your current %s is %s naira" %(self.budget[self.category], self.budget_balance[self.category]))
            amount = int(input("How much would you like to transfer?"))
            budget_account = int(input("Where would you like to transfer funds to? \n1. Food 2. Accomodation 3. Utility bills")
            #if budget_account == self.budget[self.category]:

            if budget_account == self.budget[self.category]:
                print("Can only make transfer of funds to different budgets")
            
            elif budget_account != self.budget[self.category] and amount <= self.budget_balance[self.category]:
                print("Transfer processing...")
                self.budget_balance[Budget_account] -= amount
                self.budget_balance[]  

