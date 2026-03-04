# while (True):
#     word = input("Enter a word:")
#     print("You Enter a word:",word)
#     if word == "wolf":
#         print("you print wolf,exiting the loop")
#         break 


# number =1
# for number in range(21):
#     if(number%3!=0):
#         print(number)
#     else:
#         continue
#     number = number +1

         
        
# i=0    
# while(i<20):
#     i = i +1          # Pehle badhaya (1 ho gaya)
#     if(i%3==0):       # Check: Kya ye 3 se divide nahi hota?
#         continue
#     print(i) 


# correct_pin= 1234
# limit = 3
# while (limit>0):
#     user_pin = int(input("ENter pin"))
#     if(user_pin==1234):
#         print("Unlock successful")
#         break
#     elif(user_pin!=1234):
#         print("Wrong Pin")
#         limit = limit -1
#     if(limit<=0):
#         print("Phone Locked")
#         break
    
        
# Goal: Ek program likh jo tab tak chale jab tak machine khali na ho jaye.
# Rules:
# Stock: stock = 5 (Loop ke bahar).
# Loop: while stock > 0:
# Input: User se puch: "Kitni Coke chahiye?"
# Conditions:
# User bole 0 (Zero): Print "Bye Bye" aur loop tod do (break).
# User maange Stock se zyada (e.g., Stock 3 hai, user ne 4 maangi): Print "Itna maal nahi hai!" aur loop upar bhejo (continue).
# Valid Request: Stock mein se utni coke ghata do (stock = stock - user_input) aur print karo "Ye lo tumhari coke. Ab X bachi hain."
# Game Over: Loop ke baad (ya jab stock 0 ho jaye) print hona chahiye: "Machine Empty! Dukan Band."

stock = 5
while(stock>0):
    user_input=int(input("Kitni Coke Chahiye? "))
    if(user_input==0):
        print("Bye Bye!")
        break
    elif(user_input>stock):
        print("Itna Maal nahi hai")
        continue
    else:
        stock =   int(stock) - int(user_input)
        print("Ye lo tumhari coke. Ab " ,stock,"bachi hain.")
print("Machine Empty! Dukan Band.")


