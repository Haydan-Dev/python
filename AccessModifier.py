class Employee:
    def __init__(self):
        self.name = "Harry"             # Public Variable
        self._name = "Harry_Protected"  # Protected Variable (Single underscore)
        self.__name = "Harry_Private"   # Private Variable (Double underscore)

a = Employee()

# Accessing them
print(a.name)          # Output: Harry (Asani se dikhega)
print(a._name)         # Output: Harry_Protected (Dikh jayega, par ye 'Protected' hai)
# print(a.__name)      # ERROR! (Directly access nahi hoga)
print(a._Employee__name) # Name Mangling (Chorni rasta!)

class Student:
    def __init__(self):
        self._name = "harry"
    def _funName(self):
        return "code with harry"
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj1._funName())
print(obj._name)