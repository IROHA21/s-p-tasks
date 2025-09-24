class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories


    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_calories(self):
        return self._calories
    def set_calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        calories = self.get_calories()
        return calories < 200 if calories is not None else False

    def is_delicious(self):
        name = self.get_name()
        return True if name is not None else False




# Test
num1 = Dessert("strawberryCake", 150)
num2 = Dessert("OrangeCake", 250)
print(num1.is_healthy())
print(num1.is_delicious())
print(num2.is_healthy())
print(num2.is_delicious())


