#Create a Bank account with members account number, name, type of account and balance.
#Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
class bankAccount:
    def __init__(self,name,accountNo,Accounttype,balance):
        self.name = name
        self.accountNo = accountNo
        self.Accounttype = Accounttype
        self.balance = balance
    def deposit(self,a):
        self.balance = self.balance + a
        return self.balance
    def withdraw(self,b):
        self.balance = self.balance - b
        return self.balance
abhi = bankAccount("rony",123456,"AC",15000)  
print(abhi.deposit(1000))
print(abhi.withdraw(500))

