# It is a function that take another function as an argument returns the new function that modify the behavior of the function
# this modified new function is refered to / as a Decorator function

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx()
        print("thanks for using this function")
    return mfx

@greet
def hello(add):
    print("Hello world")
def add(a,b):
    print(a+b)


hello()
