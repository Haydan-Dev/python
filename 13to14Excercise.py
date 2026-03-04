Username = input("enter your name:")
if (Username.isupper()):
    print("Bhai chill chill, chilla kyun rahe ho?")
elif(Username.islower()):
    print("Thoda toh bada likho")
else:
    print("Theek hai")


Gamil = input("Enter your Gmail:")
if (Gamil.endswith("@gmail.com")):
    print("Access Granted")
else:
    print("Galat Email")


Spam = input("Enter a Sentence:")
if(Spam.find("buy now")!=-1 or Spam.find("free")!=-1):
    print("its a spam")
else:
    print("do what ever you want")

password = input("ENter a password:")
if(len(password)<8 and password.find(" ")!=-1):
    print("password is weak and space are not allowed")
elif(len(password)<8):
    print("Entered password is weak")
elif(password.find(" ")!=-1):
    print("Space are not allowed")
else:
    print("Password is good")


Marks = int(input("Enter marks:"))
if (Marks>90):
    print("A+")
elif(Marks<=90 and Marks>=70):
    print("A")
elif(Marks < 70 and Marks>=40):
    print("B")
else:
    print("Fail")

angle1=int(input("Enter angle-1:"))
angle2=int(input("Enter angle-2:"))
angle3=int(input("Enter angle-3:"))

if (angle1+angle2+angle3==180):
    print("A Valid Triangle")
else:
    print("invalid triangle")


string = input("Enter a string")
if(len(string)%2==0):
    print("Even word")
else:
    print("Odd word")


city = input("ENter city name:")
if(city.istitle()):
    print("Its perfect")
else:
    print(city.title())


fruit = input("ENter fruit name:")
if(fruit.lower().startswith("a") or fruit.lower().startswith("e") or fruit.lower().startswith("i") or fruit.lower().startswith("o") or fruit.lower().startswith("u")):
    print("starts with vowels")
else:
    print("no not start with vowels")

Number_1 = int(input("Enter a Number-1:"))
Number_2 = int(input("Enter a Number-2:"))
operator = input("Enter a operator(+,-,*,%,/):")

if (operator=="+"):
    print(Number_1+Number_2)
elif (operator=="-"):
    print(Number_1-Number_2)
elif (operator=="*"):
    print(Number_1*Number_2)
elif (operator=="%"):
    print(Number_1%Number_2)
elif (operator=="/"):
    print(Number_1/Number_2)
else:
    print("Invalid operator")



