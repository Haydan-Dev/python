# this is for map 

def cube(x):
    return x**3

l = [1,2,3,4,5,6,8,9,11,2,3,4,5]

new_l = map(cube,l)
new_list = list(new_l) 

print(new_list)

# this is for filter 

def filter_func(a):
    return a>50

new_filter = filter(filter_func,l)
resultofnewfilter = list(new_filter)
print(f"this is filter = {resultofnewfilter}")

# this is reduce
# Note : - 1. the fuction which take other function as an argument are known as higher order functions
# Note :-2. reduce fuction koo import karna padta hai, coder has to first import reduce before working on it  
from functools import reduce
listofnumbers = [1,2,3,4,5,6,7,8,9,10]
sum = reduce(lambda x,y: x+y,listofnumbers)
print(f"this is sum of list of numbers {sum}")

