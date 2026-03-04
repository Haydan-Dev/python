# Main_balance = 5000
# while True:
#     Option = int(input(" Wellcome TO ATM:\n 1.Chek balance \n 2.Deposit \n 3.Withdraw \n 4.Exit \n Select an option:"))
#     match Option:
#         case 1:
#             print("Total balance:",Main_balance)
#         case 2:
#              Deposit_amount = float(input("Enter Amount to Deposit:"))
#              Main_balance = Main_balance+Deposit_amount
#              print("Total Amount After Deposit:",Main_balance)
#         case 3:
#              Withdraw_amount = float(input("Enter Amount to Withdraw:"))
#              Main_balance = Main_balance - Withdraw_amount
#              print("Total Balance After Withdraw:",Main_balance)
#         case 4:
#             Exit = input("Are you sure you want to Exit ? (yes/No)").lower()
#             if(Exit == "yes"):
#                 print("tata  bye bye")
#                 break
#         case _:
#              print("Please Enter a Valid Option, In-valid Option")


# users = ["Haydan", "Rahul", "Bot_1", "Zayan", "Spammer_99"]
# banned_users = ["Bot_1", "Spammer_99"]

# for i in users:
#     if (i in banned_users):
#         print("Alert!",i,"is Banned. Access Denied!")
#     else:
#         print("Welcome",i,"Access Granted!")
    


# 1. The Prime Range Explorer (For Loop): Tujhe 1 se lekar 100 tak ke saare Prime Numbers print karne hain.

# Condition: Tujhe nested loops ka use karna hai aur har prime number ke baad ek space dena hai.

 # step-1 user ke paas se input lena 
 # step-2 uss input ko divide by 10 karna 


# num = int(input("Enter Number:"))
# print(num%10)

# number = int(input("Enter a number to check its even or not"))

# step-1 1 se 50 tak ke number ko total may print karna abb 
# step -2  sab se pehle to range may 51 lena hoga kyu ki 50 lunga to python last digit ko count hi nahi karega 
# ek loop bhi bana na padega 
# pehle 1 se shuru karo and ussko ek khali variable may bharo phir next number par jaaw uss ko phir ussi variable may jaha uss ek khali variable may bhara tha uss hi may + kardo ye process 50 aane tak karo phir ruck jaaw

sum = 0
for i in range(51):
    sum = sum + i
print(sum)


# Scenario: User se ek lamba number input lo (e.g., 582036). Loop ke khatam hone par ye 3 reports nikalni hain:
# Count: Total kitne digits hain? (Output: 6)
# Even Sum: Jitne Even digits hain, unka total kya hai? (8+2+0+6 = 16)
# Odd Count: Kitne digits Odd hain? (5 aur 3; Total: 2)

# Step-1 user ke paas se number lena 
# step -2 uss number ke total kitne digits hai uss ko check karna hai dekh ye ham kese kar sakte hai %10 se kyu ki uss may hi hamme last digit miltihai 
# ek bar total digits mil gaye to phir pata chale ga total kitne digits hai
# ek bar total digits nikal jaaye to phir uss har ek digit ko 2 se % karayenge to pata chal jaayega ke phir uss ka total karnege
# odd digits ka total vaue baataayenge

number = int(input("Enter a Number:")) # for exacple 5420
num = 0 # 0,2,4=6,5=11
digit_count=0
sum = 0
odd_count = 0
digit = 0
while (number>0): # 0,1,2,3,4<= 0.5 no loop ends here
    digit = number%10
    num = num + digit # 0,2,4,5
    if(digit%2==0):
        sum = sum+digit
    else:
        odd_count = odd_count+1
    number = (number//10) # 542 , 54.2 (// --> 54 lowest round fegure),5.4 (//-->5 lowest round fegure),0.5
    digit_count=digit_count+1 # 1,2,3,4

print("Total of even Number is = ",sum)
print("Total Number of odds:",odd_count)
print("Total numbers of digit",digit_count)


number = int(input("Enter a number:")) #2003
num = 0   #0,3,0,0
digit = 0 # 0,3,0,0
found_zero = 0 #0,0,1,1,=2,
while (number>0): #true -->,true-->,true-->,true-->
    num = number%10 # 2003%10 = 3,0,0,2
    digit = num # 3,0,0,2
    number = number//10 # 200,20,2,0.20
    if(digit==0): # check -->3 flase, check --> true
        found_zero = found_zero +1 # 0,1,1=2,











