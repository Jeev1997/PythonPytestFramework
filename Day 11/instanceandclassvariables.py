
# class Variables:
#
#     a,b,c = 1,2,3   # class varaibles
#
#     def method(self, x,y,z):  # method varaibles
#         print(self.a+ self.b+ self.c)
#         print(x*3)
#
# m = Variables()
# m.method(5,4,5)


# global , class , method variables


a,b,c = 1,2,3    # global varaibles

class Mix():

    a,b,c = 10,20,30

    def sum(self, a, b,c):

        print(a+b+c)       # local variables
        print(self.a+self.b+self.c) # class varaibles
        print(globals()['a']+globals()['b']+globals()['c'])                  # global varaibles

s=Mix()
s.sum(100,200,300)



