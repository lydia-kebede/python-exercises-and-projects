# Functions OOP and Solid principles 
# python functions 
# A functin is a resusable block of code designed to perform a particular task.

def greet(name):
    message = f"Hello,{name}!"
    return message 

result = greet("Abel")
print(result)
# python function follows snake case meaning we use underscore between two words.
# print and return 
# types of function arguments
# Positional argument 
# Arguments assigned according to their position.
def introduce(name,age, city):
    print(f"My name is {name}")
introduce("sara",22,"Addis Ababa")

# Keyword argument
def fruits(first, second, third):
    print(f"I prefer {first} other than  {second} and {third} fruits.")
fruits(
    second = "Mango",
    first = "Apple",
    third = "strawberry"
)
# Default argument
# when the parameter have a predefined value
def greeeting(name, language="English"):
    if language == "English":
        return f"Hello,{name}"
    elif langugage == "Amharic":
        return f"Hello {name}"
    return f'Language is not supported '

print(greeeting("Lydia","English"))
# parameters without default generally become before parameter with defaults.
# understanding args 
# def add(*args):
    
# print(add (9,7))
# inside a function arg is a tuple .
# understanding kwargs 
