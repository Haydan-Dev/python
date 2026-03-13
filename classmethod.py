class Employee:
    company = "Apple"
    def show(self):
        print(f"the name of Employee is {self.name} and company is {self.company}")
    
    @classmethod
    def changecompany(cls,newcompany):
        cls.company = newcompany

e1 = Employee()
e1.name = "haydan"
e1.show()

e1.changecompany("Gulf-company")
e1.show()
print(Employee.company)