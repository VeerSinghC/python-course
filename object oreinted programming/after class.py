class Tom : 
    name = "Tom"
    country = "India"
    type = "Robot"
    made_by = "Harsh"

    def introduce(self):
        print("Hello, my name is " + self.name + ". I am from " + self.country + ". I am a " + self.type + ".")
    def made(self):
        print(" I am made by " + self.made_by + " in India.")

ob = Tom()
ob.introduce()
ob.made()

class Jerry :
    name = "Jerry"
    country = "USA"
    type = "Robot 2"
    made_by = "Harsh"

    def introduce(self):
        print("Hello, my name is " + self.name + ". I am from " + self.country + ". I am a " + self.type + ".")
    def made(self):
        print(" I am made by " + self.made_by + " in USA.")
ob = Jerry()
ob.introduce()
ob.made()