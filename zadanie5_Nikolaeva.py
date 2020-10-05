class fruits:
    def __init__(self, w, n = 0):
        self.what = w
        self.numbers = n

f1 = fruits('apple', 150)
f2 = fruits('pineapple')

print(f1.what, f1.numbers)
print(f2.what, f2.numbers)

class fruits:
    def __init__(self, n = 0, w):  #error
        self.what = w
        self.numbers = n

f1 = fruits(150, 'apple')
f2 = fruits('pineapple')

print(f1.what, f1.numbers)
print(f2.what, f2.numbers)