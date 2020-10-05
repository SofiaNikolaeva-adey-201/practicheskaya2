class Second:
    color = 'red'
    form = 'circle'
    size = '15'

    def changecolor(self, newcolor):
        self.color = newcolor
    def changeform(self, newform):
        self.form = newform
    def changesize(self, newsize):
        self.size = newsize


obj1 = Second()
obj2 = Second()
obj3 = Second()

print(obj1.color, obj1.form, obj1.size)
print(obj2.color, obj2.form, obj2.size)
print(obj3.color, obj3.form, obj3.size)

obj1.changecolor('green')
obj1.changecolor('blue')
obj2.changeform('oval')
obj2.changesize('44')

obj3.changecolor('black')
obj3.changeform('rhombus')
obj3.changesize('100')

print(obj1.color, obj1.form, obj1.size)
print(obj2.color, obj2.form, obj2.size)
print(obj3.color, obj3.form, obj3.size)