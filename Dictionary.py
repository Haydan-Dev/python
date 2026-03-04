information = {
    "Haydan":['is a student!'],
    "Name":"Haydan","Occupation":"Student","age":22
}

# note [] ye errors throw karega jab key invalid hogi tab 
# jab ham chahe ke key naa hone par error throw hoo tab ye use karna hai 
print(information["Haydan"])

# note ye .get() ye error throw nahi karega 
# tab use hota hai jab hamme chahiye ke key na hone par error throw naa hoo. 
print(information.get("age"))
# for example
print(information.get("haydan"))
# is ka answer none aayega

# # keys ko lena with function
print(information.keys())
# # keys ki values ko lena with function
print(information.values())

# # keys ko lena using for loop
for keys in information.keys():
    print(information[keys])


# # keys ki values ko lena using for loop
for values in information.values():
    print(values)
# gives key and values in pairs (key,values).
print(information.items())


# ep1 = {122:45,123:89,567:69,670:67}
# ep2 = {222:67,566:90}

# # update() a dictionary putting other dic's key and values it itself
# # ep1.update(ep2)
# # print(ep1)

# # clear() a dictionary and make it empty === {}
# # ep1.clear()
# # print(ep1)


# # pop() cut 1 key and values
# ep1.pop(122)
# print(ep1)

# #popitem() remove/cut last item key value in dic's
# # for example
# ep1.popitem()
# print(ep1)

# # EXCERSICE
def The_Grade_Card():
    student_scores = {"Harry": 85, "Rohan": 92, "Shubham": 78} # dic may key and values store hai
    User_input = input("Enter a name pls!:").capitalize()  # user se input lena and uss ko capitalize karna checking ke liye
    print(student_scores.get(User_input,"Not Found!")) # abb ye bhi samjh gaya may
The_Grade_Card() # fuction ko call karna 

def Inventory():
    inventory = {"Apple": 100, "Banana": 40, "Mango": 150}
    print(F"--------------value before changes--------------\n{inventory}")
    inventory["Banana"] = 60
    inventory["Grapes"]= 80
    print(F"--------------Vlues After Changes-------------------\n{inventory}")
Inventory()    


def Square():
    user_number = int(input("Enter a Number:"))
    dictionary={}
    for Number in range(1,user_number+1):
        dictionary[Number] = Number*Number
    print(dictionary)
Square()



def Total_Bill_Calculator():
    cart = {"Laptop": 50000, "Mouse": 500, "Keyboard": 1000}
    sum = 0
    for value in cart.values():
        sum=sum+value
    print("total = ",sum)
Total_Bill_Calculator()




# Q5. The String Counter (Interview Fav) 
# Word hai: "MISSISSIPPI".
# Ek dictionary bana jo bataye kaunsa letter kitni baar aaya hai.
# Expected Output: {'M': 1, 'I': 4, 'S': 4, 'P': 2}
# Dimaag laga. Start ho ja. 
# Pseudo Code
empty_dict = {}
for letter in "MISSISSIPPI":
    # count = 0
    if letter in empty_dict:
        empty_dict[letter] +=1 
    else:
        empty_dict[letter]= 1
print(empty_dict)



marks = {"Harry": 85, "Rohan": 28, "Shubham": 92, "Vikram": 30}
passed_students = {}

# .items() use kiya taaki Name aur Score dono mile
for name, score in marks.items():
    if score > 33:
        passed_students[name] = score  # Pass walon ko nayi list mein daal diya

print(passed_students)