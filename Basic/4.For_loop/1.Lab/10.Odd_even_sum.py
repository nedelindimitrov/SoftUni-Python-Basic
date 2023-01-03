how_much = int(input())

first_sum = 0
second_sum = 0

first_or_no = 1

for n in range(how_much):

    current = int(input())

    if first_or_no % 2 == 0:
        second_sum += current
    else:
        first_sum += current

    first_or_no += 1

if first_sum == second_sum:
    print("Yes")
    print(f"Sum = {first_sum}")
else:
    print("No")
    print(f"Diff = {abs(first_sum - second_sum)}")
