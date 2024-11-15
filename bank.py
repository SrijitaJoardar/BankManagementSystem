from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists!")
        else:
            self.accounts[account_number] = Account(account_number, holder_name, initial_balance)
            print(f"Account created for {holder_name} with account number {account_number}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for account in self.accounts.values():
                account.display_balance()
                print("-" * 20)
