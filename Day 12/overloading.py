class Value:

    def a1(self,name=None):
        if name is None:
            print(name)
        else:
         print(f"Hello {name}")     # using default parameter concept we can use same method in different ways

ob = Value()
ob.a1()
ob.a1("John")
