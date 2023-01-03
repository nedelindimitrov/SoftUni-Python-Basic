student_name = input()
all_grades = 0
failed_attempts = 0
year_of_study = 1
while year_of_study <= 12 and failed_attempts < 2:
    year_grade = float(input())
    if year_grade < 4:
        failed_attempts += 1
    else:
        all_grades += year_grade
        year_of_study += 1
if failed_attempts < 2:
    average_grade = all_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {year_of_study} grade")
