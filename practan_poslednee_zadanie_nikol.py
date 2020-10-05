class Figure:
    def __init__(self, color):
        self.color = color
        self.color = 'white'
    def changecolor(self, newcolor):
        self.color = newcolor

class Oval(Figure):
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter
        super().__init__(self)
        self.color = 'white'


class Foursquare(Figure):
    def __init__(self, side_length, diagonal):
        self.side_length = side_length
        self.diagonal = diagonal
        super().__init__(self)
        self.color = 'white'


fig1 = Oval(25, 13)
fig1.changecolor('black')
fig2 = Foursquare(13, 18)
fig2.changecolor('red')

print(fig1.color, fig1.square, fig1.perimeter)
print(fig2.color, fig2.side_length, fig2.diagonal)
print(fig1.color)
print(fig2.color)