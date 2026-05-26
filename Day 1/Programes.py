#Get a number from the user and print whether it's positive, negative, or zero.

# num = int(input("Enter the number: "))
#
# if num >0:
#         print("the number is positive")
# elif num <0:
#     print("the number is negative")
#
# else:
#    print("the number is zero")

#Take a single letter as input and check if it's a vowel (a, e, i, o, u) or a consonant.

# word = input("Enter the letter: ")
#
# if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":  # if word in 'aeiou' :
#     print("the number is vowel")
# else:
#     print("the number is consonant")

# Get a student's score (0-100) and assign a letter grade (A, B, C, D, or F) based on a simple scale.

# score = int(input("Enter student score: "))
# if score >= 90 and score <= 100:
#     print("Student grade is A")
# elif score >= 80 and score <= 50:
#     print("Student grade is B")
# else:
#     print("Student grade is C")

#Get a number and calculate the sum of its digits using a while loop.

# num = int(input("enter the number: "))
# sum = 0
# while num > 0:
#       sum = sum+num
#       num = num-1
# print(sum)

#Take a number and print its reverse. For example, reversing 1234

# num = int(input("enter the number: "))
# rev = 0
#
# while num > 0:
#     num1 = num % 10
#     rev = rev * 10 + num1
#     num = num//10
#
# print(rev)

# # Print the multiplication table for a number entered by the user, up to 10.
# num = int(input("enter the number: "))
# for i in range(1, 10):
#     print(f"{num}*{i} = {i*num}")

#Take a number from the user and print a solid square of that size
#
# num = int(input("enter the number: "))
#
# for i in range(1, num):
#     print(f"{i}*{num} = {i*num}")

# number = int(input("enter the number: "))
# sum = 0
# for i in range(1, number):
#     sum = sum + i
# print(sum)

# word = input("enter a word: ")
# count = 0
# for i in word:
#     if i in 'aeiou':
#         count +=1
# print(count)

#Repeatedly ask the user to enter a number between 1 and 10. Use a while loop and break to exit the loop only when a valid number is

# number = int(input("enter the number (1-10) : "))
#
# while True:
#     if 1<= number <=10:
#         print("Number is valid")
#         break
#     else:
#       print("Number is invalid try again")

#  Print all numbers from 1 to 20, but skip the numbers
# that are multiples of 3 using the continue statement.

# for i in range(1, 21):
#     if i%3 ==0:
#         continue
#     else:
#         print(i)

#Write a program to create strings using single quotes, double quotes, and str() constructor. Print them and check their type using type().

# x = 'Leela'
# y = "Welcome"
# value = str("hello")
#
# print(type(x))
# print(type(y))
# print(type(value))


# create a string "hello", print its memory address using id().

# s = "hello"
# print(id(s))
# print(s)
# s = s + (" world")
# print(id(s))
# print(s)

#Take two strings "Python" and "Rocks".

# s = "python"
# s2 = "rock"
#
# print(s+ " " +s2)
#
# print(s*3)

#  Take a string "welcome". Print:

# s = "welcome"
#
# print(s[1:5])
# print(s[0:5])
# print(s[-3:])
# print(s[2:-2])
#
#
# print("Characters from index 1 to 4:", s[1:5])   # "elco"
# print("First 5 characters:", s[:5])              # "welco"
# print("Last 3 characters:", s[-3:])              # "ome"
# print("Middle substring 'lco':", s[2:5])         # "lco"

# Write a program that asks the user to input a word.

# word = input("Enter a word: ")
#
# if "Python" in word:
#     print("found")
# else:
#     print("Not found")
#
# print("completed")

# My name is <name>, and I am <age> years old.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
#
# print(f"My name is {name} and I am {age} years old.")

# Case Conversion Methods

# word = input("Enter a word: ")
#
# print(f"this is cap {word.capitalize()}")
# print(word.lower())
# print(word.upper())
# print(word.title())
# print(word.swapcase())

#  Given string "banana", count how many times "a" appears.

# s = input("Enter a string")
# # count = 0
# # for i in s:
# #     if i == "a":
# #        count += 1
# print(s.count("a"))
#
# s1 =" i like bannana"
# s2 = s1.replace("banana","orange")
# print(s2)

#  Ask the user to input a string. Check if:

# word = input("Enter a word: ")
#
# print(word.isalpha())
# print(word.isdigit())
# print(word.isalnum())

#  " apple,banana,grape ",
# s =  " apple,banana,grape "
# print(s.strip())
# value = s.split(",")
# print(value)

# x = [10, 20, 30]
# x.append([40, 50])
# print(x)
#
# fruits = ["apple", "banana", "cherry"]
# print(len(fruits))
#
# print(list())
# print([])
#
# x = [1, 2, 3, 4, 5]
# print(x[1:4])
#
# x = [1, 2, 3, 4]
# print(x.pop())

d = {"a":1}
d2 = d
d2["a"] = 100
print(d["a"])


