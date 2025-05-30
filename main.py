# This is a sample Python script.
# from curses.ascii import isupper
# from tkinter.font import names
#
# from Tools.scripts.mailerdaemon import emparse_list_from
# from os.path import split
import math
from functools import total_ordering
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and
# name = input("enter your name: ")
# print(name)
# age = int(input("enter age: "))
# print(age)

# exp1 = eval(input("enter any equation here: "))
# swap two numbers
# x = 12
# y = 13
# temp = x
# x = y
# print(temp)
# print(x)
# y = temp
# print(y)
# print( "value of x is" ,x)
# print( "value of y is" ,y)
# methd2
# a=30
# b=40
# a,b=b,a
# print(b)
# print(a)
# write a program to convert a float into integer

# x=12.4
# print(type(x))
# x = int(x)
# print(type(x))
# print(x)

# write a progam to take details from a student for id card and print it in different lines

# name = input( "enter the name of the student: " )
# grade = input( "enter the grade of the student: " )
# age = int(input("enter the age of the student:"))
# email = input("enter the email the student:")
# ph_no = input("enter the phone number of the student:")
# print("student id card")
# print("name:",name)
# print("grade:",grade)
# print("age:",age)
# print("email:",email)
# print("phone number:",ph_no)

# write a program to take an user input as integer then convert it into float
# a = int(input("enter a number here: "))
# print(a)
# print(type(a))
# a = float(a)
# print("after conversion",a)
# print(type(a))


# print(8//3)
# print(2**5)
# print(3>2)
# print(3>6)
# print(3==6)
# print(3!=6)
# print(not(3>4 and 3<4))

# identity operator
# a = 1234
# b = "1234"
#
# print(a is not b)
# print(bin(15))
# xor
# a = 10
# b = 8
# print(a ^ b)
# zero fill left shift
# print(10>>1)
# zero fill right shift
# print(10<<2)
# a = "hello"
# print("e" not in a)
# conditional statement

# marks = 87
#
# if marks >=90:
#     print ('you will get a mobile phone')
# else:
#     print("no phone for 1 week")
#
# print ("thank you")

# if-elif-else statement

# marks = 70
#
# if marks >= 90:
#     print('you can go to a trip')
# elif marks >= 80 and  marks <90:
#     print("you will get a new phone")
# elif marks >=70 and marks <80:
#       print("you will get a new book")
# else:
#     print("you will not get your phone back")

# nested if statement
# marks =78
# if marks >=80:
#     print("you will get a new phone")
#     if marks >=95:
#         print("you will get  to a trip")
#
#
# else:
#     print("no phone for a month")


# short hand if else statement
# marks=97
# print("you will go to trip") if marks >=90 else print("you will not get phone for a month")
# write a program to check if a number is positive.
# num=int(input("enter your number here: "))
# if num>0:
#     print("it is positive")


 # write a program to check whether a number is odd or even
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# write a program to create area calculator
# print("******AREA CALCULATOR******")
# print("""press 1 to get the area of square
# press 2 to get the area of rectangle
# press 3 to get the area of circle
# press 4 to get the area of triangle""")
#
# choice = int(input("Enter your number between 1-4: "))
# if choice == 1:
#     side = float(input("Enter the length of one side: "))
#     area = side**2
#     print("The area of square is: ",area)
#
# elif choice == 2:
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))
#     area = length*width
#     print("The area of rectangle is: ",area)
# elif choice == 3:
#     radius = float(input("enter the radius of circle: "))
#     area = 3.14*(radius**2)
#     print("The area of circle is: ",area)
# elif choice == 4:
#     height = float(input("Enter the height of the triangle: "))
#     base = float(input("Enter the base of the triangle: "))
#     area = 0.5*height*base
#     print("The area of triangle is: ",area)
#
# else:
#     print("invalid input")
# write a program check whether the passed letter is a vowel or not
# letter = input("enter a letter here: ")
# if (letter in "aeiou") or (letter in "AEIOU"):
#     print("it is a vowel")
# else:
#     print("it is a consonant")
# write a program to check if a number is a single digit number,2digit nuber and so on upto 5 digit
# num = int(input("Enter a number here up to 5 digits: "))
# if num >=0 and num<=9:
#     print("The number you entered is single digit")
# elif num >=10 and num<=99:
#     print("The number you entered is double digit")
# elif num >=100 and num<=999:
#     print("The number you entered is triple digit")
# elif num >=1000 and num<=9999:
#     print("The number you entered is four digit")
# else:
#     print("The number you entered is 5 digit")
# for loop
# for i in range (1,6,2):
#     print(i)
# n=int(input("Enter the no here: "))
#
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)
# while loop
# n = 0
# while n<=10:
#     print(n)
#     n +=2
# n = 1
# a = 12
# while n<=10:
#     print(a,"x",n,"=",n*a)
#     n+=2
#
# while True:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     print(num1+num2)
#     repeat = input('Do you want stop the program: ')
#     if repeat == "yes":
#         break
# nested loop
# for i in range (1,4):
#     for j in range (1,11):
#         print(j,end ="")
#     print()
# pattern
# for i in range (1,6):
#     for j in range (1,i+1):
#         print(j,end =" ")
#     print()
# conditional statement
# for i in range (1,11):
#     if i ==3:
#         print("add this song to favs")
#     else:
#         print(i)
# for i in range (1,101):
#     if i %8==0 and i%12 ==0:
#         print(i)
# n=1
# while n <=10:
#     if n==3:
#         print("add this to favs")
#     else:
#          print(n)
#     n += 1
# for i in range (1,11):
#     if i == 5:
#         break
#     else:
#          print(i)
# print("thank you")
# sum=0
# for i in range(1,51):
#     if i % 2 == 0:
#         sum += i
#
# print(" the sum of all the even number up to 50 is", sum)

# write a program to write first 20 numbers and their squared
# for i in range(1,21):
#     print(i, i**2)
# write a program to find sum of first 10 odd numbers using while loop
# sum = 0
# n = 0
# while n < 20:
#     if n%2 !=0:
#         sum += n
#     n += 1
# print('the sum of the first 10 odd number',sum)
# write a program to check if number is divisible by8 and 12 to upto 100
# for i in range(1,100):
#     if i % 8 ==0 and i % 12 ==0:
#         print (i)
# write a program to create a billing system at supermarket
# while True:
#     name = input("enter customer name: ")
#     total = 0
#
#     while True:
#         print("enter the amount and the quantity")
#         amount  = float(input("enter the amount: "))
#         quantity = float(input("enter quantity: "))
#         total += amount*quantity
#         repeat = input('do you want to add more items? (yes/no): ')
#         if repeat == "no" or repeat == "No":
#             break
#     print("-"*40)
#     print("Name: ", name)
#     print("amount to be paid: ", total)
#     print("-"*40)
#     print("*******Happy Shopping*******")
#
#     repeat1 = input("do you want to go to next customer? (yes/no): ")
#     if repeat1 == "no" or repeat1 == "No":
#         break


# A="Why fit in,When you are born to Stand Out!"
# write a program to find the length of the following string
# print(len(A))
# or
# b=len(A)
# print(b)
# write a program to check how many time alphabet o is occuring
# print(A.count("o"))
# write a program to convert the whole string into lower and upper cases.
# x = A.lower()
# print(x)
# y = A.upper()
# print(y)
# write a program to convert the following string into a title.
# z = A.title()
# print(z)
# write a program to find the index number of "fit in"
# print(A.find("fit in"))
# write a program to print pattern
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(j,end=" " )
#     print()
# for i in range (1,6):
#     for j in range (5,i,-1):
#         print(" ",end=" ")
#     for k in range (i):
#         print(j,end = " ")
# # #
#     print()
# for i in range(1, 6):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="  ")
#     print()
# for i in range(5,0,-1):
#     for k in range(0,i-1):
#         print("*",end="  ")
#     print()

# for i in range (1,11):
#     for j in range (1,i+1):
#         print(i*j,end=" ")
#     print()

# a = "hello world"
# print(type(a))
# print(a)
#
# a = "Harry  Potter and the goblet of the fire"
# print(a)
#
# print(len(a))
# print(a.count(("H")))
# print(a.upper())
# print(a.lower())
# print(a.index("o",15,34))
# print(a.capitalize())
# print(a.casefold())
# print(a.find("o",15,34))
# name = "John"
# age = 24
# b = "my name is {}. and my age is {}"
# print(b.format(name,age))
# print(name.center(20,"*"))
# a = "hello"
# b = "Hello123"
# c = "123456"
# d = "HELLO"
# e = " "
# f = "Hello 123"
# g ="1.234"
# h = "Harry Potter And The Goblet of Fire"
# print(a.isupper())
#isalnum Returns True if all characters in the string are alphanumeric
# print(a,a.isalnum())
# print(b,b.isalnum())
# print(c,c.isalnum())
# print(f,f.isalnum())
# print(g,g.isalnum())


#isalpha Returns True if all characters in the string ore in the alphabet
# print(a,a.isalpha())
# print(b,b.isalpha())
# print(c,c.isalpha())
# print(f,f.isalpha())
# print(g,g.isalpha())


#isdecimal Returns True if all characters in the string are decimals
# print(a,a.isdecimal())
# print(b,b.isdecimal())
# print(c,c.isdecimal())
# print(d,d.isdecimal())
# print(e,e.isdecimal())
# print(f,f.isdecimal())
# print(g,g.isdecimal())


#isdigit Returns True if all characters in the string are digits
# print(a,a.isdigit())
# print(b,b.isdigit())
# print(c,c.isdigit())
# print(d,d.isdigit())
# print(e,e.isdigit())
# print(f,f.isdigit())
# print(g,g.isdigit())


#isnumeric Returns True if all characters in the string are numeric
# print(a,a.isnumeric())
# print(b,b.isnumeric())
# print(c,c.isnumeric())
# print(d,d.isnumeric())
# print(e,e.isnumeric())
# print(f,f.isnumeric())
# print(g,g.isnumeric())

# islower - check if the string is lower case or not
# print(a,a.islower())
# print(b,b.islower())
# print(c,c.islower())
# print(d,d.islower())
# print(e,e.islower())
# print(f,f.islower())
# print(g,g.islower())



# isupper - Returns True if all characters in the string are upper case
# print(a,a.isupper())
# print(b,b.isupper())
# print(c,c.isupper())
# print(d,d.isupper())
# print(e,e.isupper())
# print(f,f.isupper())
# print(g,g.isupper())

# isspace - Returns True if all characters in the string are whitespaces

# print(e,e.isspace())
# print(f,f.isspace())

# istitle - Returns True if the string follows the rules of a title
# print(d,d.istitle())
# print(f,f.istitle())
#
# print(h,h.istitle())

# endswidth() - Returns true if the string ends with the specified value
# a = "Harry Potter"

# print(a.endswith("t",6,9))
# startwith() - Returns true if the string starts with the specified value
# print(a.startswith("P",6,9))

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
# print(a.swapcase())
# strip() - Return a trimmed version of the string
# a = "*******Harry Potter .........."
# print(a)
# print(a.strip("*,."))
# split() - Splits the string at the specified separator, and returns a list
# a = "#OOFD#BRB#OMW#TB"
# b ="hello. my name is john. i am 23 years old"
# print(a.split("#"))
# print(b.split("."))

# ljust() - Return a left justified version of the string
# a = "Harry Potter"
# x = a.ljust(20,"*")
# print(x, "is my favourite movie")
# rjust() - Returns a right justified version of the string
# a = "Harry Potter"
# x = a.rjust(20,"*")

# print(x, "is my favourite movie")
# replace() - returns a string where a specified value is replaced with a
# specified value

# a = "my name is john. john likes to play football."
# print(a)
# print(a.replace("john","lisa"))

# rindex() - Searches the string for a specified value and returns the position of where it was found.

# a = "Harry potter and the Prisoner of Azkaban"
# print(a.rindex("Prisoner"))

# rfind() - Searches the string for a specified value and returns the last position of where it was found
# a = "Harry potter and the Prisoner of Azkaban"
# print(a.rfind("a",6,20))

# string slicing
# a = "Harry Potter and the Goblet of fire"
# b = "012346789"
# print(a)
# print(b[::3])
# print(a[0:5])
# print(a[6:12])
# print(a[:5])
# print(a[-4:])
# print(b[:7:2])
# print(b[::-1])
# print(b[6::-1])

# 1. Write a program to get Fibonacci series up to 10 numbers.
# a = 0
# b = 1
#
# print(a)
# print(b)
# n = int(input("enter a number here: "))
# if n == 1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range (2,n):
#         c = a+b
#         a = b
#         b = c
#         print(c)
# 2. Write a program to check if a number is prime or not.
# num = int(input("enter a number here: "))
# if num <= 1:
#     print("it is not a prime number")
# else:
#     for i in range (2,num):
#         if num% i ==0:
#             print("number is not a prime number")
#             break
#     else:
#         print("it is a prime number")
# 3. Write a program to find a palindrome of integers.
# num = int(input("enter a number here: "))
# temp = num
# rev = 0
# while num > 0:
#     dig = num%10
#     rev = rev*10 + dig
#     num = num//10
#
# if rev == temp:
#     print("it is pallindrome")
# else:
#     print("it is not palindrome")

# 4. Write a program to create an area calculator.
# print("******AREA CALCULATOR******")
# while True:
#     print("""press 1 to get the area of square
#     press 2 to get the area of rectangle
#     press 3 to get the area of circle
#     press 4 to get the area of triangle""")
#
#     choice = int(input("Enter your number between 1-4: "))
#     if choice == 1:
#         while True:
#             side = float(input("Enter the length of one side: "))
#             area = side ** 2
#             print("The area of square is: ", area)
#             repeat = input("Do You want to try again with square?")
#             if repeat == "no":
#                 break
#
#
#     elif choice == 2:
#         while True:
#             length = float(input("Enter the length of the rectangle: "))
#             width = float(input("Enter the width of the rectangle: "))
#             area = length * width
#             print("The area of rectangle is: ", area)
#             repeat = input("Do You want to try again with rectangle?")
#             if repeat == "no":
#                 break
#
#     elif choice == 3:
#         while True:
#             radius = float(input("enter the radius of circle: "))
#             area = 3.14 * (radius ** 2)
#             print("The area of circle is: ", area)
#             repeat = input("Do You want to try again with circle?")
#             if repeat == "no":
#                 break
#
#     elif choice == 4:
#         while True:
#             height = float(input("Enter the height of the triangle: "))
#             base = float(input("Enter the base of the triangle: "))
#             area = 0.5 * height * base
#             print("The area of triangle is: ", area)
#             repeat = input("Do You want to try again with triangle?")
#             if repeat == "no":
#                 break
#
#     repeat1 = input("Do You want to repeat the menu again")
#     if repeat1 == "no":
#         break

# A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"


# Write a program to separate the following string into coma(,) separated values.
# a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# b = a.split(".")
# print(b)
# 2. Write a program to sort strings alphabetically in python.
# a = input("Enter anything here: ")
# b = sorted(a)
# print(b)
# 3. Write a program to remove a given character from a string.
# a = "hello"
# b = a.replace("e","")
# print(b)
# Z="F.R.I.E.N.D.S."
#
# 4. Write a program to remove dot(.) from the following string.
# Z="F.R.I.E.N.D.S."
# B = Z.replace(".","")
# print(B)
# 5. Write a program to check the number of occurrence of a substring of a string
# a = "she sells seashells on the sea shore"
# b = a.count("sea")
# print("the number of times substring sea is occuring is", b)

# 1. Take an input from a user as a string then, reverse it.
# a = input("enter anything here: ")
# print(a[::-1])
# 2. Write a program to check if a string contains only digits.
# a = input("enter anything here: ")
# b = (a.isdigit())
# if b == True:
#     print("it contains only digits")
# else:
#     print("it does not contain only digits")
# 3. Write a program to check if a string is palindrome.
# a = input("enter anything here: ")
# rev = a[::-1]
#
# if a == rev:
#    print("it is palindrome")
# else:
#    print("it is not palindrome")
# 4. Write a program to find number of vowels in a string.
# a = input("Enter anything here: ")
# vowels = 0
# for i in a:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i =="A" or i =="E" or i =="I" or i =="O" or i =="U":
#         vowels += 1
# print("the number of vowels in the following string are",vowels)
# 5. Write a program to check if every word in a string begins with a capital letter.
# a = input("Enter anything here: ")
# print(a.istitle())
# list
# fruits = ["apple", "banana", "cherry",12,45.2]
# print(fruits)
# print(type(fruits))
# list slicing
# a = ["Ironman","Thor","Captain America","Hulk"]
# print(a[1])
# print(a[1:3])
# print(a[:2])
# print(a[1:])
# print(a[::2])
# print(a[-3:-1])
# print(a[::-1])
# print(a[-1:-4:-1])

# list iteration
# Iteration Using For Loop
# a = ["Hulk","Thor","Ironman","Captain America"]
# for i in a:
#     print(i)



#Iteration Using For Loop with Range and Length function
# for i in range(len(a)):
#     print(a[i])


#Iteration Using While Loop
# i = 0
# while i<len(a):
#     print(a[i])
#     i +=1


#Using Short-Hand For Loop

# [print(i) for i in a]

# list function
# a = ["Thor","Hulk","Ironman","Captain america"]
# print(a)
# to find the length of a list
# print(len(a))
# to count an occurence of a particular element
# print(a.count("Hulk"))
# to add to the list
# a.append("Spiderman")
# to add to a specific location
# a.insert(3,"Vision")
# print(a)

#to remove from a list
# a.remove("Spiderman")
# print(a)
# to remove from a certain location
# print(a.pop(1))
# print(a)


#LO create a copy of a LIST
# b = []
# print(b)
# b = a.copy()
# print(b)

#to access an element
# print(a.index("Ironman"))
# print(a.index("Thor"))
#to entend the list
# c = ["vision","spiderman"]
# a.extend(c)
# print(a)
#to reverse the list
# a.reverse()
# print(a)
#to sort the list
# d = [1,2,6,7,8,9,3,4,5,]
# d.sort()
# print(d)

#to clear allthe data from the list
# d.clear()
# print(d)

# list comprehension
# l1 = [30,40,50,60]
# l2 = []
# for i in l1:
#     if i > 45:
#         l2.append(i)
#
# print(l2,"\n",l2)
#
# l3 =[i for i in l1 if i > 45]
# print(l3)

# A = ["Ross", "Rachel", "Monica", "Joe"]
# 1. Write a program to swap first and forth element.
# A[0],A[3]=A[3],A[0]
# print(A)
# 2. Write a program to add a new value at second position.
# A.insert(1,"Phoebe")
# print(A)
# 3. Write a program to delete a value from 3rd position.
# A.pop(2)
# print(A)
# B = [13, 7, 12, 10]
# 1. Write a program to multiply all the numbers in the list.

# mul = 1
# for i in (B):
#     mul *= i
#     print(mul)


# 2. Write a program to get the largest number from the list.
# B.sort()
# print(B)
# print("The largest value in the given list is", B[-1])



# 3. Write a program to get the smallest number from the list.
# print("The smallest value in the given list is", B[0])

# Tuples
# a = "apple","mango","banana",1,67,1.23
# print(type(a))
# print(a)
# # a.add("Kiwi")
# b = ("Ironman",)
# print(type(b))

# slicing and iteration in tuples
# a =("Oneplus","Vivo","Redmi","SumSung","Nokia")
# print(a[1:3])
# print(a[:3])
# print(a[2:])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[2::-1])
# for i in a :
#     print(i)
# along with range and length in for loop
# for i in range(len(a)):
#     print(a[i])
# along with while loop
# i = 0
# while i < len(a):
#     print(a[i])
#     i+=1

# a = ("Oneplus","Nokia","Redmi")
# print(a.count("Redmi"))
# print("the index of redmi",a.index("Redmi"))

# a = list(a)
# print("after conversion",type(a))
# a.append("Vivo")
# print(a)
# a = tuple(a)
# print(type(a))

# Convert the following dictionary into JSON format.
# import json
from itertools import product

# Student_data = {"name": "David", "age":13, "marks":87}
# print(type(Student_data))
# data = json.dumps(Student_data)
# print(data)
# print(type(data))

# 2. Access the value of age from the given data.
# Student_data = '{"name": "David", "age":13, "marks":87}'

#
# data = json.loads(Student_data)
# print(data["age"])

# 3. Pretty Print following JSON data.
# Student_data = {"name": "David", "age":13, "marks":87}
#
# data= json.dumps(Student_data,indent=4,separators=(",","="))
# print(data)
# 4. Sort the following JSON keys and write them into a file.
# Student_data = {"name": "David", "age":13, "marks": 87}
# f = open("demo.json","w")
#
# data = json.dumps(Student_data,indent=4,sort_keys=True)
# f.write(data)
# print("the data has been added to file")
# 5. Access the nested key marks from the following nested data
# student_data ="""{ "student":
#                   {"grade":
#                     {"name":"David","marks":87 }
#                    }
#                  }"""
# data = json.loads(student_data)
# print(data["student"]["grade"]["marks"])

# dictionary
# Employee_Data = {"name":"John","age":24,"gender":"male"}
# print(Employee_Data["gender"])

# iteration in dictionary
# student = {"name":"John", "class":"6th","roll_no":23}
# for x in student:
#     print(student[x])
# using value function
# for x in student.values():
#     print(x)
# using items function
# for x,y in student.items():
#     print(x,"-",y)
# dictionary functions
# student = {"name":"John", "class":"6th","roll_no":23}
# get
# x = student.get("roll_no")
# print(x)
# item
# a = student.items()
# print(a)
# keys
# b = student.keys()
# print(b)
# values
# c = student.values()
# print(c)
# copy
# d = student.copy()
# print(d)
# setdefault
# x = student.setdefault("roll_no", 24)
# print (x)
# nested dictionary
# Employee = {1:{"name":"john","age": 23,"gender":"male"},
#             2:{"name":"lisa","age":24,"gender": "female"},
#             3:{"name":"peter","age": 23,"gender":"male"}}
# print(Employee[2]["gender"])
# problem solving
# 1. Write a python program to sort a dictionary by value.
# a = {"a":12,"b" :23,"c":6,"d":91,"e":45}
# a = sorted(a.values())
# print(a)
# 2. Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.
# a = {}
# for i in range (1,16):
#     a[i] = i**2
# print(a)
# 3. Write a program to multiply all the items in a dictionary.
# a = {"a":1,"b":2,"c":3,"d":4,"e":5}
# print(a["c"])
# product =1
# for i in a:
#     product *= a[i]
# print(product)
# 4. Write a python program to sort a dictionary by key.
# a = {12:"a",56:"b",23:"c",48:"d",91:"e"}
# a = sorted(a.keys())
# print(a)
# set
# a = {"Ironman","Hulk", "Thor","Captain America"}
# print(a)
# print(type(a))
# for x in a:
#     print(x)
# set functions
# a = {"Ironman","Hulk", "Thor","Captain America"}
# add
# a.add("spiderman")
# print(a)
# pop
# a.pop()
# print(a)
# remove
# a.remove("Thor")
# print(a)
# discard
# a.discard("Hulk")
# print(a)
# copy
# b = a.copy()
# print(b)
# a = {"Ironman","Hulk", "Thor","Captain America"}
# b ={"superman","Batman","Wonder-Woman"}
# c = {"Hulk","Thor"}
# isdisjoint
# print(a.isdisjoint(c))
# issubset
# print(c.issubset(a))
# issuperset
# print(a.issuperset(c))
# update
# a.update(c)
# print(a)
# clear
# a.clear()
# print(a)
# set function
# union
# print(a.union(c))
# difference
# x = a.difference(c)
# print(x)
# difference update
# a.difference_update(c)
# print(a)
# intersection
# x = a.intersection(c)
# print(x)

# intersection update
# a.intersection(c)
# print(a)
# symmetric difference
# x = a.symmetric_difference(c)
# print(x)
# symmetric difference update
# a.symmetric_difference_update(c)
# print(a)
# 1. Write a program to find max and min in a set.
# a = {12,56,34,8,90,1,57}
# maximum = max(a)
# minimum = min(a)
# print("the maximum value in the set is", maximum)
# print("the minimum value in the set is", minimum)
# 2. Write a program to find common elements in three lists using sets.
# a = [1,5,6,8,2]
# b = [4,5,6,7 ]
# c = [1,9,6,2,5]
# print(set(a) & set(b) & set(c))
# print("the common elements in the given list are", set(a) & set(b) & set(c))
# 3. Write a program to find difference between two sets.
# a = {1,5,6,8,2}
# b = {1,9,6,2,5}

# print(a.difference(b))
# 4. Write a Python program to remove an item from a set if it is present in the set.
# a.discard(12)
# print(a)
# 5. Write a Python program to check if a set is a subset of another set.
# b = {2,3,4}
# print(b.issubset(a))
# functions
# def hello():
#     print("hello world")
# hello()
#
# def add():
#     x = 56
#     y = 23
#     print(x + y)
# add()

# parameters and arguments
# def add(x,y):
#     print(x+y)
# add(12,67)
# add(12,56)

# def rect(length,width):
#     print("the area of the rectangle is",length*width)
#
# rect(12,3)
# arbitary argument
# def hello(*name):
#     print("hello, my name is",name[2])
# hello("John","lisa","peter")
# def hello():
#     return("hello world")
# print(hello())
# return statement
# def add(a,b):
#     return("the audition of two numbers is",a+b)
# print(add(12,4))
# recursion
# def hello():
#     return hello()
#
# print(hello())

# def fact(n):
#     if n == 0:
#         return 1
#     return (n * fact(n - 1))
#
# print(fact(5))
# a = lambda b: b*5
# print(a(4))

# x = lambda a,b,c: (a+b)*c
# print(x(3,7,3))

# local global variables
# x = 24
# print("first variables x",x)
# def hello():
#     global x
#     x = 25
#     return x
# print(hello())
# print(x)

# problem solving
# Write a function to find maximum of three numbers in Python.
# def maximum_num(val1, val2,val3):
#     if val1 > val2 and val1 > val3:
#         print(val1, "is the greatest number")
#     elif val2 > val1 and val2 > val3:
#         print(val2, "is the greatest number")
#     else:
#         print(val3, "is the greatest number")
# maximum_num(12,5,9)


# 2. Write a Python function to create and print a list where the values are square of numbers between 1 and 30.
# def create_list():
#     l = []
#     for i in range(1, 31):
#         l.append(i**2)
#     return l
#
# print(create_list())
# 3. Write a Python function that takes a number as a parameter and check if the number is prime or not.
# def check_prime(num):
#     if num == 1:
#         print("it is not prime")
#     if num == 2:
#         print("it is a prime")
#     if num>2:
#         for i in range (2,num):
#             if num % i == 0:
#                 print("it is not a prime")
#                 break
#         else:
#             print("it is a prime")
# check_prime(30)
# 4. Write a Python function to sum all the numbers in a list.
# def add(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total
# print("the sum of all the items in the kist is",add([12,4,5,6,7,8]))
# solution 2(using recursion)
# def add(numbers):
#     if len(numbers) == 1:
#         return(numbers[0])
#     else:
#         return((numbers[0])+add(numbers[1:]))
#
# print(add([12,4,5,6,7,8]))
# 5. Write a Python program to solve the Fibonacci Sequence using Recursion.
# def fs(num):
#     if num == 1:
#         return (0)
#     if num == 2:
#         return (1)
#     else:
#         return (fs(num-1) + fs(num-2))
# print(fs(7))
# modules
# import datetime
# x = datetime.datetime.now()
# print(x)
#
# y = datetime.datetime(1997,10,14)
# print(y)
# print(y.strftime("%m"))

# import random
#
# x = random.randint(1,10)
# print(x)

# import math
# x = max(13,67,45)
# print("the maximum value is",x)
# y = min(13,67,45)
# print("the minimum value is",y)
#
# a = pow(2,4)
# print(a)
#
# b = math.sqrt(256)
# print(b)
#
# c = abs(-12.345*3)
# print(c)

# k = math.ceil(2.4)
# print(k)
# m = math.floor(2.4)
# print(m)

# creation of modules
# import demo01 as d
# a = d.add(2,3)
# print(a)
#
# b = d.employee["Name"]
# print(b)