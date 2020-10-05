class Company:
    def count_budget(self, budget):
        if budget <= 5000000:
            return '|надо срочно искать инвесторов|'
        elif 5000000 <= budget <= 10000000:
            return '|надо сократить расходы компании|'
        else:
            return '|всё супер )))) |'


    def love_clients(self):
        if self.clients == 'pensioners':
            return 'надо дать скидочку 30%'
        if self.clients == 'students':
            return 'дать скидочку 10% и предложить работу'
        if self.clients == 'worker':
            return 'никакой скидочки вам'

    def __init__(self, name, budget, clients):
        self.name = name
        self.budget = self.count_budget(budget)
        self.clients = clients
        self.strategy = self.love_clients()



branch_number1 = Company('Pion', 2000000, 'students')
branch_number2 = Company('Lilac', 20000000, 'pensioners')
branch_number3 = Company('Tulip', 8000000, 'worker')

print(branch_number1.name, branch_number1.budget, branch_number1.strategy)
print(branch_number2.name, branch_number2.budget, branch_number2.strategy)
print(branch_number3.name, branch_number3.budget, branch_number3.strategy)
