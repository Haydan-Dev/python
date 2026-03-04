# if - elif , else statemant

Age = int(input("Enter Your age"))
print("your age is",Age)

if (Age>=18 and Age<=75):
    print("Your can drive")
elif(Age<18 and Age >=16):
    print("you can drive a non-Licence scooty under 50 cc engine")
else:
    print("you cant drive")