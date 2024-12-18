class BankAccount:
    bank_name = "Tech4Girls Bank"
    def __init__(self, account_holder):
        """initialize the instance variables."""
        self.account_holder = account_holder
        self.balance = 0
        
    def deposit(self, amount):
            """add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. new balance: {self.balance}")
        else:
            print("deposit amount must be positive.")
    def withdraw(self, amount):
                    """deduct money from the account, ensuring the balance doesn't go negative."""
        if amount > 0 :
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn. new balance: {self.balance}")
        else:
            print("Insufficient funds for this withdrawal.")
        else:
            print("withdrawal must be positive"):
                @staticmethod
    def bank_policy():
                print("welcome to Tech4Girls Bank.we hope to provide you a best service.")
                                    
                @classmethod
    def get_bank_name(cls):
                                        """return the bank name."""
            return cls.bank_name
            if __name__ == "__main__":
            account1 = BankAccount("Nancy")
            account2 = BankAccount("Attu")
                                        
    BankAccount.bank_policy()
            print(f"Bank Name:{BankAccount.get_bank_name()}")
            account1 . deposit(900)
            account1 . deposit(5000)
            account1 . deposit(40)
                                        
            account2 . deposit(1100)
            account2 . withdrawal(650)