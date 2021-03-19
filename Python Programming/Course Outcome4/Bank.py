class bankAccount:
    def __init__(self):
        self.balance=0
        self.accountnumber=int(input("Enter your Account number : "))
        self.name=input("Enter your name : ")
        self.accounttype=input("Enter your Account type : ")
    def display(self):
        print("Name : ",self.name)
        print("Account number : ",self.accountnumber)
        print("Account type : ",self.accounttype)
    def deposit(self):
        amount=int(input("Enter the amount to be deposited:"))
        self.balance+=amount
        print("your account balance is:",self.balance)
    def withdraw(self):
        amount=int(input("Enter the amount to be withdrawn:"))
        if(amount>self.balance):
            print("INSUFFICIENT BALANCE")
        else:
            self.balance-=amount
            print("your account balance is : ",self.balance)
account=bankAccount()
account.display()
account.deposit()
account.withdraw()


