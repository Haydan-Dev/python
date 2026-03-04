# 1. The "Name Tag" Maker 🏷️

# Task: Ek function banao make_tag(name).

# Input: Function ek naam lega (e.g., "Haydan").

# Logic: Ye function kuch return nahi karega, bas print karega: "--- [ Haydan ] ---"

# # Call: make_tag("Harry") call karke check kar.



def make_tag(name):
    print("----[",name,"]----")

make_tag("nadyah")



# The Double Dealer ✖️2️⃣

# Task: Ek function banao double_it(number).

# Input: Ek number (e.g., 5).

# Logic: Ye number ko 2 se multiply karega.

# Important: Result ko print nahi karna, return karna hai.

# Test: Bahar ek variable mein save kar: ans = double_it(10) aur phir ans ko print kar.


def Double_it(number):
    return number*2
    

result = Double_it(5)
print(result) 


def can_vote(age):
    if(age>=18):
        return True ,"Vote Daalo"
    else:
        return False , "Ghar jaaw"
voter = can_vote(19)
print(voter)


def get_total(marks_list):
    sum = 0
    for i in marks_list:
        sum = sum + i
    return sum
List = [12,12,26,50]    
Total_Marks = get_total(List)
print(Total_Marks)


# 💀 FINAL BOSS: Task 5 (Ultra Hard)
# Ab jab tera Logic set hai, toh ye aakhri Discount Engine bana ke dikha. Isme if-else, maths aur return sab lagenge.

# Reminder - The Logic:

# Function: calculate_final_price(price, coupon)

# Agar coupon "SALE20" -> 20% minus karo. (Formula: price - (price * 0.20))

# Agar coupon "MANIAC50" -> 50% minus karo.

# Else -> Original price wapas karo.


total_price = 0
def FinalPrice(price,coupon):
    if(coupon.upper() == "SALE20"):
        price = price - (price*0.20)
    elif(coupon.upper() == "MANIAC50"):
        price = price - (price*0.50)
    else:
        print("No Discount For you!")
        return price 
    return price
Discount_price = FinalPrice(20000,"MANIAC50")
print("Final Price is ",Discount_price)
