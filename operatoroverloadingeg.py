class opertorEg:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a + other.a
    def __sub__(self,other):
        return self.a - other.a
    
oe = opertorEg(10)
oe1 = opertorEg(20)
print(oe.a)
print(oe1.a)
print(oe.a + oe1.a)
print(oe + oe1)
print(oe-oe1)
