
# else block ko while and for-loop dono may use kiya jaata hai 
# hamesha last may hi likhna hai else ko  
# Note: else part loop ke breakhone par nahi. 
# balki loop ke khatam hone/finish par hi execute hoga
# agar loop break hota hai to else block execute hi nahi hoga


# for i in range (5):
#     print(i)
# else:
#     print("for-loop may nahi gaya to phir else block may aaya hai")


# # excersice
# ages = [22, 25, 19, 30, 19, 28]
# for checking in ages:
#     if checking<=18:
#         print("Enter is Closed !")
#         break
# else:
#     print("You All Are Allowed")

# ticket = [12, 45, 33, 89, 21]
# for jackpot in ticket:
#     if(jackpot==7):
#         print("You Win a Jackpot !")
#         break
# else:
#     print("Better Luck Next Time")


# Task (Dobara yaad dila raha hoon):
# List: items = ["pen", "paper", "ink"]
# Input: User se maang.
# Logic: Loop laga. Agar mile toh "Found", nahi toh "Not Found" (For-Else use kar).

def found ():
    items = ["pen", "paper", "ink"]
    user_input = input(f"Ye items available hai\n{items} \n Inn may se kya chaiye:").lower()
    for item in items:
        if (user_input == item):
            print(f"{user_input} Found!!")
            break
    else:
        print("Not Found!!")
found()