class Budget:
    def __init__(self, budget):
        self.balance = 0
        self.budget = budget
        print(f'You created a {budget} object ')

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        try:
            print(f'Your deposit of {int(self.amount)} was Successful!')
        except ValueError:
            print('Please enter a number')

    def withdraw(self, amount_withdrawal):
        self.amount_withdrawal = amount_withdrawal
        if self.amount_withdrawal < self.amount:
            self.balance = (self.amount - self.amount_withdrawal)
            print(f'You have successfully withdrawn N{self.amount_withdrawal}')
        else:

            print('Insufficient Balance, You cant withdraw that amount')

    def category_balance(self):
        print(self.balance)

    def transfer_balance(self, category):
        try:
            if self.balance > 0:
                category.balance +=  self.balance
                print(f'You have successfully transferred { self.balance} to {category.__str__()}')
            else:
                print('You have no balance')
        except ValueError:
            print('Please enter a number')


obj1 = Budget('Food')
obj2 = Budget('Cloth')
obj3 = Budget('Entertainment')

obj2.deposit(4000)
obj2.transfer_balance(obj1)
obj1.deposit(5000)
obj3.category_balance()
obj1.transfer_balance(obj3)
obj3.category_balance()