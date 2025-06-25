class Dog :

    def __init__(self, name):
        self.name = name
        print(name)

    def meow(self, x):
        return x + 1

    def bark(self):
        print("bark")



d = Dog("tim")
d2 = Dog("bill")
d.bark()
print (type(d))

print (d.meow(5))