# Lesson_one_continued
# Variables and values 
# Variable = used to store information
# Variable names cannot start with a number and python distinguishes uppercases and lower cases for example age and AGE is different .
#Exercise_one 
name = "Lydia"
age = 22
favorite_language = "python"
print(name)
print(age)
print(favorite_language)
# Lesson_two 
# Getting input from the users
# Name = int(input("Enter your name ")) 
# input() = this returns a string so if we want a number we need to moddify it's type 
# Age = int(input("Enter your age :"))
Name = input("Enter your name: ")
Age = int(input("Enter your age:"))
print(type(Age))

# Arthimetic operators 
a = int(input("Enter the first number :"))
b = int(input("Enter the first number :"))
print ( a + b)
print ( a - b)
print ( a * b)
print ( a / b)
# Comparision Operator 
# Python_program
c = int(input("Enter your first whole  number:"))
d = int(input("Enter your second whole number:"))
print (c > d)
print(c == d)
print(c < d)
# Conditional statement 
# How to make a program decide what to do ?
# The if statement run when the of code run only when the condition is true
# If the consition is false we are gonna provide else for another condition.
# Lesson4_exercise 
score = int(input("Enter your exam score:"))
if score >= 90 and score <= 100:
    print("Your score is 'A' ")
elif score >= 80 and score <= 89:
    print("Your score is 'B' ")
elif score >= 70 and score <= 79:
    print("Your score is 'C' ")
elif score >= 60:
    print("Your score is 'D' ")
else:
    print("Your score is 'F' ")

# Lesson 5 Logical operators 
age = int(input("Enter your age:"))
membership = input("Do you have membership 'Yes' or 'No' ")

if age >= 18 and membership == True:
    print("Access granted")
else:
    print("Access denied")
age = int(input("Enter your age:"))
membership = input("Do you have membership 'Yes' or 'No' ").lower()

if age >= 18 and membership == 'yes':
    print("Access granted")
else:
    print("Access denied")
# Lesson 6 
# To accomplish a reptitive task we can use loop.
print(range(7))
# range (2,9) it doesn't include 9 
n = int(input("Enter a number"))
for i in range(1,11):
    print(f"{i} * {n} = {i * n }")
# using f string
# another_exercise 
n = int(input("Enter positive integer"))
total = 0
for i in range(1, n+1):
    total = total + i
    print(f"sum = {total}")
# Accumulator 
# accumulattor is a variable that store a result and updates it repeatedly 

#  n + 1 = is to include n we added one  to it 
n = int(input("Enter a number"))
total = 0
for i in range(1, n+1):
    total = total + i
    print(total)
