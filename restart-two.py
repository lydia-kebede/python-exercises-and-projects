# Exercise 2: Sum of even numbers

num = int(input("Enter the number: "))
tot = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        tot = tot + i

print("Total =", tot)
# Exercise 3 
n = int(input("Enter a positive integer:"))
count = 0
for i in range(1,n+1):
    if i % 2 == 0:
        count = count + 1
print(count)

# Another Exercise 

odd_number = int(input("Enter a positive odd number: "))
odd = 0
for i in range(1,odd_number+1):
    if i % 2 != 0:
        odd = odd + 1
print(odd)
