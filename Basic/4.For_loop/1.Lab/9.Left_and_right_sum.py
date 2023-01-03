how_much_per_side = int(input())

first_sum = 0
second_sum = 0

for n in range(how_much_per_side):
    current_num = int(input())
    first_sum += current_num

for n in range(how_much_per_side):
    current_num = int(input())
    second_sum += current_num

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f"No, diff = {abs(first_sum - second_sum)}")
