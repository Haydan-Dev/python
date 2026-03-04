x = 4
def my_function():
    y =5
    global x 
    x = 10
    print(y)
    # print(x)
my_function()
print(x)
