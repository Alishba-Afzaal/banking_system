class BankAccount:
    def __init__(self, account_number, pincode, balance=0):
        self.account_number = account_number
        self.pincode = pincode
        self.balance = balance



    def check_balance(self):
        print(f"Current balance: ${self.balance}")



    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.check_balance()
        else:
            print("Invalid deposit amount.")



    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.check_balance()
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawn amount.")





class ATM_CDM_System:
    def __init__(self):
        self.accounts = {}



    def create_account(self, account_number, pincode, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, pincode, initial_balance)
            print("Account Created Successfully.")
    



    def authenticates(self, account_number, pincode):
        account = self.accounts.get(account_number)
        if account and account.pincode == pincode:
            print("Authentication successful.")
            return account
        else:
            print("Invalid account number or PIN.")
            return None




    def atm_menu(self, account):
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Withdraw Cash")
            print("3. Exit")


            choice = input("Select an option: ")
            if choice == '1':
                account.check_balance()
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid option. Please try again.")


        



    def cdm_menu(self, account):
        while True:
            print("\n--- CDM MENU ---")
            print("1. Check Balance")
            print("2. Deposit Cash")
            print("3. Exit")


            choice = input("Select an option: ")
            if choice == '1':
                account.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '3':
                print("Thank you for using the CDM.")
                break
            else:
                print("Invalid option. Please try again.")




def main():
    system = ATM_CDM_System()


    while True:
        print("\n--- WELCOME TO THE ATM/CDM SYSTEM ---")
        print("1. Create Account")
        print("2. ATM (Withdraw Cash)")
        print("3. CDM (Deposit Cash)")
        print("4. Exit")

        choice = input("Select an option: ")


        if choice == '1':
            account_number = input("Enter account number: ")
            pincode = input("Enter PINCODE: ")
            initial_balance = float(input("Enter initial balance (or 0 for none): "))
            system.create_account(account_number, pincode, initial_balance)


        elif choice == '2':
            account_number = input("Enter account number: ")
            pin = input("Enter PINCODE: ")
            account = system.authenticates(account_number, pincode)
            if account:
                system.atm_menu(account)


        elif choice == '3':
            account_number = input("Enter account number: ")
            pin = input("Enter PINCODE: ")
            account = system.authenticates(account_number, pincode)
            if account:
                system.cdm_menu(account)
        elif choice == '4':
            print("Thank you for using our service.")
            break

        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()


