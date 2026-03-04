# strings are immutable in python 
# strings may koi bhi changes karte hai to usska ek new string banta hai wo original change nahi hoti hai
# some methods of string
# upper() , lower() , rstrip("character ka symbol i.e #,@,!") 
a = "haydan@@@@"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("@"))
# replace("current_variable","want to change with variable") , split(" without space work nahi karta hai ye")
print(a.replace("haydan","Haydan123"))
print(a.split("a"))
# capitalize() ,center() , count("variable name") , endswith()
Heading = "introtuction to Python and is a good language for AI ML and is AllRounder Language"
print(Heading.capitalize())
print(a.center(10))
print(Heading.count("o"))
print(Heading.endswith("i"))
# find() 
print(Heading.find("is"))
# index()
print(Heading.index("good"))
# isalnum()
check = 'testingkarahahoon'
print(check.isalnum())
print(check.isalpha())
print(check.islower())
print(check.isspace())
print(check.istitle())

