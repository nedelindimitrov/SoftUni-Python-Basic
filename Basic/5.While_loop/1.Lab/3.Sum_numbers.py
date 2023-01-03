first_num = int(input())

total_sum = 0

while True:
    number = int(input())
    total_sum += number
    if total_sum >= first_num:
        print(total_sum)
        break
