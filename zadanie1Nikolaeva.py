class First:
    color = 'red'
    def out(self):
        print(self.color + '!')

obj1 = First()
obj2 = First()

print(obj1.color)
print(obj2.color)
obj1.out()
obj2.out()

#в одном случае обращаемся к классу, а в другом - к экземпляру класса