class Goat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a goat named {self.name} and I am {self.age} years old.")

    def sound(self):
        print("Siuuuuu")

class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a lion named {self.name} and I am {self.age} years old.")

    def sound(self):
        print("Asla Ham Bhi Rakhate Hai Pradhan")

Goat1 = Goat("Cristiano Ronaldo", 50)
Lion1 = Lion("Sunil Chetri", 50)

for animal in (Goat1, Lion1):
    animal.info()
    animal.sound()