
Name = input("Enter your name:")
print ("Entered Name is :",Name)

Number_1 = input("Enter Number-1:") # for example 20 input kiya
Number_2 = input("Enter Number_2:") # for example 30 input kiya 
# To Answer 2030 aayega kyu ki 
# Note VIMP: python may input always string may hi aata hai chahe phir wo integer input kiya hoo yaa float yaa double yaa koi bhi or input value hoo
# Note : python may input wale chahe jo bhi hoon , python uss ko hamesha string may hi lega. 
print(Number_1 + Number_2) # answer is always in string , jab tak input yaa phir output/print ko type caste naa kiya jaaye
# to aab hame always input ko typecaste karna padega into required or needed or desired Datatype


# for example 
Number_1 = int(input("Enter Number-1:")) # for example 20 input kiya
Number_2 = int(input("Enter Number_2:")) # for example 30 input kiya
print(Number_1 + Number_2) # abb answer 50 hoga

# another example 
Number_1 = input("Enter a Number:") # ye second tarika hai yaato input lete waqt type casting karo 
Number_2 = input("Enter a Number:")
print(int(Number_1)+int(Number_2)) # yaa phir out put nikaal te waqt type casting karo


