num_count = int(input())

biggest_num = -999999999999999999999999999
smallest_num = 999999999999999999999999999

for n in range(num_count):
    current_num = int(input())
    if current_num < smallest_num:
        smallest_num = current_num
    if current_num > biggest_num:
        biggest_num = current_num

print(f"Max number: {biggest_num}")
print(f"Min number: {smallest_num}")
