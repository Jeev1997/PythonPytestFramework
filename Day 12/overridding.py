
# overriding same method signature but implemnetation of body is different in child class

class Parent:
    name = "leela"

    def first(self):
        print("from parent class")
        return self.name

class Child(Parent):
    name = "John"
    def first(self):
        super().first()         # used for invovke immediate parent class
        print("from child class")
        print(super().name)
        return self.name

obj = Child()
obj.first()    #child class
print(obj.name)