import sys
rounds = int(input())
max_num = - sys.maxsize
sum_numbers = 0
for num in range(1, rounds + 1):
    number = int(input())
    if number > max_num:
        max_num = number
    sum_numbers += number
if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {sum_numbers - max_num}")
else:
    print("No")
    sum_others = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_others)}")
