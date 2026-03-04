# tuples are immutable
# agar sirf ek value hai tuple may (1,) to comma laga na padega warna python confuse ho jaaye ga
# tuple may ham multiple datatypes bhi de sate hai.
# tuple index ko [] square bracket use kar ke access kiya ja sakta hai

# t= (1,2,3,4,"haydan","faazil")
# print(type(t),t)
# print(t[0])
# print(t[1])
# print(t[2])

# # if else can be used in tuple like list
# if "haydan1" in t:
#     print("yes it is present!")
# else:
#     print("It is not present")

# # tuple may bhi slicing hai par wo imutable hai / unchangeable so, tuple ki original state same to same hoti hai sirf new tuple may slicing ka output hota hai
# print(t[4])
# t2 = t[2:4]
# print(t[2:5])

# # negative index and all the indexing of list is aplicable to tuple 
# # ham new tuple bhi bana sakhte hai 2 old tuple ko concatine karke
# # methods of tuple

# tup1 = (1,2,3,4,5,6,7,89,6,5,4,334,12,32,45,6,63,3,2,1,2,57,32)
# print (tup1.count(5))

# #index method
# print(tup1.index(89))
# print(tup1.index(334,1,15))
# print("length is ",len(tup1))


# excersice

# 1. The Identity Card 🆔

# Ek Tuple banao my_info jisme tera: ("Name", Age, "Role") ho.

# Iska Type print karke confirm kar ki ye Tuple hi hai.

# Sirf Role ko access karke print kar.



my_info = ("Haydan",20,"full-Stack-Intern")
print(type(my_info))

role = my_info[2]
print(my_info[2])

print(role)


countries = ("India", "USA", "UK")
new_counter=list(countries)
new_counter[2] = "Japan"
countries=tuple(new_counter) 
print(countries)

