class BankAccount:
    def __init__(self, forename, surname, starting_balance = 0):
        self._forename = forename
        self._surname = surname
        self._balance = starting_balance
        self._transaction_history = []

    def get_forename(self):
        return self._forename

    def get_surname(self):
        return self._surname

    def get_starting_balance(self):
        return self._balance

    def get_transaction_history(self):
        return self._transaction_history
        
    def set_forename(self, newforename):
        self._forename = newforename.title()

    def set_surname(self, newsurname):
        self._surname = newsurname.title()

    def set_starting_balance(self, newstarting_balance):
        self._balance = newstarting_balance
        
    def add_transaction(self, type, amount, sender=None, recipient=None):
        self._transaction_history.append(Transaction(type, amount, sender, recipient))

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance = round(self._balance - amount, 2)
            self.add_transaction("withdrawal", amount, None, self)
        else:
            print("Insufficient funds in account")
        print("Account Balance:", self._balance)

    def deposit(self, amount):
        self._balance = round(self._balance + amount, 2)
        print("Account Balance:", self._balance, "€")

    def send(self, amount, reciever):
        if amount > 0:
            if self._balance >= amount:
                self._balance = round(self._balance - amount, 2)
                reciever._balance = round(reciever._balance + amount, 2)
                print("Transaction executed, Sent:", amount, "€")
            else:
                print("Insufficient funds in account")
            print("Account Balance:", self._balance, "€")
        else: print("Invalid amount")

    def menu(self):
        print("-" * len(self._forename) + 15 * "-")
        print(f"{self._forename.upper()}'S BANK ACCOUNT")
        print("-" * len(self._forename) + 15 * "-")
        print("Open?")
        open_choice = input()
        if open_choice[0].lower() == "y" :
            self.open_account()
        elif open_choice[0].lower() == "n" :
            print("Goodbye")

    def open_account(self):
        print(
)
        print(self._forename, self._surname)
        print(self._balance, "€")
        print("Transaction History. Open? : 1")
        print("Transactions. Open? : 2")
        menu_choice = int(input())
        if menu_choice == 1:
            pass
        elif menu_choice == 2:
            print("Send. Open? : 1")
            print("Withdraw. Open? : 2")
            print("Deposit. Open? : 3")
            print("Back? : 4")
            transaction_choice = int(input())
            if transaction_choice == 4:
                self.open_account()
            else:
                amount = float(input("Amount: "))
                if transaction_choice == 1:
                    self.send(amount, account_a)
                elif transaction_choice == 2:
                    self.withdraw(amount)
                elif transaction_choice == 3:
                    self.deposit(amount)
                self.open_account()



class Transaction:
    def __init__(self, type, amount, sender=None, recipient=None):
        self.type = type
        self.amount = amount
        self.sender = sender
        self.recipient = recipient

account_a = BankAccount("James", "Renz-Shrimpton", 100)
account_b = BankAccount("Maximilian", "Schnidrig", 10)
account_b.menu()
