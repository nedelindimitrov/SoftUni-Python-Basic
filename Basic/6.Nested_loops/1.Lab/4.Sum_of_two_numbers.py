interval_start = int(input())
interval_end = int(input())

magic_num = int(input())

combination_number = 0
combination_found = False

last_num1 = 0
last_num2 = 0

for number1 in range(interval_start, interval_end + 1):
    for number2 in range(interval_start, interval_end + 1):
        combination_number += 1
        last_num1 = number1
        last_num2 = number2
        if number1 + number2 == magic_num:
            combination_found = True
            break
    if combination_found:
        break

if combination_found:
    print(f"Combination N:{combination_number} ({last_num1} + {last_num2} = {magic_num})")
else:
    print(f"{combination_number} combinations - neither equals {magic_num}")
