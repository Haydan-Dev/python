Number = int(input("Enter a Nuber"))

if(Number==0):
    print("Number is zero")
elif(Number%2==0):
    print("Even Number")
    if(Number>=100):
        print("yes even and greater than 100")
else:
    print("OddNumber")
    if(Number<=10):
        print("number is lesser than 10")

    
light= input("Enter light color:")

match light:
    case "Red":print("Stop")
    case "yellow":print("Slow Down")
    case "Green":print("GO")
    case _:print("invalid-color")
 

User_pin = int(input("Enter your Pin:"))
if(User_pin==123):
    print("Pin is valid , you can process!")
    User_Ammount = float(input("Enter Withdrawal Amount:"))
    if(User_Ammount%500==0):
        print("Withdrawal Successfull")
    else:
        print("You can't Withdraw , Amount is not Availble")
else:
    print("In-valid pin Try again!")


Year = int(input("Enter a Year to check is it leap or not"))
if(Year%4==0):
    print("Year is divisible by 4 , Checking Future")
    if(Year%100==0):
        print("Is also Divisible by 100,Checking Future")
        if(Year%400==0):
            print("It is Also Divisible by 400 , Its is a Leap Year")
        else:
            print("It is not Divisible by 400,It is not a leap Year")
    else:
        print("It is a Leap Year")
else:
    print("It is not a Laep year")



Is_Premium = input("Are You a Premium User? (yes or no)").lower()
if(Is_Premium=="yes"):
    Distance = float(input("Enter Distance:"))
    if(Distance<=10):
        Order_value = float(input("Enter Your Order Value"))
        if(Order_value<600.00):
            print("Order lesser than 600 will charge 25 rupees of delivery")
            Total_amount=Order_value+25
            print("Your total Bill is",Total_amount)
        else:
            Total_amount=Order_value
            print("Your total Bill is",Total_amount)
    elif(Distance>10 and Distance<=20):
        Order_value = float(input("Enter Your Order Value"))
        if(Order_value<2000):
            print("Mimimum 2000 Ordervalue is needed to Order")
        else:
            print("Distance more than 10KM required 100 Delivery fees")
            Total_amount=Order_value+100
            print("Your total Bill is",Total_amount)
    else:
        print("we don't do delivery in more than 20Km Distance")
else:
    Distance = float(input("Enter Distance:"))
    if(Distance<=10):
        Order_value = float(input("Enter Your Order Value"))
        if(Order_value<1000.00):
            print("Order lesser than 1000 will charge 50 rupees of delivery")
            Total_amount=Order_value+50
            print("Your total Bill is",Total_amount)
        else:
            Total_amount=Order_value
            print("Your total Bill is",Total_amount)
    elif(Distance>10 and Distance<=20):
        Order_value = float(input("Enter Your Order Value"))
        if(Order_value<2500):
            print("Mimimum0 2000 Ordervalue is needed to Order")
        else:
            print("Distance more than 10KM required 100 Delivery fees")
            Total_amount=Order_value+150
            print("Your total Bill is",Total_amount)
    else:
        print("we don't do delivery in more than 20Km Distance")
    
        

Order_value = float(input("Enter Order value:"))
delivery_price = 0 if Order_value>1000 else (50 if Order_value>=500 else 100 ) 



