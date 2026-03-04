command = input("Voice Command bolo(Light,Ac,Music)").capitalize()
time = int(input("Enter time 0-23:"))


match command:
    case "Light":
        if(time > 6 and time <18):
            print("Dhoop kaafi hai, lights band rakhte hain.")
        else:
            print("Raat ho gayi hai, lights ON kar di.")
    case "Music":
        if(time>22):
            print("Padosi jaag jayenge, volume kam rakho!")
        else:
            print("Party on! Music playing.")
    case "Ac":
        if (time >=12 and time <=16):
            print("Bahut garmi hai, AC full par hai.")
        else:
            print("Mausam thanda hai, AC ki zaroorat nahi")
    case _:
        print("Sorry, ye mere bas ki baat nahi.")