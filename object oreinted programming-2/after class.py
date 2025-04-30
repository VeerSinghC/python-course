class Employee:
    def __init__(self):
        self.num1 = 6
        self.num2 = 29
        self.num3 = 48

    def add(self):
        total = self.num1 + self.num2 + self.num3
        print("The sum of the three numbers is:", total)
        
    
ob = Employee()
ob.add()