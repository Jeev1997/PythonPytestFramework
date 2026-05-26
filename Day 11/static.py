class Value:

    def m2(self):
        print("normal method")

    @staticmethod
    def m1(self,name):   # for static method self is normal parameter and it will not represent class
        return name

a = Value()

a.m2()
print(a.m1("value","jeevitha")) # 2 parameter we need to pass

print(Value.m1("value", "Leela"))  # direct from class same we can call static method
Value.m2(12)
