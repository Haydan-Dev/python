class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of the Employee Id number-{self.id} is {self.name}")

Employee_1 = Employee("Haydan",12)
Employee_2 = Employee("Faazil",15)

print(Employee_1) # dekh bhai haydan ye sirf tujhe memory pointer lacation dega
print(Employee_2) # dekh bhai haydan ye sirf tujhe memory pointer lacation dega

# issi liye upar waali problem ko solve karne ke liye 
# tujhe showDetails() naam ka Method use karne hoga jo tune upar ussi class may create and initialize kiya hai. 

Employee_1.showDetails()
Employee_2.showDetails()

# chal abb Inheritance pe aate hai.
class Programmer(Employee):
    def showLanguage(self):
        print("The Default language in which i am coding is python")
# abb dekh haydan meri baat sunn ye jo programmer class hai wo Employee class ka beta / beti hai programmer class may saari khubiya hai employee class ki 
# for example

Employee_2 = Programmer("Faazil",15)
Employee_3 = Programmer("zoher",16)
Employee_2.showLanguage()
Employee_3.showDetails()