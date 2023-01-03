max_bad_grades = int(input())

last_problem_name = ""

total_grades_score = 0
total_problems = 0
total_bad_grades = 0

while True:
    problem_name = input()
    if problem_name == "Enough":
        average_grade = total_grades_score / total_problems
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {total_problems}")
        print(f"Last problem: {last_problem_name}")
        break
    grade = int(input())
    if grade <= 4:
        total_bad_grades += 1
    if total_bad_grades == max_bad_grades:
        print(f"You need a break, {max_bad_grades} poor grades.")
        break
    last_problem_name = problem_name
    total_grades_score += grade
    total_problems += 1
