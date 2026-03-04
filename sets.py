# Sets are the unordered collection of data items,
# They store items in a single variavle
# it is seperateed by commas and esclose within curil brateks{}.
# it is immutable / unchangable
# it do not contain duplicate items

# Note : it can contain duplicate items/values. 
# but it doesn't display them it display only single vaule of that duplicate as you can see
# it doesn't give output in order 
# it always give an unorder output 
# which is totally random with the respective values it contain

set1 = {2,4,2,6}
print(set1)

sets = {"haydan",False,43.89,4,6,10,4,6}
set2 = {1,12,3,7,8,9} 
for_testing_clear = {"hadan",12,32,44.2121,True}
haydan = set()
print(type(haydan))

for i in sets:
    print(i)


# methods of sets 
# 1. union()
print("This is union of sets = ",set1.union(sets))
# 2.intersection()
print("This is intersection of sets = ",set1.intersection(sets))
# 3. update()
# note haydan tu iss ko kisi variable may save nahi karsakta hai!!!
set1.update(set2)
print("THis is update method =",set1)

set3 = set1.symmetric_difference(set2)
print("This is symmetric_difference method of sets ",set3)

# 4. disjoint()
print(set1.isdisjoint(set2))

# 5.issuperset()
print(set1.issuperset(set2))

# 6.issubset()
print(set2.issubset(set2))

# 7.add
set2.add("haydan")
print("set2 after using add() method",set2)
# 8.remove
# note this method gives errors if value which want to removed not present in the sets
set2.remove("haydan")
print("set2 after using remove() mmethod",set2)
# 9. discard
# note this method doesn't gives any errors if value which want to discard is not present in the sets
set2.discard("haydan")
print("set2 after using discard() method",set2)

# 10. del
del sets
# 11.clear
for_testing_clear.clear()
print("This is the use of clear method",for_testing_clear)



# exsercise
nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]
s = set(nums)
print(s)

vips = {"Harry", "Rohan", "Shubham"}
if("haydan" in vips):
    print("Wellcome Sir")   
else:
    print("Bhaag yahan se")


dev_A = {"Python", "Java", "C++"}
dev_B = {"JavaScript", "Python", "Go"}

print(dev_A.intersection(dev_B))

required = {"Keyboard", "Mouse", "Monitor", "CPU"}
have = {"Mouse", "Monitor"}

print(required.difference(have))

A_Word = {"ManiacLearningPython"}
count = 0
for latters in A_Word:
    count = count + 1
    print(F"Total Letters = {len(set(latters.lower()))}")
    