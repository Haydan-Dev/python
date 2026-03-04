

def movies():
    movies = ["Iron Man", "Skyfall", "Inception", "Interstellar"]
    for index , movie in enumerate(movies , start= 1) :
        print(f"{index}. {movie}")
movies()


def tools():
    tools = ["Hammer", "Spanner", "Screwdriver", "Drill"]
    for index, tool in enumerate(tools, start=1):
        if(tool.lower() == "screwdriver"):
            print(index)
            break
tools()


def print_odd():
    numbers = [10, 20, 30, 40, 50, 60]
    for index , number in enumerate(numbers):
        if index%2!=0: 
            print(number)
print_odd()


def parallel_universe():
    names = ["Haydan", "Papa", "Partner"] 
    roles = ["Intern", "Boss", "Manager"]
    for name_index ,name in enumerate(names, start=1):
        for role_index ,role in enumerate(roles, start=1):
            if(role_index == name_index):
                print(f'{role_index}. {name} is {role}')
parallel_universe()



# Q5. The "Skip & Rename" Protocol List: files = ["config.py", "server.py", "secret.env", "db.py"]. Loop chala.
# Agar file ka naam secret.env hai, toh print mat kar (Security!).
# Agar file ka naam server.py hai, toh print kar: "Processing Index [index]: MAIN SERVER FILE".
# Baaki files ke liye normal print: "Processing Index [index]: [filename]". Challenge: Index wahi rehna chahiye jo list mein hai, manual छेड़छाड़ nahi.

def skip_protocall():
    files = ["config.py", "server.py", "secret.env", "db.py"]
    for index,file in enumerate(files):
        if(file.lower() == "secret.env"):
            continue
        elif(file.lower() == "server.py"):
            print(f"Processing Index [{index}]: MAIN SERVER FILE")
        else:
            print(f"Processing Index [{index}]: {file}")
skip_protocall()


# Q6. The Formatting Nightmare String: s = "backend" Is string ke har character ko print kar, lekin:
# Agar index Even hai, toh letter Capital mein print ho.
# Agar index Odd hai, toh letter Small mein print ho.
# Output ek line mein nahi, alag-alag line mein chalega. Example: Index 0 (b) -> B, Index 1 (a) -> a, Index 2 (c) -> C...

def The_Formatting_Nightmare_String():
    words = "backend"
    for index , latter in enumerate(words):
        if index%2==0:
            print(latter.capitalize())
        else:
            print(latter.lower())
The_Formatting_Nightmare_String()    



def db():
    db_data = [
        ("System", "Root@123"), 
        ("Papa", "secret_pass"), 
        ("Haydan", "my_pass")
    ]
    for index , (user,password) in enumerate(db_data):
        if(user.lower()=="system"):
            print(f"{index}. {user}:{password}")
        else:
            print(f"{index}. {user}:****")
db()