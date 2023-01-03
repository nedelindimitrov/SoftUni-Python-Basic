number = int(input())

total_bonus = 0

first_bonus = 0

if number <= 100:
    first_bonus = 5
elif number > 1000:
    first_bonus = number * 0.10
elif number > 100:
    first_bonus = number * 0.20

total_bonus += first_bonus

second_bonus = 0

if number % 2 == 0:
    second_bonus = 1

total_bonus += second_bonus

third_bonus = 0

if number % 10 == 5:
    third_bonus = 2

total_bonus += third_bonus

final_number = number + total_bonus

print(total_bonus)
print(final_number)
