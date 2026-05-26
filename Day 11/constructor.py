

class Const:
    name = "leela"   # class variables

    def __init__(self, name):
        print(self.name)
        print(name)

a= Const("john")

# constructor used to initize the data and assigning value to class variables

class Work:

    def __init__(self,name,age,value):   # to assign the varaibles values at the object creation we use constructor
        self.name = name
        self.age = age
        self.value = value

    def sum(self):
        print(self.name+","+self.age+","+self.value)

m = Work("john","veer","apple")
m.sum()