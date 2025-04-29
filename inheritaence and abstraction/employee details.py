class parent(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class child(parent):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        parent.__init__(self, name, idnumber)

a = child("Veer Singh", 7, 50000000, "CEO")
a.display()
print(a.salary)
print(a.post)
        
        