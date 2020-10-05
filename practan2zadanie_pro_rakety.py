class SpaceShip:
    def __init__(self):
        self.hp = 100
        self.speed = 13000
        self.crew = 64
        self.power_reserve = 56000

    def __str__(self):
        return f'Spaceship: {self.hp}; {self.speed}; {self.crew}; {self.power_reserve}'

    def draw(self):
        print('+-|--------|-+')
        print('+     пп     +')
        print('+     пп     +')
        print('+--п------п--+')

class StarDestroyer(SpaceShip):
    def __init__(self):
        super().__init__()
        self.shields = 100
        self.shields_enabled = False
        self.weapons = [100]*15

    def __str__(self):
        return f'StarDestroyer: {self.shields}; {self.shields_enabled}; {self.weapons}'

    def shields_on(self):
        self.shields_enabled = True

    def shields_off(self):
        self.shields_enabled = False

    def hit(self):
        if self.shields_enabled:
            self.shields -= 10
        else:
            self.hp -= 10

    def draw(self):
        print("       /\       ")
        print("      /  \      ")
        print("     /    \     ")
        print("    / |  | \    ")
        print("   /        \   ")
        print("  /   /::\   \  ")
        print(" /   +-----+  \ ")
        print("+---+-+--+-+---+")
        print("    |_|  |_|    ")

r2 = StarDestroyer()
r1 = SpaceShip()

print(r1.draw())
print(r2.draw())