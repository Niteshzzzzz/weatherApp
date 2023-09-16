from tkinter import *
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            l4.config(text=f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            l4.config(text="Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            l5.config(text=f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            l5.config(text="Invalid withdrawal amount. Please enter a positive number.")
        else:
            l5.config(text="Insufficient funds.")

    def check_balance(self):
        l5.config(text=f"Account balance for {self.account_holder}: ${self.balance}")

def register_account():
    account_number = t1.get()
    username = t2.get()
    initial_balance = float(t3.get())
    # Create a new bank account for the user and store it in a dictionary with the account number as the key.
    accounts[account_number] = BankAccount(account_number, username, initial_balance)
    l4.config(text=f"Account for {username} registered with an initial balance of ${initial_balance}.")

def view_balance():
    # Retrieve the account for the current account number and display their balance.
    account_number = t1.get()
    account = accounts.get(account_number)
    if account:
        account.check_balance()
    else:
        l5.config(text="Account not found.")

def deposit_money():
    account_number = t1.get()
    account = accounts.get(account_number)
    if account:
        amount = float(t3.get())  # Use t3 for the deposit amount
        account.deposit(amount)
    else:
        l4.config(text="Account not found.")

def withdraw_money():
    account_number = t1.get()
    account = accounts.get(account_number)
    if account:
        amount = float(t3.get())  # Use t3 for the withdrawal amount
        account.withdraw(amount)
    else:
        l4.config(text="Account not found.")

root =Tk()
root.title("Simple Bank System")
root.geometry('500x500')

accounts = {}  # Dictionary to store user accounts

l1 = Label(root, text="Account Number")
l2 = Label(root, text="User Name")
l3 = Label(root, text="Amount")

t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

b1 = Button(root, text="Registration", command=register_account)
b2 = Button(root, text="View Balance", command=view_balance)
b3 = Button(root, text="Deposit", command=deposit_money)
b4 = Button(root, text="Withdraw", command=withdraw_money)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)

t1.grid(row=0, column=1)
t2.grid(row=1, column=1)
t3.grid(row=2, column=1)

b1.grid(row=3, column=1)
b2.grid(row=4, column=1)
b3.grid(row=5, column=1)
b4.grid(row=6, column=1)

l4 = Label(root, text="", fg="green")
l4.grid(row=7, column=1)

l5 = Label(root, text="", fg="blue")
l5.grid(row=8, column=1)

root.mainloop()
