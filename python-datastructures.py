# List Tuples and dictionaries are python data structures
# List = used to store multiple items.
# for example
shopping_lists = ["Milk","Bread","Eggs","Coffee"]
# Instead of creating individual variable for each itemwe create them once.

# How does list work 
# Accessing the elements
print(shopping_lists[0])
# We can also make negative indexing 
print(shopping_lists[-1])

# Adding an element
shopping_lists.append("tea")
print(shopping_lists)

# Changing an element
shopping_lists[0] = "Orange"
print(shopping_lists)
# Removing an element 
shopping_lists.remove("tea")
print(shopping_lists)
# Looping through  a list 
for shopping_list in shopping_lists:
    print(shopping_list)
# Tuple = store value that shouldn't change
days = ("Monday","Tuesday","Wensday","Thursday","Friday")
# Lista and tuples are the same but we can't change the elements of tuples
# How does the tuple work
# Creating tuple 
colors = ("Red","Blue","Green")
print(colors)
# Accessing elements
print(colors[1])
# Looping through tuples 
for color in colors:
    print(color)
# Tuple unpacking 
student = ("Abeba",23,"Software Engineering")
name,age, department = student
print(name)
print(age)
# Dictionary {}
# Another python data structure of python that store variable in key value pairs
student = {
    "name" = "chala",
    "age"= 30,
    "department"="Software Engineering",
    "University" = "AAU"
}
# How dictionary works
# Accessing dictionary element
print(student("name"))
# Adding new information 
student["city"] = "Addis Ababa"
print(student)
# Updating information
student["age"] = 24
print(student)
# Removing information
student.pop("city")
print(student)
# Looping through a dictionary 
student = {
    "name": "Lydia",
    "age": 23,
    "department": "Software Engineering"
}

for key, value in student.items():
    print(key, ":", value)
# Set 
# It stores unique value 
numbers = [1,2,2,3,4,4,6]
# but in set 
# number we can't repeat values
number = {1,2,3,4,5,6}
print(number)
#Adding elements
number.add(7)
print(number)
# Removing elements 
number.remove(4)
# removing duplicates 
print(set(numbers))
