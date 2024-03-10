#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BankAccount:
    # creating a class for bank account operation
    def __init__(self, name, accountType, accountNumber, balance = 0):
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.name = name
        self.filename = str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"

        print(type(self.filename))
        self.balance = balance
        
     #function for depositing money               
    def deposit(self, amount):
        self.balance += amount
        file = open(self.filename, 'a')
        file.write(f"deposit ${amount}")
        file.close()
        print (f"${amount} has been deposited to your account, and your new balance is ${self.balance}")
    
    #function for withdrawing money   
    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient balance. Please try a different amount")
        else:
            self.balance -= amount
            file = open(self.filename, 'a')
            file.write(f"Withdraw ${amount}")
            file.close()
            print (f"${amount} has been withdrawn from your account, and your new balance is ${self.balance}")
            
       #function for checking account balance     
    def checkbalance(self):
        print(f"Your current balance is ${self.balance}.")
      
    #function for getting account type  
    def getAccountType(self):
        print("AccountType:", self.accountType)
    
    #function for getting account number
    def getAccountNumber(self):
        print("AccountNumber", {self.accountNumber})
     
    #function for getting account holder's name
    def getHolderName(self):
        print("AccountHolder's name", self.name)
      
    #function for getting transaction history
    def getTransactionsHistory(self):
        file = open(self.filename, "r")
        transaction_history = file.readlines()
        print("TransactionHistory:", transaction_history)
        file.close
        
        
   #dummy accounts created     
        
        
account1117 = BankAccount("JohnSmith", "Chequing", 1117)
account1118 = BankAccount("JillSmith", "Savings", 1118)
account1119 = BankAccount("JaneSmith","TFSA", 1119)
account1120 = BankAccount("Amanda","Savings",1120)


    



print("\n*****Neel's  Financial Bank *******")
print("1: Deposit")
print("2: Withdraw")
print("3: CheckBalance")

account1120.deposit(100000)
account1120.withdraw(20)
account1120.getAccountType()
account1120.getHolderName()
account1120.getTransactionsHistory()





# In[ ]:





# In[ ]:





# In[ ]:




