# Reuse of parent class method and variables in child class

# Single inheritance

# class A:
#     a,b = 20,30
#     def m2(self):
#         print("this is parent class")
#
#     def m1(self):
#         return self.a+self.b
#
# class B(A):
#     def a1(self):
#         pass
#
# val = B()
# val.m2()
# print(val.m1())
# val.a1()


# Multi- level inheritance

# class M:
#     name = "leela"
#     def a(self):
#         return self.name
#
# class N(M):
#     name1 = "Jeevi"
#     def b(self):
#         return self.name1
#
# class O(N):
#     name2 = "John"
#     def c(self):
#       return self.name2
#
# obj= O()
#
# print(obj.b())
# print(obj.a())
# print(obj.c())

