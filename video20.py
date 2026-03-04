# def is a keyword used for declaring a function
# function defination
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)


# function calling
calculateGmean(10,3)



# pass keyword
# for leaving the function empty
def function (a,b):
    pass

# 2 tpes 
# 1. user define 
# 2. built in function



# argument/parameters in python
def average(a=9,b=6): #types of parameter/arguments in python.
    print("THE average is ",(a+b)/2)

average()
average(4,6)
average(10)
average(b=15)
average(a=12)


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i 
    print("average is :",sum/len(numbers))

average(5,6,7,1,2,38,6,89,876,)

def name(**name):
    print("hello,", name=["fname"], name=["mname"],name=["lname"])

name["lname"]

name(mname = "buchanan",lname="barnes",fname="james")
