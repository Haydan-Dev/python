class Employee:
    companyName = "HCL" # ye ek class variable hai 
    def __init__(self,name):
        self.name = name # instance name ke liye self.name variable
        self.raise_amount = 0.2 # ye bhi ek instance variable hai 
    def showDetailsJ(self):
        print(f"name is {self.name} and raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "tcs"
emp1.showDetailsJ()
emp2 = Employee("Haydan")
emp2.showDetailsJ()