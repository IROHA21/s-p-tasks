class Dog :

    def __init__(self, name, race):
        self.name = name
        print(name)

    def meow(self, x):
        return x + 1

    def bark(self):
        print("bark")


class HowManyDogs :
    def __init__(self):
        self.NumOfDogs = []

    def Count(self,dog):
        self.NumOfDogs.append(dog)
d = Dog("tim", "first")
d2 = Dog("bill", "second")

a1 = HowManyDogs ()
a1.Count(d)
a1.Count(d2)
print(a1.NumOfDogs[0].name)



