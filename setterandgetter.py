class Player:
    def __init__(self, name, starting_score):
        self.name = name
        # Notice kar, maine underscore '_' lagaya hai. 
        # Yeh Python mein ek ishara (convention) hai ki yeh "Private/Protected" variable hai, 
        # isko direct mat chhedna.
        self._score = starting_score  

    # 🟢 GETTER: Data dekhne ka gate
    @property
    def score(self):
        print(f"--> [GETTER CALLED] {self.name} ka score check ho raha hai...")
        return self._score

    # 🔴 SETTER: Data change karne ka gate (Validation ke sath)
    @score.setter
    def score(self, new_value):
        print(f"--> [SETTER CALLED] Score ko {new_value} karne ki koshish...")
        if new_value < 0:
            # Pylance/ErrorLens yahan error phekega agar koi try karega
            raise ValueError("Bhai game hack kar raha hai kya? Score negative nahi ho sakta! 💀")
        else:
            self._score = new_value
            print("--> [SUCCESS] Score update ho gaya!")

# --- Aab Isko Test Karte Hain ---

# 1. Player banaya
p1 = Player("Haydan", 10)

# 2. Getter Use kiya (Dekh, function ki tarah p1.score() nahi likha, variable ki tarah access kiya)
print(f"Current Score: {p1.score}\n")

# 3. Setter Use kiya (Valid)
p1.score = 50
print(f"New Score: {p1.score}\n")

# 4. Setter Use kiya (Invalid - Yahan code phatega!)
p1.score = 20  # Yeh line error degi ValueError!

print("--------------------------------------------------------------------------------------")

class MyClass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"valie is {self._value}")
    @property
    def multi_10_value(self):
        return 10 * self._value
    @multi_10_value.setter
    def multi_10_value(self,newvalue):
        self._value = newvalue/10
        # return 5 * self._value
    
obj = MyClass(10)
obj.multi_10_value = 67
print(obj.multi_10_value)
obj.show()

        