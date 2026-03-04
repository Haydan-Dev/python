# 🟢 LEVEL 1: EASY (Syntax Warmer)
# Goal: Sirf syntax sahi bithana hai. Result = Value1 if Condition else Value2

# Challenge 1: The Coffee Logic ☕ Variable: temp = 45 Logic: Agar temp 50 se zyada hai toh status "Hot" hona chahiye, 
# warna "Cold". Task: Iska one-liner likho.

temp = 45
print("Hot") if(temp > 50) else print("Cold")




# Challenge 2: The Even/Odd Checker 🔢 Variable: number = 8 Logic: Agar number % 2 == 0 hai toh res 
# "Even" hona chahiye, warna "Odd". Task: Iska one-liner likho.

number = 8 
print("Even") if(number%2==0) else print("Flase")



# 🟡 LEVEL 2: MEDIUM (Real Backend Logic)
# Goal: Ab print mat karna. Value ko variable mein store karna hai.

# Challenge 3: The API Status (Status Codes) 🌐 Backend development mein 200 ka matlab "OK" hota hai.

# Scenario: Ek variable hai status_code = 404.

# Logic: Ek naya variable message banao. Agar status_code 200 hai, toh message "Success" hona chahiye, warna "Error".

# Task: message = ... (One Liner likho).

status_code = 404
response = "Success" if(status_code == 200) else "Error"
print(response)





# Challenge 4: The Discount System (Comparisons) 🏷️

# Scenario: Shopping cart ka total = 1500 hai.

# Logic: Ek variable final_price set karna hai. Agar total 1000 se zyada ya barabar (>=) hai, toh final_price hoga total * 0.9 (10% discount), warna total same rahega.

# Task: final_price = ... (One Liner likho).


total = 1500

final_price = total*0.9 if(total>=1000) else total
print(final_price)
