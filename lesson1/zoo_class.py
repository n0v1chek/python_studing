import math
class ZOO:
    def __init__(self, name, food, weight):
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

