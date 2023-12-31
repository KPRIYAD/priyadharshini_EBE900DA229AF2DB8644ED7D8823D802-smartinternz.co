class bankaccount:

  def __init__(self, acc_num, acc_name, balance):
    self.__acc_number = acc_num
    self.__acc_holder_name = acc_name
    self.__acc_balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.__acc_balance += amount
      return (self.__acc_balance)

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__acc_balance:
      self.__acc_balance -= amount
      return (self.__acc_balance)

  def display_balance(self):
    return (self.__acc_balance)


account = bankaccount(1001, "priya", 1000)
print(account.display_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.display_balance())
