class Employee :
    # Constructor
    def __init__(self):
        print("Employee Created.")

    def __del__(self):
        print("Destructor  Called. Employee Deleted.")

obj = Employee()
del obj        
        