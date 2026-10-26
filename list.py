# List store multiple value in one variable 
skills = ["python","html","js"]
print(skills)
print(skills[0])
skills_i_want_to_learn = ["frontend", "backend","AI"]
print(skills_i_want_to_learn[0])
print([skills_i_want_to_learn[-1]])


for skill in skills:
    print(skill)
print(len(skills_i_want_to_learn))
# Modify a list 
print(skills.append("React"))
print(skills.append("SQL"))
skills.remove("html")
print(skills)
print(len(skills))
for skill in skills:
    print(skill)

a =  [1,2,3,4,5,6]
b = [11,23,45,67]
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[2])
print(b[1])
print(b[2])
print(b[3])
print(b[-1])
for i in a:
    print(i)
for j in b:
    print(j)
print(a + b)
a.remove(3)
print(a)
print(len(a))
num = [1,2,34,4,5,6,]
n = int(input("Enter a number "))
if n in num:
    print("Found the number")
else:
    print("Their is no such a number in the list.")

    
