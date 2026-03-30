import csv
import matplotlib.pyplot as plt

students = {}

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Save to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    for name, marks in students.items():
        writer.writerow([name, marks])

# Calculations
total = sum(students.values())
avg = total / len(students)

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("\n--- Analysis ---")
print("Average Marks:", avg)
print("Topper:", highest, "-", students[highest])
print("Lowest:", lowest, "-", students[lowest])

# Grade system
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print(name, "-", marks, "Grade:", grade)

# 📊 Graph
names = list(students.keys())
marks = list(students.values())

plt.bar(names, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.show()