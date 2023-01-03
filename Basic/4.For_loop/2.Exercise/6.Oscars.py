name = input()
points_from_academy = float(input())

total_points = points_from_academy

number_of_grading_people = int(input())

early = False

for _ in range(number_of_grading_people):
    grading_person_name = input()
    person_symbols = len(grading_person_name)
    points_from_him = float(input())

    current_points = (person_symbols * points_from_him) / 2
    total_points += current_points

    if total_points >= 1250.50:
        print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")
        early = True
        break

if not early:
    print(f"Sorry, {name} you need {1250.50 - total_points:.1f} more!")
