locations = [
    ("Delhi",(28.70),77.10),
    ("Mumbai", (19.07), 72.87),
    ("Bangalore", (12.97), 77.59),
]

for   (latitute),city,longitute  in locations:
    print("Name:",city,"Latitute:",latitute)
    
Questions = [
    "python language kisne banaaiye hai?",
    "Kya tuple Mutable hai (yes/no)",
    "List ke end main item jodne ke liye kaunsa method use hota hai?",
    "Python mein code block define karne ke liye kya use hota hai? (Brackets/Indentation)",
]

Answers = [
    "guido van rosum",
    "no",
    "append",
    "indentation",
]

prize = 0 
i = 0

for question in Questions:
    print(question)
    user_answers = input("Enter your answer:")
    if(user_answers.lower()==Answers[i]):
        prize = prize+1000
        print("Right Answer,Your Price = ",prize)
    else:
        print("Wrong answer,You didnt get nay price!")
        break
    i = i+1
if prize >0:
    print("Congratulation you have win",prize)    
else:
    print("Sorry, Better Luck Next Time")