#to avoid termination of programe we try to catch the error in exception

# print("first statemnet")
# try:
#  print(x)
# except:
#     print("this is a exception")
# print("second statemnet")

#Finally block
n = int(input("Enter a number: "))
x = n/100
try:
  if n==0:
    print("exception")
  else:
     print(x)
finally:
    print("success")

