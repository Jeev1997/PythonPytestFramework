# variables and methods wrapped in single entity

class Encap:

    def __init__(self,name):
        self.name = name
        self.__Mark = 0   # private varaible

    def m2(self):
        return self.__Mark

    def val(self, mark):
        if mark > 100 :
            self.__Mark = mark    # assigned value to class variable
            print("this is class varaible")
        else:
           print("this is not class varaible")


obj = Encap("leela")
print(obj.m2())
obj.val(99)