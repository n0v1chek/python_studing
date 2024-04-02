import math
from zoo_class import ZOO
class Gipo(ZOO):
    def __init__(self, name, food, weight, asssize):
        super().__init__(name, food, weight)
        self.asssize = asssize


