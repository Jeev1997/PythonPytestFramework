#day = 1

# match day:
#     case 1: print("Sunday")
#     case 2: print("Monday")
#     case 3: print("Tuesday")
#     case 4: print("Wednesday")
#     case 5: print("Thursday")
#     case 6: print("Friday")
#     case 7: print("Saturday")
#     case _: print("invalid week")

#combine
day = 1
match day:
     case 2|3|4|5|6 : print("week day")
     case 1|7 : print("weekend")