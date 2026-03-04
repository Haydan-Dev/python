#loops in python
#2 tpyes 
#1. for looop
#2. while loop and other some types but not used that much sometimes come in handy so knowledge is needed but not required for codding normally

name = "abhishek"
for i in name:
    print(i)

colors = ["red","blue","green"]
for i in colors:
    for j in i:
        print(j)

# the above code is for list

# range is a function mostly use in loops starts with 0 and end at n-1 means range (5) = 0,1,2,3,4

for k in range(5):
    print(k+1)


for num in range(1,50): # it will go untill 49 0 to 49 we told it to go to from 1 to 49
    print(num)  #answer will always be n-1 
