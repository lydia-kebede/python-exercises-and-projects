# finding the largest and smallest  value in a list 
numbers = [14,6,23,3,11,8]
smallest = 14
current_number = 3
if current_number < smallest:

    smallest == current_number
  
numbers = [14, 6, 23, 3, 11, 8]

smallest = numbers[0]
largest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

    if i > largest:
        largest = i

print("Smallest number:", smallest)
print("Largest number:", largest) 
# this is to find the largest and smallest value in the long list 

