first_group = 0
second_group = 0
third_group = 0
fourth_group = 0
fifth_group = 0

total_groups = int(input())

total_people = 0

for _ in range(total_groups):
    current_group = int(input())
    total_people += current_group

    if current_group <= 5:
        first_group += current_group
    elif current_group <= 12:
        second_group += current_group
    elif current_group <= 25:
        third_group += current_group
    elif current_group <= 40:
        fourth_group += current_group
    elif current_group > 40:
        fifth_group += current_group

first_percent = first_group / total_people * 100
second_percent = second_group / total_people * 100
third_percent = third_group / total_people * 100
fourth_percent = fourth_group / total_people * 100
fifth_percent = fifth_group / total_people * 100

print(f"{first_percent:.2f}%")
print(f"{second_percent:.2f}%")
print(f"{third_percent:.2f}%")
print(f"{fourth_percent:.2f}%")
print(f"{fifth_percent:.2f}%")
