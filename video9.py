# Type casting in python 
# the process of conversion of a datatype into another datatype
# 2 types
# 1. explicit which is user side's
# 2. implicit which is python's side
# 
a = "1" # coz in Double quotes it is a string "1"
b = "2" # coz in Double quotes it is a string "2"
print(int(a)+int(b)) # this is called explicit type casting

# example of explicit typecasting
string = "15"
number = 7
string_number = int(string)
sum = string_number + number
print (sum)

# another example of explicit typecasting
string = "15"
number = 7
string_number = str(number)
sum =  string + string_number 
print (sum)

# an example of implicit typecasting
c = 1.9 # it is a float value which is have more preference and has a higher order than integer value
d = 8 # it is an integer value which have lower preference and prdering than float value 

print (c+d)


