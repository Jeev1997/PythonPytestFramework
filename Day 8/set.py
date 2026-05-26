set ={"apple", "banana", "cherry"}
set1 = {"1", "2", "3", "4"}
set2 = {"1", "8"}

# # set.remove("banana")
# # print(set)
# set.remove("cccccc")   # will give error
# print(set)
#
# # set.discard("cherry")
# # print(set)
# set.discard("zzzzz")   # will not give error
# print(set)

value = set.union(set1&set2)
print(value)

