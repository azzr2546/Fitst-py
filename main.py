# print("Hello World")
# print(5)
# print("Bye", 5)
# print(12+8)
# print(12*5)

# print("Hey I am a good boy
#       and this viewer is also a good boy/girl"){incorrect}

# {correct}
# print("Hey I am a good boy\nand this viewer is also a good boy/girl")
# print("Hey I am a \"good boy\"\nand this viewer is also a good boy/girl")

# a = 1
# print(a)

# b = "Apple"
# print(b)

# DATA TYPES 

# a = 123
# a1 = 123
# b = "Apple"
# c = True
# d = None
# e = 1.2
# f = complex(2 ,3)

# print(a+a1)
# print("The type of a is ", type(a))
# print("The type of b is ", type(b))
# print("The type of c is ", type(c))
# print("The type of d is ", type(d))
# print("The type of e is ", type(e))
# print("The type of f is ", type(f))

# LIST

# list1 = [8, 2.4,[-2,7], ["apple","banana"]]
# print(list1)

# TUPLE

# tuple1 = (("parrot", "sparrow"),("Lion", "Tiger"))
# print(tuple1)

# dict(Dictionary)
# dict1 = {"name":"Apple", "age":12,"canVote":True}
# print(dict1)

# ARITHMETIC OPERATORS

# Addition(+)
# Subtraction(-)
# Multiplication(*)
# Division(/)
# Modulus(%)
# Floor Division(//)
# Exponental(power)(**)

# print(15+6)
# print(15-6)
# print(15*6)
# print(15/6)
# print(15%6)
# print(15//6)
# print(2**4)

# Expercise 1

# a = 10
# b = 2
# ans1 = a+b
# print("Addition of",a,"and",b,"is",ans1)
# ans2 = a-b
# print("Subtraction of",a,"and",b,"is",ans2)
# ans3 = a*b
# print("Multiplication of",a,"and",b,"is",ans3)
# ans4 = a/b
# print("Division of",a,"and",b,"is",ans4)
# ans5 = a%b
# print("Modulus of",a,"and",b,"is",ans5)
# ans6 = a//b
# print("Floor Division of",a,"and",b,"is",ans6)
# ans7 = a**b
# print("Exponental of",a,"and",b,"is",ans7)

# a = 12
# b = 2

# print("The value of", a,"+",b, "is: ", a + b)
# print("The value of", a,"-",b, "is: ", a - b)
# print("The value of", a,"*",b, "is: ", a * b)
# print("The value of", a,"/",b, "is: ", a / b)
# print("The value of", a,"%",b, "is: ", a % b)
# print("The value of", a,"//",b, "is: ", a // b)
# print("The value of", a,"**",b, "is: ", a ** b)

# CONVERTING TO OTHER TYPES

# a = "1"
# b = "2"
# print(a+b)
# output will "12" bacause its a string


# a = "1"
# # a = 1
# b = "2"
# # b = 2
# print(int(a)+int(b))

# # Implicite TypeCasting
# c = 1.9
# d = 9

# print(c + d)

# Taking User Input

# a = input("Enter your Laptop brand: ")
# print("I have", a , "Laptop")

# WE ARE ADDIND TWO STRINGS

# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print(a + b)

# ADDING TWO INT
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print(int(a) + int(b))

# SLICING

# fruit = "Mango"
# mangoLen = len(fruit)
# print(mangoLen)
# # including 0 but not 4
# print(fruit[0:4])
# # including 1 but not 4
# print(fruit[1:4])
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
# print(fruit[-1:len(fruit)-3])
# print(fruit[-3:-1])

# Quiz
# nm = "Apple"
# print(nm[-4:-2])


# STRING METHODS

# String are immutable
# a ="Apple"

# # check the length
# print(len(a))
# print(a)

# # change all char to uppercase
# print(a.upper())

# # change all char to lowercase
# print(a.lower())

# # remove unwanted char or symble from this obj
# b = "Apple!!!!!!!"
# print(b)
# print(b.rstrip("!"))

# # replace
# c = "Apple 2"
# print(c)
# print(c.replace("Apple 2","Apple"))

# # convert to list
# d = "Apple1 Apple2 Apple3"
# print(d)
# print(d.split(" "))

# # convert first letter to uppercase and other letters to lowercase of the paragraph
# e = "appLe iS tHe most SecUre cOmpany."
# print(e)
# print(e.capitalize())

# # Aline center
# f = "Apple is the most secure company."
# print(f)
# print(f.center(50))
# print(len(f))
# print(len(f.center(50)))

# # Counting
# ab = "Apple is the most secure company, Apple company is also called iPhone company, Apple Lounch 1 model of phone every year."
# print(ab)
# print(ab.count("Apple"))

# # ENDINGS OF THE OBJECT CHECK IF THE OBJECT IS END WITH GIVEN OBJ THEN IS SHOW TRUE ELSE FALSE
# abc = "Apple is the most secure company !!!"
# print(abc)
# print(abc.endswith("!!!"))
# print(abc.endswith("ab"))

# # IS THE GIVEN OBJ IS END WITH GIVEN INDEX NUMBER (TRUE OR FALSE)
# abcd = "Apple is the most secure company !!!"
# print(abcd)
# print(abcd.endswith("is",3,8))
# print(abcd.endswith("is",3,7))

# # find the index of given first obj
# print(abcd.find("is"))

# # if the given obj is not available in find method the its return -1 index so we can use index to check the error message
# print(abcd.find("isss"))
# # print(abcd.index("isss"))

# # checking the string is write with A-Z,a-z,0-9 its return true or false
# ba = "WelcomeToConsole1"

# # here we add space so it will return false
# bac = "Welcome To Console1"
# print(ba)
# print(ba.isalnum())
# print(bac.isalnum())

# # checking the string is write with A-Z,a-z its return true or false
# bc = "WelcomeToConsole"
# bca = "WelcomeToConsole1"
# print(bc)
# print(bc.isalpha())
# print(bca)
# print(bca.isalpha())

# # checking the string is in lowercase its return true or false

# bcd = "welcome to console"
# bcad = "Welcome to console"
# print(bcd)
# print(bcd.islower())
# print(bcad)
# print(bcad.islower())

# # if the string is print able then its return true else false
# bcda = "Welcome To Console"
# bb = "Welcome to console\n apple"
# print(bcda)
# print(bcda.isprintable())
# print(bb)
# print(bb.isprintable())

# # cheching to the content is title
# print(bcda)
# print(bcda.istitle())

# # convert to tital case
# print(bb)
# print(bb.title())

# STATEMENTS
# IF ELSE STATEMENT
# a = int(input("Enter your age: "))
# print("Your age is:",a)

# # Conditional operators
# # >, <, >=, <=, ==, !=

# if(a>18):
#     print("You can drive")
    
# else:
#     print("You cannot drive")

# applePrice = 210
# budget = int(input("Enter your budget: "))
# if  (budget > applePrice):
#     print("Alexa, add 1 kg of Apples to the cart.")
      
# else:
#     print("Alexa, do not add Apples to the cart.")
#     print("You don't have budget")

# num = int(input("Enter the value of number: "))

# if (num < 0):
#     print("Number is negative.")
# elif (num == 0):
#     print("Number is Zero.")
# elif (num == 999):
#     print("Number is Special")
# else:
#     print("Number is positive")
# print("I am happy now")

# NESTED IF STATEMENT

# num = int(input("Enter any of number: "))
# if (num < 0):
#     print("Number is negative")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")

# LOOPS

# name = "Apple"
# for i in name:
#     print(i)
#     if (i=="l"):
#         print("This is something special!")

# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# Range in loop
# for k in range(5):
#     print(k)
# for c in range(0,20000):
#     print(c + 1)

# skipping the number between 
# for k in range(1, 12, 2):
#     print(k)

# WHILE LOOP
# i = 0
# while(i<=10):
#     print(i)
#     i = i + 1
# print("Done with the loop")

# i = int(input("Enter the number: "))
# while(i <= 38):
#     i = int(input("Enter the number: "))
#     print(i)
    
# print("Done with the loop")

# count = 5
# while (count > 0):
#     print(count)
#     count = count - 1
    
# while with else
# count = 5
# while (count > 0):
#     print(count)
#     count = count - 1

# # when the while statement is end it will print else

# else:
#     print("I am inside else")

# DO WHILE LOOP
# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if(i%100 == 0):
#         break

# Break Statement
# for i in range(12):
#     if (i == 10):
#         break
#     print("5 X", i+1, "=", 5 * (i+1))
    
# print("Left and go the Loop")

# Continue Statement
# for i in range(12):
#     if (i == 10):
#         print("Skip the iteration")
#         continue
#     print("5 X", i, "=", 5 * i)

# # FUNCTIONS
# # TWO TYPES OF FUNCTION 
# # 1. Built-in function{min(),max(),len(),sum(),type(,etc)}
# # 2.User-define function which user can create ehich is create in blow dowm

# # NOW WE CAN CREATE THE FUNCTION FOR THIS BECAUSE WE DONT HAVE TO WRITE AGAIN AND AGAIN
# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
    
# def isGreater(a, b):
#     if(a>b):
#        print("First number is greater")
#     else:
#        print("Second number is greater or equal")

# a = 9
# b = 8
# # if(a>b):
# #     print("First number is greater")
# # else:
# #     print("Second number is greater or equal")
# # gmean1 = (a*b)/(a+b)
# # print(gmean1)
# # now we will just call the function instead of re write the formula again and again
# calculateGmean(a, b)
# isGreater(a, b)

# c = 8
# d = 74

# # if(c>d):
# #     print("First number is greater")
# # else:
# #     print("Second number is greater or equal")
# # gmean2 = (c*d)/(c+d)
# # print(gmean2)
# # now we will just call the function instead of re write the formula again and again
# calculateGmean(c, d)
# isGreater(c, d)


# FUNCTION ARGUMENTS AND RETURN STATEMENT

# def average(a, b):
#     print("The average is ", (a+b)/2)
    
# average(4, 6)

# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)
    
# average()

# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)
# if I will add the value ao a,b here it will ignore first values
# average(1, 5)

# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)
# # or we can add just one value 
# average(a=5)
# # or we can add b value

# def average (*numbers):
#     # print(len(numbers))
#     # print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ",sum/len(numbers))
    
# average(4,5,7)

# def name(**name):
#     print("Hello,", name["fname"],
# name["mname"], name["lname"])
    
# name(mname = "Buchnan", lname = "Barnes",
#      fname = "James")


# PYTHON LIST

# l = [2,4,5]
# print(l)
# print(type(l))

# # we can aslo add any type in list
# marks = [3, 4, 5, "Apple", True]
# print(marks)
# print(type(marks))
# # list index
# # print(marks[0])
# # print(marks[1])
# # print(marks[2])
# # print(marks[3])
# # print(marks[4])

# # negative index
# print(marks[-3])

# # Positive index
# print(marks[len(marks)-2]) 

# # Positive index
# print(marks[5-2])

# # Positive index
# print(marks[3])

# if 7 in marks:
#     print("Yes")
    
# else:
#     print("No")
    
# if "Apple" in marks:
#     print("Yes")
    
# else:
#     print("No")

# Same thing applies for string ass well!
# if "le" in "Apple":
#     print("Yes")

# marks = [3, 4, 5, "Apple", True, 8, 11, 13, 22, 32]
# print(marks)
# print(marks[1:9])
# print(marks[1:9:2])

# LIST COMPREHESION
# lst = [i for i in range(10)]
# print(lst)

# # here we are *ing index to index
# lst = [i*i for i in range(10)]
# print(lst)

# # here we add condition if the %of 2 is = 0 just print that numbers
# lst = [i*i for i in range(10) if
#        i%2==0]
# print(lst)

# LIST METHODS

# # append method is for add the obj in last index
# l = [12,10,63,1,2,3,4,6,1,1,1]
# print(l)
# l.append(9)
# print(l)

# sort method is for assending and decending order method
# l.sort()
# print(l)
# for decending order
# l.sort(reverse=True)
# print(l)

# reverse method
# l.reverse()
# print(l)

# index method
# print(l.index(1))

# count method
# print(l.count(1))

# copy method (we can copy of aur orignal list and we ca change the obj of our new list but not change in orignal obj)
 
# m = l.copy()
# m[0]=0
# print(m)

# insert method

# l.insert(1,899)
# print(l)

# extend method
# m = [900,1000,1100]
# # l.extend(m)
# # or
# k = l+m
# print(k)

# tuples its like a list but we cant change the obj its const
# tup = (1,2,7,8, "Apple")
# # tup =(1,)
# print(type(tup), tup)
# print(tup[0])
# print(len(tup))
# print(tup[-1])
# print(tup[3])

# if 8 in tup:
#     print("Yes 8 is present in this tuple")

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

# tuple1 = (0,1,2,34,2,31,1,3,2,3)
# # res = tuple1.count(3)
# # res = tuple1.index(3)
# res = len(tuple1)
# # res = tuple1.index(3,4,8)
# # print('Count of 3 in tuple1 is: ', res)
# # print('index of 3 in tuple1 is: ', res)
# # print('index of 3 in tuple1 is: ', res)
# print('length of tuple1 is: ', res)


# Exercise 2

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

# import time
# t = time.strftime('%H:%M:%S')
# hour =int(time.strftime('%H'))
# hour =int(input("Enter hour: "))
# print(hour)

# if(hour>=0 and hour<12):
#     print("Good Morning Sir!")
# elif(hour>=12 and hour<17):
#     print("Good Aftenoon Sir!")
# else:
#     print("Good Night Sir!")


# f-string(STRING FORMATTING)

# letter = "Hey my name is {} and I am from {}"
# country = "India"
# name = "Apple"

# print(letter.format(country,name))
# print(letter.format(name,country))

# letter = "Hey my name is {1} and I am from {0}"
# country = "India"
# name = "Apple"

# print(letter.format(country,name))
# print(f"Hey my name is {name} and I am from {country}")

# for only 2 decimals and it will round out

# txt = "For only {price:.2f} dollars"
# print(txt.format(price = 49.09999))

# price = 49.09999
# txt = f"For only {price:.2f} dollars!"
# print(txt)

# convert to string

# print(f"{2*30}")
# print(type(f"{2*30}"))

# Docstring in python

# def square(n):
#     # it is docstring not a comment
#     '''Takes in a number n, return the square of n'''
#     print(n**2)
# square(5)
# # if we want to show the docstring
# print(square.__doc__)


# PEP 8

# if we open terminal and first we run "python" and then we run "import this" the we see a poem its call PEP 8


# Recursion in python

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# how is it works
# 5 * factorial(5-1=4)
# 5 * 4 * factorial(4-1=3)
# 5 * 4 * 3 * factorial(3-1=2)
# 5 * 4 * 3 * 2 * factorial(2-1=1)
# 5 * 4 * 3 * 2 * 1







