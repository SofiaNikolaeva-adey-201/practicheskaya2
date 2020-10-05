class Things:
    def __init__(self, n, t):
        self.namething = n
        self.total = t

th1 = Things('table', 5)
th2 = Things('computer', 7)


print(th1.namething, th1.total)
print(th2.namething, th2.total)

th1.color = 'green'
th2.color = 'red'  #чтобы исправить ошибку добавляем ему это свойство

print(th1.color)
print(th2.color)