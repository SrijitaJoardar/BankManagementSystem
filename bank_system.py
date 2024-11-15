from bank import Bank

def main():
    bank = Bank()
    while True:
        print("\n --- Banking System -----")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            account_number = input("Enter account number: ")
            holder_name = input("Enter holder name: ")
            initial_balance = float(input("Enter Initial balance: "))
            bank.create_account(account_number, holder_name, initial_balance)

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")    

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")   

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.display_balance()
            else:
                print("Account not found.")   
    
        elif choice == "5":
            bank.display_all_accounts()

        elif choice == "6":
            print("Exiting the System!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
