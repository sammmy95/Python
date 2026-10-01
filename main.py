from college.student import get_student_details
from college.result import calculate_total, calculate_percentage, calculate_grade

name, roll, m1, m2, m3 = get_student_details()

total = calculate_total(m1, m2, m3)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

print("\n========== COLLEGE MANAGEMENT SYSTEM ==========")
print("Student Name :", name)
print("Roll Number  :", roll)
print("-----------------------------------------------")
print("Subject 1    :", m1)
print("Subject 2    :", m2)
print("Subject 3    :", m3)
print("-----------------------------------------------")
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("===============================================")