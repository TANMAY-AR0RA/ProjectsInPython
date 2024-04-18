class Bank:

    def __init__(self,initial_amount=0.00):
       self.balance = initial_amount

    def Transaction_record(self,transaction_comment):
     with open('Bank_Transaction.txt','a') as file:
        file.write(f'{transaction_comment}\t\tCurrent Balance:{self.balance}\n')

    def withdraw(self,amount):
     try:
        amount = float(amount)
     except ValueError:
        amount = 0  

     if amount:
       self.balance-=amount  
       self.Transaction_record(f'Withdrew:{amount}\n')

    def deposit(self,amount):  
     try:
        amount = float(amount)
     except ValueError:
        amount = 0

     if amount:
      self.balance+=amount  
      self.Transaction_record(f'Deposited: {amount}\n')

b = Bank(100)
while True:
    try:
     x = input('Do you want to withdraw or deposit, type it:\t')
     x = x.lower()
    except KeyboardInterrupt:
     print("You are leaving the Bank")
     break

    if x in ['withdraw','deposit']:
        print('Okay, so you want to',x)
        if x == 'withdraw':
            amt = input(f'Enter amount that you want to withdraw:\t')
            b.withdraw(amt)
        else: 
            amt = input(f'Enter amount that you want to deposit:\t')
            b.deposit(amt)

        print('Your effective balance is',b.balance)
    else:
        print('Please, Type correct option')




