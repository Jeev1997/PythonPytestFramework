
#tuple and string,int ,float is immutable change will not happen
# list and dic,set mutatable

# s= "value"
#
# #s[1] = "w"   # we cant change the value of s
#
# print(s)
# print(id(s))
#
# s="w" + s[2:]
#
# print(s)
# print(id(s))

list= [1, 4, 5, 7, 8]
print(f"Before change {list}")
print(id(list))
list[2] = 90
print(f"after change {list}")
print(id(list))
