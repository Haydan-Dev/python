# marks = [3,5,6,8,10,"haydan",4.8,True]
# print (marks)
# print(type(marks))

# # List is always starts with index 0
# # list are mutable (can be changed)
# # multiple data types can be stored in list like int, str, float, bool etc.
# # negative indexing is also allowed in list
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[-4])
# # if else can be used to check presence of an element in list
# if 6 in marks:
#     print("6 is present in marks list")
# else:
#     print("6 is not present in marks list")

# # if else can be used to check absence of an element in list
# # this if else can also be used with negative indexing , string , float etc.
# # slicing is also allowed in list
# print(marks[1:4])  # prints from index 1 to index 3
# print(marks[::2])  # prints all elements with a step of 2
# print(marks[:3])
# print(marks[2:])
# print(marks[1::2])


# lst = [i for i in range(4)]
# lst = [i*i for i in range(10)]
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)
#  #----------------------------------------------#
#  # excerise for list

# movies_list =["harry potter","inception","Hit","pirates of the carribean","Avengers"]
# print(movies_list)
# print(movies_list[2:3])
# print(movies_list[-1])


# method in list 
# ls = [1,12,33,4,15,16,8,2,9,10,21,26,30]
# print(ls)
# ls.append(6)  # adds 6 at the end of the list
# print(ls)
# ls.sort()
# print(ls)  # sorts the list in ascending order
# ls.reverse()
# print(ls)  # reverses the list
# print(ls.index(15))  # returns the index of the first occurrence of 15
# ls.reverse()
# print(ls)
# mls = ls.copy()  # creates a copy of the list
# print(mls)
# mls.insert(0,100)  # inserts 100 at index 0
# print(mls)

# nls = ["mango","banana","grapes"]
# mls.extend(nls)  # extends mls by adding elements of nls at the end
# print(mls)

# kls = nls + mls  # concatenates nls and mls
# print(kls)

# mls.remove(15)  # removes the first occurrence of 15
# print(mls)



# coding excersise for list methods
guests = ["Rohan","Sohan","Mohan"]
guests.insert(0,"Haydan")
guests.append("Harry")



data = [10,20,555,30,40,555]
for i in range(len(data)):
    if  555 in data:
        data.remove(555)
data.pop()    
print(data)



matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
         ]

new_matrix = []

for i in matrix:
    for j in i:
        new_matrix.append(j) 
print(new_matrix)