from class_poloska import Poloska
from class_legs import Legs

class Zebra(Legs,Poloska):
    name = "Marti"
    def __init__(self, legs_number, poloska_number, voice):
        Legs.__init__(self, legs_number)
        Poloska.__init__(self, poloska_number)
        self.voice = voice
    def info(self):
        print(f"{self.name} have {self.legs_number} legs and {self.poloska_number} wanna say {self.voice}")       


