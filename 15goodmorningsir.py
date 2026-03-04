import time as t
hours = int(t.strftime("%H"))
print("hours=",hours)


if (hours>=6 and hours<=11):
    print("good Morning")
elif(hours>=12 and hours<=15):
    print("good after noon")
elif(hours>=16 and hours<=19):
    print("Good Evenig")
elif(hours>19 and hours<=23):
    print("Good Night")
else:
    print("Good Late-Night")