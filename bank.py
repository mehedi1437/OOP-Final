import uuid
from datetime import datetime

class User:
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = uuid.uuid4() 
        self.min_withdraw = 100
        self.max_withdraw = 100000
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_amount = 0
    
    def available_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.now() , "Deposit", amount))
    
    def withdraw(self,amount):
        if self.balance < amount :
            print("Withdrawal amount exceeded")
        elif amount < self.min_withdraw :
            print("Minimun withdrawl amount limit is 100 ")
        elif amount > self.max_withdraw :
            print("Maximum withdrawl amount limit is 100000")
        else:
            self.balance -= amount
            print(f"Here is your money {amount}")
            print(f"Your balance after withdrawl {self.balance} ")
            self.transaction_history.append((datetime.now() , "Withdeawl", amount))

    def transfer(self,reciver_name,amount):
        reciver = (user for user in admin.users if user.name == reciver_name)
        if reciver:
            if self.balance >= amount :
                self.balance -= amount
                reciver.balance += amount
                self.transaction_history.append((datetime.now(),"Teansfer",amount,reciver.name))
            else:
                print("Insufficiant balance to transfer !")
        else:
            print("Account does not exist")


    def take_loan(self,amount):
        if self.loan_taken <2 :
            self.loan_taken += 1
            self.balance += amount
            self.loan_amount += amount 
            self.transaction_history.append((datetime.now(),"Take Loan",amount))
            print(f"Loan of {amount} taken successfully")
        else:
            print("You have already taken the maximum number of loans")
    
    def check_loan(self):
        return self.loan_amount
    
    def pay_loan(self,amount):
        if amount > self.balance:
            print("Insufficiant balance to pay the loan")
        else:
            self.balance -= amount
            self.loan_amount -= amount
            self.transaction_history.append((datetime.now(),"Pay Loan",amount))
            print("Loan paid successfully")

class Admin:
    def __init__(self,name) :
        self.name = name
        self.users = []

    def creat_account(self,name,email,address,acount_type):
        user = User(name,email,address,acount_type)
        self.users.append(user)
        return user 
    
    def delete_account(self,user_name):
        for user in self.users:
            if user.name == user_name:
                self.users.remove(user)
                print(f"User name : {user.name} has been deleted")
                return
        print("User account not found")
    
    def is_bankrupt(self,status):
        if status:
            print("Bank is bankrupt")
        else:
            print("Bank is not bankrupt")
        
    def total_loan_amount(self):
        return sum(sum(transaction[2] for transaction in user.transaction_history if transaction[1] == "Take Loan") for user in self.users)

    def loan_status(self,status):
        if status:
            print("Loan feature is enable")
        else:
            print("Loan feature is disable")



user = User("Korim",'korim23@gmail.com',"Dhaka","Type1")
admin = Admin("Rohim")

def user_menu():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    address = input("Enter your address: ")
    account_type = input("Enter your Acount type : ")
    user = User(name=name,email=email,address=address,account_type=account_type)
    
    while True:
        print(f"Welcome {user.name} !")
        print("1. Check balance")
        print("2. Diposit")
        print("3. Withdrawl")
        print("4. Transfer Money")
        print("5. Take loan")
        print("6. Repay loan")
        print("7. Check loan amount")
        print("8. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            return print(f"Your balance is : {user.available_balance()} ")
        elif choice == 2:
            amount = int(input("Enter your amount :"))
            return user.deposit(amount)
        elif choice == 3:
            amount = int(input("Enter your amount :"))
            return user.withdraw(amount)
        elif choice == 4:
            ricever_name = input("Enter ricever name :")
            ricever = (u for u in admin.users if u.name == ricever_name) 
            if ricever:
                amount = int(input("Enter your amount :"))
                return user.transfer(ricever,amount)
            else:
                print("Ricever not found !!")
        elif choice == 5:
            amount = int(input("Enter your amount :"))
            return user.take_loan(amount)
        elif choice == 6:
            amount = int(input("Enter your amount :"))
            return user.pay_loan(amount)
        elif choice == 7:
            return print(f"Your current loan is : {user.check_loan()}")
        elif choice == 8:
            break
        else:
            print("Invalid input !!")




def admin_menu():
    
    while True:
        print(f"Welcome Admin !")
        print("1. Creat account")
        print("2. Delete user account")
        print("3. Total available balance")
        print("4. Total loan amount")
        print("5. Loan features status")
        print("6. Controle bankrupt")
        print("7. All users")
        print("8. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            address = input("Enter your address: ")
            account_type = input("Enter your Acount type : ")
            new_user = admin.creat_account(name,email,address,account_type)
            print(f"Account created for {new_user.name} with accpunt number {new_user.account_number}")
        elif choice == 2:
            user_name = input("Enter user name : ")
            user = (u for u in admin.users if u.name == user_name) 
            if user:
                return admin.delete_account(user_name)
            else:
                print("User not found !!")
        elif choice == 3:
            total = sum(user.balance for user in admin.users)
            print(f"Total available balance : {total}")
        elif choice == 4:
            print(f"Total loan amount : {admin.total_loan_amount()}")
        elif choice == 5:
            status = bool(input("Enter the status (True/False): "))
            admin.loan_status(status)
        elif choice == 6:
            status = bool(input("Enter the status: "))
            admin.is_bankrupt(status)
        elif choice == 7:
            print("All user accounts list : ")
            for user in admin.users:
                print("Name:", user.name)
                print("Email:", user.email)
                print("Address:", user.address)
                print("Account Type:", user.account_type)
                print()
        elif choice == 8:
            break
        else:
            print("Invalid input !!")


while True:
    print("Welcome to our bank !")
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input")

        


    
            
            
    
            

    
        
