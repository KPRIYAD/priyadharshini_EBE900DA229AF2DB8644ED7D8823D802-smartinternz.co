class bankaccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposite(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited {}. New balance:{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposite amount.please deposite a positive amount.:")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw {}. New balance:{}".format(amount,self.__account_balance))
    else:
      print("Invalid withdrawl amount or insufficient balance")
  def display_balance(self):
    print("Account balance for {} (Account #{}:{}".format(
        self.__account_holder_name, self.__account_number,self.__account_balance))
account=bankaccount(1001,"Hariprabhu",1000)
print(account.display_balance())
print(account.deposite(500))
print(account.withdraw(200))
print(account.display_balance())