import math
from wild_cat import WildCat
class HomeCat(WildCat):
    def __init__(self, name, food, weight, claws, myau):

        super().__init__(name, food, weight, claws)
        self.myau = myau


