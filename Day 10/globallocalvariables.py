
x = 200  # global variable

def value():
    global x
    x=23      # local
    print(x) # 23

value()
print(x) # 23