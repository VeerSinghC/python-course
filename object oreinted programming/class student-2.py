class student:
    grade = 10
    name = "Penguin Kumar"
    city = "AntarcticaPuri"
    election = "Raja Ji"
    def intro(self):
        print("Hi I am a student of grade", self.grade)
        print("I am from", self.city)
        print("My name is", self.name)

    def details(self):
        print("I am gangster of",self.city)
        print("Everyone fears the name", self.name)
        print("I am the", self.election, "of my city")

ob = student()
ob.intro()
ob.details()        