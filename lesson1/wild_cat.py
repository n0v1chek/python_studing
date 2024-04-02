import math
from zoo_class import ZOO
class WildCat(ZOO):
    def __init__(self, name, food, weight, claws):
        super().__init__(name, food, weight)         
        self.claws = claws


