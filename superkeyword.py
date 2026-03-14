class ParentClass:
    def parent_method(self):
        print("this is parent methos from parent class")
class ChildClass(ParentClass):
    def parent_method(self):
        print("haydan")
        super().parent_method()
    def Child_method(self):
        print("this is a child method from child class")
        super().parent_method()

child_object = ChildClass()
child_object.Child_method()
child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")

print(harry.name)
print(harry.id)
print(harry.lang)