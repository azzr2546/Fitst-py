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
a ="Apple"

# check the length
print(len(a))
print(a)

# change all char to uppercase
print(a.upper())

# change all char to lowercase
print(a.lower())

# remove unwanted char or symble from this obj
b = "Apple!!!!!!!"
print(b)
print(b.rstrip("!"))

# replace
c = "Apple 2"
print(c)
print(c.replace("Apple 2","Apple"))

# convert to list
d = "Apple1 Apple2 Apple3"
print(d)
print(d.split(" "))

# convert first letter to uppercase and other letters to lowercase of the paragraph
e = "appLe iS tHe most SecUre cOmpany."
print(e)
print(e.capitalize())

# Aline center
f = "Apple is the most secure company."
print(f)
print(f.center(50))
print(len(f))
print(len(f.center(50)))

# Counting
ab = "Apple is the most secure company, Apple company is also called iPhone company, Apple Lounch 1 model of phone every year."
print(ab)
print(ab.count("Apple"))

# ENDINGS OF THE OBJECT CHECK IF THE OBJECT IS END WITH GIVEN OBJ THEN IS SHOW TRUE ELSE FALSE
abc = "Apple is the most secure company !!!"
print(abc)
print(abc.endswith("!!!"))
print(abc.endswith("ab"))

# IS THE GIVEN OBJ IS END WITH GIVEN INDEX NUMBER (TRUE OR FALSE)
abcd = "Apple is the most secure company !!!"
print(abcd)
print(abcd.endswith("is",3,8))
print(abcd.endswith("is",3,7))

# find the index of given first obj
print(abcd.find("is"))

# if the given obj is not available in find method the its return -1 index so we can use index to check the error message
print(abcd.find("isss"))
# print(abcd.index("isss"))

# checking the string is write with A-Z,a-z,0-9 its return true or false
ba = "WelcomeToConsole1"

# here we add space so it will return false
bac = "Welcome To Console1"
print(ba)
print(ba.isalnum())
print(bac.isalnum())

# checking the string is write with A-Z,a-z its return true or false
bc = "WelcomeToConsole"
bca = "WelcomeToConsole1"
print(bc)
print(bc.isalpha())
print(bca)
print(bca.isalpha())






