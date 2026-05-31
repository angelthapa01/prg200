class Student:
    def __init__(self, name, age, student_id, marks):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Student ID :", self.student_id)
        print("Marks :", self.marks)
//class 


students = []

# Input for 10 students
for i in range(10):
    print("\nEnter details for student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    student_id = input("Enter student ID: ")
    marks = float(input("Enter marks: "))

    s = Student(name, age, student_id, marks)
    students.append(s)

# Display all students
print("\nStudent Details")
for s in students:
    s.display()

# Calculate average, highest, minimum
total = 0
highest = students[0].marks
minimum = students[0].marks

for s in students:
    total += s.marks

    if s.marks > highest:
        highest = s.marks

    if s.marks < minimum:
        minimum = s.marks

average = total / 10

print("\nAverage Marks =", average)
print("Highest Marks =", highest)
print("Minimum Marks =", minimum)