class Math:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num = self.num + n
    @staticmethod
    def add(a,b):
        return a + b

# resutl = math.add(a,2)
# print(result) # O/P = 3

a  = Math(5)
print(a.num)
a.addtonum(9)
print(a.num)
