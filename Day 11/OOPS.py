class First:

    def m1(self):   # self is parameter and it represents class
        pass         # it will not return anything

    def val(self,num):
        return num*2

m = First()                   # 1 object
m.m1()
print(m.val(10))

m2 = First()                 # 2 object
m2.m1()
print(m2.val(11))