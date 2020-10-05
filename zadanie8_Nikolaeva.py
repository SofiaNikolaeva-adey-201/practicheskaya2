class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h
    def outing(self):
        print(self.long, self.width, self.height)

class Kitchen(Table):
    def howplaces(self,n):
        if n < 2:
            print('It is not kitchen table')
        else:
            self.places = n
    def outplaces(self):
        print(self.places)

t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplaces()

t_2 = Table(1,3,0.7)
t_2.outing()
#t_2.howplaces(8)

class Hall(Table):
    def howplaces(self,n):
        if n < 10:
            return('It is not hall table')
        else:
            self.places = n
            return n
    def volume(self):
        return self.long * self.width * self.height
    def square(self):
        return self.long * self.width
    def price(self, n):
        return n * 1000


table220 = Hall(5, 6, 2)
print(table220.howplaces(2))
print(table220.volume())
print(table220.square())
print(table220.price(2))
