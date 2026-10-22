# loop-review
for i in range(1,21):
    print(i)

for i in range(10,0, -1):
    print(i)
print("Blast off!")

# 3.i will take 2,4,6,8,10
# the loop execute 5 times
# The end of the range so it doesn't include the range(11)
#  it means the loop must 2 numbers before going to the second itteration.

n  = int(input("Enter a number"))
for i in range(1,n+1):
    print(i)
number = int(input("Enter a number:"))
for i in range(1,number + 1):
    print(f"{i} * { number} = {i * number}")

# Square of numbers 
num = int(input("Enter a number"))
for i in range(num):
    print(f"{i} * {i} = {i*i}")

# Sum all numbers 
nu = int(input("Enter a positive integer:"))
total = 0
for i in range(1, nu+1):
    total = total + i
    print(f"{total}")
# count numbers  
ni = int(input("Enter a number: "))

even_numbers = []
odd_numbers = []

for i in range(1, ni + 1):
    if i % 2 == 0:
        even_numbers.append(i)  # Adds even number to the even list
    else:
        odd_numbers.append(i)   # Adds odd number to the odd list

print(f"Even numbers list: {even_numbers}")
print(f"Odd numbers list: {odd_numbers}")

i = 1
while i < 4:
    print(i)
    i += 1
countt= 10
while countt > 0:
    print(countt)
    countt-=1
