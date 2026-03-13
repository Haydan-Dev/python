class math:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
       self.num = self.num +n
    @staticmethod
    def add(a,b):
        return a+b
        
a = math(6)
print(a.num)
a.addtonum(10)
print(a.num)
