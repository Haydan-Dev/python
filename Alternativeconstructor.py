class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e = Employee("haydan",35000)
print(e.name)
print(e.salary)

string = "Haydan-35000"
info = Employee(string.split("-"),55000)
print(e.name)
print(e.salary)