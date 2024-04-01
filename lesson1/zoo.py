import math


class ZOO:
    def init(self, name, food, weight):
        self.name = name
        self.food = food
        self.weight = weight

    def name(self):
        return self.name

    def food(self):
        return self.food

    def weight(self):
        return self.weight

    def info(self):
        print(f"{self.name}, are weight {math.fabs(self.weight)}, and eat {self.food}")
animal = ZOO('HZ', 'aпвап',200)
print(animal.info())

class WildCat(ZOO):
    def init(self, name, food, weight, claws):
        ZOO.init(self, name, food, weight)
        self.claws = claws
wild_cat = WildCat('Barsick','extractiooon', 100, 'BIG')
print(wild_cat.info())
class HomeCat(WildCat):
    def init(self, name, food, weight, claws, myau):

        WildCat.init(self, name, food, weight, claws)
        self.myau = myau


home_cat = HomeCat('Uma', 'fish', 3, 'rare', 'mr-mr-mr')
print(home_cat.info())
class Gipo(ZOO):
    def init(self, name, food, weight, asssize):
        ZOO.init(self, name, food, weight)
        self.asssize = asssize
gippopotamus = Gipo('gipop', 'grass', 400, 200)
print(gippopotamus.info())