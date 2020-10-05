class Male:
    def __init__(self, name, age, job, money, weight, height):
        self.name = name
        self.age = age
        self.job = job
        self.money = money
        self.weight = weight
        self.height = height


class Female:
    def __init__(self, name, age, job, money, weight, height):
        self.name = name
        self.age = age
        self.job = job
        self.money = money
        self.weight = weight
        self.height = height

    def get_money(self, Male):
        self.money += Male.money
        Male.money = 0


Adward = Male('Adward', 38, 'professor', 1000000, 95, 180)

Amy = Female('Amy', 29, 'florist', 70000, 55, 169)
Amy.get_money(Adward)

print(Amy.money)
print(Adward.money)

