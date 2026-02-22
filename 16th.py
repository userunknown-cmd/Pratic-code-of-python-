# write a program to accept marks of 6 students and display then in sorted manner 
# using the sorted method()

Marks = []

student1 = int(input("marks of the first student : "))
Marks.append(student1)
student2 = int(input("marks of the first student : "))
Marks.append(student2)
student3 = int(input("marks of the first student : "))
Marks.append(student3)
student4 = int(input("marks of the first student : "))
Marks.append(student4)
student5 = int(input("marks of the first student : "))
Marks.append(student5)
student6 = int(input("marks of the first student : "))

Marks.append(student6)

Marks.sort()
print(Marks)