# Function with arbitaroy arguments or variable-length arguments

# this is used when function should accept random n number of values

def sum(*numbers):
    total = 0
    for i in numbers:
        total = total+i
    return total

#print(sum(10, 300, 56, 78))
#print(sum()) # 0

# Function in positional or keyword arguments

# positional order we send the dat same order it will store

def val(a,b):
    return a+b

print(val(2,3) ) # positional arguments

def val2(a,b=100): # default assigment parameter
    print(a+b)

val2(12)

# Mixed positional and default

def y(a,b, c=90):
    return a+b+c
print(y(12,19,78))