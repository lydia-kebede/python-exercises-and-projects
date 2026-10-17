num = int(input("Enter positive whole number:"))
largest = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        if i > largest:
            largest = i

       
print(largest) 
# count matching numbers = count = count + 1
#  sum matching total = total + i
# the largest number =  largest = i
n = int(input("Enter a positive integer number: "))
smallest = None

for i in range(1, n + 1):
    if i % 2 == 0:
        if smallest is None or i < smallest:
            smallest = i

if smallest is not None:
    print("Smallest even number:", smallest)
else:
    print("There is no even number in this range.")
