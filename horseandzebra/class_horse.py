from class_legs import Legs

class Horse(Legs):
    name = "Spirit"
    def __init__(self, legs_number, voice):
        super().__init__(legs_number)
        self.voice = voice
    def info(self):
        print(f"{self.name} have {self.legs_number} legs and say {self.voice}")       
h1 = Horse({1,2,3,4}, "Igogo")
print(h1.info())