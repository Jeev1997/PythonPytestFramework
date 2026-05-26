
# list = [1,3,7,8,2,5]
# list.sort()
# print(f"after sort {list}")
# list.sort(reverse=True)
# print(list)


mytuple = ('a', 'b', 'c')
# tuple[1] = 'd'
# print(tuple)    # error immutable

# tuple.append('e')
# print(tuple)



val = list(mytuple)
print(val)
val.append('e')
print(val)

# converting tuple >>>>>>>>>>. list >>>>>>>>>> tuple
mytuple= tuple(val)
print(mytuple)

print(mytuple.count('e'))
print(len(mytuple))

